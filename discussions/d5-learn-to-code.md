# D5 — If AI Writes All Our Software, Do We Still Need to Learn to Code?

**Session 8 · Tue Sep 22 · week 5 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Thu Sep 24, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### Two experiments that disagree

A **randomized controlled trial (RCT)** assigns participants to conditions by chance rather than by choice — here, "you get the AI tool" or "you don't." Randomization is what licenses a causal claim: because the groups differ only by luck, a gap in outcomes can be credited to the treatment. What it does not do is extend that claim beyond the people and tasks actually in the trial.

Two such trials, both competently run, disagree.

In May–June 2022, Sida Peng (Microsoft Research) with colleagues at GitHub and MIT Sloan recruited 95 freelance programmers on Upwork and asked them to implement an HTTP server in JavaScript as fast as possible. Forty-five got GitHub Copilot; fifty did not. The Copilot group finished **55.8% faster** — 71 minutes on average against 161.

From February to June 2025, the research nonprofit METR ran a trial with **16 experienced open-source maintainers** across **246 real issues** in their own repositories — projects averaging 22,000+ GitHub stars and a million lines of code, where each developer had roughly five years of history. Each issue was randomly assigned to allow or forbid AI tools (mostly Cursor Pro with Claude 3.5/3.7 Sonnet). With AI, they took **19% longer** per task.

### What the trials actually found

Peng et al.'s speedup carries a 95% confidence interval of **21–89%** — a very wide band — and is computed among developers who completed the task. The study did define "correct": the repository shipped a **twelve-check test suite** participants could see but not alter. The Copilot group's success rate was 7 percentage points higher, but that difference was **not statistically significant** (CI −0.11 to 0.25). Speed moved; measured correctness did not detectably move. The paper also reports that *less* experienced developers gained the most.

METR's second result concerns self-report rather than speed. Beforehand, participants forecast AI would make them 24% faster; afterward, measured 19% slower, they still believed it had sped them up by about 20%. The authors explicitly decline the general reading: their work is not evidence that AI fails to speed up many or most developers. It describes veterans, in code they know deeply, with early-2025 tooling.

Notice what each study *could* measure. Peng et al. had a written-down definition of done, so it could report time and correctness. METR's task was "resolve this GitHub issue," which has no ground truth, so wall-clock time was nearly all there was.

### Why it still matters

Beyond the trials: DORA's 2025 report (~5,000 self-selected professionals, correlational) finds a *positive* relationship between AI adoption and delivery throughput, reversing its own 2024 finding, while AI "does continue to have a negative relationship with software delivery stability." A 2022 Stanford lab study (Perry et al., 47 participants, OpenAI's codex-davinci-002) found participants with an AI assistant "wrote significantly less secure code" and were "more likely to believe they wrote secure code."

