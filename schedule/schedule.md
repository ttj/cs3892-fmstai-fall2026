# Schedule — CS 3892 / 5892, Fall 2026

Tuesday / Thursday, 11:00 a.m. – 12:15 p.m. · **28 meetings**

Dates follow the Vanderbilt Registrar's
[2026–27 academic calendar](https://registrar.vanderbilt.edu/calendars/2026-27-academic.php).
Classes begin Wednesday Aug 26, so our first meeting is **Thursday Aug 27**. No class Thu Oct 22
(Fall Break). Thanksgiving holidays run Mon Nov 23 – Fri Nov 27 (the registrar states the range as
Nov 22–29, both of which are Sundays), which for a T/R course means **Tue Nov 24 and Thu Nov 26**
are lost and classes resume Mon Nov 30. Last day of classes is Thu Dec 10.

Topics may shift by a session; **deadlines will not move without notice on Brightspace.**

| # | Date | Unit | Session | Due |
|---:|---|---|---|---|
| 1 | Thu Aug 27 | 0 · Framing | **💬 D1 (30 min): Has AI ever killed anyone?** — Course intro. What formal methods are and what they guarantee. The verification triple: model + spec → verifier → verdict. FM4AI vs AI4FM. Why the Erdős #728 episode is the argument for this course. | |
| 2 | Tue Sep 1 | 1 · AI risk | Taxonomy of AI failure modes. Alignment, hallucination, jailbreaking, adversarial perturbation, backdoors, provenance, IP, human factors. **Case studies I: agentic failures.** | |
| 3 | Thu Sep 3 | 1 · AI risk | **💬 D2 (30 min): A survey of harms: when software and AI hurt people** — Risk frameworks and regulation. NIST AI RMF (and its ongoing revision), NIST AI 100-2 adversarial-ML taxonomy, EU AI Act as amended July 2026, ISO/IEC 24029-2, EASA. | |
| 4 | Tue Sep 8 | 1 · AI risk | **💬 D3 (30 min): Are LLMs theft? Training data, copyright, and fair use** — Guardrails vs. sound checks. Model-based filtering vs. solver-backed policy checking. AWS Bedrock Automated Reasoning checks: the translate/validate split and where soundness actually lives. **Case studies II.** | **Quiz 1** |
| 5 | Thu Sep 10 | 2 · Logic | Sets, set-builder notation, predicates. Propositional logic: syntax, semantics, satisfiability vs. validity. | |
| 6 | Tue Sep 15 | 2 · Logic | **💬 D4 (30 min): What are AI's environmental impacts — real, or overstated?** — First-order and higher-order logic. Quantifiers. The duality between formulas and sets of states — the idea the rest of the course runs on. | |
| 7 | Thu Sep 17 | 3 · SAT/SMT | SAT: CNF, DPLL/CDCL, resolution, UNSAT cores. Proving by refutation (`¬φ` UNSAT). | |
| 8 | Tue Sep 22 | 3 · SAT/SMT | **💬 D5 (30 min): If AI writes all our software, do we still need to learn to code?** — SMT: theories (LIA, bit-vectors, EUF), DPLL(T). Z3 from Python and SMT-LIB. Encoding problems as constraints. Bounded reachability. | **Quiz 2** |
| 9 | Thu Sep 24 | 4 · Modeling | Transition systems `T = (S, S₀, →, AP, L)`. Traces, reachability. Invariants and *inductive* invariants; strengthening. The SMV language. | **HW1 due** |
| 10 | Tue Sep 29 | Project | **Project proposal lightning talks.** 5–10 min per team, roughly 5–7 slides. | **Proposal report + slides due 11:00 a.m.** |
| 11 | Thu Oct 1 | 5 · Temporal logic | LTL: `G`, `F`, `X`, `U`. Safety vs. liveness. Writing English requirements as formulas — and the ways that goes wrong. Temporal properties over *agent traces*. | **HW2 out** |
| 12 | Tue Oct 6 | 5 · Temporal logic | **💬 D6 (30 min): Who is liable when AI-assisted software fails?** — CTL and path quantifiers; `EF` vs `AF`. ω-words, ω-regular languages, Büchi automata, and the automata-theoretic view: check `L(system) ∩ L(¬φ) = ∅`. | **Quiz 3** |
| 13 | Thu Oct 8 | 6 · Model checking | Explicit-state and symbolic model checking. BDDs, image computation, fixpoints, quantifier elimination. | |
| 14 | Tue Oct 13 | 6 · Model checking | Bounded model checking; k-induction and IC3. nuXmv in practice: counterexample-guided debugging, fairness, composition. | **HW2 due** |
| 15 | Thu Oct 15 | 7 · Programs | Programs as transition systems over memory states. Bounded model checking of C with CBMC: unwinding, unwinding assertions, nondeterministic inputs, reading a trace. | **HW3 out** |
| 16 | Tue Oct 20 | 7 · Programs | **💬 D7 (30 min): Can we verify what we cannot specify?** — Deductive verification: Hoare logic, loop invariants, ACSL and Frama-C. Why the obvious invariant is usually not inductive. | |
| — | Thu Oct 22 | | **Fall Break — no class** | |
| 17 | Tue Oct 27 | 7 · Programs | Abstract interpretation: abstract domains, Galois connections, widening; what precision is lost at a join. Static, dynamic, and concolic analysis; automated test generation. | **Quiz 4** |
| 18 | Thu Oct 29 | 8 · Theorem proving | **Lean 4 I:** terms, types, `def`, `theorem`, tactics. Curry–Howard. Induction. Live proving. | **HW3 due · HW4 out** |
| 19 | Tue Nov 3 | 8 · Theorem proving | **Lean 4 II:** transition systems in Lean. The inductive-invariant pattern — init lemma, step lemma, strengthening. Proving a *parametric* bound a model checker cannot settle. | |
| 20 | Thu Nov 5 | 8 · Theorem proving | **💬 D8 (30 min): The future role of the software engineer: correctness, or design?** — **Cslib I — the complete arc.** Labelled transition systems, bisimulation (including the greatest-fixed-point characterization), Hennessy–Milner logic, and the machine-checked Hennessy–Milner theorem: two states satisfy the same HML formulas iff they are bisimilar. A modal logic, a semantics over transition systems, an equivalence, and the theorem tying them together — with no missing pieces. | |
| 21 | Tue Nov 10 | 8 · Theorem proving | **Cslib II — ω-automata, and the honest gap.** Büchi acceptance; deterministic Büchi automata are strictly weaker than nondeterministic (`not_da_buchi`); the generalized-Büchi intersection construction — literally the intersection step of the pipeline from session 12; closure of ω-regular languages under complementation, which is what makes "check ¬φ" legitimate. Then the four things Cslib does **not** have — no LTL, no LTL→Büchi translation, no emptiness check, no system×property product — i.e. exactly where "proved" stops and "asserted on a slide" begins. | **Quiz 5** |
| 22 | Thu Nov 12 | Project | **Project milestone presentations.** 8–15 min per team, **live demo of running tooling required.** | **Milestone due · HW4 due** |
| 23 | Tue Nov 17 | 9 · AI4FM | Autoformalization: English → LTL, → SMV, → ACSL, → Lean. What the measured success rates actually are — semantic correctness runs far below syntactic, and how you would even measure the difference. | |
| 24 | Thu Nov 19 | 9 · AI4FM | **💬 D9 (30 min): Does system architecture still matter in the age of agentic coding?** — LLM proof search and the state of AI theorem proving. Saturated benchmarks. **The soundness gap:** a machine-checked proof of a machine-generated formalization certifies only that the two agree. The Erdős arc, revisited with the machinery to understand it. | |
| — | Tue Nov 24 | | **Thanksgiving — no class** | |
| — | Thu Nov 26 | | **Thanksgiving — no class** | |
| 25 | Tue Dec 1 | 10 · NN verification | Robustness as a formal property. Complete vs. incomplete methods; IBP, CROWN-style linear relaxation, branch-and-bound. ONNX and VNN-LIB 2.0. | **HW5 out** |
| 26 | Thu Dec 3 | 10 · NN verification | Tools and results: α,β-CROWN, NNV, n2v, NeuralSAT, PyRAT, Marabou. VNN-COMP 2026 as a live dataset. Scaling limits, stated honestly. Certification practice in aviation. | |
| 27 | Tue Dec 8 | Project | **Final project presentations I.** ~15 min per team plus questions. | |
| 28 | Thu Dec 10 | Project | **Final project presentations II.** Course wrap-up. *Last day of classes.* | **HW5 due** |

**Thu Dec 10, 5:00–7:00 p.m. — CS Immersion Showcase**, Adams Atrium, Featheringill Hall
**[confirm]**. Required for students using this course for the CS project or Immersion
requirement. Note it falls on the last day of classes: finish your poster or demo before then.

**Finals period, Sat Dec 12 – Sat Dec 19:** final project reports and artifacts due. There is no
final exam. Exact deadline on Brightspace.

## In-class discussions

Nine sessions give ~30 minutes to a structured discussion of a contested question, run as
**think–pair–share**. Weekly for the first five weeks, then every other week. Case-study
background, discussion questions, and readings are in
[`discussions/`](../discussions/README.md); each week's reading is posted on Brightspace a week
ahead. After each session you submit a one-paragraph reflection — see
[`participation.md`](../discussions/participation.md).

| | Session | Date | Week | Question |
|---|---:|---|---:|---|
| **D1** | 1 | Thu Aug 27 | 1 | Has AI ever killed anyone? |
| **D2** | 3 | Thu Sep 3 | 2 | A survey of harms: when software and AI hurt people |
| **D3** | 4 | Tue Sep 8 | 3 | Are LLMs theft? Training data, copyright, and fair use |
| **D4** | 6 | Tue Sep 15 | 4 | What does a prompt cost the planet? |
| **D5** | 8 | Tue Sep 22 | 5 | If AI writes all our software, do we still need to learn to code? |
| **D6** | 12 | Tue Oct 6 | 7 | Who is liable when AI-assisted software fails? |
| **D7** | 16 | Tue Oct 20 | 9 | Can we verify what we cannot specify? |
| **D8** | 20 | Thu Nov 5 | 11 | Correctness or design? What is left for the engineer |
| **D9** | 24 | Thu Nov 19 | 13 | Does system architecture still matter in the age of agentic coding? |

The technical content of a discussion session is correspondingly lighter; the homework and the
FMAIV notebooks carry the drill work. D7 is placed deliberately on the CBMC session — "can we
verify what we cannot specify" is that lecture's question, not a digression from it.

## Deadlines at a glance

| Deliverable | Out | Due |
|---|---|---|
| Quiz 1 — AI failure modes and risk | — | Tue Sep 8 |
| Quiz 2 — logic, sets, first-order logic | — | Tue Sep 22 |
| HW1 — logic, SAT/SMT, bounded reachability (Z3) | Thu Sep 10 | **Thu Sep 24** |
| **Project team sign-up** (Brightspace groups, max 4) | — | **Tue Sep 22** |
| **Project proposal** report + lightning talk | Thu Aug 27 | **Tue Sep 29, 11:00 a.m.** |
| **Lightning-talk slides** | — | **Tue Sep 29, 11:00 a.m.** |
| Quiz 3 — transition systems, invariants, SMV | — | Tue Oct 6 |
| Quiz 4 — temporal logic and model checking | — | Tue Oct 27 |
| HW2 — temporal logic and model checking (nuXmv) | Thu Oct 1 | **Tue Oct 13** |
| HW3 — program analysis (CBMC, abstract interpretation) | Thu Oct 15 | **Thu Oct 29** |
| Quiz 5 — program analysis and Lean basics | — | Tue Nov 10 |
| **Project milestone** + live demo | — | **Thu Nov 12** |
| HW4 — interactive theorem proving (Lean 4) | Thu Oct 29 | **Thu Nov 12** |
| HW5 — neural network verification | Tue Dec 1 | Thu Dec 10 |
| **Final presentations** | — | **Tue Dec 8 / Thu Dec 10** |
| **Final report, demo, artifacts** | — | **Finals period** |

Quizzes open on Brightspace one week before they close and are due at 11:00 a.m. on the listed
day — before the class that uses the material. Lowest of the five is dropped.

## Session budget — where the time went, and why

| Unit | Sessions | Note |
|---|---:|---|
| 0 · Framing | 1 | |
| 1 · AI risk, standards, case studies | 3 | Down from four in Fall 2025 — the case studies are folded into the lecture sessions rather than standing alone |
| 2 · Logic | 2 | |
| 3 · SAT/SMT | 2 | |
| 4 · Modeling | 1 | |
| 5 · Temporal logic | 2 | Büchi automata introduced here, revisited machine-checked in session 21 |
| 6 · Model checking | 2 | |
| 7 · Programs | 3 | |
| **8 · Theorem proving (Lean + Cslib)** | **4** | Up from ~1 in Fall 2025 |
| 9 · AI4FM | 2 | |
| 10 · NN verification | 2 | |
| Project sessions | 4 | Proposal, milestone, two final-presentation days |

## Planning notes

- **Büchi automata appear twice, on purpose.** Session 12 introduces them as the algorithmic
  foundation of LTL model checking; session 21 shows the same objects machine-checked in Lean,
  and then shows exactly which parts of the pipeline are *not* proved. Seeing the gap is the point,
  and it is a ready-made capstone project.
- **The Cslib unit is split rather than crammed.** Session 20 is a complete, self-contained,
  fully machine-checked arc (HML + bisimulation + the Hennessy–Milner theorem). Session 21 is the
  ω-automata material plus the honest inventory of what is missing. Running them as one session
  guarantees the second half gets cut live.
- **Two project gates before the withdraw deadline.** The proposal (Sep 29) lands well before the
  Oct 30 withdrawal deadline, so you will know whether the course suits you while you still have
  options. The milestone (Nov 12) is deliberately four weeks from the end.
- **Lean gets four sessions and HW4 gets three weeks**, spanning Thanksgiving on purpose. It is the
  steepest part of the course.
- **The last two weeks are compressed.** NN verification gets two sessions and HW5 is deliberately
  the lightest homework, because final projects are landing at the same time.
