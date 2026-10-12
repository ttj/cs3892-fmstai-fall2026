# CS 3892 / CS 5892 — Formal Methods: Safe and Trustworthy AI

**Vanderbilt University · Fall 2026 · Tuesday & Thursday, 11:00 a.m. – 12:15 p.m.**
Instructor: [Taylor T. Johnson](https://www.taylortjohnson.com)

Course materials: syllabus, schedule, homeworks, project topics, and rubrics.

> **Where things are.** Announcements, due dates, submissions and grades are in Brightspace, and
> Brightspace is authoritative. Runnable examples and homework starters are in
> [`ttj/cs3892-examples`](https://github.com/ttj/cs3892-examples).

## Contents

| Path | What it is |
|---|---|
| [`syllabus/syllabus.md`](syllabus/syllabus.md) | The syllabus. [PDF](syllabus/syllabus.pdf) |
| [`schedule/schedule.md`](schedule/schedule.md) | All 28 sessions, with every homework, quiz, and project deadline |
| [`projects/README.md`](projects/README.md) | Project instructions and deliverables |
| [`projects/project-topics.md`](projects/project-topics.md) | **Eight defined project topics** with tools, benchmarks, and success criteria |
| [`projects/rubrics.md`](projects/rubrics.md) | How each project deliverable is graded |
| [`assignments/README.md`](assignments/README.md) | The five homeworks. Handouts so far: [HW1](assignments/hw1.md), [HW2](assignments/hw2.md) |
| [`discussions/README.md`](discussions/README.md) | **Nine in-class discussion packets** — case-study background, questions, readings |
| [`discussions/participation.md`](discussions/participation.md) | The reflection you submit after each discussion, and how it is graded |
| [`quizzes/README.md`](quizzes/README.md) | Quiz format and coverage |
| [`labs/README.md`](labs/README.md) | Tool setup, zero-install paths, and the Lean version pin |
| [`LINK-AUDIT.md`](LINK-AUDIT.md) | Every URL in the course materials, checked and dated |
| [`course.yml`](course.yml) | Dates, weights and the nine discussions, in one place; the documents are checked against it |

## The course in one paragraph

Generative AI industrialized software *production* without a matching advance in software
*validation*. Formal methods are the part of computer science that produces guarantees rather than
test results. This course covers the guarantees — SAT/SMT, model checking, abstract interpretation,
interactive theorem proving, neural network verification — and asks what they can cover when the
artifact under scrutiny is a neural network or an agent (**FM4AI**), and whether AI can finally
make these methods cheap enough to use routinely (**AI4FM**). Students apply both directions in a
semester-long team project that satisfies the CS project and Immersion requirements.

## Structure at a glance

28 sessions, Aug 27 – Dec 10:

| Sessions | Unit |
|---|---|
| 1 | Framing: the verification triple; FM4AI and AI4FM |
| 2–4 | AI failure modes, risk frameworks, regulation; guardrails vs. solver-backed checks |
| 5–6 | Logic and preliminaries |
| 7–8 | SAT, SMT, and decision procedures (Z3) |
| 9 | Transition systems, invariants, SMV |
| 10 | *Project proposal talks* |
| 11, 12 | Temporal logic: LTL, CTL, ω-words, Büchi automata |
| 13–14 | Model checking: explicit, symbolic, bounded (nuXmv) |
| 15–17 | Program analysis: CBMC, deductive verification, abstract interpretation |
| **18–21** | **Interactive theorem proving: Lean 4, then Cslib in two parts** |
| 22 | *Project milestone* |
| 23–24 | AI for formal methods: autoformalization, proof search, the soundness gap |
| 25–26 | Neural network verification |
| 27–28 | Final project presentations |

**Grading:** 50% project · 20% homeworks · 10% quizzes · 20% case studies, discussions, and
participation.

**Nine structured discussions** run inside those sessions — weekly for the first five weeks, then
every other week, 30 minutes each, think–pair–share. Topics include *Has AI ever killed anyone?*,
*Are LLMs theft?*, *Can we verify what we cannot specify?*

Each packet opens with a **case-study background** — 400–550 words on what happened, when and
where, and what the investigation, court, or regulator actually found — written for someone who has
never heard of it. Then a dated timeline, three to five genuinely contested questions, and 5–10
fetch-verified sources chosen to include some that cut against the framing. After each session you
submit a one-paragraph reflection. See [`discussions/`](discussions/README.md) and
[`participation.md`](discussions/participation.md).

## Tooling

Everything has a zero-install path. Students are never required to build a toolchain locally.

- **Lab spine:** [`ttj/fmaiv`](https://github.com/ttj/fmaiv) — a short course threading one bounded
  counter through Z3, nuXmv, Lean, CBMC, and Cryptol, with a Codespaces container and Colab
  notebooks. The homeworks follow that thread.
- **Z3:** in-browser at <https://microsoft.github.io/z3guide/>
- **Model checking:** smvis in-browser; NuSMV in the container (nuXmv is licence-gated)
- **Lean 4:** <https://live.lean-lang.org/> for week 1;
  [Cslib](https://github.com/leanprover/cslib) work happens in Codespaces or locally
- **NN verification:** Colab notebooks; VNN-COMP 2026 benchmarks

**Lean version pin for the term: Lean v4.33.0 + Mathlib v4.33.0 + Cslib v4.33.0.** Do not follow
Cslib's README, which points at `main` and pulls a release-candidate toolchain. Details in
[`labs/README.md`](labs/README.md).

## What changed from Fall 2025

| Change | Why |
|---|---|
| **Project topics are provided** (8 defined topics) | Free proposal produced uneven scoping and one team that changed direction after the milestone and could not recover. |
| **The milestone is a gate** — a verifier must run | The most common Fall 2025 milestone feedback was "you need to get going on the formal side." |
| **Five homeworks added** (20%) | Previously project-plus-participation only, so students met the tools for the first time inside their projects. |
| **Five quizzes added** (10%) | Cheap early signal on whether the reading is landing. |
| **Repository required at proposal time** | Repo links used to surface at the milestone or later. |
| **Theorem proving expanded to four sessions + Cslib** | Deliberate deepening. Cslib did not exist in Fall 2025; it is split across two sessions so the ω-automata material does not get cut live. |
| **AI-risk unit compressed 4 sessions → 3** | To fund the above. Case studies are folded into the lecture sessions rather than standing alone. |
| **Nine structured discussions added** | The course had case studies but no scheduled discussion time. 89 verified references across nine contested questions. |
| **Team size: four ideal, three with an undergraduate, graduate pairs allowed** | ABET teamwork assessment, attrition risk, Showcase logistics — and team size is a Showcase judging metric. |
| **Currency pass on every citation** | Standards, tool versions, and competition results all moved. See [`LINK-AUDIT.md`](LINK-AUDIT.md). |

## Keeping this repo and the instructor repo in step

Every fact that appears in more than one place — a date, a weight, a discussion title, a due date —
lives once in [`course.yml`](course.yml). The markdown is checked against it rather than trusted.

```
make check     # 14 consistency and leak checks (fast, no network)
make links     # every cited URL; fails only on conclusively dead ones
make pdf       # rebuild the syllabus PDF and stamp its source hash
```

**`make check` enforces:** packet headers, section order, and both index tables match `course.yml`;
the 💬 markers sit on the right sessions; manifest dates appear in the syllabus; grading weights sum
to 100 and agree across the syllabus and `participation.md`; the reflection spec is worded
identically everywhere; the reading-list invariant (89 URLs, 3 unverified marks) is intact; internal
links resolve; the committed PDF was built from the current markdown; no scratch or draft files; and
**nothing instructor-only has leaked into this repo** — run sheets, answer keys, instructor voice
("assign only pp. 1–2"), secrets, or student data.

That last one is not theoretical. During drafting, four agent scratch files and 89 instructor-voice
reading annotations reached this repo before being caught by hand. The check exists so the next one
is caught by CI.

**CI** runs the consistency and PDF checks on every push and PR, and the link check weekly.
The private instructor repo vendors a copy of `course.yml`, validates its guides against it, and
opens a sync PR to itself when this file changes. See that repo's README for the one-time token
setup.

**If you change a date:** edit `course.yml`, run `make check`, fix whatever it names, and commit.
The instructor repo will follow within a day, or immediately if the dispatch token is configured.

## Repository conventions

- `main` is the published state. Work lands via pull request.
- **This repository is shared with the class.** Nothing instructor-only belongs here — no run
  sheets, no answer keys, no grading internals. Those live in a separate private repository. Before
  merging anything, ask whether you would be content for a student to read it.
- No student data, ever — no rosters, no submissions, no grades. This repo is private, but the
  rule holds regardless.
- No credentials, no `.env`, no cloud keys.
- Markdown is the source of truth; PDFs are generated. **When you change `syllabus/syllabus.md`,
  run `make pdf` and commit the regenerated PDF in the same commit** — git does not preserve
  mtimes, so a stale PDF on `main` will not announce itself.
- `make links` re-checks every URL in the repo. Run it at the start of each term; see
  [`LINK-AUDIT.md`](LINK-AUDIT.md) for hosts that block automated checkers but are live in a
  browser, so you don't "fix" a working link.

## Licence

Course materials © 2026 Taylor T. Johnson. Third-party materials are cited and remain under their
own licences.
