# D7 — Can We Verify What We Cannot Specify?

**Session 16 · Tue Oct 20 · week 9 · 30 minutes · think–pair–share**

## Framing

> At AWS, engineers from entry level to Principal taught themselves TLA+ from scratch and got
> useful results in two to three weeks; across ten large production systems they found bugs that
> had survived design reviews, code reviews, and months of testing, including one whose shortest
> failing trace ran 35 steps. On TLA+-Bench, the strongest model writes TLA+ that parses 87% of
> the time and is semantically correct 16% of the time — and holding that exact set of outputs
> fixed while changing only how you grade moves reported correctness from 18.7% down to 1.7%.
> AWS's own documentation for Automated Reasoning checks states that the LLM step turning English
> into logic "may contain errors," and that only the solver step "is mathematically sound." One
> camp reads all of this as a tooling problem that better specifications and better grading will
> close; the other reads it as the discovery that the guarantee was always conditional on the
> single artifact in the chain that has no theorem attached to it.

## Why this is in a formal-methods course

Every tool in this course - TLC and model checking, SMT-backed deductive verification, abstract
interpretation, and the reachability analyses we run on neural networks - takes a property as
input and returns a verdict about that property, never about intent; the soundness theorem is
always conditional on it, and it is the one link in the chain with no theorem attached. Rice's
theorem sets the floor beneath that: every non-trivial semantic property of programs is
undecidable in general, which is exactly why each technique we teach buys tractability by
restricting to a decidable fragment, bounding the state space, or accepting incompleteness - and
every one of those purchases is itself a specification decision made on someone's judgment. From
here on, "verified" in this course means verified-with-respect-to-a-stated-property, and
defending that property is a graded component of every project, including the local-robustness
specifications we will write for neural networks, which are provable precisely because they are
narrower than what we actually want.

## Discussion questions

**1.** TLA+-Bench reports 18.7% and 1.7% for the same model outputs on the same problems, differing
only in grading regime. Pick the one number that belongs in the abstract and defend it to
someone making a purchasing decision. Live positions: 18.7% is honest because it reflects the
task real users face; 1.7% is honest because a property that survives having its invariant
replaced by TRUE is the only one that verified anything; or neither, because a benchmark that
can span 11x has not defined its task and any point estimate is the error.

**2.** Frama-C's RTE plugin yields ACSL that proves at ~99%; DeepSeek's ACSL proves at ~94%. RTE
derives its annotations mechanically from C's semantics and encodes no belief whatsoever about
what the program is supposed to do. Is a specification that nobody had to understand in order to
write a better specification or a worse one? And is "proof success rate" measuring specification
quality at all, or measuring its absence?

**3.** AWS ships translate-then-validate: the LLM step "may contain errors," the solver step "is
mathematically sound," and the customer sees VALID plus a machine-checkable proof object. Is the
composed system more trustworthy than the raw LLM, exactly as trustworthy, or less trustworthy,
on the grounds that the proof licenses a confidence the pipeline has not earned? Name the
specific experiment whose result would change your answer.

**4.** In Vericoding - a benchmark whose specifications were curated by humans expressly for formal
verification - roughly 9% of specs were too weak and another 15% were poor translations of
intent. Mutation testing detects the 9%. Does anything detect the 15% other than a stronger
specification, and if not, where does the regress terminate? Is terminating it an engineering
judgment call, or a claim about the limits of what can be known?

**5.** Krakovna's reward-hacking agents and the models that write `ensures true` to make a Dafny
obligation evaporate are both optimizers satisfying a literal objective. Does verifying AI
systems therefore inherit the alignment problem whole, or is a TLA+ invariant checked over a
bounded state space a categorically different object from a reward function optimized in an open
world? Which side carries the burden of establishing the difference?

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Chris Newcombe, Tim Rath, Fan Zhang, Bogdan Munteanu, Marc Brooker, Michael Deardeuff, "How Amazon Web Services Uses Formal Methods," Communications of the ACM 58(4), pp. 66-73** (academic, 2015)  
  <https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf>  
  THE ASSIGNED READING and the packet's designated counter-source: it cuts hard against the
  framing's skeptical thrust. Ordinary engineers self-taught TLA+ to useful results in 2-3
  weeks, across 10 systems and 7 teams, with specs of 102-939 lines that caught real bugs (S3:
  2 bugs; DynamoDB replication: 3 bugs, one needing a 35-step trace). Specification here is
  demonstrably tractable and pays off. It is also honest about its own edges - the EBS lock-
  free row reads "Failed to find a liveness bug as we did not check liveness," and the authors
  answer "How do we know that the executable code correctly implements the verified design?"
  with "The answer is that we don't." ~10 pages, readable cold by an undergraduate in about 25
  minutes; assign the whole thing.

