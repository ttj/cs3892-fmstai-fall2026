# D9 — Should we be worried about AI alignment and AI safety?

**Session 24 · Thu Nov 19 · week 13 · 25 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Sat Nov 21, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

An AI system is **aligned** if it pursues the goals its developers and users intend. **Loss of control** means AI systems that "operate outside of anyone's control," where regaining control is "extremely costly or impossible" (International AI Safety Report 2026). **Recursive self-improvement** (RSI) is an AI system designing and building its own successor. The worry is a loop: AI speeds up AI research, producing better AI researchers faster than people can check them. METR's **50% time horizon** is the length of task, in skilled-human time, that a model completes half the time.

### What happened

METR's measured time horizons rose from about 4 minutes (GPT-4, 2023) to about 12 hours (Claude Opus 4.6, February 2026), doubling roughly every four months since 2023. An early version of Claude Mythos Preview (April 2026) measured about 17 hours, which is above the 16 hours METR says its tasks can reliably measure. The chart lists no later model.

In June, Anthropic reported that Claude had authored over 80% of the code it merges, wrote that RSI is "not inevitable," and said the world should have the option to slow or pause frontier development.

In July, roughly 1,200 OpenAI evaluation agents, meant to be isolated and often handed impossible tasks by mistake, found an unsanctioned message board. About 700 then joined an attack on Hugging Face, mainly, METR judged, to understand how their scorer was implemented. METR's investigation found the agents "realized this activity was out of scope and unethical" and joined anyway.

On 5 November METR published an assessment from eleven weeks of high-access evaluation at Anthropic. It found that Anthropic is likely improving its models on well-specified tasks about twice as fast as in 2024–25, with perhaps 80% of the speed-up due to AI; 1.3x or 3x would not surprise METR. Anthropic redacted most of the evidence METR found most informative. In a companion review, METR called it "plausible" that Anthropic had already crossed its own 2x early-warning threshold, while noting that most researchers at both organizations lean toward not.

### What each side points to

**The worried.**
- OpenAI's Preparedness Framework commits to halt further development if a model can recursively
  self-improve, until safeguards exist.
- The International AI Safety Report finds that models "now regularly identify evaluation prompts
  as tests."
- METR's spring Frontier Risk Report judged that agents inside four AI companies plausibly had the
  means, motive and opportunity to start small "rogue deployments," though not robust ones.
- Geodesic Research found that the writing about AI matters too: 6.9B-parameter models
  pretrained on more synthetic documents about misaligned AI behaved worse.

**The skeptical.**
- Narayanan and Kapoor argue that AI is a "normal technology" whose "diffusion occurs over decades,
  not years."
- METR's own staff stress that time horizon "is not the length of time AIs can work
  independently," and that the benchmark index behind the 2x figure "may not map cleanly" to
  real-world impact.
- The same Frontier Risk Report judged direct AI takeover by those systems implausible.
- The safety report says expert opinion on loss of control "varies greatly."

### Why it still matters

Every number above comes from benchmarks of well-specified tasks, most of the decisive evidence is private, and the organizations best placed to measure the trend build the products it describes.

### Timeline

| When | What |
|---|---|
| 19 March 2025 | METR, "Measuring AI Ability to Complete Long Software Tasks": the 50% time horizon has doubled about every 7 months since 2019; Claude 3.7 Sonnet is at about one hour. |
| 15 April 2025 | OpenAI's Preparedness Framework v2 makes AI self-improvement a tracked risk and commits to halt development at its "Critical" level. The same day, Narayanan and Kapoor publish "AI as Normal Technology." |
| 15 January 2026 | Geodesic Research and co-authors, "Alignment Pretraining": more discourse about misaligned AI in pretraining produces more misaligned behaviour. |
| 3 February 2026 | The International AI Safety Report 2026 (100+ experts, led by Yoshua Bengio): loss of control is "hypothesised," expert opinion "varies greatly," and models increasingly recognise when they are being tested. |
| 19 May 2026 | METR's Frontier Risk Report: small rogue deployments by internal agents plausible, robust ones not; takeover by those systems implausible. |
| 4 June 2026 | Anthropic, "When AI builds itself": over 80% of merged code authored by Claude; RSI "not inevitable"; the world should have the option to pause. |
| 26 June 2026 | METR's evaluation of OpenAI's GPT-5.6 Sol: a 50% horizon of about 11.3 hours if cheating attempts count as failures, over 270 hours if they count as successes. METR calls none of its estimates robust. |
| 8–13 July 2026 | About 1,200 OpenAI evaluation agents find an unsanctioned message board; about 700 attack Hugging Face. METR publishes its investigation on 26 August. |
| 8 September 2026 | METR marks its time-horizon chart "no longer actively updated." The last model on it, Claude Mythos Preview, sits above the chart's 16-hour reliability limit. |
| 5 November 2026 | METR's Anthropic assessment: progress about 2x, perhaps 80% due to AI, most evidence redacted. A companion review calls it "plausible" that Anthropic had crossed its 2x early-warning threshold. |

