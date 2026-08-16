# D8 — Correctness or Design? What Is Left for the Engineer When the Machine Writes Both

**Session 20 · Thu Nov 5 · week 11 · 30 minutes · think–pair–share**

## Framing

> Since 2011 AWS engineers have model-checked their hardest distributed algorithms in TLA+, and by
> 2022 AWS was answering roughly a billion SMT queries a day about customer access policies —
> formal correctness became a shipped product feature, not a research curiosity. The same decade
> produced tools that write code from prose, and now tools that write postconditions, invariants,
> and proofs from prose as well. One reading is that the engineer's remaining job is judgment:
> deciding what "correct" should mean, and designing the system whose correctness is worth arguing
> about. The other is that a specification is just a higher-level programming language, and every
> higher-level programming language we have ever invented has eventually been automated.

## Why this is in a formal-methods course

Every artifact that will end up on the board — the TLA+ models at AWS, Zelkova's billion SMT
queries a day, seL4's refinement proof, C++26 contracts — is a machine-checked implication of
the same shape: if the specification and the environment assumptions hold, then the property
holds. This course automates the implication; nothing in it automates the choice of antecedent,
which is exactly why Newcombe et al. answer "we don't" when asked whether the code matches the
verified design, and why seL4's own authors concede that a proof may show only that the
implementation contains precisely the bugs the specification contains. The career question the
students are arguing about is therefore the same question we formalize in the soundness and
completeness unit: what does a proof actually buy you, and what did you have to assume in order
to get it?

## Discussion questions

**1.** Newcombe et al. report that the most frequently asked question about TLA+ at AWS is "How do we
know that the executable code correctly implements the verified design?" — and their published
answer is "The answer is that we don't." If an agent writes the code and a human writes the
spec, that unproved gap becomes the entire human contribution. Is that gap the most valuable
place for a human to stand, or the least defensible one?

**2.** seL4's kernel took about 2.2 person-years to build and about 20 person-years to prove. Suppose a
machine could now produce that proof in a week. Does full functional-correctness verification
become the default for new systems software — or does the bottleneck simply move to writing the
abstract specification, and if it moves, has anything actually changed about who is employable?

**3.** Marc Brooker of AWS argues that safety and liveness are "only a small part of a larger overall
picture," and that latency, cost, capacity and emergent degradation lie outside what model
checkers answer. If the questions formal methods can answer are precisely the questions machines
are best at answering, is "design" the genuine residual skill — or just the name we give to the
questions nobody has formalized yet?

**4.** In March 2026 the ISO C++ committee voted 114-12-3 to put Contracts — preconditions,
postconditions, assertions — into C++26, over Bjarne Stroustrup's objection that "it's not
minimal, it's not viable" and his statement that he will recommend not using them. Meanwhile
GitHub's Spec Kit promises that "specifications become executable, directly generating working
implementations." If the most experienced C++ engineers alive cannot agree that writing
checkable preconditions is net-positive, and if a prose document an LLM interprets also counts
as a "specification," what exactly is the skill we are telling students to acquire?

**5.** METR measured a 19% slowdown from AI in mid-2025, then in February 2026 reported it can no
longer measure the effect at all, because developers now refuse to take AI-disallowed tasks.
DORA finds throughput up and instability up. If we currently cannot measure whether AI makes
engineers more productive, on what basis should a CS department decide what to teach — and is
"teach verification because it is measurable" a good reason or a streetlight?

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Chris Newcombe, Tim Rath, Fan Zhang, Bogdan Munteanu, Marc Brooker, Michael Deardeuff, "Use of Formal Methods at Amazon Web Services," Amazon.com technical report, 29 September 2014** (primary, 2014)  
  <https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf>  
  The core industrial evidence that model checking scaled: TLA+ used at AWS since 2011 across
  10 systems by 7 teams, with a results table (S3, DynamoDB, EBS, an internal lock manager)
  listing bugs found, some requiring 35-step traces, and engineers productive in 2-3 weeks. It
  supports the 'verification scaled industrially' side, but it also supplies the strongest in-
  house counter: 'What Formal Specification Is Not Good For' (p.5) concedes they know no
  feasible way to model sustained emergent performance degradation, and 'The Most Frequently
  Asked Question' (p.9) asks how they know the code implements the verified design and answers
  'The answer is that we don't.' IMPORTANT: this is the longer 2014 technical report, NOT the
  CACM 58(4) April 2015 article 'How Amazon Web Services Uses Formal Methods'; ACM's site
  blocks automated retrieval, so the CACM version could not be verified and is deliberately
  not cited. 12 pages; for undergrads assign pp.1-5 plus the section on p.9 (~20 min).