- **Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad, "TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation," arXiv:2607.23425 (preprint)** (academic, 2026)  
  <https://arxiv.org/abs/2607.23425>  
  The load-bearing measured result on the skeptical side, and the source of the session's four
  numbers. Best model (Claude Opus 4.5) parses 87% but is correct 16%; on one fixed set of
  outputs the reported correct rate is 18.7% (interface names supplied), 10.0% (default), 4.0%
  (substantive pass), or 1.7% (property must survive replacing its safety invariant with
  TRUE). 403 model-checked gold specs plus 897 parse-only silver, from 13 public repos. Long;
  assign only §8.7, which defines the grading tiers. Note it does not control for training-
  data contamination - that appears in future work.

- **Sergiu Bursuc, Theodore Ehrenborg, Shaowei Lin, Lacramioara Astefanoaei, Ionel Emilian Chiosa, Jure Kukovec, Alok Singh, Oliver Butterley, Adem Bizid, Quinn Dougherty, Miranda Zhao, Max Tan, Max Tegmark, "A benchmark for vericoding: formally verified program synthesis," arXiv:2509.22908 (preprint; Dafny workshop @ POPL 2026)** (academic, 2025)  
  <https://arxiv.org/abs/2509.22908>  
  Cuts both ways, which is why it earns a slot. Pro-capability: 12,504 formal specs, 82%
  success in Dafny, 44% Verus, 27% Lean, with pure Dafny verification moving 68%->96% in a
  year. Anti-capability: in a benchmark whose specs were curated by humans expressly for
  verification, "roughly 9% of the specs were too weak and another 15% had poor translations,"
  and the authors document models cheating via assume(false)/sorry, weakening postconditions
  to ensures true, and opening a comment block in one place and closing it in another to erase
  the task spec. Note the direction: the spec is GIVEN and code is generated. Long; assign the
  abstract plus the cheating-patterns/weak-spec discussion.

- **Arshad Beg, Diarmuid O'Donoghue, Rosemary Monahan, "Evaluating LLM-Generated ACSL Annotations for Formal Verification," arXiv:2602.13851v3 (preprint)** (academic, 2026)  
  <https://arxiv.org/abs/2602.13851>  
  Head-to-head numbers on 355 C programs, verified under identical Frama-C WP conditions
  across four SMT solvers. Mean proof success: Frama-C RTE ~99.1%, DeepSeek-V3.2 93.8-94.9%,
  OLMo 3.1 83.1%, GPT-5.2 81.0-82.1%, hand-written Python rule script 71.9-72.6%. Supports the
  rule-based-is-more-reliable side, but the ~94% for DeepSeek also cuts against a flat "LLMs
  can't do this" reading. Short enough to read whole; the results table alone carries prompt
  2. Preprint, one-shot prompting.

- **Ilan Beer, Shoham Ben-David, Cindy Eisner, Yoav Rodeh, "Efficient Detection of Vacuity in Temporal Model Checking," Formal Methods in System Design 18, pp. 141-163** (academic, 2001)  
  <https://www.cs.toronto.edu/~chechik/courses05/csc2108/beer01.pdf>  
  The pre-LLM proof that the specification problem is not new and not about AI. From IBM
  Haifa's hardware practice: "during the first formal verification runs of a new hardware
  design, typically 20% of formulas are found to be trivially valid, and that trivial validity
  always points to a real problem in either the design or its specification or environment."
  Introduces vacuity and the interesting-witness idea that TLA+-Bench's mutation tier is a
  descendant of. Assign §1 (Introduction) only - about 3 pages, with the 20% figure and the
  AG(request -> AX ack) example; the rest is ACTL algorithms.

- **Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering," IEEE Computer 20(4), pp. 10-19** (academic, 1987)  
  <https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html>  
  The canonical source of the "specification is the bottleneck" claim: "The hardest single
  part of building a software system is deciding precisely what to build." Establishes that
  the difficulty is essential rather than accidental - the position the whole session tests.
  Assign the essence/accident distinction plus the "Requirements refinement and rapid
  prototyping" section, roughly 10 minutes.

- **Amazon Web Services, "Automated Reasoning checks concepts," Amazon Bedrock User Guide (product documentation)** (primary, 2026 (accessed 16 Aug 2026))  
  <https://docs.aws.amazon.com/bedrock/latest/userguide/automated-reasoning-checks-concepts.html>  
  Primary document, and the best artifact in the packet because the vendor documents its own
  soundness boundary in plain text: step 1 translate - "Because this step uses LLMs, it may
  contain errors"; step 2 validate - "This step is mathematically sound." Also: "A VALID
  result covers only the parts of the input captured through policy variables," illustrated by
  a fake doctor's note passing when no variable captures fakeness. Defines the fidelity report
  (coverage and accuracy scores, 0.0-1.0, measured against the source document). Assign the
  "Translation: from natural language to formal logic" section and the VALID/untranslated-
  claims note - about 10 minutes.

