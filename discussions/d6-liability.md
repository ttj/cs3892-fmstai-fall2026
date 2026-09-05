# D6 — Who is liable when AI-assisted software fails?

**Session 12 · Tue Oct 6 · week 7 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Thu Oct 8, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What happened

In November 2022, after his grandmother died, Jake Moffatt asked the chatbot on Air Canada's website about bereavement fares. It told him he could book at full price and claim the discount retroactively within 90 days; the airline's real policy allowed no such thing. He paid about C$845, was refused, and sued in British Columbia's Civil Resolution Tribunal, a small-claims body.

In July 2025 Australia's Department of Employment and Workplace Relations published a roughly A$440,000 Deloitte report on the system that automatically penalises welfare recipients. A University of Sydney academic, Dr Christopher Rudge, found fabricated references in it.

That same month two US federal judges withdrew orders from their own dockets: Julien Neals (D.N.J.) in *In re CorMedix Inc. Securities Litigation*, Henry Wingate (S.D. Miss.) in *Jackson Federation of Teachers v. Fitch*. Senator Chuck Grassley demanded explanations.

### What was found

**Moffatt v. Air Canada (February 2024).** The claim was *negligent misrepresentation*: Moffatt had to show a duty of care, an inaccurate statement, carelessness, reliance, and loss. Air Canada argued the chatbot was "a separate legal entity responsible for its own actions." The tribunal rejected that: the chatbot was part of its website, and customers need not check one page against another. Award, $812.02. Less quoted: Air Canada's contract defence failed only because it never filed the terms, and the record never established whether the bot was a language model or a decision tree.

**Deloitte (October 2025).** Deloitte repaid the final instalment of its contract, not the fee. Its corrected report disclosed an "Azure OpenAI GPT - 4o" tool chain — a methodology note, not a finding that AI caused the errors. Deloitte stood by its conclusions; the department said "the substance of the independent review is retained, and there are no changes to the recommendations." Each fake reference, Rudge noted, was replaced by five to eight real ones.

**The judges (October 2025).** Neither judge used AI: a law clerk used Perplexity, an intern used ChatGPT "without authorization, without disclosure, and contrary to ... chambers policy." Both letters locate the cause in process, not the tool: an unfinished draft was docketed that never should have been ("a lapse in human oversight"; "human error"). The fixes were organisational — second independent review, printing every cited case, a written ban on AI drafting. No disciplinary outcome is reported either way.

**Scale.** Damien Charlotin's database of decisions finding reliance on hallucinated material held 1,922 entries on 16 August 2026: 16 from 2023, 59 from 2024, 845 from 2025, 1,002 from 2026 so far. Most involve self-represented litigants, not lawyers; inclusion means a court addressed the material, not that anyone was sanctioned.

### Why it still matters

*Product liability* makes a manufacturer pay for harm from a defective product without the victim proving anyone was careless — *strict* liability, unlike negligence. Software has sat awkwardly outside it: the EU's 1985 directive needed a 1988 Commission clarification to cover software. The 2024 revision, applying to products marketed from 9 December 2026, says "all types of software are covered ... including applications, operating systems and AI-systems," and that whoever substantially modifies a product "becomes a manufacturer." Its companion instrument, which would have eased proving that an AI caused harm, was withdrawn. So far the money has been small and the remedies procedural.

### Timeline

| When | What |
|---|---|
| Sep 2022 | The European Commission proposes two liability instruments at once: a revised Product Liability Directive, and a separate AI Liability Directive that would have created a rebuttable presumption of causality and court-ordered disclosure for high-risk AI systems. |
| Feb 2024 | British Columbia's Civil Resolution Tribunal decides Moffatt v. Air Canada, 2024 BCCRT 149 — awarding $812.02 and rejecting the airline's argument that its chatbot was "a separate legal entity responsible for its own actions." |
| 8 Dec 2024 | The revised EU Product Liability Directive enters into force, putting software and AI systems inside strict liability. Member states have until 9 Dec 2026 to transpose it, and it applies to products placed on the market from that date. |
| 30 Jun 2025 | Judge Neals's chambers dockets a draft opinion in In re CorMedix, withdrawn after defense counsel's 22 July letter; Judge Wingate's dockets a draft order on 20 July, removed and replaced on 23 July after an unopposed motion to correct. |
| 4 Jul 2025 | Australia's employment department publishes Deloitte's review of the automated welfare-penalty system. Dr Christopher Rudge later identifies fabricated references in it, including reports attributed to academics who never wrote them. |
| 6 Oct 2025 | The department confirms Deloitte will repay the final instalment of its contract; the corrected report adds an appendix disclosing an Azure OpenAI GPT-4o tool chain, while both parties maintain the findings and recommendations are unchanged. |
| 23 Oct 2025 | Senator Grassley publishes both judges' letters. Neither judge had used AI personally — a law clerk and a law-school intern had — and both chambers adopt new internal review policies. |
| 16 Aug 2026 | Charlotin's database records 1,922 decisions involving reliance on hallucinated material — 1,002 of them dated to 2026 alone, up from 16 in all of 2023. |

