# D7 — Can We Verify What We Cannot Specify?

**Session 16 · Tue Oct 20 · week 9 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Mon Oct 26, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What a specification is, and what happened when Amazon wrote them

A **specification** is a property stated in advance, precisely enough that a tool can check it — "no two replicas ever disagree about the same key," not "the database should be reliable." A verification tool returns a verdict about *that property* — never about what you meant.

In Newcombe et al., "How Amazon Web Services Uses Formal Methods" (*CACM*, April 2015), seven AWS teams applied the specification language TLA+ to ten large production systems. Engineers "from entry level to Principal have been able to learn TLA+ from scratch and get useful results in 2 to 3 weeks." The specs ran 102 to 939 lines. On DynamoDB's replication system the model checker found three bugs, one whose "shortest error trace exhibiting the bug contained 35 high level steps" — a bug that "had passed unnoticed through extensive design reviews, code reviews, and testing."

The paper marks its own limits. A results row reads "Improved confidence. Failed to find a liveness bug as we did not check liveness," and to "How do we know that the executable code correctly implements the verified design?" the authors answer, "The answer is that we don't."

### What the measurements found

**TLA+-Bench** (July 2026 preprint; 403 model-checked specs) separates *syntactic* correctness — the output parses — from *semantic* correctness — a model checker agrees it says the right thing. The strongest model parses 87% of the time but is "correct 16% of the time by default and 26% when given the interface names, open models at most 1%." Its sharper finding concerns grading, not models: on one fixed set of outputs "the correct rate moves sixfold, from 10.0% to 1.7%," and adding the interface-supply choice "widens the range to elevenfold, from 18.7% to 1.7%." Its strictest tier adds a mutation check: replacing a specification's safety invariant with TRUE.

**Beg et al.** (February 2026 preprint) compared ACSL annotations — formal comments on C code — across 355 programs under Frama-C's WP prover. Frama-C's RTE plugin derives its annotations mechanically from C's semantics — no division by zero, no overflow — and encodes no belief about what the program is *for*. Mean proof success: RTE 99.2%, DeepSeek-V3.2 94.9%, GPT-5.2 81.0%. Whether proof success tracks specification quality is a separate question.

**AWS Bedrock Automated Reasoning checks** documents this split itself. Step 1 translates English into logic using LLMs: "Because this step uses LLMs, it may *contain errors*." Step 2 checks it with an SMT solver: "This step *is mathematically sound*." AWS adds that "a VALID result covers only the parts of the input captured through policy variables" — their own example is a claim about a fake doctor's note passing because no variable captures fakeness.

### Why it still matters

Rice's theorem is the floor: no single procedure decides a non-trivial semantic property for *all* programs. It does not say a particular program cannot be verified against a particular property, and it says nothing about specifications. What it says is that every technique buys tractability somewhere — a decidable fragment, a bounded state space, accepted incompleteness — and each purchase is a judgment about what to check. Brooks said it in 1987: "The hardest single part of building a software system is deciding precisely what to build." Whether LLMs changed that problem's nature or only its throughput is the live question.

### Timeline

| When | What |
|---|---|
| 1987 | Fred Brooks publishes "No Silver Bullet" in IEEE Computer: "The hardest single part of building a software system is deciding precisely what to build." The specification bottleneck is named four decades before LLMs. |
| 2001 | Beer, Ben-David, Eisner and Rodeh publish "Efficient Detection of Vacuity in Temporal Model Checking" (Formal Methods in System Design), from IBM Haifa's hardware practice: a formula can pass because it is trivially valid rather than because the design is right. |
| April 2015 | Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 58(4)): seven AWS teams, TLA+ specs of 102-939 lines on ten production systems, finding bugs that had cleared design reviews, code reviews and months of testing. |
| 7 January 2025 | The Register interviews Byron Cook, who runs AWS's Automated Reasoning group. Cook: "to define what truth is, is surprisingly hard"; errors can enter "in the translation from natural language to logic"; "Hallucination is a problem we'll have to live with for a long time." |
| 6 August 2025 | AWS makes Automated Reasoning checks generally available in Amazon Bedrock. The launch blog headlines "up to 99% verification accuracy" and attaches no benchmark, dataset, methodology, or third-party evaluation. |
| 26 September 2025 | The Vericoding benchmark preprint posts: 12,504 human-curated formal specifications, 82% success in Dafny, 44% Verus, 27% Lean — but with the specification given and the code generated, the opposite direction from writing a spec. |
| 14 February 2026 | Beg, O'Donoghue and Monahan post their ACSL comparison on 355 C programs under Frama-C WP and four SMT solvers: RTE's mechanically derived annotations prove at 99.2%, DeepSeek-V3.2's at 94.9%, GPT-5.2's at 81.0%. |
| 26 July 2026 | TLA+-Bench preprint posts: the strongest model parses 87% of the time and is correct 16%; on one fixed set of outputs the reported correct rate spans 18.7% to 1.7% on grading choices alone. |