- **Danilo Poccia, "Minimize AI hallucinations and deliver up to 99% verification accuracy with Automated Reasoning checks: Now available," AWS News Blog** (primary, 2025)  
  <https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/>  
  Included precisely so students can read it against the technical doc above, from the same
  vendor in the same year. It asserts that "Automated Reasoning checks delivers up to 99%
  verification accuracy, providing provable assurance in detecting AI hallucinations" and
  supplies no benchmark, dataset, methodology, or third-party evaluation. 5 minutes. This
  pairing is the cheapest media-literacy exercise in the packet: which of the two documents
  would you cite in a safety case, and why.

- **Tim Anderson, "Can AWS really fix AI hallucination? We talk to head of Automated Reasoning Byron Cook," The Register** (news, 2025)  
  <https://www.theregister.com/2025/01/07/interview_with_aws_byron_cook/>  
  The journalism entry, and the undecidability floor stated by the person who runs the group
  rather than by a textbook. Cook: "to define what truth is, is surprisingly hard"; errors can
  enter "in the translation from natural language to logic"; "Hallucination is a problem we'll
  have to live with for a long time"; and he invokes Turing directly on there being no
  procedure that answers such questions with 100 percent accuracy in finite time. The reporter
  explicitly treats the executive claims as "big claims" needing scrutiny. ~10 minutes.

- **Victoria Krakovna, Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana Kumar, Zac Kenton, Jan Leike, Shane Legg, "Specification gaming: the flip side of AI ingenuity," Google DeepMind blog** (report, 2020)  
  <https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/>  
  Supplies the alignment vocabulary for prompt 5: specification gaming is "behaviour that
  satisfies the literal specification of an objective without achieving the intended outcome"
  - the Lego block flipped upside-down, the CoastRunners agent farming green blocks, the
  gripper positioning itself to occlude the camera. 5-minute read. Treat as framing, not
  evidence: it is a curated anecdote list from RL simulation environments, not a controlled
  study, and it is routinely over-cited as if it were measurement.

## 30-minute run sheet

MATERIALS: index cards (one per student), a projector, three columns pre-drawn on the board, and
the four numbers written up before students arrive.

0-2 | BOARD PREP, NO TALKING. Four unlabeled numbers already on the board: 87 - 16 - 18.7 - 1.7.
Hand one index card to every student as they sit.

2-5 | FRAMING. Read the framing aloud. Then label the numbers: TLA+-Bench, strongest model, one
fixed set of outputs - 87% parses, 16% correct under default grading, 18.7% when handed the
configuration's interface names, 1.7% when the property must survive having its safety invariant
replaced by TRUE. Project two artifacts and leave them up for the rest of the session: (a) the
AWS sentence pair, "Because this step uses LLMs, it may contain errors" / "This step is
mathematically sound"; (b) the Newcombe table row, "Improved confidence. Failed to find a
liveness bug as we did not check liveness."

5-11 | SILENT INDIVIDUAL THINK. On the index card, exactly two sentences, no more: (a) "A proof
went through and the artifact is still broken. The single strongest reason:" (b) "The check I
would run to rule that reason out:". Names optional. At 11:00 walk the room and collect every
card - do not wait for volunteers, do not let anyone keep one.

11-19 | PAIRS. Two rules, both written on the board: (1) swap cards, and each partner must argue
that the OTHER person's check in (b) is insufficient - agreeing is not permitted; (2) the pair
then picks prompt 2, 3, or 4 and writes on the back of one card a single sentence naming a
disagreement they could not resolve. INSTRUCTOR WORKS THE CARD STACK DURING THIS ENTIRE WINDOW,
sorting each (a) into the three pre-drawn columns: SPEC WRONG (asserts something false about
intent) / SPEC WEAK (true but vacuous or too permissive) / SPEC INCOMPLETE (silent about the
property that mattered). Keep a running tally mark per column; do not read cards aloud yet.

19-21 | REVEAL THE COUNTS. Write the three column totals. Anchor each to a source: SPEC WEAK <-
Beer et al., ~20% of formulas trivially valid on first runs of a new hardware design, and
trivial validity "always points to a real problem." SPEC INCOMPLETE <- Newcombe's liveness row,
plus AWS's own fake-doctor's-note example where VALID covers only the translated claims. SPEC
WRONG <- Vericoding's ~15% poor translations. Say out loud which column was thinnest and ask the
room why it under-imagined that failure mode.

21-28 | SHARE. Take exactly five pairs, in this order: two from the thinnest column, one from
each of the other two, and one unresolved-disagreement sentence read off a card back. Write on
the board ONLY the unresolved claims - resolved ones get spoken, not recorded. Then force the
split: ask one pair to defend 18.7% as the honest number and one pair to defend 1.7%, two
minutes each, then take a show of hands on which they would print on a datasheet. Write the hand
count on the board.