On jobs: Brynjolfsson, Chandar and Chen, using ADP payroll data through June 2026, place 22–25 year olds in AI-exposed occupations 19% below where employment would be had it kept pace with less-exposed peers, through reduced hiring rather than layoffs. They call these "early, descriptive indicators — canaries in the coal mine — rather than causal estimates," and do not single out software developers. (That 19% and METR's are unrelated quantities that happen to share digits.)

### Timeline

| When | What |
|---|---|
| May–June 2022 | Peng et al. run the Copilot RCT: 95 freelance programmers recruited on Upwork, an HTTP-server task in JavaScript, graded by a fixed 12-check test suite participants can see but not alter. |
| November 2022 | Perry, Srivastava, Kumar and Boneh post "Do Users Write More Insecure Code with AI Assistants?" to arXiv (later CCS '23): 47 analyzed participants, OpenAI codex-davinci-002; assisted participants wrote significantly less secure code and were more likely to believe it was secure. |
| February 13, 2023 | The Copilot trial is posted to arXiv (2302.06590): 55.8% faster, 95% CI 21–89%, computed among task completers; the treated group's success rate is 7 points higher and not statistically significant. |
| March 19, 2025 | Simon Willison argues that "vibe coding" — which he characterizes, quoting Karpathy, as forgetting the code exists — has drifted into a label for all AI-assisted programming. |
| February–June 2025 | METR runs its RCT: 16 veteran open-source maintainers, 246 real issues in repositories they have worked in for about five years, mostly Cursor Pro with Claude 3.5/3.7 Sonnet. |
| July 10, 2025 | METR publishes: developers took 19% longer per task with AI, having forecast a 24% speedup and still believing afterward they were about 20% faster. |
| September 23, 2025 | The 2025 DORA report (~5,000 respondents) reports a positive relationship between AI adoption and delivery throughput — reversing its own 2024 finding — while AI "does continue to have a negative relationship with software delivery stability." |
| August 12, 2026 | Stanford Digital Economy Lab revises "Canaries in the Coal Mine": ADP payroll data through June 2026 places 22–25 year olds in AI-exposed occupations 19% below where employment would be had it kept pace with less-exposed peers, via reduced hiring; the authors call this descriptive, not causal. |

## The question

**Is knowing when the AI is wrong a coding skill?**

> In 2022, ninety-five freelance developers were randomized to build an HTTP server with or
> without GitHub Copilot; the ones with it finished 55.8% faster. In 2025, sixteen experienced
> open-source developers were randomized across 246 real issues in repositories they had
> contributed to for about five years; the ones with AI took 19% longer, and still believed
> afterward that they had been sped up by 20%. Both were genuine randomized experiments, both were
> competently run, and they disagree because they studied different people, doing different work,
> under different definitions of "done." Your job for the next half hour is to work out what
> someone starting a CS degree in 2026 should actually conclude from that.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

**1.** METR's developers mis-estimated their own speed by roughly 39 percentage points, in the
direction that flattered the tool. Suppose that miscalibration is general. Does that make
developer self-report worthless as evidence about AI productivity — or does it make self-report
the single most important thing to measure, given that hiring, tooling, and curriculum decisions
will be made on perceived value regardless of measured value?

**2.** Peng et al. measured a 55.8% speedup on a task with a fixed, immutable 12-check test suite. METR
measured a 19% slowdown on real GitHub issues, where there is no ground-truth definition of
'done.' Assume both numbers are correct. Is the difference mainly about the people (novice
freelancers versus veteran maintainers), or mainly about whether anyone had written down what
'finished' means — and which of those two differences will still exist in the job you take after
graduating?

**3.** DORA 2025 reports that AI raises throughput and lowers stability, and argues AI is an
'amplifier' of whatever engineering practice already exists. If that is right, the scarce skill
is no longer producing code but operating the control systems — tests, review, version control,
fast feedback — that make acceleration survivable. Is that still 'learning to code,' or is it a
different discipline that we are labeling continuously with the past to reassure ourselves?

**4.** Assembly gave way to compilers, compilers to high-level languages, and at each step someone
argued the lower layer was essential knowledge. Is natural-language prompting the next rung on
that ladder, or a different kind of step altogether? Name the strongest disanalogy you can find
between a compiler and an LLM — then argue against your own disanalogy.

**5.** Brynjolfsson et al. find a 19% employment gap for 22–25 year olds in AI-exposed occupations, but
explicitly call it descriptive rather than causal, and never single out software developers.
Suppose that ambiguity is never resolved in time to help you. Does not knowing whether the
entry-level market shrank because of AI or because of the post-2022 rate environment change what
you should personally do this semester — or is the rational response identical under both
explanations?

## Why this is in a formal-methods course

The one study in this packet that produced a clean, statistically significant effect could do so
only because someone had written down in advance what "correct" meant: Peng et al. gated
completion time on an immutable 12-check test suite, whereas METR could measure nothing but
wall-clock time because "resolve this GitHub issue" has no ground truth, and Perry et al. needed
human analysts to hand-grade security. The measurement problem running through this entire
literature is therefore a specification problem — which is precisely this course's subject. And
note what happened in the one place correctness *was* measured: Copilot's speed effect was
significant while its 7-percentage-point success-rate advantage was not, which is exactly the
gap between "produced code faster" and "produced correct code" that verification exists to
close.

## Readings

9 sources. One is assigned; the rest are here if you want to go further, or to check a claim that comes up in the room.

- **Joel Becker, Nate Rush, Elizabeth Barnes, David Rein — "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (METR)** (report, 2025)  
  <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>  
  The assigned reading (~20 min) and the strongest evidence that AI can slow experts down: 16
  veteran OSS developers, 246 real issues, 19% slower while forecasting a 24% speedup and
  still believing afterward they were 20% faster. Supports the 'still learn to code' side.
  Do not skip the caveats section — the authors explicitly refuse the generalization most
  people draw from this study. Fuller version is arXiv:2507.09089.

- **Sida Peng (Microsoft Research), Eirini Kalliamvakou & Peter Cihon (GitHub), Mert Demirer (MIT Sloan) — "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot," arXiv:2302.06590** (academic, 2023)  
  <https://arxiv.org/abs/2302.06590>  
  The strongest source on the other side: 55.8% faster on an HTTP-server task. The part you
  need is the abstract plus Results (~10 min). Three details carry the weight here: the 95%
  CI is a very wide 21–89%, the effect is computed conditioning on task completion, and the
  paper reports that *less*-experienced developers benefited most — the exact mirror of METR.
  Two of four authors worked for GitHub, the vendor of the tool studied.

- **Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh — "Do Users Write More Insecure Code with AI Assistants?" arXiv:2211.03622 (CCS '23)** (academic, 2022)  
  <https://arxiv.org/abs/2211.03622>  
  Supports the 'still learn to code' side: participants with an AI assistant wrote
  significantly less secure code while being *more* likely to believe it was secure. The
  durable finding is the confidence/security divergence, not any single percentage. Note the
  model studied (codex-davinci-002) is now several generations obsolete — whether that
  invalidates the result is itself a live argument.

- **Google Cloud / DORA — "Announcing the 2025 DORA Report: State of AI-assisted Software Development"** (report, 2025)  
  <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>  
  Cuts both ways, and the best antidote to cherry-picking. Across ~5,000 professionals, AI
  adoption is now positively associated with delivery throughput — an explicit reversal of
  DORA's own 2024 finding — while it 'does continue to have a negative relationship with
  software delivery stability.' Read the announcement post rather than the full report; the
  framing of AI as an 'amplifier' of existing practice is the part worth arguing with.

- **Stack Overflow — 2025 Developer Survey, AI section** (tool, 2025)  
  <https://survey.stackoverflow.co/2025/ai>  
  Practitioner sentiment at scale: 84% use or plan to use AI tools, yet only 3.1% highly trust
  their accuracy, ~46% actively distrust, and 66% name 'almost right, but not quite' as their
  top frustration. Skim in 10 minutes. Watch the limitation before you cite any of it: this is
  a self-selected, non-probability sample — it measures sentiment among opt-in respondents,
  not tool quality.

- **GitClear — "The Maintainability Gap: 2026 AI Code Quality Research"** (report, 2026)  
  <https://www.gitclear.com/the_ai_code_quality_maintainability_gap>  
  The maintainability case against AI-authored code: 623M changes analyzed 2023–2026, block
  duplication up 81% since 2023, moved/refactored code down from 21% (2022) to 3.8% (2026).
  It is also a good source on which to practice *discounting*: GitClear sells code-analytics
  tooling, the moved-vs-copy/paste categories are proprietary definitions, and the report
  itself claims correlation rather than causation.

- **Erik Brynjolfsson, Bharat Chandar, Ruyu Chen — "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence," Stanford Digital Economy Lab (rev. Aug 12, 2026)** (academic, 2026)  
  <https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/>  
  The primary evidence on entry-level hiring: ADP payroll data through June 2026 shows workers
  aged 22–25 in AI-exposed occupations sitting 19% below where they would be had they kept
  pace with less-exposed peers, driven by reduced hiring rather than separations. Long — the
  parts you need are the six facts and the caveats. Crucially, the authors call these 'early,
  descriptive indicators... rather than causal estimates,' and the paper does not single out
  software developers.

- **Stanford Digital Economy Lab — "Canaries, Interest Rates, and Timing: More on Recent Drivers of Employment Changes for Young Workers"** (report, 2026)  
  <https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers>  
  The source that most complicates the easy story, and it comes from the same lab that told
  the story. It rebuts the interest-rate explanation (AI-exposed jobs are on average *less*
  rate-sensitive) but concedes that under firm-time fixed effects the decline is significant
  only after 2024, and that 'we do not believe that AI is always and everywhere the sole
  determinant of employment.' Short; read it alongside the Canaries paper.

- **Simon Willison — "Not all AI-assisted programming is vibe coding"** (news, 2025)  
  <https://simonwillison.net/2025/Mar/19/vibe-coding/>  
  Establishes what 'vibe coding' actually meant, quoting Karpathy's original framing verbatim
  — 'fully give in to the vibes, embrace exponentials, and forget that the code even exists,'
  for throwaway weekend projects — and argues the term has drifted to cover all AI-assisted
  work. A 5-minute read, and the one to do first: letting the definition slide silently
  decides the debate before it starts. (Karpathy's original post is on X, which cannot be
  fetched; this is a secondary source quoting it.)

## What you submit

One paragraph, 150–250 words, by **Thu Sep 24, 11:59 p.m.**, to the `D5` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