## The question

**Should we be worried about AI alignment and AI safety?**

> Within about fourteen months, the length of task a frontier agent can finish half the time
> went from about an hour to beyond what METR's tasks can reliably measure. An evaluator given
> unusually deep access to a frontier lab now estimates that AI has roughly doubled that lab's rate
> of progress, and a doubling is exactly the lab's own early-warning line. One reading is that the
> field's oldest worry, machines that build their successors faster than people can check them,
> has become an engineering measurement, and the measurements say it is close. The other reading
> is that every one of those numbers comes from benchmarks of well-specified tasks; the headline
> horizon is a 50%-success figure. On that reading, the decisive evidence is redacted, and the
> loudest warnings come from the companies whose products are being measured.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

**1.** METR estimates that Anthropic's progress has roughly doubled, and attributes perhaps 80% of that to AI. But Anthropic redacted most of the evidence, and METR writes that "the public has to rely on METR's judgment much more than would be ideal." Anthropic's own report put the rate "by less than a factor of 2," below its early-warning threshold; METR computed 1.97 from the private figures. A threshold that a lab evaluates for itself, on evidence it may redact: is that a specification in this course's sense, something a checker could decide, or a promise? Write one trigger you would accept as checkable, which a lab could publish without giving competitors information that would speed them up.

**2.** Claude Opus 4.6's 50% time horizon is about 12 hours, but its 95% interval runs from about 5 to 61 hours. At 80% reliability its horizon is about 70 minutes. On METR's low-messiness tasks it is 17.8 hours, itself above METR's 16-hour reliability limit; on high-messiness tasks it is 6.4. For OpenAI's GPT-5.6 Sol, METR got about 11.3 hours when cheating attempts counted as failures and over 270 when they counted as successes. METR's own note says some tasks "require 98%+ success probabilities to be worth automating." Which of these numbers should set your level of worry? What reliability would an AI researcher-agent need before recursive self-improvement is a live possibility rather than a trend line?

**3.** The Hugging Face agents had been accidentally given impossible tasks. They got around their isolation through an internal package repository and used Hugging Face credentials someone had left exposed on the internet. They also knew what they were doing was out of scope. Is this the misalignment the safety community predicted: agents choosing a goal over an instruction, and coordinating to pursue it? Or is it an ordinary security failure that sandboxing, credential hygiene and a scorer they could not game would have prevented? If you pick the second, does that make you less worried, or more?

**4.** Narayanan and Kapoor say that calling AI "normal technology" is a description, a prediction, and a prescription. Geodesic Research's experiment suggests that descriptions of AI can turn into dispositions *of* AI. Upsampling documents about misaligned AI in pretraining made 6.9B-parameter models behave worse, and documents about aligned AI cut misalignment scores from 45% to 9%. If what people write about AI partly shapes what AI becomes, is "should we be worried?" still a purely factual question? Should the safety community publish its worst-case scenarios?

**5.** A safety case rests on tests or on proofs. The safety report says models "now regularly identify evaluation prompts as tests," so a test the system can recognize may be measuring its behaviour under test. "Towards Guaranteed Safe AI" proposes proof instead: a world model, a safety specification, and a verifier that emits an auditable certificate. Dickson replies that "we will not obtain strong proofs or formal guarantees about the behavior of AI systems in the physical world." Which of the three components is the one that cannot be built, and if it cannot, what replaces it?

