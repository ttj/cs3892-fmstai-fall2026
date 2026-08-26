# Status and open items

Last updated: **2026-08-16** · syllabus is share-ready; both repos green

The syllabus, schedule, homework specs, project topics, and rubrics are drafted and internally
consistent. Below is what still needs a decision or an external confirmation.

## Needs confirmation from Vanderbilt

| # | Item | Detail | Who |
|---|---|---|---|
| 1 | ~~**Cross-listing with CS 5892**~~ **— RESOLVED** | Confirmed by the instructor: 3892 and 5892 are **the same course, taught together, in one Brightspace shell** (OU 646125). The only difference is **extra coursework for the graduate students**. So: no second OU, no separate section, no duplicated grade structure — just the differentiated project components already specified in syllabus §7 and the rubrics. | — |
| 2 | ~~**Immersion Showcase date**~~ **— CONFIRMED** | **Thu Dec 10, 2026, 5–7 p.m., Adams Atrium, Featheringill Hall**, confirmed against the engineering page and the coordinator's pre-semester announcement. Poster/video files due **Thu Dec 3**; 40AU awards $3,500/$1,000/$500. Note it falls on the **last day of classes**. The CCC copy of the page (`computing.vanderbilt.edu/cs-immersion-showcase/`) is stale — still showing Spring 2026 — so do not send students there. | — |
| 3 | ~~**Room and meeting time**~~ **— RESOLVED** | T/R 11:00–12:15 in **Featheringill Hall (FGH) 209**. In the syllabus header, §4, and `course.yml` (checked). | — |
| 4 | ~~**TA assignment**~~ **— RESOLVED** | **Michaela Winfree** (michaela.winfree@vanderbilt.edu), the same TA as Fall 2025. Named in syllabus §1. TA office hours still to be announced. | — |
| 5 | **Graduate academic calendar** | The registrar's 2026–27 page is the *undergraduate* calendar. The Graduate School publishes a separate one whose add/drop dates may differ for a 5892 section. | Graduate School |

## Decisions still open

| # | Item | Recommendation |
|---|---|---|
| 6 | ~~**Cslib build cost**~~ **— MEASURED 2026-08-16, resolved** | Cold build of the pinned triple is **1 m 34 s wall on a 24-core machine** (2,803 jobs, 1066% CPU ≈ 17 CPU-minutes, peak RSS 3.1 GB). Dependency fetch including the Mathlib cache adds ~1 m 45 s. Extrapolating to a 4-core/8-thread student laptop: **roughly 5–10 minutes of compilation, ~10 minutes end to end.** That is fine — no container or self-hosted `lean4web` is needed. **The real constraint is disk: ~10.7 GB** (7.8 GB project `.lake` + 2.9 GB toolchain), and **RAM: budget 4 GB free.** Tell students in week 1 so nobody discovers it on Oct 29. Full method in `labs/README.md`. |
| 7 | **AWS credits** | Project topic 3 (guardrails / Automated Reasoning checks) needs Bedrock access. Apply for AWS Educate or research credits before the term so teams are not blocked in October. |
| 8 | **Case-study assignment mechanism** | Participation includes each student leading one in-class case study. Decide whether to assign from the menu in the research brief or let students claim topics; either way, publish the sign-up in week 1. |
| 9 | **Quiz question banks** | Coverage and format are specified in `quizzes/README.md`; the actual question banks are not yet written. Five banks of ~12 questions each, to be built in Brightspace. |
| 10 | **Homework starter repos** | The homework specs reference `ttj/fmaiv` starters, which exist. Whether to fork per-assignment starter repos (GitHub Classroom) or point at FMAIV directly is undecided. Classroom gives autograding; direct pointing is less setup. |
| 11 | **Textbook for the Lean unit** | Recommendation: *Functional Programming in Lean* as the gentle path, *Hitchhiker's Guide to Logical Verification* (2026 ed.) as the verification-focused one. Neither is required; pick one to assign readings from. |

## Where to pick up

**Both repos are green, `main` only, nothing unpushed.** The anti-drift CI is live and the
`COURSE_SYNC_TOKEN` is working (verified 2026-08-16; **expires 2027-01-31**).

Deliberately paused, at the instructor's request, until the course sequence and syllabus have been
reviewed in detail:

- quiz question banks (5 × ~12 questions)
- individual homework handout files
- project proposal / milestone / final handout documents
- the currency pass over the ~20 Fall 2025 lecture decks — the largest remaining job; the
  correction list is under *Currency notes to carry into the slides* below

Time-sensitive and independent of that review:

- **The nine Brightspace reflection assignments** — D1 is the first day of class, **Aug 27**. Spec
  is in the instructor repo at `brightspace/discussion-setup.md`; build once, one shell (OU 646125).
- **Immersion funding** — fall cycle closes **Sep 14**; $1,000/student for Senior Design.
- **AWS credits** — needed before project topic 3 is viable.
- **Sharing this repo with the class** — still private with one collaborator. If it is made public,
  `COURSE_SYNC_TOKEN` becomes unnecessary.

**Any change to a date, weight, title, or due date starts in `course.yml`**, then `make check`.
That is what keeps the two repos from drifting.

## Confirmed since the first draft

- **Final exam slot: Mon Dec 14, 2026, 9:00 a.m.** — the registrar's block for an 11:00–12:15 TR
  course. No exam is planned, but the slot is reserved and the syllabus now names it, along with
  the condition under which one would be added. Engineering allows three hours and gives no
  alternate sitting.