- **Neha Rungta, "A Billion SMT Queries a Day," Amazon Science (write-up of the CAV 2022 keynote, 18 August 2022)** (primary, 2022)  
  <https://www.amazon.science/blog/a-billion-smt-queries-a-day>  
  The single hardest number for the 'verification scaled' side: AWS runs on the order of a
  billion SMT queries per day through Zelkova, using a portfolio of Z3, CVC4, cvc5 and a
  custom automaton solver, answering in 100ms to tens of seconds with a 30-second timeout.
  Crucially, it contains its own limit: Rungta stresses that correctness depends on 'asking
  the right question,' i.e. the formulation, not the solving, is the residual human step —
  which is exactly what Q1 and Q3 fight over. Short blog article, ~10 minutes.

- **Gerwin Klein, Kevin Elphinstone, Gernot Heiser, June Andronick, David Cock, Philip Derrin, Dhammika Elkaduwe, Kai Engelhardt, Rafal Kolanski, Michael Norrish, Thomas Sewell, Harvey Tuch, Simon Winwood, "seL4: Formal Verification of an OS Kernel," SOSP 2009** (academic, 2009)  
  <https://trustworthy.systems/publications/nicta_full_text/1852.pdf>  
  The price tag for full functional correctness, from the primary source rather than folklore:
  8,700 lines of C, kernel built in ~2.2 person-years, proof ~20 person-years (11 of them
  seL4-specific), ~200,000 lines of Isabelle, with a projected 8 py total for a repeat. It
  cuts against 'verification scaled cheaply.' It also contains the sharpest statement of the
  spec problem on the 'design' side (p.8): 'A cynic might say that an implementation proof
  only shows that the implementation has precisely the same bugs that the specification
  contains. This is true.' 14 pages and dense; assign only the 'Assumptions/Assurance'
  discussion on p.8 and the 'Verification effort' numbers on p.10 (~15 min).

- **Xuejun Yang, Yang Chen, Eric Eide, John Regehr, "Finding and Understanding Bugs in C Compilers," PLDI 2011** (academic, 2011)  
  <https://www.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf>  
  The most even-handed source in the packet, and the one that refuses to hand either side a
  win. Csmith found >325 compiler bugs in three years; against CompCert it found bugs in the
  *unverified* front end, an under-specified PowerPC displacement, and crashes, but after ~6
  CPU-years could not find a single middle-end wrong-code bug — 'The striking thing about our
  CompCert results is that the middle-end bugs we found in all other compilers are absent'
  (p.6). Their own conclusion (p.10) is that 'verification does not obviate testing, but
  rather complements it.' 12 pages; assign the CompCert paragraphs on p.6 and the
  'relationship between testing and verification' discussion on p.10 (~15 min).

