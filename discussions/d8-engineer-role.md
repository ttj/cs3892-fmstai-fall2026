# D8 — Correctness or Design? What Is Left for the Engineer When the Machine Writes Both

**Session 20 · Thu Nov 5 · week 11 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Sat Nov 7, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What happened

*Formal methods* means using mathematics to prove that a system satisfies a stated property. In 2009 a NICTA team published **seL4**: an OS microkernel of ~8,700 lines of C, proved functionally correct against an abstract specification in the Isabelle/HOL proof assistant — some 200,000 lines of proof.

Since 2011 Amazon Web Services engineers have written **TLA+** specifications: abstract models that a *model checker* explores exhaustively. Newcombe et al. (2014) report use on 10 systems, 7 teams, specs of 102 to 939 lines, catching bugs that needed 35-step traces and had survived months of review and testing.

Verification also shipped as a product: AWS's **Zelkova** compiles a customer access-control policy plus a question into logic for SMT solvers (which decide whether a formula is satisfiable). By 2022 AWS was answering roughly a billion SMT queries a day — via Z3, CVC4, cvc5 and a custom automaton solver — inside S3 Block Public Access and IAM Access Analyzer. Meta runs **Infer** (static analysis for null dereferences, leaks, races) and **Sapienz** (automated test design) since 2017.

### What the practitioners' own reports say

The success papers carry their own limits. Newcombe et al. include a section titled "The Most Frequently Asked Question": how do they know the executable code implements the verified design? Their answer: "The answer is that we don't." What was checked was the design, not the service. They also concede no feasible way to model sustained emergent performance degradation.

seL4's authors are blunter: "A cynic might say that an implementation proof only shows that the implementation has precisely the same bugs that the specification contains. This is true." The price: ~2.2 person-years to build the kernel and 20 to prove it, some 11 seL4-specific.

Csmith, a random program generator, found over 325 bugs across C compilers in three years. Against **CompCert**, whose optimizing core is verified, it found bugs in the *unverified* front end, plus crashes. What it did not find, after about six CPU-years (as of 2011), was a middle-end wrong-code bug; its authors conclude "verification does not obviate testing, but rather complements it." Marc Brooker, an AWS principal engineer and co-author of the 2014 AWS paper, argues industry targets safety and liveness rather than full verification — "only a small part of a larger overall picture," with latency, cost and capacity outside.

### Why it still matters

If the durable human job is writing specifications, that job is also a target. Endres et al. (FSE 2024) show language models turning informal intent into formal *postconditions* — machine-checkable statements about what must hold when a function returns — that caught 64 real historical bugs. GitHub's Spec Kit promises "specifications become executable, directly generating working implementations rather than just guiding them" — a claim its README files under "Experimental Goals."

Whether specification-writing pays is unsettled among experts: on 28 March 2026 the ISO C++ committee approved C++26 including Contracts — preconditions, postconditions, assertions — by 114-12-3, over Bjarne Stroustrup's objection: "It's not minimal, it's not viable." Whether AI helps developers is currently unmeasured: DORA's 2025 survey of ~5,000 developers (self-report, not a randomized controlled trial, so correlation only) finds AI adoption improving throughput while increasing delivery instability, and METR called its own 19% slowdown figure likely no longer representative in February 2026, its follow-up estimates crossing zero.

### Timeline

| When | What |
|---|---|
| 2009 | seL4 published at SOSP: ~8,700 lines of C proved functionally correct in Isabelle/HOL — ~2.2 person-years to build the kernel, ~20 person-years to prove it. |
| 2011 | AWS engineers begin using TLA+ on production distributed systems; Csmith's PLDI paper reports >325 bugs found across C compilers in three years, and no middle-end wrong-code bug in CompCert after about six CPU-years. |
| 29 September 2014 | Newcombe et al., "Use of Formal Methods at Amazon Web Services" — 10 systems, 7 teams — including "The Most Frequently Asked Question" and its answer, "The answer is that we don't." |
| 2 June 2022 | Marc Brooker's HPTS'22 note, "Formal Methods Only Solve Half My Problems": safety and liveness are "only a small part of a larger overall picture." |
| 18 August 2022 | Amazon Science publishes "A Billion SMT Queries a Day" on Zelkova — Z3, CVC4, cvc5 and a custom automaton solver behind S3 Block Public Access and IAM Access Analyzer. |
| 2024 | Endres et al. (FSE 2024) show LLMs translating natural-language intent into formal postconditions; the generated postconditions catch 64 real historical bugs. |
| 2025 | DORA's AI report (~5,000 respondents) finds AI adoption raising delivery throughput and delivery instability; METR publishes its 19% AI slowdown result (N=16, CI +2% to +39%). |
| 24 February and 28 March 2026 | METR reports the 19% figure is likely no longer representative and its follow-up estimates unreliable; a month later WG21 approves C++26 including Contracts by 114-12-3, over Bjarne Stroustrup's objection "It's not minimal, it's not viable." |

## The question

