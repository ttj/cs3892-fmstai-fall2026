# D6 — Who is liable when AI-assisted software fails?

**Session 12 · Tue Oct 6 · week 7 · 30 minutes · think–pair–share**

## Framing

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

## Discussion questions

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

## Readings

10 sources, 9 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Soh Kian Peng & Vanessa Ng, "Chatbots and Liability for Negligent Misrepresentation: Moffatt v Air Canada 2024 BCCRT 149" (case comment), [2025] SAL Prac 16, SAL Practitioner (Technology), Singapore Academy of Law, published 6 June 2025** (academic, 2025)  
  <https://journalsonline.academypublishing.org.sg/Journals/SAL-Practitioner/Technology/ctl/eFirstSALPDFJournalView/mid/595/ArticleId/2065/Citation/JournalsOnlinePDF>  
  THE ASSIGNED READING (~10 pages, readable in 25 minutes). It is the only source here that
  supplies pinpoint paragraph cites into a decision this machine could not retrieve, and it
  cuts both ways: it confirms Air Canada did argue "the chatbot was a separate legal entity
  responsible for its own actions" (rejected at [27]-[29]) and that the total award was
  $812.02 at [44], but it then attacks the popular reading, noting "the first premise, that
  the chatbot in question was powered by AI, cannot simply be assumed" — the record never
  established whether the bot was an LLM or a deterministic decision-tree. Its
  deterministic/non-deterministic split is the hinge of the whole discussion.

- **Moffatt v. Air Canada, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, 14 February 2024) — the decision itself** (legal, 2024) ⚠️ *not fetch-verified*  
  <https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html>  
  The primary document, listed so students can see the original rather than only commentary.
  NOT VERIFIED: CanLII returned HTTP 403 to every retrieval attempt from this machine
  (WebFetch, curl, and a render proxy), and the BC CRT's own decisions server began returning
  403 mid-session; the URL is the one four independent search engines return for this
  citation, but I did not read the page, so it is flagged accordingly. Read the SAL comment
  above for pinpoint cites into it. Instructors on a normal browser should be able to open it.

- **Ayinde v London Borough of Haringey; Al-Haroun v Qatar National Bank, [2025] EWHC 1383 (Admin), Divisional Court (Dame Victoria Sharp P. and Johnson J.), handed down 6 June 2025 — official text, The National Archives Find Case Law** (legal, 2025)  
  <https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383>  
  The best primary source for the escalation-of-penalties strand, and it supports the
  framing's thrust: at [23] the court lists its full ladder — "public admonition of the
  lawyer, the imposition of a costs order, the imposition of a wasted costs order, striking
  out a case, referral to a regulator, the initiation of contempt proceedings, and referral to
  the police" — with the factors governing choice at [24]. LONG: assign only paragraphs 1-33,
  plus [70] where the court declines contempt against one barrister and warns that "this
  court's decision not to initiate contempt proceedings in respect of Ms Forey is not a
  precedent."

- **U.S. Senate Committee on the Judiciary, "Grassley Releases Judges' Responses Owning Up to AI Use, Calls for Continued Oversight and Regulation" (press release), 23 October 2025** (primary, 2025)  
  <https://www.judiciary.senate.gov/press/rep/releases/grassley-releases-judges-responses-owning-up-to-ai-use-calls-for-continued-oversight-and-regulation>  
  Primary congressional document for the judges strand: the orders "misquoted state law,
  referenced individuals who didn't appear in the case and attributed fake quotes to
  defendants," and the remedies adopted were purely organizational — Wingate requiring "all
  draft opinions, orders and memos to undergo a second independent review" with "all cited
  cases to be printed and attached to the final draft," Neals adopting "a written policy that
  prohibits all law clerks and interns from using AI when drafting opinions or orders." Short.
  Pair it against Ayinde to expose the lawyer/judge accountability asymmetry.

- **Damien Charlotin, "AI Hallucination Cases" database (retrieved 16 August 2026; site states "Last updated: 16 August 2026")** (tool, 2026)  
  <https://www.damiencharlotin.com/hallucinations/>  
  The tracker everyone cites, and the source that most reliably breaks the story students
  expect. As retrieved: 1,922 cases; USA 1,313, Canada 211, Australia 98, UK 62; and by party,
  Pro Se Litigant 1,111 versus Lawyer 761 and Judge 28. It also carries its own scope limits —
  it covers decisions where a court "has explicitly found (or implied) that a party relied on
  hallucinated content," not all fake citations — and the warning that naming a tool "does not
  necessarily mean that tool was responsible." Browse for 10 minutes; do not read
  exhaustively. Note the author also built an automated reference checker (PelAIkan), which is
  itself an argument about what kind of problem this is.