- **Marc Brooker, "Formal Methods Only Solve Half My Problems" (one-page submission to HPTS'22), Marc's Blog, 2 June 2022** (primary, 2022)  
  <https://www.brooker.co.za/blog/2022/06/02/formal.html>  
  THE ASSIGNED READING — one page, readable in five minutes, and it cuts hardest against the
  framing's apparent thrust from the inside. Brooker is an AWS principal engineer and a co-
  author of the 2014 TLA+ paper above, yet he argues that in industry formal methods are not
  used for full verification, that they target safety and liveness, and that safety and
  liveness are 'only a small part of a larger overall picture' — latency, cost, capacity and
  failure-mode behavior are not addressed at all. It is the strongest argument for 'design is
  the residual skill' and, read the other way, the strongest argument that we simply have not
  formalized those questions yet.

- **DORA (Google Cloud), "State of AI-assisted Software Development" 2025 report** (report, 2025)  
  <https://dora.dev/research/2025/dora-report/>  
  The field evidence on where AI actually lands and where human review still matters: ~5,000
  respondents surveyed 13 Jun-21 Jul 2025 plus 100+ hours of qualitative data. 90% use AI and
  >80% believe it raised their productivity, yet 30% report little or no trust in AI-generated
  code. The headline finding is that AI adoption now *improves* delivery throughput — 'a key
  shift from last year' — while still *increasing* delivery instability, and the report
  explicitly recommends training people to 'critically guide, evaluate, and validate AI-
  generated work.' 142-page PDF: assign the Executive summary only, pp.3-9 (~15 min). Note it
  is a self-report survey, so it licenses correlational claims only.

- **Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud, "We are Changing our Developer Productivity Experiment Design," METR, 24 February 2026** (report, 2026)  
  <https://metr.org/blog/2026-02-24-uplift-update/>  
  The most important corrective in the packet, and the reason not to cite the famous 19%
  number as current. METR's own authors report that the 19% slowdown (CI +2% to +39%, N=16,
  Feb-Jun 2025) is likely no longer representative; that their larger follow-up (57
  developers, 143 repos, 800+ tasks) yields point estimates of -18% and -4% whose intervals
  both cross zero; and that they judge those estimates unreliable because 30-50% of
  participants withheld tasks they did not want to do without AI. It cuts against the packet's
  own AI-skeptical evidence as much as against AI boosters — the honest position is that
  nobody can currently measure this. ~10 minutes. The superseded 2025 study is at
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ and now carries an
  'out of date' banner.

- **GitHub, Spec Kit — README ("Define what to build before building it — with any AI coding agent"), open-source repository** (tool, 2026)  
  <https://raw.githubusercontent.com/github/spec-kit/main/README.md>  
  The 'AI writes code, humans write specs' thesis stated plainly by a vendor, in its own
  words: 'specifications become executable, directly generating working implementations rather
  than just guiding them.' Essential for Q4 because it lets students compare this sense of
  'specification' with a TLA+ model. Equally important, the README files its aims under
  'Experimental Goals' and talks about 'validating the hypothesis' — the project's own framing
  is that spec-driven development is unproven, which is the honest way to present it. ~10
  minutes; read the 'What is Spec-Driven Development?', 'Core Philosophy' and 'Experimental
  Goals' sections.

- **Madeline Endres, Sarah Fakhoury, Saikat Chakraborty, Shuvendu K. Lahiri, "Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?", Proc. ACM Softw. Eng. (PACMSE), FSE 2024; arXiv:2310.01831** (academic, 2024)  
  <https://arxiv.org/abs/2310.01831>  
  The counter-argument that verification is not a safe harbour either: peer-reviewed evidence
  that LLMs can already translate informal intent into formal, machine-checkable
  postconditions (nl2postcond), with generated postconditions catching 64 real historical bugs
  from Defects4J. If spec-writing is the human moat, this is the paper showing the moat is
  already being drained at the assertion level. NOTE: I retrieved and read the arXiv abstract
  page only, not the results sections — do not quote precision/recall figures from this entry.
  Assign the abstract and introduction (~15 min).

- **Tim Anderson, "Contracts are in C++26 despite disagreement over their value," The Register, 31 March 2026** (news, 2026)  
  <https://www.theregister.com/software/2026/03/31/contracts-are-in-c26-despite-disagreement-over-their-value/5229065>  
  Journalism, short, and the best live proof that 'writing specifications' is not a settled,
  obviously-valuable skill. WG21 approved C++26 on 28 March 2026 including Contracts
  (preconditions, postconditions, assertions) on a split vote of 114-12-3, over Bjarne
  Stroustrup's objection that 'it's claimed to be a minimal viable product. It's not minimal,
  it's not viable,' his statement that he will recommend not using contracts, and his worry
  'about whether we can use it correctly.' Herb Sutter concedes 'sustained technical
  concerns.' Contracts were also in the C++20 draft and removed in 2019. It cuts against the
  packet's spec-centric thrust: the most experienced practitioners alive disagree about
  whether lightweight specification pays. ~8 minutes.

## 30-minute run sheet

