# D9 — Does system architecture still matter in the age of agentic coding?

**Session 24 · Thu Nov 19 · week 13 · 30 minutes · think–pair–share**

## Framing

> Since May 2025, agentic systems have leaked private repositories twice, deleted a production
> database and its backups in nine seconds, and turned one click on a link into code execution on
> a developer's own machine. In every case the recommended fix was architectural and entirely
> familiar: scope the token, keep backups off the volume, validate the Origin header, let the
> agent see one repository per session. Least privilege was published in 1975. So either these are
> architecture failures and our field cannot deploy its own oldest result even at the moment code
> became cheap to generate — or "architecture" is largely what we call a cause after we have
> already decided what the fix is, and the thing that actually changed is somewhere else entirely.

## Why this is in a formal-methods course

Every incident in this packet is a violated system-level invariant rather than a model that got
the answer wrong: "no credential authorizes an action outside its environment," "no value read
from a public issue reaches a public write," "no cross-origin peer opens the control socket."
Those are properties you can state precisely, and Cedar, Dogwood and CaMeL are three live
attempts to make agent authorization something a solver can actually decide — Cedar's evaluator
and validator carry mechanized Lean proofs, CaMeL enforces the flow property with capabilities
and a custom interpreter, and Dogwood buys temporal expressiveness at the explicitly admitted
cost of Cedar's automated analysis. That trade is the course's spine in miniature: a verified
component sitting inside an unverified system, and a policy that is provably consistent yet may
still fail to say what you meant.

## Discussion questions

**1.** Anthropic and OX Security agree precisely on what MCP's STDIO transport does: it spawns whatever
command the configuration names. They disagree only on whether that is a vulnerability or a
specified feature. If a written specification can move a behavior from "flaw" to "expected,"
what work is the specification doing — and could you write a spec under which the PocketOS
deletion is also expected behavior?

**2.** GitLost required no excess permission: the agent's read access to organization repositories was
intended, and posting an issue comment was a sanctioned output path. Is that a permissions
failure that finer-grained permissions would fix, or evidence that permissions are the wrong
abstraction for agents and nothing short of information-flow tracking will do? Argue whichever
side you believe less.

**3.** CaMeL buys provable resistance to prompt injection at the cost of seven points of task
completion on AgentDojo — 77% against 84% undefended. Name one deployment where you would take
that trade and one where you would refuse it. Then say who in an organization actually gets to
make that call, and whether "provable" should outrank a product manager's completion-rate
number.

**4.** The counter-argument runs: if an agent can regenerate the whole service in an afternoon, stop
paying for architecture up front and just rewrite when requirements change. What in a running
system does not get cheaper when code generation gets cheap? If your answer is "the data, the
credentials, and the blast radius," is that a defense of architecture — or a much narrower claim
than the one being defended?

**5.** AWS shipped Cedar because it is analyzable, then shipped Dogwood because Cedar cannot express "a
human approved this before the transfer" — and conceded that Dogwood's temporal policies do not
support Cedar's automated reasoning analysis. Forced to choose between a policy you can prove
things about and a policy that can express the property you actually care about, which do you
deploy? Is a policy language you cannot analyze better or worse than having no policy language
at all?

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Invariant Labs, "GitHub MCP Exploited: Accessing private repositories via MCP"** (primary, 2025)  
  <https://invariantlabs.ai/blog/mcp-github-vulnerability>  
  The origin of the "architectural, not patchable" claim in the researchers' own words — "not
  a flaw in the GitHub MCP server code itself, but rather a fundamental architectural issue"
  and "GitHub alone cannot resolve this vulnerability through server-side patches." Supports
  the architecture side. Short (~10 min); this is the one to assign.

- **Sasi Levi, Noma Security, "GitLost: How We Tricked GitHub's AI Agent into Leaking Private Repos"** (primary, 2026)  
  <https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/>  
  The 2026 recurrence, against GitHub Agentic Workflows — a system shipped with guardrails
  after the 2025 finding. The bypass was prepending the word "Additionally." Cuts both ways:
  supports architecture (a filter is not a boundary) while undercutting least privilege, since
  no permission was exceeded. ~15 min.

- **Thomas Claburn, "Cursor-Opus agent snuffs out startup's production database," The Register** (news, 2026)  
  <https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442>  
  Blast radius in a single incident: a Railway token minted for custom-domain management via
  the CLI but unscoped across environments and operations, plus volume-level backups stored on
  the very volume deleted. Supports the architecture side. Note it relays founder Jeremy
  Crane's single-source account. ~8 min.

