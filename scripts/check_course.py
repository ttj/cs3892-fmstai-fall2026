#!/usr/bin/env python3
"""Consistency checks for the class-facing CS 3892 repo.

Validates every fact that appears in more than one place against course.yml,
and enforces that nothing instructor-only has leaked into a repo the students
can read.

    python3 scripts/check_course.py            # all checks
    python3 scripts/check_course.py --list     # what it checks, without running

Exit code 0 if clean, 1 if anything failed. Designed to be readable when it
fails: every failure names the file, what was expected, and what was found.
"""
from __future__ import annotations

import fnmatch
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES: list[str] = []
CHECKS_RUN = 0


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def load_manifest() -> dict:
    path = os.path.join(ROOT, "course.yml")
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML is required: pip install pyyaml")
    with open(path) as fh:
        return yaml.safe_load(fh)


def read(rel: str) -> str:
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def fail(check: str, detail: str) -> None:
    FAILURES.append(f"{check}: {detail}")


def ok(check: str) -> None:
    global CHECKS_RUN
    CHECKS_RUN += 1
    print(f"  ok    {check}")


def run(check: str, fn) -> None:
    """Run one check; a check reports problems by returning a list of strings."""
    global CHECKS_RUN
    CHECKS_RUN += 1
    try:
        problems = fn() or []
    except Exception as exc:  # a crashing check is a failing check
        problems = [f"check raised {type(exc).__name__}: {exc}"]
    if problems:
        print(f"  FAIL  {check}")
        for p in problems:
            print(f"          {p}")
            FAILURES.append(f"{check}: {p}")
    else:
        print(f"  ok    {check}")


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------
def check_packet_headers(m):
    """Each packet's H1, session, date, week and due date match the manifest."""
    problems = []
    for d in m["discussions"]:
        rel = f"discussions/{d['file']}"
        try:
            s = read(rel)
        except FileNotFoundError:
            problems.append(f"{rel} is missing")
            continue

        h1 = s.split("\n", 1)[0]
        want_h1 = f"# {d['id']} — {d['title']}"
        if h1.strip() != want_h1:
            problems.append(f"{rel} H1\n            want: {want_h1}\n            got:  {h1.strip()}")

        hdr = re.search(r"\*\*Session (\d+) · ([^·]+) · week (\d+)", s)
        if not hdr:
            problems.append(f"{rel} has no parsable session/date/week header line")
        else:
            got = (int(hdr.group(1)), hdr.group(2).strip(), int(hdr.group(3)))
            want = (d["session"], d["date"], d["week"])
            if got != want:
                problems.append(f"{rel} header want session/date/week {want}, got {got}")

        due = re.search(r"due \*\*([^,]+), 11:59", s)
        if not due:
            problems.append(f"{rel} has no parsable reflection due date")
        elif due.group(1).strip() != d["due"]:
            problems.append(f"{rel} due date want {d['due']!r}, got {due.group(1).strip()!r}")
    return problems


def check_packet_sections(m):
    """Every packet has the required sections, in order."""
    problems = []
    want = m["packet_sections"]
    for d in m["discussions"]:
        rel = f"discussions/{d['file']}"
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        got = re.findall(r"^## (.+?)\s*$", read(rel), re.M)
        if got != want:
            problems.append(f"{rel}\n            want: {want}\n            got:  {got}")
    return problems


def check_tables(m):
    """The schedule table and the discussions index agree with the manifest."""
    problems = []
    row_re = re.compile(r"^\| \*\*(D\d)\*\* \| (\d+) \| ([^|]+?)\s*\| (\d+) \| ([^|]+?)\s*\|")
    for rel in ("schedule/schedule.md", "discussions/README.md"):
        rows = {}
        for line in read(rel).split("\n"):
            mt = row_re.match(line)
            if mt:
                rows[mt.group(1)] = (int(mt.group(2)), mt.group(3), int(mt.group(4)), mt.group(5))
        if len(rows) != len(m["discussions"]):
            problems.append(f"{rel} has {len(rows)} discussion rows, expected {len(m['discussions'])}")
        for d in m["discussions"]:
            got = rows.get(d["id"])
            if got is None:
                problems.append(f"{rel} is missing a row for {d['id']}")
                continue
            want = (d["session"], d["date"], d["week"], d["short"])
            if got != want:
                problems.append(f"{rel} {d['id']}\n            want: {want}\n            got:  {got}")
    return problems