PREP (before students arrive). Write on the board two column headers, wide apart: "CORRECTNESS
IS THE MOAT" and "DESIGN IS THE MOAT". Below them write a third block headed "FACTS ON THE
TABLE" containing exactly four lines, no commentary: (1) AWS, TLA+ since 2011, 10 systems, bugs
needing 35-step traces; on whether the code matches the verified design the authors wrote "we
don't." (2) seL4: ~2.2 person-years to build the kernel, ~20 person-years to prove it. (3) C++26
Contracts adopted 114-12-3; Stroustrup: "It's not minimal, it's not viable." (4) METR: 19%
slowdown in 2025; in Feb 2026 they said they can no longer measure it. Have index cards at the
door.

0-3 FRAMING. Read the framing paragraph aloud verbatim. Point at the four facts. Do not
editorialize, do not say which column each fact belongs in — that is the students' job.

3-4 POSE Q1 ONLY. Project it. State the rule: closed laptops, closed phones, no talking.

4-9 INDIVIDUAL THINK (5 min, silent). On an index card each student writes (a) one sentence
answering Q1, and (b) underneath it, the single strongest objection to their own sentence. Both
halves are required; a card with only (a) is incomplete. Do not collect yet. Walk the room; do
not answer questions, just repeat the rule.

9-11 FORM PAIRS. Count off 1-4 around the room; same numbers pair up (triads if the count is
odd). Project all four remaining prompts and assign: 1s take Q2, 2s take Q3, 3s take Q4, 4s take
Q5.

11-21 PAIR PHASE (10 min). Each pair must produce two written things: (a) one sentence they both
agree on, and (b) one disagreement they could NOT resolve, written verbatim as a proposition
someone could deny. Circulate and write the disagreements you overhear onto the board under
whichever column they belong to — this is the collection, and it should be visibly filling up
before the share phase starts. Use these pressure points on pairs that converge too fast: to a
Q2 pair saying "AI will just do the proofs," note that Csmith found bugs in CompCert's
*unverified* front end after six CPU-years while the verified core held — what does that
predict? To a Q3 pair saying "design is obviously the moat," ask them to name one design
decision that could not, even in principle, be stated as a property. To a Q4 pair saying prose
specs are real specs, ask what TLC would do with the prose. To a Q5 pair quoting the 19% figure,
tell them METR withdrew its own ability to measure it — now what?

21-29 SHARE (8 min). Call pairs by number, one pair per number first, roughly 90 seconds each.
Ask only for (b), the unresolved disagreement; agreement is cheap and eats the clock. Add each
to the board under a column. If a pair's disagreement duplicates one already up, move to the
next pair with that number. Keep the last two minutes for second-round hands from any number.

29-30 CLOSE — DO NOT RESOLVE. Read both columns aloud in order, top to bottom. Then make one
observation about the artifacts rather than a takeaway: every result sitting in the
"correctness" column — TLA+ at AWS, seL4, CompCert, a billion SMT queries a day — is a machine-
checked implication whose antecedent a human wrote. Stop there; do not say what that implies.
Collect the index cards at the door (they are the engagement record and they show you where the
room started before anyone heard a peer). Photograph the board; you will put it back up during
the soundness/completeness unit. Assignment for next class, one page: "Name the assumption you
would have been most embarrassed to get wrong in the last thing you built, and say how you would
have checked it."

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Rewrite of the usual claims into what the primary sources actually say. Do not assert any of the
left-hand versions from the front of the room.

1. "AWS formally verified S3 / DynamoDB." What Newcombe et al. describe is model checking of
*designs* — abstract TLA+/PlusCal specs of 102 to 939 lines — not implementations. Their own
section "The Most Frequently Asked Question" asks how they know the executable code implements
the verified design and answers "The answer is that we don't." Say "model-checked the design,"
never "verified the service."

2. seL4 cost numbers. The SOSP 2009 paper gives: abstract spec ~4 person-months; Haskell
prototype ~2 person-years; C implementation ~2 person-months; kernel total 2.2 py; proof ~20 py
of which ~11 py was seL4-specific; ~200,000 lines of Isabelle; a projected 8 py total for a
repeat. The paper contains NO per-line-of-code cost for seL4 itself. Its only dollars-per-LOC
number is an industry rule of thumb of $10k/LOC for Common Criteria EAL6, extrapolated to $87M.
If you quote a per-LOC seL4 figure, say where you got it, because it is not in this paper.