## The question

**Does a second reviewer prevent failures, or just assign blame?**

> In February 2024 a small-claims tribunal in British Columbia made Air Canada pay $812.02 because
> its website chatbot described a refund policy the airline did not have. In October 2025 two US
> federal judges told the Senate Judiciary Committee that staff in their chambers had used
> generative AI to draft orders that misquoted state law and attributed fake quotes to defendants,
> and both responded by rewriting their chambers' review procedures. In March 2026 Amazon told
> engineers that a run of outages — at least one tied to its own AI coding assistant — would be
> met with more documentation, more approvals and deliberate "controlled friction," while
> disputing the specific characterization that junior and mid-level engineers must now get senior
> sign-off for AI-assisted changes. Each of those is a different answer to the same question, and
> the EU has meanwhile written software and AI systems into strict product liability while
> withdrawing the separate directive that would have made it easier for a victim to prove an AI
> caused the harm.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

**1.** The revised EU Product Liability Directive says a person who substantially modifies a product
becomes its manufacturer. A three-person startup fine-tunes an open-weights model whose training
data it cannot inspect, wraps it in a retrieval layer, and sells it to a hospital, which writes
its own prompts and thresholds. A patient is harmed. Which of the three is the manufacturer of
that defect — and does your answer change if the startup can demonstrate the identical failure
in the unmodified base model?

**2.** Amazon's documented response to AI-linked outages was more documentation, more approvals, audits
by Tier-1 system owners, and deliberate 'controlled friction' — and the internal finding that an
existing two-person authorization rule had been 'either lacking or bypassed.' Suppose a firm did
adopt the stronger rule Amazon disputed, requiring senior sign-off on AI-assisted changes. Does
that reduce the defect rate, or does it mainly produce a named human who is accountable for a
change they could not realistically have re-derived? What measurement would let you tell those
two apart before the next outage?

**3.** Lawyers, physicians and structural engineers are held to a professional standard of care because
a licensed profession defines and polices one; Ayinde could invoke regulators, wasted costs and
contempt precisely because that scaffolding exists. Software has no equivalent. Is 'the care a
reasonable software engineer would take with an AI coding assistant' a coherent legal standard
today? If it is not, is the right move to build the profession, to skip negligence entirely and
go to strict product liability as the EU has, or to leave the loss where it falls on the user?

**4.** Deloitte's corrected report replaced fabricated citations with real ones, and both Deloitte and
the department maintained that the findings and recommendations were unchanged; one reviewer
noted that a single fake reference was often replaced by five to eight genuine ones. If the
conclusions survived, what was the client actually deprived of — and was refunding the final
instalment the right remedy, too generous, too small, or the wrong instrument for the wrong
injury?

**5.** Charlotin's database lists more pro se litigants than lawyers, and 28 judges. When a self-
represented person files a hallucinated citation, when a lawyer does, and when a judge's
chambers does, the same artifact enters the record — but the sanction ladders are wildly
different, and for judges the observable response has been correspondence and new internal
policies. Is that gradient tracking something real about culpability and capacity, or is it
tracking proximity to power over the record?

## Why this is in a formal-methods course

Every liability regime argued about here runs on a buried premise: that someone can state what
the system was supposed to do and then show whether it did it — a specification and a check —
and that the answer is attributable to a person or a firm. Formal methods is the part of this
field that makes both artifacts explicit and machine-auditable, which is exactly why the
boundary is the lesson: 'this citation names a case that exists' is a decidable, near-free check
that nobody ran and that Charlotin automated in a side project, while 'this fine-tuned model
will never misstate a fare rule' is not a property any current verification technique
discharges. Run the four scenarios through that partition — which failure a specification could
have caught, which a runtime monitor or a two-person authorization gate could have contained,
and which lies outside anything we know how to verify — because that partition is the rest of
the semester, and it is also, in practice, where courts will end up drawing the standard of
care.

## Readings

10 sources, 9 verified by direct fetch. One is assigned; the rest are there if you want to go further, or if you want to check a claim someone makes in the room.

