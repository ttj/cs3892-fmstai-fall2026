# D5 — If AI Writes All Our Software, Do We Still Need to Learn to Code?

**Session 8 · Tue Sep 22 · week 5 · 30 minutes · think–pair–share**

## Framing

> In 2022, ninety-five freelance developers were randomized to build an HTTP server with or
> without GitHub Copilot; the ones with it finished 55.8% faster. In 2025, sixteen experienced
> open-source developers were randomized across 246 real issues in repositories they had
> contributed to for about five years; the ones with AI took 19% longer, and still believed
> afterward that they had been sped up by 20%. Both were genuine randomized experiments, both were
> competently run, and they disagree because they studied different people, doing different work,
> under different definitions of "done." Your job for the next half hour is to work out what
> someone starting a CS degree in 2026 should actually conclude from that.

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

## Discussion questions

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

## Readings

9 sources, 9 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Joel Becker, Nate Rush, Elizabeth Barnes, David Rein — "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (METR)** (report, 2025)  
  <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>  
  The assigned reading (~20 min) and the strongest evidence that AI can slow experts down: 16
  veteran OSS developers, 246 real issues, 19% slower while forecasting a 24% speedup and
  still believing afterward they were 20% faster. Supports the 'still learn to code' side.
  Direct students to the caveats section — the authors explicitly refuse the generalization
  most people draw. Fuller version is arXiv:2507.09089.

- **Sida Peng (Microsoft Research), Eirini Kalliamvakou & Peter Cihon (GitHub), Mert Demirer (MIT Sloan) — "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot," arXiv:2302.06590** (academic, 2023)  
  <https://arxiv.org/abs/2302.06590>  
  The deliberate counterweight and the strongest source on the other side: 55.8% faster on an
  HTTP-server task. Assign the abstract plus Results (~10 min). Three details do the teaching:
  the 95% CI is a very wide 21–89%, the effect is computed conditioning on task completion,
  and the paper reports that *less*-experienced developers benefited most — the exact mirror
  of METR. Two of four authors worked for GitHub, the vendor of the tool studied.