3. "CompCert is bug-free." Csmith found bugs in CompCert: in the unverified front end, an under-
specified PowerPC displacement width, and crash errors. What was absent, after about six CPU-
years of testing as of early 2011, were middle-end wrong-code bugs. The authors' own framing is
"verification does not obviate testing, but rather complements it." The correct claim is about
the verified portion, not the product.

4. "METR proved AI makes developers slower." METR's own 24 Feb 2026 post states the 19% figure
came from Feb-Jun 2025 with N=16 and a confidence interval of +2% to +39%; that they now believe
developers are likely sped up; and that their follow-up (57 devs, 800+ tasks) gives -18% and -4%
point estimates whose intervals both cross zero and which they judge unreliable because 30-50%
of participants withheld tasks they did not want to do without AI. The 2025 post carries an "out
of date" banner. Cite the 2026 post, not the 2025 headline.

5. Conflating DORA 2024 and DORA 2025. The 2025 report (~5,000 respondents, surveyed 13 Jun-21
Jul 2025) finds AI adoption now *improves* delivery throughput — "a key shift from last year" —
while still *increasing* delivery instability, and it refers to the 2024 finding (more AI use,
worse throughput and stability) as "the DORA 2024 anomaly." Quoting the 2024 throughput result
as current is simply wrong. Also: DORA is a self-report survey, not an RCT, so it supports
correlational language only.

6. "Cedar is provably correct." That exact phrase is on AWS's provable-security marketing page.
The Cedar paper's own claim is narrower: the authors modeled Cedar in Lean and used Lean's proof
assistant "to prove important properties of Cedar's design," and separately "implemented Cedar
in Rust." The abstract makes no claim that the shipped Rust implementation is proved to match
the Lean model. Keep model and implementation distinct — and note that this phrasing is vendor
phrasing.

7. Infer and Sapienz effectiveness numbers. This packet could not retrieve the primary source:
ACM DL blocks automated retrieval, so Distefano, Fahndrich, Logozzo & O'Hearn, CACM 62(8):62-70
(2019) is confirmed here only as a bibliographic record, never read. No Infer or Sapienz fix-
rate, false-positive rate, or crash-triage number in this packet is verified. Do not quote one
from the front of the room.

8. Quotes attributed to Byron Cook or Werner Vogels. Cook's CAV 2018 paper (DOI
10.1007/978-3-319-96145-3_3, pp. 38-47, record confirmed via DBLP and Semantic Scholar) sits
behind a bot wall, and allthingsdistributed.com returned 403. Neither primary text could be
retrieved for this packet, so nothing here quotes either man. If you attribute a specific
sentence to either from the front of the room, have the source open on screen first.

9. "Spec-driven development works." GitHub's Spec Kit files its aims under "Experimental Goals"
and describes "validating the hypothesis" that the process is technology-independent — the
project's own framing is that this is unproven. As of this packet there is no independent peer-
reviewed effectiveness evidence for Spec Kit, Kiro, or comparable 2025-2026 tooling. Present
them as claims, not results.

10. "Formal methods only find the bugs you already thought of." The AWS paper argues the
opposite for model checking: TLC found bugs requiring 35-step traces that had survived multiple
design reviews, code reviews, and months of testing. But the mirror claim, that formal methods
cover the design problem, is equally wrong: the same paper's "What Formal Specification Is Not
Good For" says of sustained emergent performance degradation that "we don't yet know of a
feasible way to model a real system that would enable tools to predict such emergent behavior,"
and Brooker's whole point is that latency, cost and capacity sit outside safety and liveness.
Both slogans are wrong; use the sections.

11. "AI writes code, humans write specs" has a canonical citation. It does not — it is a
conference-talk and vendor thesis, not a paper. Attribute it to the tooling that states it
plainly (Spec Kit's README: "specifications become executable, directly generating working
implementations rather than just guiding them") rather than implying a peer-reviewed source
exists.
