# Homeworks — CS 3892 / 5892, Fall 2026

Five homeworks, roughly biweekly, **20% of the course grade** (4% each).

These are new for Fall 2026. In Fall 2025 the course was project-plus-participation only, and the
consequence was predictable: students met the tools for the first time inside their projects,
which is an expensive place to learn `nuXmv`'s syntax. The homeworks exist to guarantee that every
student has personally run every tool class before they have to choose one for a project.

## Design principles

**One tool per homework, one property throughout.** Every homework verifies a variant of the *same*
running example — a bounded counter that must never exceed 10 — with a different tool. The machine
and the property are defined once, in
**[`labs/running-example.md`](../labs/running-example.md)**; read it before HW1. By HW5 you will
have proved essentially one fact five ways and will understand, concretely, what each style of
verification buys and what it costs. This is the [`ttj/fmaiv`](https://github.com/ttj/fmaiv)
capstone structure, spread across a semester.

**HW1 is the exception, on purpose.** It works a variant with the guard removed, where the property
is *false* and a bounded checker can find the violation. Every homework after it uses the canonical
machine, where the property holds.

**Everything runs in the browser.** No student should lose a weekend to a toolchain. Every
homework has a zero-install path (GitHub Codespaces or Google Colab); local installation is
supported but never required.

**Every homework has an AI component.** Not decoration — you will be asked to record where an AI
assistant helped, where it produced something confidently wrong, and how you detected the
difference. Detecting the difference is the skill.

**Autogradable core, judged extension.** The mechanical part (does it verify? is it `sorry`-free?)
is checked automatically. The interesting part (why does the counterexample look like that?) is
read by a human.

## Schedule

| # | Out | Due | Topic | Primary tool | Zero-install path |
|---|---|---|---|---|---|
| HW1 | Thu Sep 10 | Thu Sep 24 | Logic, SAT/SMT, bounded reachability | Z3 (Python + SMT-LIB) | Colab / Codespaces |
| HW2 | Thu Oct 1 | Thu Oct 15 | Temporal logic and model checking | nuXmv / NuSMV | smvis in browser / Codespaces |
| HW3 | Thu Oct 15 | Thu Oct 29 | Program analysis: BMC and abstract interpretation | CBMC (+ Frama-C or the course abstract interpreter) | Codespaces |
| HW4 | Thu Oct 29 | Thu Nov 12 | Interactive theorem proving | Lean 4 | live.lean-lang.org / Codespaces |
| HW5 | Tue Dec 1 | Thu Dec 10 | Neural-network verification | α,β-CROWN / Marabou / auto_LiRPA | Colab |

Due dates are on the [course schedule](../schedule/schedule.md); submission is through Brightspace.

## Late policy

Four late days for the semester, usable in whole-day units on homeworks, no more than two on any
single homework, no questions asked. Beyond that, 20% per day. Late days do not apply to project
deliverables, which are presented in class and therefore cannot slip.

## The five homeworks

### HW1 — Logic, SAT/SMT, and bounded reachability
*Out Thu Sep 10, due Thu Sep 24. Tool: Z3.*

1. **Logic warm-up.** Translate five English statements into propositional and first-order logic;
   for each, decide satisfiability and validity by hand, then confirm with Z3. (Confirming by hand
   *and* by machine is the point: you are calibrating your own judgment against a decision
   procedure.)
2. **Encoding.** Encode a combinatorial puzzle as an SMT query (pigeonhole, n-queens, sudoku, or
   KenKen — starters provided). Report solve times as size grows and say where the wall is.
3. **Bounded reachability.** Write the counter as a transition system and ask Z3 whether `x` can
   reach 11 within `N` steps. Find the smallest `N` for which the answer changes, and explain
   precisely why that `N`.
4. **AI component.** Ask an LLM to produce the SMT-LIB encoding for part 3. Report what it got
   right, what it got wrong, and — critically — *how you knew*. An encoding that is `unsat` for
   the wrong reason looks exactly like a correct one until you check it.

*Starters:* [`fmaiv/day01/examples`](https://github.com/ttj/fmaiv/tree/main/day01/examples) ·
[Colab](https://colab.research.google.com/github/ttj/fmaiv/blob/main/notebooks/01_day1_logic_sat_smt.ipynb)

### HW2 — Temporal logic and model checking
*Out Thu Oct 1, due Thu Oct 15. Tool: nuXmv / NuSMV.*

1. **Read a model.** Given an SMV file, identify its initial states, transition relation, and
   state space size, and predict each property's verdict *before* running the tool. Then run it.
   Report where your prediction was wrong.
2. **Write specifications.** Formalize eight English requirements as LTL or CTL over a supplied
   model. At least two must be liveness, at least one must require distinguishing `EF` from `AF`
   (the vehicle-actuated traffic light makes this substantive).
3. **Break it.** Introduce a bug into `next(x)`, obtain a counterexample, and explain the trace
   step by step: which transition fires, why the property fails at that state.
4. **Bound hunt.** Using `bmc_depth.smv`, which hides a bug at depth 12, find the smallest BMC
   bound that exposes it, and explain what a *passing* BMC run at bound 10 would and would not
   have told you.
5. **AI component.** Have an LLM produce LTL for the same eight requirements. Check its formulas
   mechanically against yours (model-check `mine <-> llm`) rather than by eye, and report the
   disagreements.

*Starters:* [`fmaiv/day02/examples`](https://github.com/ttj/fmaiv/tree/main/day02/examples) ·
[smvis in-browser](https://bit.ly/fmaiv_smvis)

### HW3 — Program analysis: bounded model checking and abstract interpretation
*Out Thu Oct 15, due Thu Oct 29. Tools: CBMC, plus Frama-C or the course abstract interpreter.*

1. **CBMC.** Verify the counter in C. Then weaken the assertion, read the counterexample trace,
   and explain the role of `--unwind` and `--unwinding-assertions`. Say what an unwinding
   assertion actually protects you from.
2. **Loop invariants.** Supply a loop invariant strong enough to verify `array_max` or `binsearch`
   unboundedly, and explain why the obvious invariant is not inductive.
3. **Abstract interpretation.** Run the interval and sign domains over the supplied C examples.
   Find a program where the interval domain is too imprecise and say exactly what is lost at the
   join, and what a relational domain would have kept.
4. **Test generation.** Use `cbmc --cover branch` to generate a branch-covering test suite for
   `gcd`, and compare it to tests an LLM writes for the same function. Coverage is measurable;
   measure it.
5. **AI component.** Have an LLM write ACSL contracts (or CBMC assertions) for two functions, then
   check them. Report any *vacuous* contract it produced — a specification the code satisfies
   trivially. Vacuity is the characteristic failure of AI-written specifications and you should
   expect to find it.

*Starters:* [`fmaiv/day04/examples`](https://github.com/ttj/fmaiv/tree/main/day04/examples) ·
Fall 2025 abstract-interpretation demo (interval/sign domains, five annotated C examples)

### HW4 — Interactive theorem proving in Lean 4
*Out Thu Oct 29, due Thu Nov 12. Tool: Lean 4.*

1. **Warm-up.** Finish the tactic ladder (`CounterLadder.lean`) — six rungs from `rfl` to the
   counter's base case. If you have not played the Natural Number Game, do that first.
2. **Discrete maths in Lean.** Prove a small set-theory batch: subset transitivity, De Morgan,
   distribution of `∩` over `∪`. These are the propositions from week 4, now machine-checked.
3. **Transition system.** Define a transition system in Lean, state an invariant, and prove it by
   the inductive-invariant pattern (init lemma + step lemma + strengthening). You will be given a
   property that is **not** inductive as stated and must strengthen it yourself. That step is the
   whole assignment.
4. **Parametric.** Generalize a bound from `10` to arbitrary `N` and prove it for all `N` — the
   thing HW2's model checker could not do.
5. **AI component.** Use an AI assistant as a proof partner and keep a per-lemma log: who wrote
   it, how many iterations, and every hallucinated lemma name (Lean will tell you — the compiler
   is the ground truth, which is exactly why this is a good place to study AI reliability).

**Acceptance:** `lake build` clean and **sorry-free**. `sorry` compiles and proves nothing; it is
checked for automatically.

*Starters:* [`fmaiv/day03`](https://github.com/ttj/fmaiv/tree/main/day03) ·
[Lean web editor](https://live.lean-lang.org/) · [Natural Number Game](https://adam.math.hhu.de/)

### HW5 — Neural-network verification
*Out Tue Dec 1, due Thu Dec 10. Tools: α,β-CROWN / Marabou / auto_LiRPA.*

1. **Robustness as a query.** For a small MNIST network, state local robustness at a given input
   and `ε` as a formal property, and verify it. Report verified / falsified / timeout.
2. **The `ε` frontier.** Binary-search the largest `ε` you can verify and the smallest at which
   you can find an adversarial example. Explain the gap between them: what lives in it, and why
   incompleteness rather than a bug is the usual reason.
3. **Two tools.** Run at least two verifiers on the same queries and compare verdicts and times.
   If they disagree on a verdict, that is a finding — investigate it.
4. **Bounds.** Compare a cheap incomplete bound (IBP) with a tighter one (CROWN/α-CROWN) on the
   same property and explain the precision/cost trade-off you measure.
5. **AI component.** The network is the AI. Additionally: have an LLM generate VNN-LIB
   specifications from English property descriptions and check whether the generated properties are
   (a) syntactically valid and (b) actually the property you asked for.

*Starters:* [`fmaiv/day04/examples/nn`](https://github.com/ttj/fmaiv/tree/main/day04/examples/nn) ·
[Colab](https://colab.research.google.com/github/ttj/fmaiv/blob/main/notebooks/05_day4_nn_robustness.ipynb) ·
VNN-COMP 2026 benchmarks

## Collaboration and AI use

Discussion is encouraged; submitted work must be your own. AI assistants are **allowed and
expected** — this is a course about the reliability of AI-produced artifacts, and pretending you
did not use one would be beside the point. Two conditions:

1. **Disclose.** Every homework has an AI-use section. Say what you used and for what.
2. **Verify.** You are responsible for everything you submit. "The model said so" is not a
   justification, and in this course it is a particularly poor one — every tool we use is a
   decision procedure that can tell you whether the model was right. Use it.

Submitting an AI-generated proof you have not checked is both an honour-code problem and, in a
verification course, a self-inflicted wound: the compiler will catch it.
