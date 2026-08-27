# Project rubrics — CS 3892 / 5892, Fall 2026

Point totals are out of 50, matching the project's 50% share of the course grade: proposal 5, milestone 10, and the final 35 &mdash; report 15, presentation and demo 10, artifact quality 10.

These rubrics are published in advance because you should be able to predict your grade. If you
can read the rubric and cannot tell what you would score, tell me and I will fix the rubric.

---

## Proposal — 5 points

| Criterion | Pts | What full marks looks like |
|---|---:|---|
| Topic and scope | 1 | A menu topic (or an approved own topic), scoped to one semester for this team size. Not "we will survey X." |
| **FM half identified** | 1 | The specific method and the specific tool, plus what verdict you expect it to produce. |
| **AI half identified** | 1 | FM4AI or AI4FM stated explicitly, in one sentence, without hand-waving. |
| Data / benchmark | 0.5 | Named, with evidence of access. Credentialing (PhysioNet, cloud credits) already in motion. |
| Success criterion | 0.5 | Falsifiable. States what a *negative* result would look like and why it would still be worth reporting. |
| Responsibilities + repository | 0.5 | Who does what, concretely. Repository exists, is non-empty, has a README. |
| Risks and fallback | 0.5 | The most likely failure mode named, with a fallback plan. |

**Lightning talk** is graded within the above: 5–7 slides, 5–10 minutes, **names on the title
slide**, and you can show your primary tool producing output on a toy input.

Common ways to lose points: no fallback; "we'll use AI to help write code" offered as the AI half;
a success criterion that cannot fail.

---

## Milestone — 10 points

| Criterion | Pts | What full marks looks like |
|---|---:|---|
| **Gate: a verifier runs** | 3 | Your tool executes and produces real output on real input — not a plan, not a trained model with nothing checking it. Demonstrated live or by recording. |
| Progress since proposal | 2 | Substantive movement on both halves. Changes of direction are fine, and are explained. |
| Technical depth | 2 | You can answer questions about *why* the tool says what it says, not just what it printed. |
| **Mathematical formulation** | 1 | Every technical term you use is defined *mathematically* on a slide. If your project mentions RMSE, RUL, monotonicity, or robustness, there is a formula. |
| Presentation quality | 1 | Names on title slide. Consistent axes, fonts, and units across figures. No slide so dense it cannot be read from the back. |
| Repository and process | 1 | Public/accessible repo, real commit history distributed across the semester, README that explains how to run it. |

The gate is worth 3 of 10 on its own, and a team that does not clear it cannot earn full marks on
the final either — by mid-November there is not enough time left to do the remaining work
properly. This is stated plainly here so that nobody is surprised in December.

---

## Final report — 15 points

| Criterion | Pts | What full marks looks like |
|---|---:|---|
| Problem and motivation | 1 | Why this matters, for someone who is not in this class. |
| Background | 1 | Enough for a reader to follow; correct; cited. |
| **Approach** | 4 | FM and AI components clearly delineated. Design choices justified, including the ones that did not work out. |
| Implementation | 1 | What you actually built, at a level of detail that lets someone rebuild it. |
| **Evaluation** | 4 | Quantitative results against the success criterion from the proposal. Baselines where meaningful. Negative results reported, not buried. Enough runs to distinguish signal from noise. |
| Related work | 1 | Positioned, not listed. (Graduate students: 8–12 papers making an argument.) |
| Threats to validity | 1 | What could make your conclusion wrong. Graduate students test at least one. |
| Writing and format | 1 | ACM or IEEE conference format, 6–10 pages, readable figures, correct citations. |
| Responsibilities + AI disclosure | 1 | Both present and specific. |

*Approach and Evaluation carry more than half of the report between them, deliberately: they are
where the FM half and the AI half either meet or do not.*

A report that reports a *negative* result honestly and analyzes why can score full marks. A report
that quietly reframes the question so the result looks positive cannot.

---

## Final presentation and demo — 10 points

| Criterion | Pts | What full marks looks like |
|---|---:|---|
| Structure and clarity | 3 | ~15 minutes, well paced, the audience knows what you did and why by minute three. |
| **Demo** | 3 | Something runs. Live if possible; recorded is acceptable. A demo that shows the *verifier*, not just the model, scores highest. |
| Technical accuracy | 2 | Claims are precise. "Verified" and "tested" are not used interchangeably. |
| Handling questions | 1 | You can say "we don't know" and mean it. |
| Slide craft | 1 | Names on the title slide; consistent figures; mathematical definitions present. |

---

## Artifact quality and reproducibility — 10 points

| Criterion | Pts | What full marks looks like |
|---|---:|---|
| **Reproducibility** | 4 | A grader follows your README and reproduces your headline result. This is tested, not assumed. |
| Code quality | 2 | Organized, readable, no dead scaffolding, no secrets committed. |
| Data and models | 2 | Included or fetchable by a documented script; licences and provenance stated. |
| Documentation | 1 | README covers setup, run, and expected output. |
| Commit history | 1 | Work distributed across the semester by more than one person. |

### The Showcase poster (within the final presentation score)

The poster or video file due **Thursday December 3** is graded as part of the final presentation
block, not separately. Full marks means: the problem and the need are legible to a judge from
outside formal methods in under a minute; there is something *visual* (a counterexample trace, a
caught-vs-missed comparison, a short screen recording); and the formal result is stated precisely
rather than vaguely ("nuXmv found a violation at depth 9," not "we verified the system").

The poster is **required for undergraduate teams** and encouraged for graduate teams. A missing
poster costs points here **and** removes the team from 40AU award consideration entirely — see
[syllabus §12](../syllabus/syllabus.md#12-cs-project-requirement-immersion-and-the-showcase).

**Never commit:** API keys, `.env` files, cloud credentials, or any dataset you are not licensed
to redistribute. A committed credential is an automatic deduction and, more importantly, an
incident — tell me immediately and we will rotate it.

---

## Graduate students (CS 5892)

Graduate work is assessed on the same rubrics with a higher expectation at every level, plus these
components folded into the report and evaluation rows:

| Component | Where it is graded |
|---|---|
| Related-work survey, 8–12 papers, making an argument | Final report — related work |
| Second independent evaluation axis (dataset, tool family, or ablation) | Final report — evaluation |
| Threats to validity with at least one testing experiment | Final report — threats |
| Workshop-submission-quality writing | Final report — writing |

In mixed undergraduate/graduate teams these components are owned by the graduate members and that
ownership must appear in the responsibility breakdown.

---

## Peer and self assessment

At the milestone and at the end, each member submits a short confidential assessment of the team's
division of work, including their own. These do not automatically change grades, but a consistent
picture across a team of one member not contributing will, after I talk to the team.