- **Thanksgiving.** The registrar states the range as Nov 22–29, but both endpoints are Sundays;
  the weekdays actually lost are Mon Nov 23 – Fri Nov 27. For a T/R course that is Nov 24 and
  Nov 26, which is what the schedule assumes. The earlier syllabus wording implied the
  university-wide range was two days, which was wrong.
- **Oct 30** is three coinciding 11:59 p.m. deadlines (withdraw, pass/fail election, pass/fail →
  graded), plus medical underload at 4:00 p.m. They are independently changeable in future years,
  so they are listed separately.
- **Immersion funding: $1,000 per student for Senior Design.** Monthly cycles (Sep 15, Oct 15,
  Nov 16, Dec 10); the fall cycle closes **Sep 14** per the page's prose, though its own table says
  Sep 15 — advise Sep 14. A funding workshop is required annually, and money lands 4–6 weeks after
  notification, so this has to be started in September.
- **Robert Tairas** is Immersion Coordinator for Computer Science (377 Jacobs Hall).
- **Room: Featheringill Hall (FGH) 209.**
- **CS 3892 and CS 5892 are one course in one Brightspace shell**; graduate students differ only in
  extra coursework.
- The 40AU award structure, poster deadline, and judging metrics are **not published** on any
  public Immersion page — they come from the coordinator's instructor announcement. Syllabus §12
  says so, so nobody wastes time looking for a URL.

## Repository split (2026-08-16)

This repo is **shared with the class**. Instructor-only material moved to a separate private
repository, `ttj/cs3892-fmstai-fall2026-instructor`:

- the nine think–pair–share **run sheets** (minute-by-minute choreography, prompt assignment, how to
  reopen a discussion that converges early),
- the nine **"do not assert these"** lists,
- the **Brightspace build plan** for the reflection assignments.

Links to the nine Gamma intro decks live there too. Before merging anything into *this* repo, ask
whether you would be content for a student to read it.

## Not yet written

- Quiz question banks (item 9).
- **The nine Brightspace reflection assignments and their grade items.** Specified in the instructor
  repo (`brightspace/discussion-setup.md`) but not built — Brightspace auth was deliberately left
  alone. D1 is on the first day of class, so this needs doing before Aug 27.
- Individual homework handout files. `assignments/README.md` specifies all five in enough detail to
  write them; each still needs a standalone handout with starter code links and a submission
  checklist.
- Lecture slides. Fall 2025 decks exist (~20 decks, 700+ slides) and are the base; the currency
  corrections in `LINK-AUDIT.md` and the research brief tell you what to change.
- Project proposal / milestone / final handout documents. Fall 2025 versions exist and are largely
  reusable; `projects/README.md` supersedes their structure.

## Currency notes to carry into the slides

**Scope note.** These apply to the **Fall 2025 lecture decks**, which have not been read
line-by-line. They are *not* corrections to the Fall 2025 syllabus: that document was extracted and
checked directly, and it never mentioned the EU AI Act, EASA, NIST AI 100-1, or Cslib at all. What
it did cite — the NIST AI RMF landing page, AI 600-1, AI 100-2 E2025, ISO/IEC 24029-2, Microsoft's
failure-modes taxonomy, `lean-lang.org` — was verified still-current, with one exception: the dead
`rise4fun.com/z3` link. Treat the list below as a checklist to run against the decks, not as a
record of errors already found in them.

Full detail in the research brief; the short list:

- **EU AI Act** — if any deck dates high-risk obligations from Aug 2026, that is now wrong:
  Regulation (EU) 2026/1744 moved them to Dec 2027 / Aug 2028. What lands 2 Aug 2026 is
  **Article 50 transparency**.
- **NIST AI RMF** — still 1.0, but under revision per the July 2025 AI Action Plan. Teach it as a
  live document. AI 100-1 and the RMF landing page are the same thing.
- **DoD Responsible AI Toolkit** — renamed the **AI Assurance (AIA) Toolkit**.
- **EASA** — current position is Proposed Issue 03 (June 2026); AI touching DAL A/B remains outside
  accepted means of compliance.
- **AI theorem proving** — the Fall 2025 headline (Aristotle, IMO 2025 gold) is now baseline.
  miniF2F is saturated and no longer discriminates. Be careful with IMO 2026 claims: the widely
  reported 42/42 results are natural-language and self-administered, and the one public set of Lean
  proofs used **machine-generated formal statements**, which is precisely the soundness gap the
  course should teach.
- **Erdős #728** (Jan 2026) — the first such result to survive scrutiny, and it survived *because*
  it was formalized in Lean. This is the course's thesis delivered by current events; it belongs in
  week 1 and again in Unit 9.
- **VNN-COMP 2026** ran 24–25 July 2026 at SAIV/FLoC in Lisbon. Results are public even though the
  summary report is not out yet. α,β-CROWN has now won **six** consecutive years (its own repo
  description still says 2021–2025). **VNN-LIB 2.0** shipped Dec 2025 with a formal semantics
  mechanized in Agda — a 2025 lecture treating VNN-LIB as a fixed informal format is now wrong.
- **Marabou** is no longer a VNN-COMP competitor; keep it as a teaching tool.
- **AWS Bedrock Automated Reasoning checks** went GA Aug 2025 and gained substantial capability
  through 2026. The translate/validate split — LLM translation that "may contain errors" feeding a
  step that is "mathematically sound" — is the single best classroom illustration of where
  soundness actually lives in a hybrid system.