## The question

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

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

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

## Readings

10 sources, 10 verified by direct fetch. One is assigned; the rest are here if you want to go further, or if you want to check a claim that comes up in discussion.

- **Chris Newcombe, Tim Rath, Fan Zhang, Bogdan Munteanu, Marc Brooker, Michael Deardeuff, "How Amazon Web Services Uses Formal Methods," Communications of the ACM 58(4), pp. 66-73** (academic, 2015)  
  <https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf>  
  This is the assigned reading, and it is the strongest source on the other side: it argues
  against the skeptical case the rest of the session builds. Ordinary engineers self-taught TLA+
  to useful results in 2-3 weeks, across 10 systems and 7 teams, with specs of 102-939 lines
  that caught real bugs (S3: 2 bugs; DynamoDB replication: 3 bugs, one needing a 35-step
  trace). Specification here is demonstrably tractable and pays off. It is also honest about
  its own edges - the EBS lock-free row reads "Failed to find a liveness bug as we did not
  check liveness," and the authors answer "How do we know that the executable code correctly
  implements the verified design?" with "The answer is that we don't." ~10 pages, readable
  cold in about 25 minutes; read the whole thing.

- **Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad, "TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation," arXiv:2607.23425 (preprint)** (academic, 2026)  
  <https://arxiv.org/abs/2607.23425>  
  The central measured result on the skeptical side, and the source of the four numbers in
  the question above. Best model (Claude Opus 4.5) parses 87% but is correct 16%; on one
  fixed set of outputs the reported correct rate is 18.7% (interface names supplied), 10.0%
  (default), 4.0% (substantive pass), or 1.7% (property must survive replacing its safety
  invariant with TRUE). 403 model-checked gold specs plus 897 parse-only silver, from 13
  public repos. It is long - the part you need is §8.7, which defines the grading tiers. One
  gap to hold onto: it does not control for training-data contamination, which the authors
  leave to future work.

- **Sergiu Bursuc, Theodore Ehrenborg, Shaowei Lin, Lacramioara Astefanoaei, Ionel Emilian Chiosa, Jure Kukovec, Alok Singh, Oliver Butterley, Adem Bizid, Quinn Dougherty, Miranda Zhao, Max Tan, Max Tegmark, "A benchmark for vericoding: formally verified program synthesis," arXiv:2509.22908 (preprint; Dafny workshop @ POPL 2026)** (academic, 2025)  
  <https://arxiv.org/abs/2509.22908>  
  This one cuts both ways, which is why it is worth your time. For capability: 12,504 formal
  specs, 82% success in Dafny, 44% Verus, 27% Lean, with pure Dafny verification moving
  68%->96% in a year. Against it: in a benchmark whose specs were curated by humans expressly
  for verification, "roughly 9% of the specs were too weak and another 15% had poor
  translations," and the authors document models cheating via assume(false)/sorry, weakening
  postconditions to ensures true, and opening a comment block in one place and closing it in
  another to erase the task spec. The detail most people get wrong is the direction of the
  task: the spec is GIVEN and the code is generated. It is long - read the abstract plus the
  cheating-patterns and weak-spec discussion.

- **Arshad Beg, Diarmuid O'Donoghue, Rosemary Monahan, "Evaluating LLM-Generated ACSL Annotations for Formal Verification," arXiv:2602.13851v3 (preprint)** (academic, 2026)  
  <https://arxiv.org/abs/2602.13851>  
  Head-to-head numbers on 355 C programs, verified under identical Frama-C WP conditions
  across four SMT solvers. Mean proof success: Frama-C RTE ~99.1%, DeepSeek-V3.2 93.8-94.9%,
  OLMo 3.1 83.1%, GPT-5.2 81.0-82.1%, hand-written Python rule script 71.9-72.6%. It supports
  the rule-based-is-more-reliable side, but the ~94% for DeepSeek also cuts against a flat
  "LLMs can't do this" reading. Short enough to read whole, and the results table alone is
  enough to answer question 2. Two things to hold against it: it is a preprint, and the models
  got one-shot prompting only.