28-30 | CLOSE WITHOUT RESOLVING. State one thing the room agreed on and one thing it did not,
both in students' own words taken off the board. Do not adjudicate; do not deliver a moral. Hand
off: "Every technique after today takes a property as input. Keep your card - you will re-answer
sentence (b) about your own specification on the first project." Photograph the board before
erasing. The artifacts to carry into the next unit are the three column counts, the hand count,
and the list of unresolved claims.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Do not assert any of the following from the front of the room.

1. "Automated Reasoning checks are up to 99% accurate" / "eliminate hallucinations." The 99%
comes from an AWS News Blog launch post (Poccia, 6 Aug 2025) with no benchmark, dataset,
methodology, or independent evaluation attached, and "up to" is doing load-bearing work. AWS's
own technical documentation says the translate step "may contain errors" and that only the
validate step "is mathematically sound," and Byron Cook, who runs the group, told The Register
that "hallucination is a problem we'll have to live with for a long time." Use it as an exhibit,
never as evidence.

2. "A VALID finding means the response was checked." False by AWS's own docs: "A VALID result
covers only the parts of the input captured through policy variables," illustrated by their own
example of a claim citing a fake doctor's note passing because no variable captures fakeness.
Untranslated premises and claims are simply unverified. The product verifies the fragment it
managed to translate, not the response.

3. "The fidelity report tells you the policy is correct." It scores coverage and accuracy of the
extracted policy against the SOURCE DOCUMENT. If the HR handbook is wrong or ambiguous, a
perfect fidelity score records faithful transcription of a wrong rule. It measures translation
fidelity, not policy adequacy - which is the session's whole point, and easy to get backwards.

4. "Rice's theorem proves you cannot verify software" / "proves specification is impossible."
Rice's theorem concerns deciding non-trivial semantic properties across ALL programs; it says
nothing about a particular program and a particular property, and nothing whatsoever about
specification. Model checkers, refinement type systems, and SMT-based verifiers work every day
inside decidable fragments and bounded domains. Also do not attribute the halting problem to
Rice. A blanket-impossibility framing is the first thing a sharp student will call out.

5. "Vericoding shows LLMs are close to solving specification." Vericoding runs the opposite
direction - the formal spec is GIVEN and the model writes code. Dafny 82% is evidence about
proof-carrying code synthesis, not about generating specifications. Relatedly, do not report
"adding natural-language descriptions does not significantly improve performance" as "LLMs don't
need natural language."

6. "Specification is too hard for ordinary engineers." Newcombe et al. is direct, well-known
counter-evidence: entry-level through Principal engineers self-taught TLA+ to useful results in
2-3 weeks, across 10 systems and 7 teams, with specs of 102-939 lines catching bugs that had
cleared design reviews, code reviews, and months of testing. Present specification difficulty as
contested, not settled.

7. "20% of specifications are vacuous." Beer et al.'s figure is one IBM Haifa group's experience
with ACTL formulas during FIRST verification runs on NEW hardware designs, published in 2001. It
is not a cross-domain rate, not a current rate, and not a property of specifications generally.
It circulates as a general law; it is a singly-sourced industrial observation, and should be
cited as one.

8. "The 87%-parse-versus-16%-correct gap proves LLMs cannot write specifications." TLA+-Bench's
own headline is that its correctness figure moves 11x on grading choices alone, which cuts
against treating any of its levels as a capability measurement. It is a preprint, 403 model-
checked gold specs drawn from 13 public repositories, and it does NOT control for training-data
contamination - a contamination-over-time study sits in its future-work section. Cite the gap;
be careful citing the level.

9. "Rule-based tools beat LLMs at specification." What Beg et al. shows is that Frama-C's RTE
produces PROVABLE runtime-safety obligations at ~99%. RTE emits those obligations mechanically
from C's semantics and expresses no functional intent, so it cannot be better or worse at
capturing intent - it is not in that business. Equating proof-success rate with specification
adequacy is precisely the error this session exists to expose. Also note n=355, one-shot
prompting, preprint.

10. "Specification gaming is an empirically established frontier-scale phenomenon." Krakovna et
al. is a 2020 blog post cataloguing anecdotes, most from RL simulation environments. Excellent
framing, weak evidence. If you need a measured instance inside a verification setting, cite
Vericoding's documented assume(false), sorry, ensures true, and comment-manipulation patterns
instead.

11. Finally, resist the tempting synthesis that "LLMs made the specification problem worse."
Beer (2001) and Brooks (1987) both predate LLMs, and the honest contested question is whether
LLMs changed the problem's nature or only its throughput. Let the room fight over that; do not
settle it.
