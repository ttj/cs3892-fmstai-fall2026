# CS 3892 / 5892 — Term Project Topic Menu (Fall 2026)

You must choose one of the **eight topics below**, or propose your own (see
[*Proposing your own topic*](#proposing-your-own-topic) at the end — the bar is higher).

Each topic is written so that a team of 3–4 can produce a real result in one semester. Each
one names the tools, the data or benchmarks, a concrete definition of "done," and a stretch
goal. None of them is a survey.

## The one rule that decides your grade

Every project must have **both halves**:

| Half | Meaning | Bad answer | Good answer |
|---|---|---|---|
| **FM** | A formal or semi-formal method actually *runs* and produces a verdict, a proof, a counterexample, or a certified bound. | "We wrote a spec document." | "nuXmv returns a counterexample trace at depth 9; here it is." |
| **AI** | An AI/ML system is either the *subject* of the verification (FM4AI) or a *component* of the verification pipeline (AI4FM). | "We used ChatGPT to write our report." | "The LLM emits the LTL formula; we measure how often nuXmv agrees with the human-written reference." |

In Fall 2025 the single most common piece of feedback on milestone presentations was
**"where is the AI?"** — teams built a nice formal artifact and then had no AI in it, or built
an AI demo and never ran a verifier. The topics below are constructed so this cannot happen
accidentally. If your project drifts, the milestone gate will catch it, and by then it costs
you real points.

The second most common problem was starting the formal work too late. Hence: **a running
verifier by the milestone is a hard requirement**, not a suggestion.

---

## Topic 1 — Autoformalization: natural language → temporal logic → model checker

**Category:** AI4FM · **Difficulty:** ●●○○ · **Team:** 3–4

Requirements documents are written in English. Model checkers consume LTL/CTL and SMV. The gap
between the two is where most industrial formal-methods effort is actually spent. Your job is to
measure how well a 2026 LLM closes it, and — more interestingly — to characterize *how it fails*.

**Build.** A pipeline that takes an English requirement plus a system model and emits (a) an
LTL or CTL formula and (b) an SMV model, then runs nuXmv/NuSMV and reports the verdict.

**Evaluate.** Assemble a benchmark of 40–80 English requirements with human-written reference
formulas. Sources: the `spec_challenge.smv` exercise and the annotated models in
[`ttj/fmaiv` day02](https://github.com/ttj/fmaiv/tree/main/day02/examples) (every spec is labelled
`HOLDS` or `DELIBERATELY FALSE`), plus requirements you write for the traffic-light, elevator,
mutex, and producer–consumer models. Measure:
- **Syntactic validity** — does nuXmv parse it at all?
- **Semantic equivalence** to the reference formula. Do not eyeball this: check equivalence
  mechanically by model-checking `ref <-> llm` on the same model, or by finding a distinguishing
  trace. This is the technically interesting part of the project.
- **Verdict agreement** — does the LLM's formula produce the same true/false answer?

**Done means:** a table of ≥3 models × ≥40 requirements with all three metrics, plus a taxonomy of
failure modes with examples (our prediction: `G`/`F` nesting, "until" vs "weak until", implicit
scoping of `X`, and confusing safety with liveness).

**Stretch:** closed-loop repair — feed the nuXmv parse error or the distinguishing trace back to
the model and measure how many attempts convergence takes.

**Watch out for:** an LLM that writes a *trivially true* formula (`G TRUE`) scores well on
"verdict agreement" and is worthless. Your metric set must catch that.

---

## Topic 2 — Lean 4 + Cslib: proving what the model checker only checked

**Category:** AI4FM · **Difficulty:** ●●●● · **Team:** 3–4

A model checker answers a question about *one finite model*. A proof assistant answers it about
*all instances of a family*. This project lives exactly on that boundary, and connects the
theorem-proving half of the course back to the model-checking half.

**Build.** Take a system we model-check in class — the counter, the traffic light, mutex,
Peterson's algorithm — and prove the same property in Lean 4 for a *parametric* version
(`n` processes, bound `N` instead of `10`). Use the `TransitionSystem` / `Invariant` /
`InductiveInvariant` scaffolding in
[`ttj/fmaiv` day03](https://github.com/ttj/fmaiv/tree/main/day03/examples/CounterDemo), which
already gives you the inductive-invariant and k-induction machinery.

Then connect to **Cslib**, the Lean 4 library for computer-science structures (automata,
labelled transition systems, bisimulation, process calculi — see the course reading list for the
current repo URL and module names, which we will confirm in Week 10). The pedagogically valuable
link: **LTL model checking is automata-theoretic** — you check `L(system) ∩ L(¬φ) = ∅` via Büchi
automata — and Cslib is where that construction can be stated and proved rather than asserted on
a slide.

**AI half — this is required, not optional.** Instrument your proof effort. For each lemma record:
did you write it, or did an LLM (Claude Code, or a Lean-specific tool) write it? How many
iterations? Did it hallucinate a Mathlib lemma name that does not exist? Report a per-lemma table.
`sorry`-free is the acceptance criterion — `scripts/check-no-sorry.sh` in `ttj/fmaiv` enforces it.

**Done means:** a `lake build`-clean Lean project, sorry-free, proving a parametric property that
a model checker cannot settle for all `n`, plus your AI-assistance instrumentation table.

**Stretch:** extend `scripts/smv2lean` (an SMV→Lean translator already in the FMAIV repo) so it
emits proof obligations for a model it does not currently handle.

**Watch out for:** Lean's learning curve is real and front-loaded. If nobody on your team has
finished the Natural Number Game by the proposal deadline, pick a different topic.

---

## Topic 3 — Guardrails and automated reasoning: autoformalizing a policy

**Category:** FM4AI + AI4FM · **Difficulty:** ●●○○ · **Team:** 2–3

Filtering LLM output with another LLM is a heuristic. Amazon's *Automated Reasoning checks* in
Bedrock take a different route: encode the policy as logic, then use a solver to decide whether a
model's answer is consistent with it — a sound check with an actual certificate. This is the most
direct commercial instance of the course's thesis, and it is genuinely usable by undergraduates.

**Build.** Pick a policy domain with real structure — HR leave eligibility, a prescription-safety
rule set, an academic-integrity policy, export-control rules. Write it in English. Then:
1. Encode it as a formal policy (Bedrock Automated Reasoning checks, or your own Z3/SMT encoding).
2. Generate model answers to questions about the policy.
3. Have the checker decide each answer; classify as valid / invalid / no-decision.
4. Compare against a guardrail-style filter and against an LLM-as-judge baseline.

Start from the `vsc_awsbrg` case-study scaffolding from Fall 2025 (`toy_example.py`,
`case_study.py`); a Fall 2025 team took this route and it worked well.

**Done means:** confusion matrices (true/false positives and negatives — define them precisely; a
Fall 2025 team lost points for saying "blocked/not blocked" without defining the terms), for at
least two policy domains, with an analysis of *what the solver caught that the filter missed* and
vice versa. Include at least one case where the formal check is wrong because the
**formalization** is wrong — that failure mode is the intellectual payload of the project.

**Stretch:** measure the autoformalization step itself. Have an LLM produce the formal policy from
the English, and quantify how often the resulting policy is subtly wrong (over-restrictive,
under-restrictive, or unsatisfiable).

**Watch out for:** cloud costs and credentials. Use the course AWS credits, never commit a key,
and keep `.env` in `.gitignore`.

---

## Topic 4 — Neural-network verification on a VNN-COMP 2026 benchmark

**Category:** FM4AI · **Difficulty:** ●●●○ · **Team:** 3–4

VNN-COMP is the annual neural-network verification competition; the 2026 edition ran at SAIV /
FLoC 2026 in Lisbon in July 2026 with 13 participating tools, 24 scored benchmarks, and 6
extended-track benchmarks. All benchmarks, networks (ONNX), and specifications (VNN-LIB) are
public. Your instructor is one of the organizers, so the data and the context are close at hand.

**Build.** Choose one benchmark and go deep. Strong candidates:

| Benchmark | Why it is interesting |
|---|---|
| `soundnessbench` | Networks with *planted* violations that verifiers should find. If a verifier reports "verified," it has a soundness bug. Hunting for those is a genuinely publishable activity for an undergraduate team. |
| `malbeware` | Malware-detection networks — robustness in a security setting where the adversary is real. |
| `safenlp` | Verification touching NLP models; a bridge to the LLM half of the course. |
| `monotonic_acasxu_2026` / `isomorphic_acasxu_2026` | New 2026 extended-track variants of the classic aircraft collision-avoidance benchmark. |
| `collins_rul_cnn` | Remaining-useful-life prediction — a Fall 2025 team worked on RUL and monotonicity. |

Run at least three verifiers (α,β-CROWN, Marabou, nnenum, NNV, NeuralSAT, PyRAT are all open) and
compare verdicts, times, and disagreements. **Disagreements are the finding.**

**AI half.** Either (a) the networks under verification are the AI, plus you use an LLM to
generate or mutate VNN-LIB specifications and check whether the generated properties are
meaningful; or (b) you use an LLM to triage and explain counterexamples.

**Done means:** a reproducible harness, a results table across tools, and at least one
substantive observation — a disagreement between sound tools, a scaling wall you characterize, or
a property that is true but that no tool can prove in the timeout.

**Stretch:** submit a new benchmark proposal for VNN-COMP 2027.

**Watch out for:** out-of-memory is the default outcome on large networks. Start small
(ACAS Xu-scale), confirm the pipeline end to end, then scale. A Fall 2025 team hit an OOM wall on
image segmentation preimages and had to reformulate late.

---

## Topic 5 — Certifying monotonicity and fairness in tabular models

**Category:** FM4AI · **Difficulty:** ●●○○ · **Team:** 3–4

Some model behaviours are not merely desirable, they are *required by domain semantics*: risk
should not decrease when severity increases; a loan score should not improve when debt rises.
Standard networks violate these constraints routinely, and — unlike accuracy — such constraints
can be **formally verified**, because they are stated over the input domain rather than over a
test set.

**Build.** On a public tabular dataset (MIMIC-IV via PhysioNet, UCI Adult, a credit dataset),
train (a) an unconstrained MLP and (b) a monotone-by-design model (e.g. lattice networks or a
monotone architecture). State monotonicity as a verification query over box constraints set to
the empirical 1st–99th percentile of each feature, and verify with Marabou or α,β-CROWN.

**The research question that makes this a project and not an exercise:** does monotone-by-design
make verification *cheaper*, or does it merely make the property *true*? Measure both — violation
rate and verification time/timeouts — and separate the two effects.

**AI half.** The models are the AI. For a stronger AI4FM component, have an LLM read the dataset
documentation and *propose* which features should be monotone in which direction, then check
those hypotheses formally — a nice instance of AI generating specifications that formal methods
then adjudicate.

**Done means:** violation rates and verification cost for both model families, with an honest
accuracy-vs-verifiability trade-off curve. The trade-off is real; reporting it clearly is the
point.

**Watch out for:** MIMIC-IV requires PhysioNet credentialing, which takes time. Start that
paperwork in week 1 or choose a dataset that does not need it.

---

## Topic 6 — Explaining and repairing counterexamples with LLMs

**Category:** AI4FM · **Difficulty:** ●●○○ · **Team:** 3–4

Verifiers are good at saying *no* and bad at saying *why*. A CBMC trace or a CrossHair
counterexample is a wall of variable assignments. If an LLM can turn that into a correct
explanation — and then a correct fix — that is a real contribution to usability. If it produces
a *plausible but wrong* explanation, that is a real finding about AI-assisted verification.

**Build.** A pipeline: buggy program → verifier (CrossHair for Python, CBMC for C, Kani for Rust)
→ counterexample → LLM explanation → LLM-proposed repair → re-verify. The re-verification step is
what makes this a formal-methods project rather than a prompting exercise.

**Evaluate.** Three axes, each needing an operational definition:
- **Faithfulness** — does the explanation match the actual trace? (Checkable: does it name the
  right variables and the right branch?)
- **Repair correctness** — does the fix make the verifier pass *and* not trivially delete the
  assertion? (Automatable — and watch for exactly that cheat.)
- **Usefulness** — a small human study with your classmates.

Benchmarks: SV-COMP's `sv-benchmarks`, or Python programs with pre/post-conditions. Translating a
subset of SV-COMP C benchmarks to Python with an LLM is itself a legitimate contribution if you
validate the translations.

**Done means:** ≥4 LLMs × ≥50 counterexamples, all three metrics, plus a clear statement of how
often the model produced a confident wrong explanation. A Fall 2025 team built a web interface
for this and it was one of the strongest demos of the semester — a good bar to beat.

---

## Topic 7 — Verifying AI-generated code: specifications as the contract

**Category:** AI4FM + FM4AI · **Difficulty:** ●●●○ · **Team:** 3–4

LLMs write a great deal of code. Tests sample the input space; verification covers it. The
question is whether an LLM can produce a *specification* strong enough to be worth verifying
against — or whether it merely writes specs that its own code trivially satisfies.

**Build.** Pick a verification-aware language/tool pair: ACSL + Frama-C or CBMC (C), Verus or Kani
(Rust), CrossHair or `icontract` (Python). Have an LLM generate, for each task, both an
implementation and a specification. Then verify, and measure.

**The trap you must design around — and the most interesting result available here:** an LLM asked
for code and a spec will happily write a *vacuous* spec (`requires false`, or a postcondition that
restates the implementation). Your evaluation must detect this. Suggested detectors: mutation
testing (does the spec still verify against a deliberately broken implementation? then it is
worthless), and specification strength comparison against a human reference.

**Done means:** a benchmark of ≥30 tasks with pass/fail verification results, a vacuity analysis,
and a comparison of LLM-written vs human-written specifications.

**Stretch:** the closed loop — when verification fails, feed the failure back and measure how many
rounds it takes to converge, and whether it converges by fixing the code or by weakening the spec.
(It will sometimes weaken the spec. Catch it.)

---

## Topic 8 — Formal models of agentic AI: tool use, prompt injection, and policy enforcement

**Category:** FM4AI · **Difficulty:** ●●●○ · **Team:** 3–4

Agentic systems — LLMs that call tools, read untrusted content, and act — are the fastest-moving
attack surface in AI, and they are a *natural* fit for the transition-system machinery from this
course. An agent's tool-use policy is a reactive system; "never send a secret to an external
endpoint after reading untrusted content" is a safety property; "every destructive action is
preceded by a confirmation" is exactly a temporal-logic formula.

**Build.**
1. Model an agent's tool-use protocol (e.g. an MCP-style client with file, network, and shell
   tools) as a transition system in SMV, with an attacker who can inject content through any
   untrusted-read action.
2. State the security properties in LTL/CTL. At minimum: no exfiltration after taint, mandatory
   confirmation before destructive actions, and least privilege on tool escalation.
3. Model-check. Extract counterexample traces — these are *attack traces*.
4. Take one counterexample and reproduce it against a real (sandboxed) agent to show the model's
   trace corresponds to a real behaviour.

**AI half.** The agent is the AI. For the AI4FM side, use an LLM to generate the SMV model from
the tool documentation and measure how faithful the generated model is.

**Done means:** an SMV model, a property set, counterexample attack traces, and at least one
end-to-end demonstration that a trace is realizable.

**Watch out for:** run everything in a sandbox — a container or a throwaway VM, never your own
account. Do not attack third-party services. Anything touching a live system needs to be cleared
with the instructor first, and the ethics section of the report is graded.

---

## Alternates

Viable, slightly narrower, and available on request:

- **A. Smart-contract verification with AI assistance.** A DeFi vault with planted
  vulnerabilities; Slither (static analysis), Echidna (property-based fuzzing), TLA+/TLC or
  Certora for the model. The AI half must be explicit — LLM-generated invariants or
  LLM-translated models — because this is precisely where a Fall 2025 team got the "where is the
  AI?" question.
- **B. Runtime monitoring of AI trajectories with STL.** Signal temporal logic monitors over
  LLM-agent or control-policy traces; robustness semantics give you a *quantitative* margin
  rather than a yes/no. The `vsc_stl` pendulum demo from Fall 2025 is a working starting point.

---

## Proposing your own topic

Allowed, and some of the best Fall 2025 projects were self-proposed — but the bar is higher,
because you also have to prove the topic is well-posed. A self-proposed topic needs, at proposal
time:

1. Both halves (FM and AI) identified explicitly, in one sentence each.
2. The specific tool you will run, and evidence you have already run it once on a toy input.
3. The dataset or benchmark, and evidence you can access it.
4. A falsifiable success criterion — what result would count as a negative result, and why that
   would still be worth reporting.
5. A named fallback if the main idea proves infeasible by the milestone.

Approval is required before the proposal presentation. Come to office hours.

---

## Grad students (CS 5892)

Graduate students carry a deeper project. In addition to everything above:

- **Related-work survey.** 8–12 papers, situating your approach — not a list of summaries but an
  argument about where your work sits.
- **A second, independent evaluation axis.** A second dataset, a second tool family, or an ablation
  that isolates one design choice.
- **A stated threat to validity** section, and at least one experiment designed to test it.
- **Publication-shaped writing.** The final report should be a credible 8–10 page workshop
  submission in ACM/IEEE format.

Mixed teams are allowed. In a mixed team the graduate members own the additional components and
this must be stated in the responsibility breakdown.