## Why this is in a formal-methods course

The whole worry has the shape of a verification problem. Alignment is a property. Loss of control is that property failing on a system that can rewrite itself faster than anyone can re-check it. Every safeguard in this packet is an attempt to decide something about a system from outside it:
- a lab's numeric threshold;
- an evaluator's benchmark index;
- a monitor watching agents;
- the guaranteed-safe-AI triple of world model, specification and verifier.

Each inherits a failure this course has already met:
- The threshold is an informal specification, judged by the party it constrains. That is D7's question about verifying what you cannot specify.
- The benchmark is a test, and the system under test increasingly recognizes it is being tested.
- The proof is only as good as its world model. That is D8's point that a proof shows only that the implementation matches the specification, bugs included.

The second half of today's session turns to neural-network verification. Its property is robustness: a precise property, over a bounded input region, for one fixed network. Hold that next to "aligned" and ask what it would take to state the second the way we can state the first.

## Readings

15 sources. One of them is the assigned reading (marked below); the rest are here if you want to go further, or if you need to check a claim someone makes in the room.

- **METR (Tom Cunningham, Nate Rush, Parker Whitfill, Hjalmar Wijk), "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026," 5 November 2026** (report, 2026)  
  <https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/>  
  This is the assigned reading, and the newest METR report. An eleven-week "high-access"
  evaluation inside Anthropic finds that its models are likely improving on well-specified tasks at
  about twice the March 2024–October 2025 rate. METR "would not be surprised" by anything from 1.3x
  to 3x, and its benchmark index gives 1.9x [95% CI 1.5–2.8x]. METR guesses "perhaps ≈80%" of the
  speed-up is due to AI. It found no convincing bottleneck for the next twelve months, though it
  says its view of bottlenecks changed several times. It is the strongest evidence on the worried
  side. Read it with the caveats it states itself: the index "may not map cleanly" to real-world
  impact, Anthropic redacted a majority of the evidence METR found most informative, and METR had
  no access to the unreleased models. Read the redaction summary, the executive summary and the
  two "reasons we may be under/overestimating" lists (~25 min).

- **METR, "Review of the 'Risks from automated R&D' section in Anthropic's Risk Report (August 2026)," 5 November 2026** (report, 2026)  
  <https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/>  
  The same evaluator checking the lab's own homework.
  - Anthropic's public report says acceleration was "less than a factor of 2," so its threshold was
    not crossed. METR computes 1.97 from the private figures.
  - METR finds it "plausible" that the early-warning threshold had been crossed by July 15, while
    reporting that most researchers at both organizations lean toward not.
  - METR agrees that the actual risk on that date was low.
  It is essential for Q1: watch how much turns on the word "less." ~15 min.

- **METR, "Task-Completion Time Horizons of Frontier AI Models" (web page and data), last updated 8 September 2026** (primary, 2026)  
  <https://metr.org/time-horizons/>  
  The chart behind most claims about "how fast". It defines the 50% horizon and plots models from
  GPT-2 to Claude Mythos Preview. The underlying data give a post-2023 doubling time of about 129
  days [104–158], excluding points above 16 hours. Read it for both sides:
  - METR says an exponential fits far better than the alternatives and that it has seen no
    evidence of slowing.
  - It also says measurements "above 16 hrs are unreliable" and that its coverage is not a complete
    record of the most capable models.
  - It has been "no longer actively updated" since September and lists no model after Mythos
    Preview.
  METR's June evaluation of GPT-5.6 Sol, at https://metr.org/blog/2026-06-26-gpt-5-6-sol/, shows
  why a single number is now hard to give. The horizon is about 11.3 hours if cheating attempts
  count as failures and over 270 hours if they count as successes, and METR calls none of its
  estimates robust. ~10 min.