- **Krishani Dhanji, "Deloitte to pay money back to Albanese government after using AI in $440,000 report," The Guardian (Australia), 6 October 2025** (news, 2025)  
  <https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report>  
  Verified via curl (WebFetch is blocked for this host). Carries the three facts the secondary
  coverage mangles: the refund was "the final instalment under its contract," not the
  A$439,000 fee; the corrected report disclosed only that part of the work "included the use
  of a generative artificial intelligence (AI) large language model (Azure OpenAI GPT - 4o)
  based tool chain licensed by DEWR," without saying AI caused the errors; and DEWR's position
  that "the substance of the independent review is retained, and there are no changes to the
  recommendations." Also the sharpest detail in the whole packet — Dr Christopher Rudge noting
  each fake reference was replaced by "five, six or seven or eight" real ones, implying the
  underlying claim rested on no single source. Under 10 minutes.

- **Eugene Kim, "Amazon orders 90-day reset after code mishaps cause millions of lost orders," Business Insider, 10 March 2026 (URL slug: "amazon-tightens-code-controls-after-outages-including-one-ai-2026-3")** (news, 2026)  
  <https://www.businessinsider.com/amazon-tightens-code-controls-after-outages-including-one-ai-2026-3>  
  CUTS AGAINST THE FRAMING, and is the reason the Amazon example belongs in landmines as much
  as in evidence. Based on internal documents: SVP Dave Treadwell's "trend of incidents" since
  Q3 2025, at least one "tied to Amazon's AI coding assistant Q," "high blast radius changes,"
  and — decisively — that some failures traced back to "a requirement to have two people
  authorize code changes, that were either lacking or bypassed." It then records that "the
  Amazon spokesperson told Business Insider that it is not accurate to say junior and mid-
  level engineers are required to get sign off from senior engineers for any AI-assisted
  changes," contradicting the FT-derived version circulating in TechRadar and elsewhere. NOTE:
  paywalled for some readers; instructor should excerpt the two quoted passages onto the
  handout.

- **European Commission, "Liability for defective products" — official page on Directive (EU) 2024/2853 (revised Product Liability Directive), DG Internal Market (retrieved 16 August 2026)** (primary, 2024)  
  <https://single-market-economy.ec.europa.eu/single-market/goods/free-movement-sectors/liability-defective-products_en>  
  Supports the framing's thrust and supplies the "who is the manufacturer" machinery. Confirms
  "all types of software are covered by the new directive, including applications, operating
  systems and AI-systems," including defects that appear later "as a result of updates,
  upgrades or a machine-learning feature"; that "a product that has been substantially
  modified ... is considered to be a new product. The person that has made the modification
  becomes a manufacturer"; the chain of liable operators (manufacturer, importer or authorised
  representative, fulfilment service provider, distributor); "destruction or corruption of
  data" as compensable; entry into force 8 December 2024 and transposition by 9 December 2026,
  with the 1985 directive still governing earlier products. CAVEAT: this is the Commission's
  own summary page, not the legislative text — EUR-Lex blocked automated retrieval from this
  machine, so the Article numbers were not read directly.

- **European Parliament, Legislative Train Schedule, "AI liability directive" (file record; proposal COM(2022) 496, 28 September 2022; status: withdrawn) (retrieved 16 August 2026)** (primary, 2022)  
  <https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-ai-liability-directive>  
  THE REFERENCE THAT CUTS AGAINST THE FRAMING. The instrument that would have eased a
  claimant's burden against AI — a rebuttable presumption of causality plus court-ordered
  disclosure of evidence about high-risk AI systems — is recorded as withdrawn, following the
  withdrawal announced in the Commission Work Programme 2025. The institution most associated
  with expanding AI liability chose not to. Deliberately stated without an Official Journal
  citation or a precise withdrawal date: two of my retrievals disagreed on the date and
  neither was a raw read of the OJ, so the packet does not assert one. Two minutes to read.