**Is a specification just a higher-level programming language?**

> Since 2011 AWS engineers have model-checked their hardest distributed algorithms in TLA+, and by
> 2022 AWS was answering roughly a billion SMT queries a day about customer access policies —
> formal correctness became a shipped product feature, not a research curiosity. The same decade
> produced tools that write code from prose, and now tools that write postconditions, invariants,
> and proofs from prose as well. One reading is that the engineer's remaining job is judgment:
> deciding what "correct" should mean, and designing the system whose correctness is worth arguing
> about. The other is that a specification is just a higher-level programming language, and every
> higher-level programming language we have ever invented has eventually been automated.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

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

## Readings

10 sources. One of them is the assigned reading (marked below); the rest are here if you want to go further, or if you need to check a claim someone makes in the room.

- **Chris Newcombe, Tim Rath, Fan Zhang, Bogdan Munteanu, Marc Brooker, Michael Deardeuff, "Use of Formal Methods at Amazon Web Services," Amazon.com technical report, 29 September 2014** (primary, 2014)  
  <https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf>  
  The core industrial evidence that model checking scaled: TLA+ used at AWS since 2011 across
  10 systems by 7 teams, with a results table (S3, DynamoDB, EBS, an internal lock manager)
  listing bugs found, some requiring 35-step traces, and engineers productive in 2-3 weeks.
  Read it for the 'verification scaled industrially' case, but read it also for the strongest
  in-house counter: 'What Formal Specification Is Not Good For' (p.5) concedes they know no
  feasible way to model sustained emergent performance degradation, and 'The Most Frequently
  Asked Question' (p.9) asks how they know the code implements the verified design and answers
  'The answer is that we don't.' IMPORTANT: this is the longer 2014 technical report, NOT the
  CACM 58(4) April 2015 article 'How Amazon Web Services Uses Formal Methods'. The CACM
  version sits behind the ACM paywall and could not be checked, so it is deliberately not
  cited here. 12 pages, but the part you need is pp.1-5 plus the section on p.9 (~20 min).

- **Neha Rungta, "A Billion SMT Queries a Day," Amazon Science (write-up of the CAV 2022 keynote, 18 August 2022)** (primary, 2022)  
  <https://www.amazon.science/blog/a-billion-smt-queries-a-day>  
  The single hardest number for the 'verification scaled' side: AWS runs on the order of a
  billion SMT queries per day through Zelkova, using a portfolio of Z3, CVC4, cvc5 and a
  custom automaton solver, answering in 100ms to tens of seconds with a 30-second timeout.
  It also states its own limit: Rungta stresses that correctness depends on 'asking the right
  question,' i.e. the formulation, not the solving, is the residual human step — which is
  exactly what Q1 and Q3 turn on. Short blog article, ~10 minutes.

- **Gerwin Klein, Kevin Elphinstone, Gernot Heiser, June Andronick, David Cock, Philip Derrin, Dhammika Elkaduwe, Kai Engelhardt, Rafal Kolanski, Michael Norrish, Thomas Sewell, Harvey Tuch, Simon Winwood, "seL4: Formal Verification of an OS Kernel," SOSP 2009** (academic, 2009)  
  <https://trustworthy.systems/publications/nicta_full_text/1852.pdf>  
  The price tag for full functional correctness, from the primary source rather than folklore:
  8,700 lines of C, kernel built in ~2.2 person-years, proof ~20 person-years (11 of them
  seL4-specific), ~200,000 lines of Isabelle, with a projected 8 py total for a repeat. Those
  numbers are the case against 'verification scaled cheaply.' It also contains the sharpest
  statement of the spec problem on the 'design' side (p.8): 'A cynic might say that an
  implementation proof only shows that the implementation has precisely the same bugs that
  the specification contains. This is true.' 14 pages and dense — read only the
  'Assumptions/Assurance' discussion on p.8 and the 'Verification effort' numbers on p.10
  (~15 min).

- **Xuejun Yang, Yang Chen, Eric Eide, John Regehr, "Finding and Understanding Bugs in C Compilers," PLDI 2011** (academic, 2011)  
  <https://www.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf>  
  The most even-handed source here, and the one that refuses to hand either side a win.
  Csmith found >325 compiler bugs in three years; against CompCert it found bugs in the
  *unverified* front end, an under-specified PowerPC displacement, and crashes, but after ~6
  CPU-years could not find a single middle-end wrong-code bug — 'The striking thing about our
  CompCert results is that the middle-end bugs we found in all other compilers are absent'
  (p.6). Their own conclusion (p.10) is that 'verification does not obviate testing, but
  rather complements it.' 12 pages; read the CompCert paragraphs on p.6 and the
  'relationship between testing and verification' discussion on p.10 (~15 min).