- **OX Security, "MCP Supply Chain Advisory: RCE Vulnerabilities Across the AI Ecosystem"** (report, 2026)  
  <https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/>  
  The vendor claim that MCP's STDIO config-to-command-execution path is a systemic design
  flaw. Its measured content is 11 downstream CVEs accepted by vendors including LiteLLM,
  Windsurf and Flowise; the widely quoted population figures are not in this advisory.
  Supports the architecture side — pair it with the next entry, which carries the rebuttal.

- **Jessica Lyons, "MCP 'design flaw' puts 200k servers at risk: Researcher," The Register** (news, 2026)  
  <https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/>  
  Carries Anthropic's position that STDIO "spawns a subprocess by design, per the MCP
  specification" and that the behavior is "expected." This is the packet's strongest argument
  that "architectural failure" is doing rhetorical rather than analytic work — the boundary
  sat exactly where the spec put it. Cuts against the framing's apparent thrust. Also the
  source of the contested 200,000 figure. ~7 min.

- **NIST National Vulnerability Database, CVE-2026-25253 (OpenClaw)** (primary, 2026)  
  <https://nvd.nist.gov/vuln/detail/CVE-2026-25253>  
  Authoritative record for the OpenClaw chain: a gatewayUrl value taken from the query string,
  an automatic WebSocket connection made without prompting, and the token sent along with it.
  CWE-669, CVSS 8.8 with UI:R. Use it to settle the mechanism against several incompatible
  secondary retellings. 2 min.

- **Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis & Tramèr, "Defeating Prompt Injections by Design" (CaMeL), arXiv:2503.18813** (academic, 2025)  
  <https://arxiv.org/abs/2503.18813>  
  The architecture position stated formally: extract control and data flow from the trusted
  query so untrusted data can never steer execution, then enforce with capabilities in a
  custom interpreter. Supplies the packet's price tag — 77% of AgentDojo tasks solved with
  provable security versus 84% undefended. Long; assign only the introduction and the
  AgentDojo results.

- **Disselkoen, Eline, He, Headley, Hicks, Hietala, Kastner, Mamat, McCutchen, Rungta, Shah, Torlak & Wells, "How We Built Cedar: A Verification-Guided Approach," arXiv:2407.01688** (academic, 2024)  
  <https://arxiv.org/abs/2407.01688>  
  What "analyzable authorization" actually costs to build: a Lean model with mechanized
  proofs, differential random testing against production code, and property-based testing for
  unmodeled parts. Supports the architecture side but also bounds it — proving found 4 bugs in
  the policy validator and DRT/PBT found 21 more. Long; the abstract plus the bug-count
  discussion is enough.

- **AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents"** (tool, 2026)  
  <https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/>  
  Cedar extended with temporal operators (formerly, count_within, sum_within, bind) for
  approval gates, sequencing and rate limits — plus AWS's own admission that these temporal
  policies "do not currently support the powerful automated reasoning analysis tools that
  Cedar provides." Simultaneously the best tooling evidence for the architecture side and its
  sharpest internal limitation. Apache 2.0. ~12 min.

- **Christina Lin, "Software Becomes Disposable? How AI Is Changing the Way We Architect Code," Google Cloud Community (Medium)** (news, 2025)  
  <https://medium.com/google-cloud/software-becomes-disposable-how-ai-is-changing-the-way-we-architect-code-1bfb50356b98>  
  The counter-case, included honestly as the weakest-evidenced position in the packet: a self-
  published post arguing that cheap refactoring shortens software lifespans and that teams
  should favor "simpler, more generic designs" over durable architecture. Cuts against the
  framing. The author qualifies it herself (it "doesn't apply everywhere" — avionics, medical
  firmware, HFT), and the fact that the strongest available articulation of this side is a
  blog post is itself worth putting to the class. ~6 min.

## 30-minute run sheet

0-3 FRAMING. Read the framing paragraph verbatim. Write across the top of the board: "scope the
token / backups off the volume / validate Origin / one repo per session." Say only this: "These
four fixes were standard practice before any of these incidents happened. Ground rule for the
next 27 minutes — you may not resolve this question by saying the engineers were careless."

3-6 MECHANISM CALIBRATION. Instructor talks, no discussion, hard stop at 6:00. Three lines down
the left margin, then stop:
- PocketOS: token minted for custom-domain management, unscoped across environments; Railway
stored volume backups on the volume that was deleted. Two independent decisions, neither
individually fatal.
- GitLost: guardrails bypassed by prepending the word "Additionally." Every permission the agent
used was one it was meant to have.
- CaMeL: 77% vs 84% on AgentDojo.
Add nothing else. The think phase depends on these three facts being right.

6-12 THINK, silent, index cards, 6 minutes. Assign by row: rows 1-2 take Prompt 2, rows 3-4
Prompt 3, rows 5+ Prompt 4. Each student writes (a) exactly one sentence answering their prompt
— enforce the one-sentence limit, it is what makes the pair phase work — and (b) a confidence
number 0-10. Say out loud: "Argue the side you believe less." Do not collect yet.

