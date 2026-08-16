# Quizzes — CS 3892 / 5892, Fall 2026

Five short online quizzes, **10% of the course grade**, **lowest score dropped** (so each of the
four that count is worth 2.5%).

## Format

- Delivered in **Brightspace**, auto-graded.
- 10–15 minutes, 8–12 questions: multiple choice, multiple select, short numeric, and
  match-the-formula-to-the-English.
- **Open notes, open tools.** You may run Z3 or a model checker while taking one. The questions are
  written on the assumption that you can — which means they test whether you can *interpret* what a
  tool tells you, not whether you memorized syntax.
- Open one week before the deadline; due at **11:00 a.m.** on the listed day, i.e. before the class
  that uses the material.
- One attempt. If something goes wrong technically, email immediately — do not restart.

## Why quizzes exist

They are a readiness check, not an exam. Lecture is written to assume you have done the reading;
the quiz tells both of us — cheaply, and early enough to matter — when that assumption is wrong.
The lowest score is dropped so that one bad week costs you nothing.

## Schedule and coverage

| # | Due | Covers | Typical question |
|---|---|---|---|
| **1** | Tue Sep 8 | AI failure modes and risk taxonomy. Microsoft failure-modes taxonomy; NIST AI 100-2 categories; the difference between an intentional and an unintended failure; what a guardrail can and cannot express. | Given an incident description, classify the failure mode and say whether a per-request filter could have caught it. |
| **2** | Tue Sep 22 | Logic. Propositional and first-order syntax and semantics; satisfiability vs. validity; quantifier scope; the formula/state-set duality. | Is this formula satisfiable, valid, both, or neither? |
| **3** | Tue Oct 6 | Transition systems and modeling. `T = (S, S₀, →, AP, L)`; traces; reachability; invariants vs. *inductive* invariants; reading SMV. | Given a model and a candidate invariant, is it inductive? If not, which transition breaks it? |
| **4** | Tue Oct 27 | Temporal logic and model checking. LTL and CTL operators; safety vs. liveness; `EF` vs `AF`; explicit / symbolic / bounded trade-offs; what a passing BMC run at bound *k* does and does not establish. | Match four English requirements to four formulas — with plausible distractors that differ only in operator nesting. |
| **5** | Tue Nov 10 | Program analysis and Lean basics. Loop invariants; CBMC unwinding assertions; abstract domains and what is lost at a join; Lean terms, types, tactics, and what `sorry` means. | Which abstract domain is precise enough to prove this assertion, and why is the interval domain not? |

## Preparation

Each quiz covers the sessions since the previous one plus any assigned reading. The most useful
preparation is to *run the examples* rather than reread the slides — the questions are written
against tool behaviour, and someone who has run `nuXmv` on a broken model and read the
counterexample will find quiz 4 straightforward.

## Accommodations

Extended-time and other accommodations arranged through
[Student Access](https://www.vanderbilt.edu/student-access/) are applied automatically in
Brightspace. If you have an approved accommodation and the quiz timer looks wrong, tell me before
you start it.