- **Soh Kian Peng & Vanessa Ng, "Chatbots and Liability for Negligent Misrepresentation: Moffatt v Air Canada 2024 BCCRT 149" (case comment), [2025] SAL Prac 16, SAL Practitioner (Technology), Singapore Academy of Law, published 6 June 2025** (academic, 2025)  
  <https://journalsonline.academypublishing.org.sg/Journals/SAL-Practitioner/Technology/ctl/eFirstSALPDFJournalView/mid/595/ArticleId/2065/Citation/JournalsOnlinePDF>  
  This is the assigned reading (~10 pages, 25 minutes). It is the only source here that gives
  you pinpoint paragraph cites into the decision itself, which is hard to open directly (see
  the next entry), and it cuts both ways: it confirms Air Canada did argue "the chatbot was a
  separate legal entity responsible for its own actions" (rejected at [27]-[29]) and that the
  total award was $812.02 at [44], but it then attacks the popular reading, noting "the first
  premise, that the chatbot in question was powered by AI, cannot simply be assumed" — the
  record never established whether the bot was an LLM or a deterministic decision-tree. Its
  deterministic/non-deterministic split is the hinge of the whole discussion.

- **Moffatt v. Air Canada, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, 14 February 2024) — the decision itself** (legal, 2024) ⚠️ *not fetch-verified*  
  <https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html>  
  The primary document, listed so you can read the original rather than only commentary. Not
  fetch-verified: CanLII returned HTTP 403 to every automated retrieval attempt (WebFetch,
  curl, and a render proxy), and the BC CRT's own decisions server started returning 403
  mid-session as well; the URL is the one four independent search engines return for this
  citation, but the page behind it was never actually read, so it is flagged accordingly. A
  normal browser should open it; if yours does not, the SAL comment above carries pinpoint
  cites into it.

- **Ayinde v London Borough of Haringey; Al-Haroun v Qatar National Bank, [2025] EWHC 1383 (Admin), Divisional Court (Dame Victoria Sharp P. and Johnson J.), handed down 6 June 2025 — official text, The National Archives Find Case Law** (legal, 2025)  
  <https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383>  
  The best primary source on how penalties escalate, and the strongest evidence that a
  licensed profession with real enforcement machinery already has teeth: at [23] the court
  lists its full ladder — "public admonition of the lawyer, the imposition of a costs order,
  the imposition of a wasted costs order, striking out a case, referral to a regulator, the
  initiation of contempt proceedings, and referral to the police" — with the factors governing
  choice at [24]. It is long, so read only paragraphs 1-33, plus [70], where the court declines
  contempt against one barrister and warns that "this court's decision not to initiate
  contempt proceedings in respect of Ms Forey is not a precedent."

- **U.S. Senate Committee on the Judiciary, "Grassley Releases Judges' Responses Owning Up to AI Use, Calls for Continued Oversight and Regulation" (press release), 23 October 2025** (primary, 2025)  
  <https://www.judiciary.senate.gov/press/rep/releases/grassley-releases-judges-responses-owning-up-to-ai-use-calls-for-continued-oversight-and-regulation>  
  The primary congressional document behind the judges story: the orders "misquoted state law,
  referenced individuals who didn't appear in the case and attributed fake quotes to
  defendants," and the remedies adopted were purely organizational — Wingate requiring "all
  draft opinions, orders and memos to undergo a second independent review" with "all cited
  cases to be printed and attached to the final draft," Neals adopting "a written policy that
  prohibits all law clerks and interns from using AI when drafting opinions or orders." Short.
  Read it next to Ayinde and the lawyer/judge accountability asymmetry is hard to miss.

- **Damien Charlotin, "AI Hallucination Cases" database (retrieved 16 August 2026; site states "Last updated: 16 August 2026")** (tool, 2026)  
  <https://www.damiencharlotin.com/hallucinations/>  
  The tracker everyone cites, and the numbers in it will probably break whatever story you
  walked in with — it is easy to assume this is mainly lawyers behaving badly. As retrieved:
  1,922 cases; USA 1,313, Canada 211, Australia 98, UK 62; and by party, Pro Se Litigant 1,111
  versus Lawyer 761 and Judge 28. It also carries its own scope limits — it covers decisions
  where a court "has explicitly found (or implied) that a party relied on hallucinated
  content," not all fake citations — and the warning that naming a tool "does not necessarily
  mean that tool was responsible." Browse for 10 minutes; do not read exhaustively. The author
  also built an automated reference checker (PelAIkan), which is itself an argument about what
  kind of problem this is.