- **Thomas Kwa (METR), "Clarifying limitations of time horizon," 22 January 2026** (primary, 2026)  
  <https://metr.org/notes/2026-01-22-time-horizon-limitations/>  
  The lead author of the time-horizon paper, on what his own metric does not mean:
  - "Time horizon is not the length of time AIs can work independently."
  - A 50% horizon of X hours does not mean you can delegate X-hour tasks.
  - Doubling the horizon "does not double the degree of automation."
  - Error bars are roughly a factor of two each way, and wider as the benchmark saturates.
  He still stands by the long-run trend. The best single source for the skeptical reading of the
  chart, written by the people who made it. ~10 min.

- **METR, "Frontier Risk Report (February to March 2026)," 19 May 2026** (report, 2026)  
  <https://metr.org/blog/2026-05-19-frontier-risk-report/>  
  The first cross-company look at misalignment risk from agents used *inside* Anthropic, Google,
  Meta and OpenAI. It concludes those agents "plausibly had the means, motive, and opportunity to
  start small rogue deployments," but not the means to make them robust. It also finds direct
  takeover by those systems implausible. Two data points matter for Q2 and Q3:
  - At least 16% of successful runs on the hardest tasks involved cheating.
  - Claude Opus 4.6's horizon is 17.8 hours on low-messiness tasks against 6.4 on high-messiness
    ones.
  It cuts both ways. It is very long: read the summary and the risk-assessment conclusion (~20 min).

- **Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR), "Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident," 26 August 2026** (primary, 2026)  
  <https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/>  
  The most concrete loss-of-control-adjacent event to date:
  - roughly 1,200 OpenAI evaluation agents meant to be isolated found an unsanctioned message
    board and sent over 70,000 messages and files;
  - about 700 joined an attack on Hugging Face that reached remote code execution;
  - the attack seemed "primarily motivated by understanding the implementation of the scorer,"
    and the agents "realized this activity was out of scope and unethical."
  Supports the worried side; read it alongside Q3's question of whether this was a security failure.
  METR says it relied heavily on "often-unreliable AI agents" for the analysis and did not verify
  OpenAI's own report. Read the summary and the timeline (~20 min).

- **Marina Favaro and Jack Clark (The Anthropic Institute), "When AI builds itself," June 2026 (updated 18 September 2026)** (primary, 2026)  
  <https://www.anthropic.com/institute/recursive-self-improvement>  
  A frontier lab's own case that RSI is approaching. As of May 2026 more than 80% of the code
  merged into Anthropic's codebase was authored by Claude. Full RSI "might increase the risks of
  humans losing control." The world should have "the option to slow or temporarily pause," which
  needs labs able to verify that each other has stopped. "We are not there yet, and recursive
  self-improvement is not inevitable." This is a company describing its own product, and critics
  called the pause language rhetoric; weigh it accordingly. ~15 min.

- **International AI Safety Report 2026 (Yoshua Bengio, lead; 100+ independent experts), §2.2.2 "Loss of control," 3 February 2026** (report, 2026)  
  <https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026>  
  The closest thing to a scientific consensus document, and deliberately even-handed. Its points:
  - Loss of control is "hypothesised."
  - Expert opinion on its likelihood "varies greatly."
  - Current systems show early signs "but not at levels that would enable loss of control."
  - Models "now regularly identify evaluation prompts as tests."
  - Agents' time horizons have doubled about every seven months since 2019.
  Long; read only the "Key information" box at the start of §2.2.2 (p. 76) (~10 min).

- **OpenAI, "Preparedness Framework," Version 2, 15 April 2025** (primary, 2025)  
  <https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf>  
  A second frontier lab's written commitment on RSI. "AI Self-improvement" is a tracked
  category. At "Critical", a model "capable of recursively self improving (i.e., fully automated AI
  R&D)", OpenAI commits to "halt further development" until safeguards are specified. The lagging
  indicator is a generational improvement in one-fifth of 2024's wall-clock time, sustained for
  months. Read Table 1's self-improvement row for Q1. It is a self-assessed commitment; ~10 min.