- **Marc Brooker, "Formal Methods Only Solve Half My Problems" (one-page submission to HPTS'22), Marc's Blog, 2 June 2022** (primary, 2022)  
  <https://www.brooker.co.za/blog/2022/06/02/formal.html>  
  This is the assigned reading: one page, five minutes, and it argues against the question's
  framing from the inside. Brooker is an AWS principal engineer and a co-author of the 2014
  TLA+ paper above, yet he argues that in industry formal methods are not used for full
  verification, that they target safety and liveness, and that safety and liveness are 'only
  a small part of a larger overall picture' — latency, cost, capacity and failure-mode
  behavior are not addressed at all. It is the strongest argument for 'design is the residual
  skill' and, read the other way, the strongest argument that we simply have not formalized
  those questions yet.

- **DORA (Google Cloud), "State of AI-assisted Software Development" 2025 report** (report, 2025)  
  <https://dora.dev/research/2025/dora-report/>  
  The field evidence on where AI actually lands and where human review still matters: ~5,000
  respondents surveyed 13 Jun-21 Jul 2025 plus 100+ hours of qualitative data. 90% use AI and
  >80% believe it raised their productivity, yet 30% report little or no trust in AI-generated
  code. The headline finding is that AI adoption now *improves* delivery throughput — 'a key
  shift from last year' — while still *increasing* delivery instability, and the report
  explicitly recommends training people to 'critically guide, evaluate, and validate AI-
  generated work.' 142-page PDF; read only the Executive summary, pp.3-9 (~15 min). Watch the
  method: it is a self-report survey, so every finding in it is a correlation, not a cause.

- **Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud, "We are Changing our Developer Productivity Experiment Design," METR, 24 February 2026** (report, 2026)  
  <https://metr.org/blog/2026-02-24-uplift-update/>  
  The most important corrective here, and the reason not to cite the famous 19% number as
  current. METR's own authors report that the 19% slowdown (CI +2% to +39%, N=16, Feb-Jun
  2025) is likely no longer representative; that their larger follow-up (57 developers, 143
  repos, 800+ tasks) yields point estimates of -18% and -4% whose intervals both cross zero;
  and that they judge those estimates unreliable because 30-50% of participants withheld
  tasks they did not want to do without AI. It cuts against the AI-skeptical evidence in this
  list as hard as it cuts against AI boosters — the honest position is that nobody can
  currently measure this. ~10 minutes. The superseded 2025 study is at
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ and now carries an
  'out of date' banner.

- **GitHub, Spec Kit — README ("Define what to build before building it — with any AI coding agent"), open-source repository** (tool, 2026)  
  <https://raw.githubusercontent.com/github/spec-kit/main/README.md>  
  The 'AI writes code, humans write specs' thesis stated plainly by a vendor, in its own
  words: 'specifications become executable, directly generating working implementations rather
  than just guiding them.' Essential for Q4: hold this sense of 'specification' next to a TLA+
  model and see whether they are the same kind of object. Equally important, the README files
  its aims under 'Experimental Goals' and talks about 'validating the hypothesis' — by the
  project's own account spec-driven development is unproven, and this is a vendor page, so
  take the claims as claims. ~10 minutes; read the 'What is Spec-Driven Development?', 'Core
  Philosophy' and 'Experimental Goals' sections.

- **Madeline Endres, Sarah Fakhoury, Saikat Chakraborty, Shuvendu K. Lahiri, "Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?", Proc. ACM Softw. Eng. (PACMSE), FSE 2024; arXiv:2310.01831** (academic, 2024)  
  <https://arxiv.org/abs/2310.01831>  
  The counter-argument that verification is not a safe harbour either: peer-reviewed evidence
  that LLMs can already translate informal intent into formal, machine-checkable
  postconditions (nl2postcond), with generated postconditions catching 64 real historical bugs
  from Defects4J. If spec-writing is the human moat, this is the paper showing the moat is
  already being drained at the assertion level. NOTE: only the arXiv abstract page was
  verified for this entry, not the results sections — do not quote precision/recall figures
  from it. Read the abstract and introduction (~15 min).

- **Tim Anderson, "Contracts are in C++26 despite disagreement over their value," The Register, 31 March 2026** (news, 2026)  
  <https://www.theregister.com/software/2026/03/31/contracts-are-in-c26-despite-disagreement-over-their-value/5229065>  
  Journalism, short, and the best live proof that 'writing specifications' is not a settled,
  obviously-valuable skill. WG21 approved C++26 on 28 March 2026 including Contracts
  (preconditions, postconditions, assertions) on a split vote of 114-12-3, over Bjarne
  Stroustrup's objection that 'it's claimed to be a minimal viable product. It's not minimal,
  it's not viable,' his statement that he will recommend not using contracts, and his worry
  'about whether we can use it correctly.' Herb Sutter concedes 'sustained technical
  concerns.' Contracts were also in the C++20 draft and removed in 2019. This one argues the
  other way on the spec-centric reading: the most experienced practitioners alive disagree
  about whether lightweight specification pays. It is a news report, not a study, so it is
  evidence of disagreement and nothing more. ~8 minutes.

## What you submit

One paragraph, 150–250 words, by **Sat Nov 7, 11:59 p.m.**, to the `D8` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
