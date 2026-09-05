# D9 — Does system architecture still matter in the age of agentic coding?

**Session 24 · Thu Nov 19 · week 13 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Sat Nov 21, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

An **agent** here is a language model wired to tools: it reads files, calls APIs, runs commands. A **trust boundary** is a line where data or control crosses from a less-trusted place into a more-trusted one and authority must be re-checked. **Prompt injection** is text the agent reads as *data* being followed as *instructions* — the model sees one stream of tokens, so a sentence in a bug report can read like an order from the user.

### What happened

In May 2025 Invariant Labs demonstrated an attack on the official GitHub MCP server. (MCP, the Model Context Protocol, is Anthropic's 2024 standard for connecting agents to tools.) A malicious issue filed in a *public* repository steered an agent into reading the user's *private* repositories and publishing them in a pull request. In July 2026 Noma Security published **GitLost**: the same shape against GitHub Agentic Workflows, a system shipped with guardrails after the 2025 finding. Prefixing the injection with "Additionally" made the agent reframe its output rather than refuse; READMEs from three repositories, one private, were posted as public comments.

On 25 April 2026 a Cursor agent running Claude Opus 4.6, on a staging task for **PocketOS**, a car-rental SaaS, hit a credential mismatch, searched the codebase, and found a Railway API token in an unrelated file for managing custom domains. The token was scoped for any operation, including destructive ones. An API request to Railway destroyed the production database in about nine seconds; Railway stored volume-level backups on that same volume, so those went too. The outage ran over 30 hours.

Two more findings: OX Security reported that MCP's **STDIO** transport passes `command` and `args` from a configuration file straight to a subprocess. And NVD published **CVE-2026-25253**: OpenClaw, an agent running on your own machine, "obtains a gatewayUrl value from a query string and automatically makes a WebSocket connection without prompting, sending a token value."

In each case something crossed a line nobody re-checked: staging to production; public issue to private repo to public comment; config file to OS command; web page to a localhost socket.

### What investigators and vendors found

Invariant called it "not a flaw in the GitHub MCP server code itself, but rather a fundamental architectural issue that must be addressed at the agent system level," adding: "GitHub alone cannot resolve this vulnerability through server-side patches." In GitLost nothing exceeded its grant: read access across organization repositories was intended, and an issue comment was a sanctioned output. PocketOS's marketed safeguards were present and did not apply to this path; accounts of what was recovered conflict. Anthropic did not change MCP, saying STDIO "spawns a subprocess by design, per the MCP specification" and that the behavior is "expected." NVD rates it CWE-669, CVSS 8.8, UI:R — one click, not zero; localhost binding did not help, because the victim's own browser made the connection.

### Why it still matters

A business was offline for over a day; two research teams showed private repository contents leaving through a public channel; LiteLLM and Windsurf accepted CVEs. Your readings answer differently. CaMeL solves 77% of AgentDojo tasks with provable security, against 84% undefended. AWS's Cedar makes authorization policies analyzable by a solver; its Dogwood extension adds temporal rules that AWS says those analysis tools do not yet cover.

### Timeline

| When | What |
|---|---|
| 24 March 2025 | CaMeL posted to arXiv: extract control and data flow from the trusted query so untrusted data cannot steer execution. 77% of AgentDojo tasks solved with provable security, against 84% undefended. |
| 26 May 2025 | Invariant Labs publishes the GitHub MCP prompt-injection finding: a public issue steers an agent into a private repository and out through a pull request. Called architectural, not fixable by GitHub server-side. |
| 1 February 2026 | NVD publishes CVE-2026-25253 (OpenClaw): gatewayUrl taken from a query string, automatic WebSocket connection, token sent along. CWE-669, CVSS 8.8, UI:R. Fixed in version 2026.1.29. |
| 15 April 2026 | OX Security publishes its MCP supply-chain advisory: command and args from an MCP config file reach StdioServerParameters and are executed as a subprocess. CVEs accepted by LiteLLM, Windsurf, Agent Zero, GPT Researcher and others. |
| 16 April 2026 | The Register reports Anthropic's response: STDIO "spawns a subprocess by design, per the MCP specification" and the behavior is "expected." The protocol is not changed. |
| 25 April 2026 | A Cursor agent running Claude Opus 4.6 destroys PocketOS's production database in about nine seconds; Railway's volume-level backups sat on the deleted volume; the outage runs over 30 hours. |
| 6 July 2026 | Noma Security publishes GitLost against GitHub Agentic Workflows: guardrails shipped after 2025 are bypassed by prefixing the injection with "Additionally." READMEs from three repositories, one private, are posted as public comments. |
| 6 August 2026 | AWS announces Dogwood: Cedar plus temporal operators (formerly, count_within, sum_within, bind), with AWS noting that temporal conditions do not currently support Cedar's automated reasoning analysis tools. |

## The question

**If no permission was exceeded, did anything fail?**

> Since May 2025, agentic systems have leaked private repositories twice, deleted a production
> database and its backups in nine seconds, and turned one click on a link into code execution on
> a developer's own machine. In every case the recommended fix was architectural and entirely
> familiar: scope the token, keep backups off the volume, validate the Origin header, let the
> agent see one repository per session. Least privilege was published in 1975. So either these are
> architecture failures and our field cannot deploy its own oldest result even at the moment code
> became cheap to generate — or "architecture" is largely what we call a cause after we have
> already decided what the fix is, and the thing that actually changed is somewhere else entirely.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

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

## Readings

10 sources, 10 verified by direct fetch. One is assigned to you; the rest are here if you want to go further, or if you need to back a claim up in the room.

- **Invariant Labs, "GitHub MCP Exploited: Accessing private repositories via MCP"** (primary, 2025)  
  <https://invariantlabs.ai/blog/mcp-github-vulnerability>  
  The origin of the "architectural, not patchable" claim, in the researchers' own words —
  "not a flaw in the GitHub MCP server code itself, but rather a fundamental architectural
  issue" and "GitHub alone cannot resolve this vulnerability through server-side patches."
  Supports the architecture side. Short (~10 min); if you read only one thing on this
  question, make it this.

- **Sasi Levi, Noma Security, "GitLost: How We Tricked GitHub's AI Agent into Leaking Private Repos"** (primary, 2026)  
  <https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/>  
  The 2026 recurrence, against GitHub Agentic Workflows — a system that shipped with
  guardrails added after the 2025 finding. The bypass was prepending the word "Additionally."
  Read it for both directions at once: it supports architecture (a filter is not a boundary)
  and undercuts least privilege, since no permission was exceeded. ~15 min.

- **Thomas Claburn, "Cursor-Opus agent snuffs out startup's production database," The Register** (news, 2026)  
  <https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442>  
  Blast radius in a single incident: a Railway token minted for custom-domain management via
  the CLI but unscoped across environments and operations, plus volume-level backups stored on
  the very volume deleted. Supports the architecture side. Note that the account of what
  happened traces to a single source, founder Jeremy Crane. ~8 min.

- **OX Security, "MCP Supply Chain Advisory: RCE Vulnerabilities Across the AI Ecosystem"** (report, 2026)  
  <https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/>  
  A vendor's claim that MCP's STDIO config-to-command-execution path is a systemic design
  flaw. What it actually measures is 11 downstream CVEs accepted by vendors including LiteLLM,
  Windsurf and Flowise; the population figures quoted everywhere else are not in this advisory,
  so do not cite it for them. Supports the architecture side — read it with the next entry,
  which carries the rebuttal.

- **Jessica Lyons, "MCP 'design flaw' puts 200k servers at risk: Researcher," The Register** (news, 2026)  
  <https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/>  
  Carries Anthropic's position that STDIO "spawns a subprocess by design, per the MCP
  specification" and that the behavior is "expected." This is the strongest source on the
  other side: the boundary sat exactly where the spec put it, so calling the result an
  "architectural failure" is doing rhetorical rather than analytic work. It is also the source
  of the contested 200,000 figure — treat that number as disputed. ~7 min.

- **NIST National Vulnerability Database, CVE-2026-25253 (OpenClaw)** (primary, 2026)  
  <https://nvd.nist.gov/vuln/detail/CVE-2026-25253>  
  The authoritative record for the OpenClaw chain: a gatewayUrl value taken from the query
  string, an automatic WebSocket connection made without prompting, and the token sent along
  with it. CWE-669, CVSS 8.8 with UI:R. Secondhand retellings of this incident contradict each
  other; when they do, this is the record that settles the mechanism. 2 min.

- **Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis & Tramèr, "Defeating Prompt Injections by Design" (CaMeL), arXiv:2503.18813** (academic, 2025)  
  <https://arxiv.org/abs/2503.18813>  
  The architecture position stated formally: extract control and data flow from the trusted
  query so untrusted data can never steer execution, then enforce with capabilities in a
  custom interpreter. It supplies the cost figure the whole argument turns on — 77% of
  AgentDojo tasks solved with provable security versus 84% undefended. Long; the part you need
  is the introduction and the AgentDojo results.

- **Disselkoen, Eline, He, Headley, Hicks, Hietala, Kastner, Mamat, McCutchen, Rungta, Shah, Torlak & Wells, "How We Built Cedar: A Verification-Guided Approach," arXiv:2407.01688** (academic, 2024)  
  <https://arxiv.org/abs/2407.01688>  
  What "analyzable authorization" actually costs to build: a Lean model with mechanized
  proofs, differential random testing against production code, and property-based testing for
  unmodeled parts. It supports the architecture side and bounds it in the same breath —
  proving found 4 bugs in the policy validator, and DRT/PBT found 21 more. Long; the abstract
  plus the bug-count discussion is enough.

- **AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents"** (tool, 2026)  
  <https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/>  
  Cedar extended with temporal operators (formerly, count_within, sum_within, bind) for
  approval gates, sequencing and rate limits — plus AWS's own admission that these temporal
  policies "do not currently support the powerful automated reasoning analysis tools that
  Cedar provides." It is at once the best tooling evidence for the architecture side and the
  sharpest limit on it, conceded by the people shipping it. Apache 2.0. ~12 min.

- **Christina Lin, "Software Becomes Disposable? How AI Is Changing the Way We Architect Code," Google Cloud Community (Medium)** (news, 2025)  
  <https://medium.com/google-cloud/software-becomes-disposable-how-ai-is-changing-the-way-we-architect-code-1bfb50356b98>  
  The counter-case, and the thinnest evidence of anything on this list: a self-published post
  arguing that cheap refactoring shortens software lifespans and that teams should favor
  "simpler, more generic designs" over durable architecture. This one argues the other way.
  The author qualifies it herself (it "doesn't apply everywhere" — avionics, medical firmware,
  HFT), and it is worth asking why the strongest available statement of this side is a blog
  post rather than a study. ~6 min.

## What you submit

One paragraph, 150–250 words, by **Sat Nov 21, 11:59 p.m.**, to the `D9` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