- **Bryan H. Choi, "Crashworthy Code," 94 Washington Law Review 39 (2019)** (academic, 2019)  
  <https://digitalcommons.law.uw.edu/wlr/vol94/iss1/3/>  
  The doctrinal case against the framing's apparent thrust, from someone who is not an
  industry apologist. Choi argues "no consensus is imminent as long as liability is pegged to
  a standard of 'crashproof' code," that "imposing damages based on failure to prevent code
  crashes will not improve software quality, but will impede the rollout of cyber-physical
  systems," and proposes metering liability on mitigation rather than prevention: "requiring
  all code to be perfect is impossible, but expecting code to be crashworthy is reasonable."
  LONG (full law review article) — assign the abstract and introduction only; the abstract
  alone states the argument.

## 30-minute run sheet

PRE-CLASS: print the SAL case comment (assigned reading) and a one-page handout carrying four
excerpted quotes verbatim — the two Amazon passages from Business Insider (the internal
'controlled friction' quote and the spokesperson's denial), DEWR's 'the substance of the
independent review is retained' line, and the Ayinde [23] powers ladder. Have four index cards
per row. Draw an empty 4-column table on the board: SCENARIO | WHO BORE THE LOSS IN FACT | WHO
THE ROOM SAYS SHOULD | WHAT EVIDENCE WOULD FLIP IT. Draw a fifth narrow column at the far right
headed CONTESTED.

0:00-0:03 - Read the framing aloud. Then write four one-line facts on the board with no
commentary: 'Air Canada — $812.02'; 'Deloitte — final instalment refunded, recommendations
unchanged'; 'Neals & Wingate — new chambers review policies'; 'Amazon — more approvals; sign-off
rule disputed by Amazon.' Say explicitly: I am not going to tell you which of these is right,
and I will not settle disputes of fact from up here — anything asserted that nobody can source
goes in the CONTESTED column.

0:03-0:04 - Count off by four along the rows. Ones take the Air Canada scenario, twos Deloitte,
threes the judges, fours Amazon. Everyone gets the same three questions (prompts 1, 2 and 3) but
answers them against their own scenario.

0:04-0:09 - SILENT INDIVIDUAL THINK. No talking, no laptops. Each student writes on an index
card, in this order and nothing else: (a) one sentence — 'In my scenario the loss should fall on
____ because ____'; (b) one line — 'I would change my mind if I learned ____'. Tell them the
cards are collected at the end and are the participation record, so the second line matters as
much as the first.

0:09-0:16 - PAIR, deliberately mismatched. Instruct: find a partner holding a DIFFERENT scenario
number. Their job is not to agree. Their job is to identify the single factual difference
between the two scenarios that best explains why their answers differ, and write it on the back
of both cards. At 0:14 the instructor calls out one escalation: 'now swap scenarios and argue
your partner's position for sixty seconds.'

0:16-0:26 - SHARE. Take one pair per scenario, 90 seconds each, filling the board table live;
the instructor writes only what students say, verbatim where possible, and adjudicates nothing.
After all four scenarios are on the board (~0:22), open the floor on whichever column shows the
widest spread — usually 'WHAT EVIDENCE WOULD FLIP IT.' If the room converges too fast, read the
Amazon spokesperson denial aloud and ask the group that just argued Amazon solved it
organizationally to re-answer.

0:26-0:30 - CLOSE, and do only these three things. (1) Collect the cards. (2) Read out the two
most frequently recurring 'I would change my mind if...' lines and name each one as an
evidentiary question — usually a specification question ('what was the system supposed to do'),
a provenance question ('who introduced this change and could they check it'), or a checkability
question ('is this property decidable at all'). (3) State the one thing the room agreed on and
the one thing it did not, then stop. Do not resolve the disagreement; say plainly that it is
unresolved in the courts too, and point at the CONTESTED column as the list of claims nobody in
the room could source. Leave the board photo on the course site as the artifact.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

DO NOT ASSERT ANY OF THE FOLLOWING FROM THE FRONT OF THE ROOM.

1. "The EU now makes AI developers strictly liable for AI harms." This conflates two instruments
moving in opposite directions. The revised Product Liability Directive (EU) 2024/2853 does bring
software and AI systems inside strict product liability — but it entered into force 8 December
2024, transposition runs to 9 December 2026, it applies to products placed on the market from
that date (the 1985 directive still governs earlier ones), and the defendant chain includes
importers, authorised representatives, fulfilment service providers and distributors, not just
"the developer." The AI Liability Directive — the fault-based instrument with the rebuttable
presumption of causality and disclosure for high-risk AI — was withdrawn. Related: the EU AI Act
does not create a private right of action; do not say it does. And do not state a precise
Official Journal date or number for the AILD withdrawal: two retrievals during preparation
disagreed, and neither was a direct read of the OJ.

2. "Air Canada claimed its AI had legal personhood and the tribunal rejected AI personhood."
Half right, and the half that is wrong matters most in this course. Air Canada did argue the
chatbot was "a separate legal entity responsible for its own actions," and the tribunal rejected
it — but the record never established the chatbot was a large language model rather than a rule-
based decision-tree bot. The SAL case comment says so directly: "the first premise, that the
chatbot in question was powered by AI, cannot simply be assumed." The tribunal decided an
attribution question, not an AI question.

3. "Moffatt established that companies are liable for their AI." It is a small-claims decision
of the British Columbia Civil Resolution Tribunal awarding $812.02 (cite the total; the
damages/fees/interest breakdown circulating online was not verified here). CRT decisions are not
binding precedent, are not appellate authority, and are not US law. Note also that Air Canada's
contract defence failed for an unglamorous reason — it never put the relevant tariff terms into
evidence — so the case is weaker authority than the headlines suggest.

4. "GPT-4o fabricated the citations in the Deloitte report." Deloitte disclosed in an appendix
that part of the work "included the use of a generative artificial intelligence (AI) large
language model (Azure OpenAI GPT - 4o) based tool chain licensed by DEWR" — a methodology
disclosure, not a causal finding. Deloitte did not attribute the errors to AI and stood by the
findings; DEWR stated the substance and recommendations were unchanged. Charlotin's database
carries the identical caveat about tool attribution. Two adjacent errors: the refund was the
final instalment of the A$439,000 contract, not the whole fee (a senator's call for a full
refund is an argument, not an outcome), and it was a Sydney academic, Dr Christopher Rudge, who
identified the fabrications — not an automated checker.

5. "Hundreds of lawyers have been sanctioned for AI hallucinations." The Charlotin database held
1,922 entries when retrieved on 16 August 2026, and the largest party category is pro se
litigants (1,111), ahead of lawyers (761), with judges at 28. Inclusion records that a court
addressed hallucinated material — not that a sanction issued — and the site states it does not
track the wider universe of fake citations. Any headline count of "sanctioned lawyers" drawn
from it is unsupported.

6. "Amazon now requires senior sign-off on AI-assisted code changes." This is the packet's live
dispute, not a fact. Business Insider, working from internal documents, records that "the Amazon
spokesperson told Business Insider that it is not accurate to say junior and mid-level engineers
are required to get sign off from senior engineers for any AI-assisted changes"; FT-derived
coverage (TechRadar) asserts the opposite, and TechRadar's headline makes a third, different
claim about senior engineers themselves needing sign-off. What is documented is broader and less
quotable: more thorough change documentation, additional approvals, "controlled friction,"
audits ordered of Tier-1 system owners and Director/VP leaders, and the finding that a pre-
existing two-person code authorization requirement was "either lacking or bypassed." Present the
disagreement as the evidence; that is the more interesting classroom object anyway.

7. "The judges were disciplined" — and equally, "the judges were cleared." Neither is
supportable from what is on the record. The Senate Judiciary release documents the judges'
admissions and their new internal review policies and Grassley's call for judiciary-wide
guidance; it does not report a disciplinary outcome, and silence in a press release is not a
finding either way. State the asymmetry against Ayinde's sanctions ladder as an open question,
not as proof that judges escaped consequences.

8. "Using AI in a court filing is contempt of court." Ayinde did not hold that. The Divisional
Court set out a menu — admonition, costs, wasted costs, strike out, regulator referral,
contempt, police referral — with factors governing the choice, and it expressly declined
contempt as to one barrister while warning at [70] that "this court's decision not to initiate
contempt proceedings in respect of Ms Forey is not a precedent."

9. "Formal verification would have caught this." For the fabricated citations, no: citation
existence is a database lookup, which is why an automated reference checker already exists;
calling it a verification problem inflates what verification is for. The symmetric error is also
available and equally wrong — do not let the room conclude that because verification would not
have caught the fake footnotes, it is irrelevant to the Amazon-style deployment failures, where
the internal finding was a bypassed two-person authorization gate. Be precise about which
property is being checked and by what.

10. Vendor-sourced framings to keep off the board entirely: claims that a given assistant
"reduces bugs by N%" or that a code-review AI catches vulnerabilities at some rate, unless
someone brings the study and its methodology. None of the sources in this packet supports any
such number, and an unsourced productivity or defect-rate figure asserted by the instructor is
the exact failure mode the discussion is about.
