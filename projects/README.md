# Term Project — CS 3892 / 5892, Fall 2026

**50% of the course grade.** This is a project course: for undergraduates it satisfies the CS
Project requirement and can be used for Vanderbilt's Immersion requirement, which means the
project is not an assignment attached to a course — it is the course's deliverable.

- **[Topic menu](project-topics.md)** — eight worked topics with tools, benchmarks, and success
  criteria. Read this first.
- **[Rubrics](rubrics.md)** — how each deliverable is graded.

## What changed from Fall 2025, and why

Three changes, each in response to something that actually happened last year.

**1. Topics are provided.** In Fall 2025 students proposed freely. The results were uneven: the
strong teams were strong, but several spent weeks converging on a question, and one changed
direction after the milestone and never recovered the lost time. Choosing from a menu removes that
failure mode without removing ambition — every topic on the menu has a stretch goal that is
genuinely open. Self-proposed topics are still allowed, with a higher bar.

**2. The milestone is a gate, not a check-in.** Last year's most common milestone feedback was a
version of *"great start, but you need to get going on the formal side."* By the milestone you
must have a **verifier that runs and produces output**. Not a plan for one. A team without running
formal tooling at the milestone cannot earn full marks on the final regardless of what arrives in
December, because at that point there is not enough semester left to do the work properly.

**3. Version control from day one.** Last year repository links surfaced at the milestone or later,
and in one case not at all. A public or instructor-accessible Git repository is required at
**proposal** time, and commit history is part of the final grade — not to police you, but because
a project with three commits on the last night did not happen the way the report claims.

## Teams

Two to four members. Undergraduates using this course for the CS Project requirement **must** be
on a team. Solo projects need instructor approval and are held to the same total scope.

Every deliverable includes a **responsibility breakdown**: who did what, concretely. "Everyone
contributed equally" is not a responsibility breakdown.

## Deliverables

| Deliverable | Weight | When | Format |
|---|---|---|---|
| Proposal (report + lightning talk) | 5% | ~Week 6 | 1–3 pages + 5–7 slides, 5–10 min |
| Milestone (presentation + running artifact) | 10% | ~Week 11 | ~8 slides, 8–15 min, **live tool demo** |
| Final (report + presentation + demo + artifacts) | 35% | Finals period | 6–10 pages + ~15 min + repository |

Exact dates are on the [course schedule](../schedule/schedule.md).

### Proposal — ~Week 6

**Report (1–3 pages).** Must contain, explicitly labelled:

1. **Topic** — which menu topic, or your own (pre-approved).
2. **The FM half** — which method, which tool, what verdict you expect it to produce.
3. **The AI half** — is the AI the subject (FM4AI) or the instrument (AI4FM)? One sentence.
4. **Data or benchmark** — named, with evidence you can access it. If it needs credentialing
   (PhysioNet, cloud credits), say where you are in that process.
5. **Success criterion** — a falsifiable statement of what "it worked" means. Also: what a
   *negative* result would look like, and why it would still be worth reporting. Projects whose
   only possible outcome is success are usually projects that measure nothing.
6. **Responsibility breakdown** — who does what.
7. **Repository URL** — created, non-empty, with a README.
8. **Risks and fallback** — the most likely way this fails, and what you do then. Last year's
   real failures were OOM on large networks, dataset access delays, and Lean's learning curve.

**Lightning talk.** 5–7 slides, 5–10 minutes. Names on the title slide — every year this has to
be said, so it is now a graded line item.

**Already-satisfied requirement:** by proposal day you must have run your primary tool **once**,
on a toy input, and be able to show the output. This is not a demo; it is proof that the
toolchain exists on your machine and that you will not discover in November that it does not
build.

### Milestone — ~Week 11

~8 slides, 8–15 minutes, live. Structure (from the Fall 2025 template, which worked):

1. Title slide **with names**
2. Motivation and overview — one slide, brief recap
3. Changes since the proposal — one slide, if any
4. Approach — 1–2 slides, with repository links, highlighting the FM and AI components
5. **Demo** — a live or recorded run of your tooling. **Required.**
6. Preliminary results — 1–2 slides
7. Remaining work — one slide
8. Questions and issues — one slide

**The gate:** a verifier runs and produces output. Trained models with no verification, or a
formal model with nothing checking it, do not clear the gate.

**On presenting mathematically.** Define your terms. If your project mentions RUL, RMSE, MAE,
monotonicity, or robustness, define each one *mathematically* on a slide. "It's the root mean
square error" is not a definition; a formula is. This was the single most repeated piece of
Fall 2025 slide feedback.

**On plot hygiene.** Consistent axes, fonts, and units across figures. Inconsistent plot styles
read as work assembled the night before, and graders are not wrong to read them that way.

### Final — Finals period

**Report, 6–10 pages, ACM or IEEE conference format** (LaTeX strongly preferred; Overleaf is
free through Vanderbilt). Target: something a workshop programme committee would take seriously.

Required sections: introduction and motivation · background · approach (with the FM and AI
components clearly delineated) · implementation · evaluation with quantitative results ·
related work · threats to validity · conclusions and future work · responsibility breakdown ·
**AI-use disclosure**.

**Presentation.** ~15 minutes plus questions, in class during the last week or the finals slot.

**Demo.** Required. Live if possible, recorded if not. Something must actually run.

**Artifacts.** Repository containing code, models, scripts, and a README that lets a stranger
reproduce your headline result. Reproducibility is graded: a grader will follow your README, and
what they get is what you get.

**Immersion Showcase.** Undergraduates using this course for the CS Project and/or Immersion
requirement must present at the School of Engineering Immersion Showcase (early December —
confirm the date with the instructor by mid-October). Plan a poster or demo accordingly.

## Grading weights within the project

| Component | Share of the 50% |
|---|---|
| Proposal | 10% (5 pts of 50) |
| Milestone | 20% (10 pts of 50) |
| Final report | 40% (20 pts of 50) |
| Final presentation and demo | 20% (10 pts of 50) |
| Artifact quality and reproducibility | 20% (10 pts of 50) |

Detailed rubrics: [rubrics.md](rubrics.md).

## Publication

A good project here is a workshop paper. Several venues take undergraduate work seriously —
NFM, SAIV, FMCAD student sessions, AAAI/NeurIPS workshops on trustworthy AI, and the VNN-COMP
and ARCH communities. If your project lands well, talk to the instructor about where to send it.
This is offered, not required, and it does not affect your grade.
