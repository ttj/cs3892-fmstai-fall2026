# Final project — presentation, report and artifacts

CS 3892 / 5892 — Formal Methods: Safe and Trustworthy AI · Fall 2026

**Worth 35 of the project's 50 points**: report 15, presentation and demo 10 (the Showcase poster is
graded here), artifacts 10. **One submission per team** (any member submits for the team), to
Brightspace → Assignments → *Project final submission — report and artifacts*.

## What to submit, and when

| What | When |
|---|---|
| **Showcase poster file** (undergraduate teams; its own folder) | **Thu Dec 3, 11:59 p.m.**, not extendable |
| **Monitor and power reservation** for the Showcase (one per team, if you want either) | **Mon Dec 7** (form link in the Brightspace announcement) |
| **Presentation slides**, one PDF, to the final folder | **11:00 a.m. on the day you present**, before class |
| **Presentation and live demo**, in class | **Tue Dec 8 or Thu Dec 10** (the order will be announced) |
| **Report** (PDF) **and repository**, to the final folder | **Fri Dec 18, 11:59 p.m.** |

Put the **repository link** and the **commit you want graded** on the report's first page and on
your title slide. Late days do not apply to project deliverables.

## The presentation: about 15 minutes, then questions

- **What you did and why, by minute three**, then the approach, the evaluation, and what you learned.
- **A demo, required.** Your verifier, or the formal-methods tool your project depends on, runs on
  real input. Live if possible; bring a short recording as a fallback. A demo that shows the
  *verifier*, not just the model, scores highest.
- **Precise claims.** "Verified" and "tested" are not interchangeable. Every technical term is
  defined mathematically on a slide.
- Names on the title slide; figures readable from the back of the room.

## The report: 6–10 pages, ACM or IEEE conference format

LaTeX strongly preferred (Overleaf is free through Vanderbilt). Required sections: introduction and
motivation · background · **approach**, with the formal-methods and AI components clearly
delineated · implementation · **evaluation** with quantitative results against the success
criterion in your proposal, baselines where meaningful, and negative results reported · related
work · threats to validity · conclusions and future work · **responsibility breakdown** (who did
what, concretely) · **AI-use disclosure**.

A report that reports a negative result honestly and analyzes why can score full marks. A report
that quietly reframes the question so the result looks positive cannot.

**Graduate students (CS 5892)** also own, and say so in the responsibility breakdown: a related-work
survey of 8–12 papers that makes an argument; a second independent evaluation axis; threats to
validity with at least one testing experiment; workshop-quality writing.

## The artifacts: a stranger can reproduce your headline result

A grader follows your README and tries to reproduce your headline result; what they get is what you
get. The README covers setup, how to run, and the expected output. Data and models are included or
fetched by a documented script, with licences and provenance stated. **Never commit** API keys,
`.env` files or credentials; if one slips in, tell me immediately.

## Peer and self assessment

Each member submits a short confidential assessment of the team's division of work, including their
own, with the final. How to submit it will be posted on Brightspace before Dec 8.

## How it is graded — 35 points

| Block | Points | Where most of the points are |
|---|---:|---|
| Report | 15 | Approach (4) and Evaluation (4) |
| Presentation and demo, including the poster | 10 | Structure (3) and Demo (3) |
| Artifact quality and reproducibility | 10 | Reproducibility (4) |

The full rubrics, criterion by criterion, are in `projects/rubrics.md` in the course repository.
A team that did not clear the milestone's gate cannot earn full marks on the final.
