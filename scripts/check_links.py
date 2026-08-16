#!/usr/bin/env python3
"""Check every external URL in the course markdown.

Fails only on links that are *definitely* dead — 404, 410, or no connection at
all. Publisher and government hosts that block datacenter IPs are listed in
course.yml under `link_allowlist`; they 403 to any automated checker and are
reported but never fail the build. LINK-AUDIT.md explains why each is there.

    python3 scripts/check_links.py            # check, fail on dead links
    python3 scripts/check_links.py --report   # never fail; just print

Extraction note: URLs here contain commas and %20 (a Therac-25 PDF filename,
among others). An extractor that stops at a comma silently truncates them and
reports healthy links as broken — that bug cost a debugging cycle once.
"""
from __future__ import annotations

import concurrent.futures as cf
import os
import re
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0.0.0 Safari/537.36")
DEAD = {"404", "410", "000"}


def load_allowlist() -> list[str]:
    import yaml
    with open(os.path.join(ROOT, "course.yml")) as fh:
        return yaml.safe_load(fh).get("link_allowlist", [])


# LINK-AUDIT.md documents URLs that were found BROKEN and replaced. Checking it
# would fail the build on links whose deadness is the whole point of the record.
SKIP_FILES = {"LINK-AUDIT.md"}


def collect_urls() -> dict[str, list[str]]:
    """url -> [files that cite it]"""
    found: dict[str, list[str]] = {}
    # Deliberately permissive: allow commas and parens-free paths, then strip
    # trailing sentence punctuation.
    pat = re.compile(r"https?://[^\s<>\"'`\)\]]+")
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", ".github"}]
        for fn in filenames:
            if not fn.endswith(".md") or fn in SKIP_FILES:
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
            with open(os.path.join(dirpath, fn), encoding="utf-8") as fh:
                for raw in pat.findall(fh.read()):
                    url = raw.rstrip(".,;:")
                    found.setdefault(url, []).append(rel)
    return found


def probe(url: str) -> tuple[str, str]:
    try:
        out = subprocess.run(
            ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "--max-time", "45", "-A", UA, url],
            capture_output=True, text=True, timeout=60,
        )
        return url, (out.stdout.strip() or "000")
    except Exception:
        return url, "000"


def main() -> int:
    report_only = "--report" in sys.argv
    allow = load_allowlist()
    urls = collect_urls()
    print(f"{len(urls)} unique URLs across the course markdown\n")

    results: dict[str, str] = {}
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        for url, code in pool.map(probe, sorted(urls)):
            results[url] = code

    dead, blocked, other = [], [], []
    for url, code in sorted(results.items()):
        host = urllib.parse.urlparse(url).netloc.lower()
        allowed = any(host == a or host.endswith("." + a) for a in allow)
        if code.startswith("2"):
            continue
        if allowed:
            blocked.append((url, code))
        elif code in DEAD:
            dead.append((url, code))
        else:
            other.append((url, code))

    healthy = len(results) - len(dead) - len(blocked) - len(other)
    print(f"  {healthy} healthy")

    if blocked:
        print(f"\n  {len(blocked)} allowlisted (block automated checkers; live in a browser):")
        for url, code in blocked:
            print(f"      {code}  {url[:110]}")

    if other:
        print(f"\n  {len(other)} non-2xx but not conclusively dead "
              f"(rate limits, redirects, transient):")
        for url, code in other:
            print(f"      {code}  {url[:110]}")
            for f in sorted(set(urls[url]))[:2]:
                print(f"            cited in {f}")

    if dead:
        print(f"\n  {len(dead)} DEAD:")
        for url, code in dead:
            print(f"      {code}  {url[:110]}")
            for f in sorted(set(urls[url])):
                print(f"            cited in {f}")

    print()
    if dead and not report_only:
        print(f"FAILED — {len(dead)} dead link(s). Fix them, or add the host to "
              f"link_allowlist in course.yml if it merely blocks bots "
              f"(and say so in LINK-AUDIT.md).")
        return 1
    print("PASSED — no dead links" if not dead else "reported only; not failing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