def check_inline_schedule_markers(m):
    """The 💬 markers inside the session table point at the right sessions."""
    problems = []
    s = read("schedule/schedule.md")
    found = dict(re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|\s*\*\*💬 (D\d)", s, re.M))
    want = {str(d["session"]): d["id"] for d in m["discussions"]}
    if found != want:
        for sess, did in sorted(want.items(), key=lambda kv: int(kv[0])):
            if found.get(sess) != did:
                problems.append(f"session {sess} should carry {did}, carries {found.get(sess, 'nothing')}")
        for sess, did in found.items():
            if want.get(sess) != did:
                problems.append(f"session {sess} carries {did}, which the manifest does not place there")
    return problems


def check_dates_in_syllabus(m):
    """Dates in the manifest actually appear in the syllabus."""
    problems = []
    s = read("syllabus/syllabus.md")
    for key, value in m["dates"].items():
        values = value if isinstance(value, list) else [value]
        for v in values:
            if v not in s:
                problems.append(f"syllabus/syllabus.md never mentions {key} = {v!r}")
    return problems


def check_grading(m):
    """Weights sum to 100, the split sums to the participation share, and the
    syllabus table matches."""
    problems = []
    g = m["grading"]
    if sum(g.values()) != 100:
        problems.append(f"grading weights sum to {sum(g.values())}, not 100")
    p = m["participation_split"]
    if sum(p.values()) != g["participation"]:
        problems.append(f"participation split sums to {sum(p.values())}, not {g['participation']}")

    s = read("syllabus/syllabus.md")
    for label, pct in (("Term project", g["project"]), ("Homeworks", g["homeworks"]),
                       ("Quizzes", g["quizzes"])):
        if not re.search(rf"\|\s*\**{label}[^|]*\**\s*\|\s*\**{pct}%", s):
            problems.append(f"syllabus grading table has no {label} row at {pct}%")

    part = read("discussions/participation.md")
    for label, pct in (("Discussion reflections", p["discussion_reflections"]),
                       ("Leading one in-class case study", p["case_study_lead"])):
        if f"{pct}%" not in part or label not in part:
            problems.append(f"participation.md does not state {label} at {pct}%")
    return problems


def check_reflection_spec(m):
    """The reflection spec is stated identically wherever it appears."""
    problems = []
    r = m["reflection"]
    words = f"{r['words_min']}–{r['words_max']} words"
    for rel in ["discussions/participation.md", "discussions/README.md", "syllabus/syllabus.md"]:
        if words not in read(rel):
            problems.append(f"{rel} does not state the reflection length as {words!r}")
    for d in m["discussions"]:
        rel = f"discussions/{d['file']}"
        if os.path.exists(os.path.join(ROOT, rel)) and words not in read(rel):
            problems.append(f"{rel} does not state the reflection length as {words!r}")
    return problems


def _section(text: str, start: str, end: str) -> str | None:
    try:
        return text[text.index(start):text.index(end)]
    except ValueError:
        return None


def check_readings_invariant(m):
    """Each packet's reading-list size matches its entry in course.yml.

    Two rewrites have passed through these files. Both times this count was the
    thing that proved nothing had been silently dropped. Per-discussion rather
    than one global total, so that adding a source is a local edit to that
    packet's number instead of a recomputed magic constant.
    """
    problems = []
    for d in m["discussions"]:
        rel = f"discussions/{d['file']}"
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        body = _section(read(rel), "## Readings", "## What you submit")
        if body is None:
            problems.append(f"{rel} has no Readings / What you submit boundary")
            continue
        urls = len(re.findall(r"<(https?://[^>]+)>", body))
        marks = body.count("⚠️")
        if urls != d["urls"]:
            problems.append(f"{rel} has {urls} reading URLs, course.yml says {d['urls']}")
        if marks != d["unverified"]:
            problems.append(f"{rel} has {marks} unverified marks, course.yml says {d['unverified']}")
    return problems


def check_prompt_counts(m):
    """Each packet has exactly the number of discussion questions course.yml
    records.

    The instructor run sheets assign specific prompts to specific rows by
    number ("rows 1-2 take Prompt 2"). Renumbering or deleting a question here
    silently breaks a run sheet over there, so the count is pinned in the
    manifest and the instructor repo checks its references against it.
    """
    problems = []
    for d in m["discussions"]:
        rel = f"discussions/{d['file']}"
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        body = _section(read(rel), "## Discussion questions",
                        "## Why this is in a formal-methods course")
        if body is None:
            problems.append(f"{rel} has no Discussion questions section")
            continue
        nums = [int(n) for n in re.findall(r"^\*\*(\d+)\.\*\* ", body, re.M)]
        if nums != list(range(1, d["prompts"] + 1)):
            problems.append(
                f"{rel} prompts are numbered {nums}, course.yml says there are "
                f"{d['prompts']} numbered 1..{d['prompts']}. If you changed them, update "
                f"course.yml AND check the run sheet in the instructor repo, which "
                f"references prompts by number.")
    return problems


def _markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", ".github", "node_modules"}]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.relpath(os.path.join(dirpath, fn), ROOT)


# Files whose job is to describe the policy, and which therefore have to be
# able to name the things the policy forbids ("no run sheets here", "instructor
# voice such as 'assign only pp. 1-2'").
#
# The exemption is deliberately narrow: it covers only the two categories that
# describe *apparatus and phrasing*. Secrets and student data are never exempt,
# anywhere, for any file.
POLICY_FILES = {"README.md", "STATUS.md", "LINK-AUDIT.md"}
POLICY_EXEMPT_CATEGORIES = {"instructor_apparatus", "instructor_voice", "instructor_voice_exact"}


def check_no_instructor_content(m):
    """Nothing instructor-only in a repo the class can read.

    Categories ending in `_exact` are matched case-sensitively — an all-caps
    stage direction is a leak, the same words in ordinary prose are not.
    """
    problems = []
    for category, patterns in m["forbidden_in_class_repo"].items():
        exact = category.endswith("_exact")
        for rel in _markdown_files():
            if category in POLICY_EXEMPT_CATEGORIES and os.path.basename(rel) in POLICY_FILES:
                continue
            text = read(rel)
            for pat in patterns:
                needle = pat if exact else pat.lower()
                for i, line in enumerate(text.split("\n"), 1):
                    hay = line if exact else line.lower()
                    if needle in hay:
                        problems.append(f"{rel}:{i} contains {category} pattern {pat!r}")
                        break
    return problems


def check_no_forbidden_paths(m):
    """No scratch, draft, or editor-leftover files anywhere."""
    problems = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            for pat in m["forbidden_paths"]:
                if fnmatch.fnmatch(fn, pat):
                    rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                    problems.append(f"{rel} matches forbidden path pattern {pat!r}")
    return problems


def check_pdf_fresh(m):
    """syllabus.pdf was built from the current syllabus.md.

    git does not preserve mtimes, so a stale PDF on main is otherwise silent.
    `make pdf` writes the source hash to syllabus/.syllabus.md.sha256.
    """
    src = os.path.join(ROOT, "syllabus/syllabus.md")
    pdf = os.path.join(ROOT, "syllabus/syllabus.pdf")
    stamp = os.path.join(ROOT, "syllabus/.syllabus.md.sha256")
    if not os.path.exists(pdf):
        return ["syllabus/syllabus.pdf is missing"]
    if not os.path.exists(stamp):
        return ["syllabus/.syllabus.md.sha256 is missing — run `make pdf` and commit it"]
    with open(src, "rb") as fh:
        want = hashlib.sha256(fh.read()).hexdigest()
    got = open(stamp).read().strip().split()[0]
    if want != got:
        return ["syllabus.pdf is stale — syllabus.md changed since the last `make pdf`. "
                "Run `make pdf` and commit both the PDF and the .sha256 stamp."]
    return []


def check_internal_links(m):
    """Every relative markdown link resolves to a file that exists."""
    problems = []
    for rel in _markdown_files():
        base = os.path.dirname(os.path.join(ROOT, rel))
        for text, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", read(rel)):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, path))):
                problems.append(f"{rel} links to {target!r}, which does not exist")
    return problems


def check_decks_present(m):
    """Every discussion has a deck URL recorded (they live in the instructor
    repo, but the manifest is where they are declared)."""
    problems = []
    for d in m["discussions"]:
        if not d.get("deck", "").startswith("https://gamma.app/"):
            problems.append(f"{d['id']} has no gamma.app deck URL in course.yml")
    return problems


def _parse_day(label: str, value: str, year: int, problems: list):
    """Parse 'Thu Aug 27' and verify the weekday actually matches the date.

    strptime will happily accept a wrong weekday, which is exactly the drift
    worth catching: a syllabus that says "Wed Aug 27" for a Thursday is wrong
    in the way students notice.
    """
    import datetime
    try:
        parsed = datetime.datetime.strptime(f"{value} {year}", "%a %b %d %Y").date()
    except ValueError as exc:
        problems.append(f"{label} = {value!r} is not a parsable date: {exc}")
        return None
    stated = value.split()[0]
    actual = parsed.strftime("%a")
    if stated != actual:
        problems.append(f"{label} = {value!r} but {parsed.isoformat()} is a {actual}, not a {stated}")
        return None
    return parsed


def check_due_offsets(m):
    """Dates are internally consistent, and reflection due dates are the stated
    offset after class unless the entry carries a `note` explaining why not."""
    problems = []
    year = m["meta"]["year"]
    for d in m["discussions"]:
        cls = _parse_day(f"{d['id']} date", d["date"], year, problems)
        due = _parse_day(f"{d['id']} due", d["due"], year, problems)
        if cls is None or due is None:
            continue
        delta = (due - cls).days
        if delta < 0:
            problems.append(f"{d['id']} reflection is due {abs(delta)} days BEFORE the session")
        elif delta != m["reflection"]["due_offset_days"] and "note" not in d:
            problems.append(
                f"{d['id']} due {delta} days after class, expected "
                f"{m['reflection']['due_offset_days']}; add a `note:` to course.yml if deliberate")
    return problems


CHECKS = [
    ("packet headers match course.yml", check_packet_headers),
    ("packet sections present and ordered", check_packet_sections),
    ("schedule + index tables match course.yml", check_tables),
    ("inline discussion markers on the right sessions", check_inline_schedule_markers),
    ("manifest dates appear in the syllabus", check_dates_in_syllabus),
    ("grading weights consistent", check_grading),
    ("reflection spec stated consistently", check_reflection_spec),
    ("per-packet reading counts match course.yml", check_readings_invariant),
    ("prompt counts match course.yml", check_prompt_counts),
    ("no instructor-only content", check_no_instructor_content),
    ("no scratch or draft files", check_no_forbidden_paths),
    ("syllabus.pdf built from current syllabus.md", check_pdf_fresh),
    ("internal links resolve", check_internal_links),
    ("every discussion has a deck", check_decks_present),
    ("dates parse, weekdays match, due offsets hold", check_due_offsets),
]


def main() -> int:
    if "--list" in sys.argv:
        for name, _ in CHECKS:
            print(name)
        return 0

    print(f"checking {ROOT}\n")
    manifest = load_manifest()
    for name, fn in CHECKS:
        run(name, lambda fn=fn: fn(manifest))

    print()
    if FAILURES:
        print(f"FAILED — {len(FAILURES)} problem(s) across {CHECKS_RUN} checks")
        return 1
    print(f"PASSED — {CHECKS_RUN} checks, no drift")
    return 0


if __name__ == "__main__":
    sys.exit(main())