- **Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh — "Do Users Write More Insecure Code with AI Assistants?" arXiv:2211.03622 (CCS '23)** (academic, 2022)  
  <https://arxiv.org/abs/2211.03622>  
  Supports the 'still learn to code' side: participants with an AI assistant wrote
  significantly less secure code while being *more* likely to believe it was secure. The
  durable finding is the confidence/security divergence, not any single percentage. Note the
  model studied (codex-davinci-002) is now several generations obsolete — whether that
  invalidates the result is itself a live argument.

- **Google Cloud / DORA — "Announcing the 2025 DORA Report: State of AI-assisted Software Development"** (report, 2025)  
  <https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>  
  Cuts both ways and is the best antidote to cherry-picking. Across ~5,000 professionals, AI
  adoption is now positively associated with delivery throughput — an explicit reversal of
  DORA's own 2024 finding — while it 'does continue to have a negative relationship with
  software delivery stability.' Read the announcement post rather than the full report; the
  framing of AI as an 'amplifier' of existing practice is the part students should argue with.

- **Stack Overflow — 2025 Developer Survey, AI section** (tool, 2025)  
  <https://survey.stackoverflow.co/2025/ai>  
  Practitioner sentiment at scale: 84% use or plan to use AI tools, yet only 3.1% highly trust
  their accuracy, ~46% actively distrust, and 66% name 'almost right, but not quite' as their
  top frustration. Skim in 10 minutes. Important limitation to state in class: self-selected,
  non-probability sample — it measures sentiment among opt-in respondents, not tool quality.

- **GitClear — "The Maintainability Gap: 2026 AI Code Quality Research"** (report, 2026)  
  <https://www.gitclear.com/the_ai_code_quality_maintainability_gap>  
  The maintainability case against AI-authored code: 623M changes analyzed 2023–2026, block
  duplication up 81% since 2023, moved/refactored code down from 21% (2022) to 3.8% (2026).
  Included partly so students can practice *discounting* a source — GitClear sells code-
  analytics tooling, the moved-vs-copy/paste categories are proprietary definitions, and the
  report itself claims correlation rather than causation.

- **Erik Brynjolfsson, Bharat Chandar, Ruyu Chen — "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence," Stanford Digital Economy Lab (rev. Aug 12, 2026)** (academic, 2026)  
  <https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/>  
  The primary evidence on entry-level hiring: ADP payroll data through June 2026 shows workers
  aged 22–25 in AI-exposed occupations sitting 19% below where they would be had they kept
  pace with less-exposed peers, driven by reduced hiring rather than separations. Long —
  assign the six facts and the caveats. Crucially, the authors call these 'early, descriptive
  indicators... rather than causal estimates,' and the paper does not single out software
  developers.

- **Stanford Digital Economy Lab — "Canaries, Interest Rates, and Timing: More on Recent Drivers of Employment Changes for Young Workers"** (report, 2026)  
  <https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers>  
  The reference that most complicates the easy story, and from the same lab that produced it.
  It rebuts the interest-rate explanation (AI-exposed jobs are on average *less* rate-
  sensitive) but concedes that under firm-time fixed effects the decline is significant only
  after 2024, and that 'we do not believe that AI is always and everywhere the sole
  determinant of employment.' Short; assign alongside the Canaries paper.

- **Simon Willison — "Not all AI-assisted programming is vibe coding"** (news, 2025)  
  <https://simonwillison.net/2025/Mar/19/vibe-coding/>  
  Establishes what 'vibe coding' actually meant, quoting Karpathy's original framing verbatim
  — 'fully give in to the vibes, embrace exponentials, and forget that the code even exists,'
  for throwaway weekend projects — and argues the term has drifted to cover all AI-assisted
  work. A 5-minute read that should be assigned first, because letting the definition slide
  silently decides the debate before it starts. (Karpathy's original post is on X, which
  cannot be fetched; this is a secondary source quoting it.)

## 30-minute run sheet

0–3 — FRAMING. Before speaking, write four unlabeled numbers on the board: -19%, +55.8%, 66%,
19%. Read the framing aloud. Tell students that all four are real, all from randomized trials or
large surveys between 2022 and 2026, and that by the end of class they should be able to say
what each measures — and why two of them being the same number is a pure coincidence. Assign one
prompt per table group (Prompts 2, 3, 4, 5 across four groups). Hold Prompt 1 in reserve.

3–8 — THINK (silent, individual, written, no devices). Hand out index cards. Each student writes
exactly two sentences: (1) their answer to their table's prompt; (2) the specific piece of
evidence that would change their mind. Say this out loud: "If your second sentence is 'nothing
would change my mind,' you have a belief, not a position — rewrite it." Circulate, read 5–6
cards silently, and mark two that disagree sharply for the share-out. While circulating, write
three column headers on the board: THROUGHPUT / STABILITY / CORRECTNESS.

8–16 — PAIR. Pair students *across* tables so the prompts differ. Each person hands their card
to their partner, who must argue the other person's position for 60 seconds before responding.
Then the pair produces one joint written claim in this exact form: "Learning to code will still
matter in 2031 because/unless ______, and the evidence is ______, which does not measure
______." The third blank is mandatory — every study in the packet fails to measure something,
and naming it is the skill being drilled.

16–26 — SHARE. Cold-call by table, one joint claim per pair, about 90 seconds each. Do not
evaluate claims as right or wrong. Instead, after each, ask the room: "Which column did that
claim actually provide evidence for?" and write it into THROUGHPUT, STABILITY, or CORRECTNESS.
Expect heavy clustering in THROUGHPUT. If a sharp student puts something in CORRECTNESS early —
likely via Perry et al. and security — do not deflect: ask whether "fewer vulnerabilities in a
hand-graded sample" is a correctness claim or a statistical one, and whether they could write
that property down formally. Around minute 22, when the CORRECTNESS column is visibly thin, say
so out loud and drop Prompt 1 on the whole room as the pivot.

26–30 — CLOSE + COLLECT. Do not resolve the question. State the one structural fact the columns
just exposed: Peng et al. is the only study in the packet with a machine-checkable definition of
correct, and it got one because somebody wrote 12 tests in advance — yet even there, the speed
effect was statistically significant while the 7-point success-rate advantage was not. Take a
show of hands on one question: "Is 'I can tell when the AI is wrong' a coding skill?" Record the
split on the board and photograph the board. Collect all index cards at the door as the entry
ticket to the next lecture, where the thin CORRECTNESS column becomes the working definition of
a specification.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Do not assert any of the following from the front of the room.

1. "METR proved AI makes developers slower." It did not. Sixteen developers, 246 tasks, mature
repositories they had worked in for about five years, early-2025 tooling. The authors explicitly
disclaim this exact reading, stating their result is not evidence that AI fails to speed up many
or most developers. State the effect for that population and setting, not in general.

2. "Copilot makes developers 55% faster." Over-strong in several ways at once: the 95% CI is
21–89%, the effect is computed *conditioning on completing the task*, participants were Upwork
freelancers recruited in May 2022 (Codex era, mostly aged 25–34, median income $10–19k), and 95
were randomized with meaningful attrition before analysis. Two of four authors worked at GitHub
and one at Microsoft Research. It is still real evidence — just about a narrow, greenfield,
fully specified task.

3. Never claim Peng et al. did not measure correctness. It did: a 12-check test suite, visible
but unalterable by participants. The correct point is subtler and stronger — the treated group's
success rate was only 7 percentage points higher and that difference was *not* statistically
significant. Speed moved; correctness did not detectably move.

4. Do not connect the two 19% figures. METR's 19% is a task-time slowdown for 16 OSS developers;
Brynjolfsson et al.'s 19% is a relative employment gap for 22–25 year olds across AI-exposed
occupations. Identical digits, unrelated quantities. This conflation circulates widely.

5. "AI took entry-level developer jobs." The Canaries authors describe their results as "early,
descriptive indicators — canaries in the coal mine — rather than causal estimates," and the
paper does not single out software developers. Their own follow-up concedes that under firm-time
fixed effects the decline is significant only after 2024, implying other forces drove earlier
declines. The interest-rate confound is partially rebutted, not eliminated.

6. "DORA shows AI hurts delivery." Stale and directionally wrong for 2025. The 2024 report found
a negative throughput relationship; the 2025 report explicitly reverses it while maintaining
that AI "does continue to have a negative relationship with software delivery stability." Get
both directions right or omit the source. Also note it is a self-selected survey of ~5,000
respondents — correlational, not experimental.

7. GitClear's duplication and churn figures are vendor research, not peer-reviewed. GitClear
sells code-analytics tooling, its moved-versus-copy/paste taxonomy is proprietary, and the
report claims correlation across a window in which many things besides AI changed. Present it as
a signal worth investigating, never as an established quality effect of AI.

8. "Studies show AI code is X% more insecure." Avoid any specific percentage. Perry et al. is a
small lab study on a 2022-era model with a narrow task set; the robust finding is the divergence
between confidence and security, not a magnitude.

9. "Vibe coding" does not mean "using AI to write code." Karpathy's original framing was
specifically about forgetting the code exists — not reading diffs, accepting all changes, for
throwaway projects. Using it as a synonym for all AI-assisted development smuggles in the
conclusion and makes the debate unwinnable for one side.

10. Stack Overflow's survey is self-selected and non-probability. Its trust and sentiment
numbers describe opt-in respondents, not the developer population, and the 2025 decline in
positive sentiment is not a measurement of tool quality.