- **Krishani Dhanji, "Deloitte to pay money back to Albanese government after using AI in $440,000 report," The Guardian (Australia), 6 October 2025** (news, 2025)  
  <https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report>  
  If you read only one thing on the Deloitte story, make it this. It carries the three facts
  the secondary coverage mangles: the refund was "the final instalment under its contract,"
  not the A$439,000 fee; the corrected report disclosed only that part of the work "included
  the use of a generative artificial intelligence (AI) large language model (Azure OpenAI
  GPT - 4o) based tool chain licensed by DEWR," without saying AI caused the errors; and
  DEWR's position that "the substance of the independent review is retained, and there are no
  changes to the recommendations." It also has the sharpest single detail in this whole list —
  Dr Christopher Rudge noting each fake reference was replaced by "five, six or seven or
  eight" real ones, implying the underlying claim rested on no single source. Under 10
  minutes.

- **Eugene Kim, "Amazon orders 90-day reset after code mishaps cause millions of lost orders," Business Insider, 10 March 2026 (URL slug: "amazon-tightens-code-controls-after-outages-including-one-ai-2026-3")** (news, 2026)  
  <https://www.businessinsider.com/amazon-tightens-code-controls-after-outages-including-one-ai-2026-3>  
  This one argues the other way, and it is also the source here most easily misquoted. Based
  on internal documents: SVP Dave Treadwell's "trend of incidents" since Q3 2025, at least one
  "tied to Amazon's AI coding assistant Q," "high blast radius changes," and — decisively —
  that some failures traced back to "a requirement to have two people authorize code changes,
  that were either lacking or bypassed." That points at process rather than at the tool. It
  then records that "the Amazon spokesperson told Business Insider that it is not accurate to
  say junior and mid-level engineers are required to get sign off from senior engineers for
  any AI-assisted changes," contradicting the FT-derived version circulating in TechRadar and
  elsewhere — so do not repeat the senior-sign-off claim as fact. Paywalled for some readers;
  the two-person authorization finding and the spokesperson's denial are the load-bearing
  passages.

- **European Commission, "Liability for defective products" — official page on Directive (EU) 2024/2853 (revised Product Liability Directive), DG Internal Market (retrieved 16 August 2026)** (primary, 2024)  
  <https://single-market-economy.ec.europa.eu/single-market/goods/free-movement-sectors/liability-defective-products_en>  
  The clearest statement that software is now inside strict liability, and the source of the
  "who is the manufacturer" machinery. Confirms "all types of software are covered by the new
  directive, including applications, operating systems and AI-systems," including defects that
  appear later "as a result of updates,
  upgrades or a machine-learning feature"; that "a product that has been substantially
  modified ... is considered to be a new product. The person that has made the modification
  becomes a manufacturer"; the chain of liable operators (manufacturer, importer or authorised
  representative, fulfilment service provider, distributor); "destruction or corruption of
  data" as compensable; entry into force 8 December 2024 and transposition by 9 December 2026,
  with the 1985 directive still governing earlier products. Watch out: this is the Commission's
  own summary page, not the legislative text — EUR-Lex blocked automated retrieval, so the
  Article numbers were never read directly. Do not cite Article numbers off this page.

- **European Parliament, Legislative Train Schedule, "AI liability directive" (file record; proposal COM(2022) 496, 28 September 2022; status: withdrawn) (retrieved 16 August 2026)** (primary, 2022)  
  <https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-ai-liability-directive>  
  The counter-fact to the story that the law is steadily closing in on AI. The instrument that
  would have eased a claimant's burden against AI — a rebuttable presumption of causality plus
  court-ordered disclosure of evidence about high-risk AI systems — is recorded as withdrawn,
  following the withdrawal announced in the Commission Work Programme 2025. The institution
  most associated with expanding AI liability chose not to. No Official Journal citation or
  precise withdrawal date is given here on purpose: two retrievals disagreed on the date and
  neither was a raw read of the OJ, so no date is asserted. Two minutes to read.

- **Bryan H. Choi, "Crashworthy Code," 94 Washington Law Review 39 (2019)** (academic, 2019)  
  <https://digitalcommons.law.uw.edu/wlr/vol94/iss1/3/>  
  The strongest doctrinal argument on the other side, from a law professor rather than an
  industry apologist. Choi argues "no consensus is imminent as long as liability is pegged to
  a standard of 'crashproof' code," that "imposing damages based on failure to prevent code
  crashes will not improve software quality, but will impede the rollout of cyber-physical
  systems," and proposes metering liability on mitigation rather than prevention: "requiring
  all code to be perfect is impossible, but expecting code to be crashworthy is reasonable."
  It is a full law review article — read the abstract and introduction only; the abstract
  alone states the argument.

## What you submit

One paragraph, 150–250 words, by **Thu Oct 8, 11:59 p.m.**, to the `D6` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