- **Ilan Beer, Shoham Ben-David, Cindy Eisner, Yoav Rodeh, "Efficient Detection of Vacuity in Temporal Model Checking," Formal Methods in System Design 18, pp. 141-163** (academic, 2001)  
  <https://www.cs.toronto.edu/~chechik/courses05/csc2108/beer01.pdf>  
  It is easy to assume the specification problem arrived with LLMs; this is the pre-LLM proof
  that it did not. From IBM Haifa's hardware practice: "during the first formal verification
  runs of a new hardware design, typically 20% of formulas are found to be trivially valid,
  and that trivial validity always points to a real problem in either the design or its
  specification or environment." It introduces vacuity and the interesting-witness idea that
  TLA+-Bench's mutation tier is a descendant of. Read §1 (Introduction) only - about 3 pages,
  with the 20% figure and the AG(request -> AX ack) example; the rest is ACTL algorithms.

- **Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering," IEEE Computer 20(4), pp. 10-19** (academic, 1987)  
  <https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html>  
  If you read only one thing on why specification is the bottleneck, make it this: "The
  hardest single part of building a software system is deciding precisely what to build." It
  establishes that the difficulty is essential rather than accidental - the position this
  whole session is testing. Read the essence/accident distinction plus the "Requirements
  refinement and rapid prototyping" section, roughly 10 minutes.

- **Amazon Web Services, "Automated Reasoning checks concepts," Amazon Bedrock User Guide (product documentation)** (primary, 2026 (accessed 16 Aug 2026))  
  <https://docs.aws.amazon.com/bedrock/latest/userguide/automated-reasoning-checks-concepts.html>  
  Primary document, and the most useful single artifact here, because the vendor documents its
  own soundness boundary in plain text: step 1 translate - "Because this step uses LLMs, it
  may contain errors"; step 2 validate - "This step is mathematically sound." Also: "A VALID
  result covers only the parts of the input captured through policy variables," illustrated by
  a fake doctor's note passing when no variable captures fakeness. It defines the fidelity
  report (coverage and accuracy scores, 0.0-1.0, measured against the source document). Read
  the "Translation: from natural language to formal logic" section and the VALID/untranslated-
  claims note - about 10 minutes.

- **Danilo Poccia, "Minimize AI hallucinations and deliver up to 99% verification accuracy with Automated Reasoning checks: Now available," AWS News Blog** (primary, 2025)  
  <https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/>  
  Read this against the technical doc above - same vendor, same year, opposite register. It
  asserts that "Automated Reasoning checks delivers up to 99% verification accuracy, providing
  provable assurance in detecting AI hallucinations" and supplies no benchmark, dataset,
  methodology, or third-party evaluation. 5 minutes. The pairing is the cheapest media-
  literacy exercise on this list: decide which of the two documents you would cite in a safety
  case, and why.

- **Tim Anderson, "Can AWS really fix AI hallucination? We talk to head of Automated Reasoning Byron Cook," The Register** (news, 2025)  
  <https://www.theregister.com/2025/01/07/interview_with_aws_byron_cook/>  
  The undecidability floor stated by the person who runs the group rather than by a textbook.
  Cook: "to define what truth is, is surprisingly hard"; errors can enter "in the translation
  from natural language to logic"; "Hallucination is a problem we'll have to live with for a
  long time"; and he invokes Turing directly on there being no procedure that answers such
  questions with 100 percent accuracy in finite time. The reporter explicitly treats the
  executive claims as "big claims" needing scrutiny. ~10 minutes.

- **Victoria Krakovna, Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana Kumar, Zac Kenton, Jan Leike, Shane Legg, "Specification gaming: the flip side of AI ingenuity," Google DeepMind blog** (report, 2020)  
  <https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/>  
  Supplies the alignment vocabulary for question 5: specification gaming is "behaviour that
  satisfies the literal specification of an objective without achieving the intended outcome"
  - the Lego block flipped upside-down, the CoastRunners agent farming green blocks, the
  gripper positioning itself to occlude the camera. 5-minute read. Treat it as framing, not
  evidence: it is a curated list of anecdotes from RL simulation environments, not a
  controlled study, and it is routinely over-cited as if it were measurement.

## What you submit

One paragraph, 150–250 words, by **Mon Oct 26, 11:59 p.m.**, to the `D7` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