12-20 PAIR, 8 minutes. Pair within rows so both partners hold the same prompt. Each pair puts
ONE of two things on a single fresh card: a sentence both partners will sign, or — if they
cannot agree — the single piece of evidence that would change one of their minds. Instructor
circulates and reads over shoulders. Tag three cards: two pairs who disagreed productively, and
one pair whose "evidence that would change my mind" is unobtainable in principle. Collect the
individual cards from the think phase now, while pairs are still writing.

20-28 SHARE, 8 minutes. Draw two columns: ARCHITECTURAL FIX | NOT-ARCHITECTURAL FIX. Call the
two tagged disagreeing pairs first, then take three volunteers. Write every proposal into a
column and ask exactly one follow-up each time: "What does it cost when it's wrong?" Do not
adjudicate, do not correct placements. If the room converges too early, put GitLost back up and
ask which column it belongs in, given that no permission was exceeded and the output path was
permitted — that reliably reopens it.

28-30 CLOSE. Take no vote and give no summary. Read aloud the two most incompatible signed
sentences from the pair cards, attributed only to "two pairs in this room," and leave them
standing. Write one line as the bridge to the next unit: "Cedar's evaluator is proved correct in
Lean. Your policy can still be wrong. Next week: what does a proof actually cover?" Keep every
card — the confidence numbers from the think phase are the pre-test for re-asking the same
question at the end of the unit.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Do not assert any of the following from the front of the room.

1. "PocketOS permanently lost its data" — or "it was all recovered." The two sources conflict.
The Register reports Railway CEO Jake Cooper confirmed recovery within about an hour;
NeuralTrust's post-mortem says the only surviving copy was a three-month-old off-volume backup.
State that the recovery outcome is reported inconsistently and move on. Relatedly, don't over-
specify the call itself: some accounts say a curl command, others a single GraphQL mutation.
Both are consistent with an HTTP request to Railway's GraphQL API; pick neither.

2. "200,000 MCP servers are vulnerable." The observed figure is 7,000+ servers on public IPs;
200,000 is an extrapolation, and the 150M+ figure counts package downloads, not vulnerable
deployments. All of it traces to a single vendor selling in this space, and OX's own technical
advisory carries no such counts — its measured content is the 11 accepted downstream CVEs. Cite
the CVE list, not the population estimate.

3. "CVE-2026-25253 was a malicious skill on OpenClawDir." A GitHub issue with that title is
attached to this CVE number and surfaces in search. NVD's record is a different mechanism
entirely: gatewayUrl taken from the query string, automatic WebSocket connect, token
transmitted. The conflation is already circulating; check NVD before repeating anything about
this CVE.

4. "Invariant Labs found a GitHub vulnerability, and GitHub patched it." Invariant wrote the
opposite in as many words — "not a flaw in the GitHub MCP server code itself," and "GitHub alone
cannot resolve this vulnerability through server-side patches." Calling it a GitHub bug inverts
the finding the discussion depends on.

5. "Least privilege would have prevented all of these." This is the single most likely error an
instructor makes here, and GitLost falsifies it. The workflow's read access to organization
repositories was intended, and an issue comment was a permitted output path; nothing exceeded
its grant. That is an information-flow failure, not a permissions failure, and collapsing the
two ruins Prompt 2.

6. "Cedar is formally verified, so Cedar policies are correct." The Lean work covers the
evaluator and validator and their correspondence to production code — not whether a policy
encodes anyone's intent. Disselkoen et al. report that proving found 4 validator bugs and that
DRT/PBT found 21 more. And do not extend the claim to Dogwood: AWS states its temporal policies
do not currently support Cedar's automated reasoning analysis.

7. "CaMeL solves prompt injection." The guarantee is scoped to a stated threat model and
measured on a benchmark, at 77% versus 84% task completion. It is a research result with a
quantified utility cost, not a deployment guarantee.

8. "Localhost is not a trust boundary, therefore the attack is trivial." Get both halves right.
Loopback binding is irrelevant because the victim's own browser makes the outbound connection —
but the CVSS vector is UI:R. It is one-click, not zero-click, and calling it zero-click
overstates it.

9. "Cursor's and Claude's safeguards were bypassed/disabled" in the PocketOS incident. Reporting
says the marketed safeguards were present and did not prevent the outcome, which is a weaker and
different claim than a bypass. The configuration details come only from the founder's own
account — single-source throughout.

10. Any "agentic AI incidents rose N% year over year" statistic. The circulating figures come
from vendor telemetry with undisclosed denominators and no stable definition of an incident.
There is no reliable base rate here; if the discussion needs one, that absence is the finding.