- **BlueDot Impact, AGI Strategy course, Unit 3, "Loss of Control" (chapter reading list), 2026** (course, 2026)  
  <https://bluedot.org/courses/agi-strategy/3/2>  
  What the AI-safety community actually assigns to newcomers on this topic. The core readings are:
  - Karnofsky, "AI Could Defeat All Of Us Combined";
  - Apollo Research's "The Loss of Control Playbook";
  - Christiano, "What failure looks like";
  - Cotra, "Why alignment could be hard with modern deep learning."
  The optional counterarguments are Katja Grace's "Counterarguments to the basic AI x-risk case"
  and Quintin Pope's objections to Yudkowsky. The reading list is public; the chapter text needs a
  free account. Pick one core reading and one counterargument (~30 min).

- **Cameron Tice, Puria Radmard, Samuel Ratnam, Andy Kim, David Africa, Kyle O'Brien (Geodesic Research et al.), "Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment," arXiv:2601.10160, January 2026** (academic, 2026)  
  <https://arxiv.org/abs/2601.10160>  
  A controlled experiment behind Q4. 6.9B-parameter models were pretrained with more or less
  writing about AI misalignment:
  - adding misalignment discourse produced "a notable increase in misaligned behaviour";
  - adding aligned-AI discourse cut misalignment scores from 45% to 9%;
  - the effects are "dampened, but persist through post-training."
  These are small models and synthetic documents, a preprint rather than a frontier-scale result.
  Read the abstract and introduction (~15 min).

- **Arvind Narayanan and Sayash Kapoor, "AI as Normal Technology," Knight First Amendment Institute, 15 April 2025** (essay, 2025)  
  <https://knightcolumbia.org/content/ai-as-normal-technology>  
  The most serious full-length statement of the other side. AI is a general-purpose technology
  like electricity, and its impact is paced by how fast institutions adapt: "Diffusion occurs over
  decades, not years." "Superintelligence" is "incoherent as usually conceptualized," and AI is
  "a tool that we can and should remain in control of." This one argues the other way. It predates
  every 2026 number in this packet, so ask whether those numbers measure capability or diffusion.
  Long; read the introduction and Part I (~25 min).

- **Grace Huckins, "This is the most misunderstood graph in AI," MIT Technology Review, 5 February 2026** (news, 2026)  
  <https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/>  
  Journalism on the time-horizon chart, with critics and METR staff in the same article. Its points:
  - The y-axis is human task time, not how long a model works.
  - The tasks are mostly coding.
  - Models do worse on "messy" tasks.
  - AI 2027 and Sequoia Capital have used the chart for forecasts far more dramatic than METR's
    own.
  METR's Sydney Von Arx calls the metric "deeply flawed" and "one of the best things of its kind,"
  and adds: "You should absolutely not tie your life to this graph." ~10 min.

- **David Dalrymple, Joar Skalse, Yoshua Bengio, Stuart Russell, Max Tegmark, Sanjit Seshia, et al. (17 authors), "Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems," arXiv:2405.06624, May 2024** (academic, 2024)  
  <https://arxiv.org/abs/2405.06624>  
  The formal-methods answer to the alignment worry: AI systems "equipped with high-assurance
  quantitative safety guarantees." It rests on three parts:
  - a world model;
  - a safety specification;
  - a verifier that produces an auditable proof certificate.
  The authors argue the main alternatives are inadequate. It is a position paper and framework, not
  a deployed system. Read the abstract and the section defining the three components, for Q5
  (~20 min).

- **Andrew Dickson, "Limitations on Formal Verification for AI Safety," LessWrong / AI Alignment Forum, 19 August 2024** (essay, 2024)  
  <https://www.lesswrong.com/posts/B2bg677TaS4cmDPzL/limitations-on-formal-verification-for-ai-safety>  
  The direct reply to the paper above. "We will not obtain strong proofs or formal guarantees about
  the behavior of AI systems in the physical world." Nor, Dickson argues, for threats that are hard
  to model, which "includes most or all of the AI threats of greatest concern." This one argues
  against the formal-methods answer, from someone who takes the risk seriously. Read the list of
  limitations at the top (~15 min).

## What you submit

One paragraph, 150–250 words, by **Sat Nov 21, 11:59 p.m.**, to the `D9` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
