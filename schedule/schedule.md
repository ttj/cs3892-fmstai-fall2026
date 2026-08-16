# Schedule — CS 3892 / 5892, Fall 2026

Tuesday / Thursday, 11:00 a.m. – 12:15 p.m. · **28 meetings**

Dates follow the Vanderbilt Registrar's
[2026–27 academic calendar](https://registrar.vanderbilt.edu/calendars/2026-27-academic.php).
Classes begin Wednesday Aug 26, so our first meeting is **Thursday Aug 27**. No class Thu Oct 22
(Fall Break) or Nov 24 / Nov 26 (Thanksgiving). Last day of classes is Thu Dec 10.

Topics may shift by a session; **deadlines will not move without notice on Brightspace.**

| # | Date | Unit | Session | Due |
|---:|---|---|---|---|
| 1 | Thu Aug 27 | 0 · Framing | Course intro. What formal methods are and what they guarantee. The verification triple: model + spec → verifier → verdict. FM4AI vs AI4FM. Tour of the semester. | |
| 2 | Tue Sep 1 | 1 · AI risk | Taxonomy of AI failure modes. Alignment, hallucination, jailbreaking, adversarial perturbation, backdoors, provenance, IP, human factors. | |
| 3 | Thu Sep 3 | 1 · AI risk | Case studies I: agentic failures. AI-orchestrated intrusion; prompt injection in tool-using agents; the coding agent that deleted a production database. Why per-request filtering cannot express the property that was violated. | |
| 4 | Tue Sep 8 | 1 · AI risk | Risk frameworks and regulation. NIST AI RMF (and its ongoing revision), NIST AI 100-2 adversarial-ML taxonomy, EU AI Act as amended July 2026, ISO/IEC 24029-2, EASA. | **Quiz 1** |
| 5 | Thu Sep 10 | 1 · AI risk | Guardrails vs. sound checks. Model-based filtering vs. solver-backed policy checking. AWS Bedrock Automated Reasoning checks: the translate/validate split and where soundness actually lives. Case study II. | |
| 6 | Tue Sep 15 | 2 · Logic | Sets, set-builder notation, predicates. Propositional logic: syntax, semantics, satisfiability vs. validity. | |
| 7 | Thu Sep 17 | 2 · Logic | First-order and higher-order logic. Quantifiers. The duality between formulas and sets of states — the idea the rest of the course runs on. | |
| 8 | Tue Sep 22 | 3 · SAT/SMT | SAT: CNF, DPLL/CDCL, resolution, UNSAT cores. Proving by refutation. | **Quiz 2** |
| 9 | Thu Sep 24 | 3 · SAT/SMT | SMT: theories (LIA, bit-vectors, EUF), DPLL(T). Z3 from Python and SMT-LIB. Encoding puzzles. Bounded reachability. | **HW1 out** |
| 10 | Tue Sep 29 | 4 · Modeling | Transition systems `T = (S, S₀, →, AP, L)`. Traces, reachability. Invariants and *inductive* invariants; strengthening. The SMV language. | |
| 11 | Thu Oct 1 | Project | **Project proposal lightning talks.** 5–10 min per team. | **Proposal due** |
| 12 | Tue Oct 6 | 5 · Temporal logic | LTL: `G`, `F`, `X`, `U`. Safety vs. liveness. Writing English requirements as formulas — and the ways that goes wrong. | **Quiz 3** |
| 13 | Thu Oct 8 | 5 · Temporal logic | CTL and path quantifiers; `EF` vs `AF`. ω-words, ω-regular languages, Büchi automata, and the automata-theoretic view: check `L(system) ∩ L(¬φ) = ∅`. Temporal properties over *agent traces*. | **HW1 due** |
| 14 | Tue Oct 13 | 6 · Model checking | Explicit-state and symbolic model checking. BDDs, image computation, fixpoints, quantifier elimination. | |
| 15 | Thu Oct 15 | 6 · Model checking | Bounded model checking; k-induction and IC3. nuXmv in practice: counterexample-guided debugging, fairness, composition. | **HW2 out** |
| 16 | Tue Oct 20 | 7 · Programs | Programs as transition systems over memory states. Bounded model checking of C with CBMC: unwinding, unwinding assertions, nondeterministic inputs, reading a trace. | |
| — | Thu Oct 22 | | **Fall Break — no class** | |
| 17 | Tue Oct 27 | 7 · Programs | Deductive verification: Hoare logic, loop invariants, ACSL and Frama-C. Why the obvious invariant is usually not inductive. | **Quiz 4** |
| 18 | Thu Oct 29 | 7 · Programs | Abstract interpretation: abstract domains, Galois connections, widening; what precision is lost at a join. Static, dynamic, and concolic analysis; automated test generation. | **HW2 due · HW3 out** |
| 19 | Tue Nov 3 | 8 · Theorem proving | Lean 4 I: terms, types, `def`, `theorem`, tactics. Curry–Howard. Induction. Live proving. | |
| 20 | Thu Nov 5 | 8 · Theorem proving | Lean 4 II: transition systems in Lean. The inductive-invariant pattern — init lemma, step lemma, strengthening. Proving a *parametric* bound a model checker cannot settle. | |
| 21 | Tue Nov 10 | 8 · Theorem proving | **Cslib**: labelled transition systems, bisimulation, Hennessy–Milner logic and the Hennessy–Milner theorem. ω-languages, Büchi acceptance, DBA ⊊ NBA, closure of ω-regular languages under complementation. And what Cslib does *not* have — no LTL, no LTL→Büchi, no emptiness check — i.e. exactly where "proved" stops and "asserted" begins. | **Quiz 5** |
| 22 | Thu Nov 12 | Project | **Project milestone presentations.** 8–15 min per team, **live demo of running tooling required.** | **Milestone due · HW3 due · HW4 out** |
| 23 | Tue Nov 17 | 9 · AI4FM | Autoformalization: English → LTL, → SMV, → ACSL, → Lean. What the measured success rates actually are (semantic correctness is far below syntactic). LLM proof search and the state of AI theorem proving. | |
| 24 | Thu Nov 19 | 9 · AI4FM | The soundness gap: a machine-checked proof of a machine-generated formalization certifies only that the two agree. Saturated benchmarks. The Erdős #728 episode — where formalization is what separated a real result from a retracted claim. | |
| — | Tue Nov 24 | | **Thanksgiving — no class** | |
| — | Thu Nov 26 | | **Thanksgiving — no class** | |
| 25 | Tue Dec 1 | 10 · NN verification | Robustness as a formal property. Complete vs. incomplete methods; IBP, CROWN-style linear relaxation, branch-and-bound. ONNX and VNN-LIB 2.0. | **HW5 out** |
| 26 | Thu Dec 3 | 10 · NN verification | Tools and results: α,β-CROWN, NNV, n2v, NeuralSAT, PyRAT, Marabou. VNN-COMP 2026 as a live dataset. Scaling limits, stated honestly. Certification practice in aviation. | **HW4 due** |
| 27 | Tue Dec 8 | Project | **Final project presentations I.** ~15 min per team plus questions. | |
| 28 | Thu Dec 10 | Project | **Final project presentations II.** Course wrap-up. *Last day of classes.* | **HW5 due** |

**Thu Dec 10, 5:00–7:00 p.m. — CS Immersion Showcase**, Adams Atrium, Featheringill Hall
**[confirm]**. Required for students using this course for the CS project or Immersion
requirement. Note it falls on the last day of classes: finish your poster or demo before then.

**Finals period, Sat Dec 12 – Sat Dec 19:** final project reports and artifacts due. There is no
final exam. Exact deadline on Brightspace.

## Deadlines at a glance

| Deliverable | Out | Due |
|---|---|---|
| Quiz 1 — AI failure modes and risk | — | Tue Sep 8 |
| Quiz 2 — logic, sets, first-order logic | — | Tue Sep 22 |
| **Project proposal** + lightning talk | Thu Aug 27 | **Thu Oct 1** |
| Quiz 3 — transition systems, invariants, SMV | — | Tue Oct 6 |
| HW1 — logic, SAT/SMT, bounded reachability (Z3) | Thu Sep 24 | Thu Oct 8 |
| Quiz 4 — temporal logic and model checking | — | Tue Oct 27 |
| HW2 — temporal logic and model checking (nuXmv) | Thu Oct 15 | Thu Oct 29 |
| HW3 — program analysis (CBMC, abstract interpretation) | Thu Oct 29 | Thu Nov 12 |
| Quiz 5 — program analysis and Lean basics | — | Tue Nov 10 |
| **Project milestone** + live demo | — | **Thu Nov 12** |
| HW4 — interactive theorem proving (Lean 4) | Thu Nov 12 | Thu Dec 3 |
| HW5 — neural network verification | Tue Dec 1 | Thu Dec 10 |
| **Final presentations** | — | **Tue Dec 8 / Thu Dec 10** |
| **Final report, demo, artifacts** | — | **Finals period** |

Quizzes open on Brightspace one week before they close and are due at 11:00 a.m. on the listed
day — before the class that uses the material. Lowest of the five is dropped.

## Planning notes

- **Two project gates before the withdraw deadline.** The proposal (Oct 1) lands well before the
  Oct 30 withdrawal deadline, so you will know whether the course suits you while you still have
  options. The milestone (Nov 12) is deliberately four weeks from the end — late enough to have
  results, early enough to change course if they are not coming.
- **Lean gets three sessions and three weeks of homework time.** It is the steepest part of the
  course and the schedule reflects that. HW4 spans Thanksgiving on purpose.
- **The last two weeks are compressed.** NN verification gets two sessions and HW5 is deliberately
  the lightest homework, because final projects are landing at the same time.
