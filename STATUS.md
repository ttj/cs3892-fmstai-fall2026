# Status and open items

Last updated: **2026-08-16**

The syllabus, schedule, homework specs, project topics, and rubrics are drafted and internally
consistent. Below is what still needs a decision or an external confirmation.

## Needs confirmation from Vanderbilt

| # | Item | Detail | Who |
|---|---|---|---|
| 1 | **Cross-listing with CS 5892** | Only `2026F.1.CS.3892.02` is provisioned in Brightspace (OU 646125, currently empty). The Fall 2025 syllabus was headed "CS3892/CS5892." The materials assume cross-listing and specify differentiated graduate requirements throughout; if the 5892 section is not created, delete §7's graduate paragraph and the grad rows in the rubrics. | Registrar / DGS |
| 2 | **Immersion Showcase date** | The CS Immersion page states **Thu Dec 10, 2026, 5–7 p.m., Adams Atrium, Featheringill Hall**. It is single-sourced: no Events@Vanderbilt entry, and the College of Connected Computing page still shows only Spring 2026. It also falls on the **last day of classes**, which is a real scheduling constraint for a project course. | Prof. Robert Tairas (CS Immersion Coordinator) |
| 3 | **Room and meeting time** | Syllabus assumes T/R 11:00–12:15, per Fall 2025. Room TBA. | Registrar |
| 4 | **TA assignment** | Syllabus has a TBA placeholder. Fall 2025 had one TA. | Department |
| 5 | **Graduate academic calendar** | The registrar's 2026–27 page is the *undergraduate* calendar. The Graduate School publishes a separate one whose add/drop dates may differ for a 5892 section. | Graduate School |

## Decisions still open

| # | Item | Recommendation |
|---|---|---|
| 6 | **Cslib build cost** | Cslib's ~200 Lean files have no prebuilt object cache and compile locally on first build. This has not been timed. Time a cold build on a representative student laptop before Unit 8, and if it is bad, ship a prebuilt container or self-host a `lean4web` instance with Cslib preloaded. |
| 7 | **AWS credits** | Project topic 3 (guardrails / Automated Reasoning checks) needs Bedrock access. Apply for AWS Educate or research credits before the term so teams are not blocked in October. |
| 8 | **Case-study assignment mechanism** | Participation includes each student leading one in-class case study. Decide whether to assign from the menu in the research brief or let students claim topics; either way, publish the sign-up in week 1. |
| 9 | **Quiz question banks** | Coverage and format are specified in `quizzes/README.md`; the actual question banks are not yet written. Five banks of ~12 questions each, to be built in Brightspace. |
| 10 | **Homework starter repos** | The homework specs reference `ttj/fmaiv` starters, which exist. Whether to fork per-assignment starter repos (GitHub Classroom) or point at FMAIV directly is undecided. Classroom gives autograding; direct pointing is less setup. |
| 11 | **Textbook for the Lean unit** | Recommendation: *Functional Programming in Lean* as the gentle path, *Hitchhiker's Guide to Logical Verification* (2026 ed.) as the verification-focused one. Neither is required; pick one to assign readings from. |

## Not yet written

- Quiz question banks (item 9).
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
