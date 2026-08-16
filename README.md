# CS 3892 / CS 5892 — Formal Methods: Safe and Trustworthy AI

**Vanderbilt University · Fall 2026 · Tuesday & Thursday, 11:00 a.m. – 12:15 p.m.**
Instructor: [Taylor T. Johnson](https://www.taylortjohnson.com)

Course materials: syllabus, schedule, homeworks, project topics, and rubrics.

> **Status: pre-semester draft.** Items marked **[confirm]** await institutional confirmation
> (cross-listing, room, TA, Immersion Showcase date). See [`STATUS.md`](STATUS.md) for the open list.

## Contents

| Path | What it is |
|---|---|
| [`syllabus/syllabus.md`](syllabus/syllabus.md) | The syllabus. [PDF](syllabus/syllabus.pdf) |
| [`schedule/schedule.md`](schedule/schedule.md) | All 28 sessions, with every homework, quiz, and project deadline |
| [`projects/README.md`](projects/README.md) | Project instructions and deliverables |
| [`projects/project-topics.md`](projects/project-topics.md) | **Eight defined project topics** with tools, benchmarks, and success criteria |
| [`projects/rubrics.md`](projects/rubrics.md) | How each project deliverable is graded |
| [`assignments/README.md`](assignments/README.md) | The five homeworks |
| [`quizzes/README.md`](quizzes/README.md) | Quiz format and coverage |
| [`labs/README.md`](labs/README.md) | Tool setup, zero-install paths, and the Lean version pin |
| [`LINK-AUDIT.md`](LINK-AUDIT.md) | Every URL in the course materials, checked and dated |

## The course in one paragraph

Generative AI industrialized software *production* without a matching advance in software
*validation*. Formal methods are the part of computer science that produces guarantees rather than
test results. This course covers the guarantees — SAT/SMT, model checking, abstract interpretation,
interactive theorem proving, neural network verification — and asks what they can cover when the
artifact under scrutiny is a neural network or an agent (**FM4AI**), and whether AI can finally
make these methods cheap enough to use routinely (**AI4FM**). Students apply both directions in a
semester-long team project that satisfies the CS project and Immersion requirements.

## Structure at a glance

| Weeks | Unit |
|---|---|
| 1 | Framing: the verification triple; FM4AI and AI4FM |
| 2–3 | AI failure modes, risk frameworks, regulation; guardrails vs. solver-backed checks |
| 4 | Logic and preliminaries |
| 5 | SAT, SMT, and decision procedures (Z3) |
| 6 | Transition systems, invariants, SMV · *proposal talks* |
| 7 | Temporal logic: LTL, CTL, Büchi automata |
| 8 | Model checking: explicit, symbolic, bounded (nuXmv) |
| 9–10 | Program analysis: CBMC, deductive verification, abstract interpretation |
| 11–12 | Interactive theorem proving: Lean 4 and Cslib · *milestone* |
| 13 | AI for formal methods: autoformalization, proof search, the soundness gap |
| 14 | Neural network verification |
| 15 | Final project presentations |

**Grading:** 50% project · 20% homeworks · 10% quizzes · 20% case studies and participation.

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
| **Theorem proving expanded to three sessions + Cslib** | Deliberate deepening; Cslib did not exist in Fall 2025. |
| **AI-risk unit compressed 3 weeks → 2** | To fund the above, with fresher case studies. |
| **Currency pass on every citation** | Standards, tool versions, and competition results all moved. See [`LINK-AUDIT.md`](LINK-AUDIT.md). |

## Repository conventions

- `main` is the published state. Work lands via pull request.
- No student data, ever — no rosters, no submissions, no grades. This repo is private, but the
  rule holds regardless.
- No credentials, no `.env`, no cloud keys.
- Markdown is the source of truth; PDFs are generated (`make pdf`).

## Licence

Course materials © 2026 Taylor T. Johnson. Third-party materials are cited and remain under their
own licences.
