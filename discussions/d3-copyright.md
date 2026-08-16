# D3 — Are LLMs Theft? Training Data, Copyright, and Fair Use (status as of August 2026)

**Session 4 · Tue Sep 8 · week 3 · 30 minutes · think–pair–share**

## Framing

> In the last week of June 2025, two judges in the same federal courthouse decided cases about AI
> companies downloading millions of books from shadow libraries, and reached opposite conclusions
> on overlapping facts. Judge Alsup held that Anthropic's training was "exceedingly
> transformative" but that keeping a permanent pirated library was not fair use, and dismissed the
> authors' fear of "an explosion of competing works" as no different from complaining that we
> teach schoolchildren to write well. Two days later Judge Chhabria held that Meta's downloads
> "all had the ultimate purpose of LLM training" and rode along with it — while writing that
> exactly that flooding effect, market dilution, "will often cause plaintiffs to decisively win"
> fair use, and ruling for Meta only because these thirteen plaintiffs put on no evidence of it.
> Fourteen months later no U.S. appellate court has resolved any of it: the first appellate
> argument on AI training and fair use was heard on June 11, 2026 and is undecided, and summary
> judgment briefing in the consolidated OpenAI cases does not close until November.

## Why this is in a formal-methods course

Every doctrinal fight in this litigation bottoms out in an unspecified predicate over a program:
"the model does not contain the work," "these outputs dilute the market," "this copy was used
only for training." Those have exactly the shape of the properties we spend the semester
learning to state precisely and then check — yet courts resolve them with duelling expert
testimony rather than reproducible artifacts, partly because nobody has been required to write
the specification down. Note the asymmetry we will formalize later: extraction attacks are bug-
finding and can witness a violation but never its absence; deduplication and DP-SGD are the
soundness-side claims, with guarantees far weaker than the legal conclusions being hung on them;
and data provenance is a supply-chain property with no accepted proof obligation attached to it.

## Discussion questions

**1.** ACQUISITION VS. USE. Bartz treats how you got the copy as a separate wrong from what you did
with it: Anthropic's training was fair use, its pirated library was not. Kadrey says the shadow-
library downloads "all had the ultimate purpose of LLM training" and are covered by it. Which
judge is right — and then apply your answer to a lab that torrents a corpus, trains a model,
publishes the weights, and deletes the corpus. Does deleting it help them, hurt them, or change
nothing?

**2.** IS DILUTION A HARM COPYRIGHT SEES? Alsup: flooding a market with similar-but-not-substantially-
similar works is "not the kind of competitive or creative displacement that concerns the
Copyright Act — the Act seeks to advance original works of authorship, not to protect authors
against competition." Chhabria and the Copyright Office say the opposite, and that it may be
decisive. If dilution counts under factor four, what stops it from swallowing parody, criticism,
and every rival textbook ever written? If it does not count, what is left for an author whose
style is imitated but whose sentences are never reproduced?

**3.** THE CIRCULARITY. The Copyright Office concludes that "[w]here licensing options exist or are
likely to be feasible, this consideration will disfavor fair use," and news publishers keep
signing licensing deals with AI companies. So does every deal signed make the next defendant's
fair use defense weaker? Argue both: that this is copyright working exactly as designed, and
that it is a market in which whoever can afford to pay gets to define the legality of what
everyone else does. Which reading survives contact with who is actually at the table?

**4.** DO THE WEIGHTS CONTAIN THE WORK? The UK High Court held Stable Diffusion is not an "infringing
copy" because it does not store the works — but Getty never alleged that it did, so the
technical point was conceded on that record; meanwhile Carlini et al. measure verbatim emission
rising with model size and data duplication. What evidence should a court demand before
accepting that a model "does not contain" a work, and which party should bear that burden? Is
"we tried to extract it and failed" the same claim as "it is not in there"?

**5.** WHAT IS THE REMEDY? Suppose a court holds that training on a work is infringement. Then what —
damages, or destruction of the model? Judge Eumi Lee refused the music publishers a preliminary
injunction partly over the enforceability and manageability of an order governing Anthropic's
future models. What exactly would a court have to be shown to believe that a model no longer
contains a work, who should be allowed to show it, and would you accept the defendant's own
evaluation as proof?

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Bartz v. Anthropic PBC, No. 3:24-cv-05417-WHA, Dkt. 231, "Order on Fair Use" (N.D. Cal. June 23, 2025) (Alsup, J.)** (primary, 2025)  
  <https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.231.0_1.pdf>  
  The strongest judicial statement for the AI-company side — training was "exceedingly
  transformative," print-to-digital conversion was fair use — and simultaneously the strongest
  for the rights-holder side on acquisition: the pirated central library was not fair use and
  was headed to trial. It also contains the flat rejection of market dilution ("training
  schoolchildren to write well") that the Copyright Office and Judge Chhabria contradict. 32
  pages; assign only pp. 1-2 (Introduction) and the factor-four passage at p. 30.

- **Kadrey v. Meta Platforms, Inc., No. 3:23-cv-03417-VC, Dkt. 598, Order Denying Plaintiffs' Motion for Partial Summary Judgment and Granting Meta's Cross-Motion (N.D. Cal. June 25, 2025) (Chhabria, J.)** (primary, 2025)  
  <https://chatgptiseatingtheworld.com/wp-content/uploads/2025/06/Judge-Chhabria-Fair-Use-decision-in-Kadrey-v.-Meta-June-25-2025.pdf>  
  Decided two days after Bartz and reasoning the opposite way on both contested points:
  shadow-library downloads ride along with training, but market dilution "will often cause
  plaintiffs to decisively win the fourth factor." Nominally a win for Meta, doctrinally a
  roadmap for authors — so it supports neither side cleanly, which is why it drives the
  discussion. 40 pages; pp. 1-5 carry the whole argument. (This is an ECF-stamped copy of Dkt.
  598 mirrored on a case-tracking blog; I confirmed the caption, case number, docket number,
  filing stamp and page count from the file itself.)

- **Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc., No. 1:20-cv-613-SB, Dkt. 770 (D. Del. Feb. 11, 2025) (Bibas, J.)** (primary, 2025)  
  <https://chatgptiseatingtheworld.com/wp-content/uploads/2025/02/Judge-Bibas-SJ-order-rejects-fair-use-defense.pdf>  
  The clearest anti-fair-use holding and the best single assigned reading — 23 pages, ~6,700
  words, plain prose. Supports the rights-holder side, but limits itself expressly ("only non-
  generative AI is before me today") and openly revises the judge's own 2023 ruling ("That is
  why I have changed my mind"), which makes it a live test of whether students will
  distinguish or over-generalize. This is the case argued to the Third Circuit on June 11,
  2026 and still undecided. (Blog-mirrored ECF-stamped copy; caption, docket number and filing
  stamp verified from the file.)

- **Getty Images (US) Inc & Ors v Stability AI Ltd [2025] EWHC 2863 (Ch), Case No. IL-2023-000007 (Mrs Justice Joanna Smith DBE, 4 Nov. 2025)** (primary, 2025)  
  <https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf>  
  Reported as a sweeping win for AI developers; read directly, it mostly supports neither side
  and teaches procedure over doctrine. Getty abandoned the training claim for want of evidence
  that training happened in the UK (¶9), abandoned the outputs claim, lost secondary
  infringement, and won only "historic and extremely limited" trade mark findings (¶757) — and
  ¶11 records that Getty never alleged the model stores copies at all. 199 pages; assign
  ¶¶8-14 and ¶¶757-758 only.

- **U.S. Copyright Office, Copyright and Artificial Intelligence, Part 3: Generative AI Training (Pre-Publication Version), Report of the Register of Copyrights, May 2025** (report, 2025)  
  <https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf>  
  The institutional case for the rights-holder side, and the source of the factor-four
  circularity problem: outputs "can dilute the market for works similar to those found in its
  training data," and "[w]here licensing options exist or are likely to be feasible, this
  consideration will disfavor fair use." Non-binding, still pre-publication as of Aug 2026.
  108 pages; assign the Executive Summary plus the market-effects discussion around pp. 60-75.

- **Mark A. Lemley & Bryan Casey, "Fair Learning," 99 Texas Law Review 743 (2021)** (academic, 2021)  
  <https://texaslawreview.org/fair-learning/>  
  The reference that cuts hardest against the framing's implicit sympathy for authors: ML
  training should be presumptively fair because systems take unprotectable facts and ideas
  rather than protected expression. Written years before this litigation, so it is free of
  litigation posture. Pair it with the Copyright Office report and make students locate the
  exact point where the two disagree about what a model "takes."

- **Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr & Chiyuan Zhang, "Quantifying Memorization Across Neural Language Models," ICLR 2023 (arXiv:2202.07646)** (academic, 2022)  
  <https://arxiv.org/abs/2202.07646>  
  The empirical ammunition against the AI-company premise that weights do not contain the
  works: memorization grows with model capacity, example duplication and prompt context, and
  is "more prevalent than previously believed." It proves no legal conclusion — it shows that
  the predicate courts assume is a measurable, model-dependent quantity nobody has been
  required to measure. Abstract plus Figures 1-2 is a ten-minute read.

- **Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 53 — Obligations for providers of general-purpose AI models** (legal, 2024)  
  <https://artificialintelligenceact.eu/article/53/>  
  Supports neither side on infringement; it changes the subject from liability to disclosure.
  Art. 53(1)(c)-(d) requires a copyright policy that identifies and honors Art. 4(3) DSM text-
  and-data-mining opt-outs "including through state-of-the-art technologies," plus a publicly
  available "sufficiently detailed summary" of training content on an AI Office template —
  applicable to GPAI providers from 2 Aug. 2025. Use it to ask why the EU regulates provenance
  disclosure while the US litigates outcomes. (This is an unofficial consolidated
  presentation; I separately fetched EUR-Lex CELEX 32024R1689 and confirmed the regulation's
  official title and date of 13 June 2024.)

- **JURIST, "Judge approves record $1.5 billion AI copyright settlement involving Anthropic" (July 2026)** (news, 2026)  
  <https://www.jurist.org/news/2026/07/judge-approves-record-1-5-billion-settlement-involving-anthropic/>  
  Corrects the procedural fact students most reliably get wrong, in a way that cuts against
  the "authors won" narrative: the $1.5B is a settlement given final approval by Judge
  Martínez-Olguín in July 2026 (~$3,000 per work), not a judgment, with no liability finding —
  and it left Alsup's pro-Anthropic training holding standing while ending the case before any
  appellate review of it. Two-minute read.

- **Murray Stassen, "Music publishers file amended lyrics lawsuit against Anthropic — just as AI firm's separate $1.5bn settlement with authors wins court approval," Music Business Worldwide (July 2026)** (news, 2026)  
  <https://www.musicbusinessworldwide.com/music-publishers-file-amended-lyrics-lawsuit-against-anthropic-just-as-ai-firms-separate-1-5b-piracy-settlement-with-authors-wins-court-approval/>  
  Keeps the Anthropic story from reading as closed, and supplies the remedy question that
  anchors prompt 5: Judge Eumi Lee denied the publishers' preliminary injunction on training
  in March 2025 partly over the enforceability of an order governing future models; publishers
  moved for partial summary judgment against fair use in March 2026 and filed a second amended
  complaint on 22 July 2026, with a separate January 2026 suit over 20,000+ songs seeking
  $3B+. Journalism, not a court document — cite it for posture, never for holdings.

## 30-minute run sheet

PRE-READ (assign at the previous class; ~7 pages, 25 minutes): Bartz Dkt. 231 pp. 1-2
(Introduction) plus the factor-four passage at p. 30 ("training schoolchildren to write well"),
and Kadrey Dkt. 598 pp. 1-5. Tell them only this: same district, decided two days apart.

BEFORE CLASS: three column headers on the board — (1) HOW THE COPY WAS OBTAINED, (2) WHAT THE
MODEL DOES WITH IT, (3) WHAT WOULD SETTLE THIS. Leave (3) blank. Hand each student a blank index
card at the door.

0-3 — Read the framing aloud. Do not explain it, do not add context. Then write under columns 1
and 2, one phrase each: Bartz = "pirated library: NOT fair use / training: fair use"; Kadrey =
"downloads rode along with training." Say nothing about which is correct.

3-9 — Silent individual think, in writing, no talking, no phones. Only the hypothetical from
prompt 1: the lab that torrents a corpus, trains, publishes the weights, deletes the corpus.
Each student writes ONE sentence on the card and a letter: A = the acquisition is a separate
wrong, B = the transformative use covers it. No names on cards.

9-10 — Hands up for A; hands up for B. Write both numbers on the board and circle them. Label
the circle "BEFORE." Say nothing about the split.

10-20 — Pairs. Instruction: "Find someone whose letter is different from yours." CONTINGENCY: if
the room is worse than roughly 70/30, skip the search — assign the minority letter to half the
pairs and require them to argue it. Each pair writes two things on one card: (i) the strongest
single sentence for the position they did NOT choose, and (ii) one fact about the world — not
about law — that would change their own mind. Circulate; if a pair is only trading conclusions,
ask them "what would you have to see?"

20-27 — Share. Call on 4-6 pairs. Ask ONLY for item (ii). Write each answer verbatim in column
3. Expect: how often models emit verbatim training text; whether a licensing market actually
clears and at what price; whether readers substitute AI output for the book. Do not evaluate any
of them, do not correct legal errors yet. If a pair gives a legal answer ("if the Supreme Court
said X"), push exactly once: "what would you measure?"

27-30 — Re-vote A/B by show of hands; write the new numbers beside the circled BEFORE. Close by
pointing at column 3: every item in that column is an empirical or formal claim about a software
system; none of the four courts we have discussed had a reproducible way to measure any of them;
each of them decided anyway. Collect all index cards at the door — column 3 is the input list
for the next lecture on writing a specification.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Do not assert any of the following from the front of the room.

1. "A court held that training AI on copyrighted books is legal." No. Alsup's holding covers
copies that were LAWFULLY ACQUIRED, is one district judge, binds no one, and was never reviewed
on appeal — the settlement ended the case first. Chhabria's holding resolves the claims of
thirteen named plaintiffs on their particular record; he says so explicitly ("this ruling does
not stand for the proposition that Meta's use of copyrighted materials to train its language
models is lawful").

2. "Anthropic lost / was found liable for $1.5 billion." There is no liability finding.
Anthropic WON the training question. The $1.5B settlement (preliminary approval by Alsup in
Sept. 2025; final approval by Judge Martínez-Olguín in July 2026, roughly $3,000 per work,
class-counsel fees cut far below the requested 12.5%) resolved the pirated-acquisition claim
before trial. Never call it a judgment or a precedent.

3. "Kadrey rejected market dilution." The opposite: Chhabria wrote that dilution "will often
cause plaintiffs to decisively win the fourth factor — and thus win the fair use question
overall — in cases like this," and granted summary judgment because these plaintiffs "barely
give this issue lip service, and they present no evidence." Kadrey is also still live;
plaintiffs sought leave for a fourth amended complaint and moved to certify the downloading
issue for interlocutory appeal (reply filed June 30, 2026). No Ninth Circuit merits decision
exists.

4. "Thomson Reuters v. Ross settles AI training." Bibas wrote "only non-generative AI is before
me today"; Ross was a non-generative research tool competing head-on with the plaintiff's own
product. The Feb. 11, 2025 opinion also REVISES his own 2023 ruling — "That is why I have
changed my mind" — so citing "the Ross holding" without a date is ambiguous. The Third Circuit
(No. 25-2153) heard argument on June 11, 2026 and has NOT ruled. Do not state or imply an
outcome.

5. "Getty lost in the UK, so training is lawful there" / "Getty won." Neither. Getty ABANDONED
the training claim because it could not show training occurred in the UK — a territoriality
failure, not a merits ruling — abandoned the outputs claim because Stability had blocked the
prompts, and lost secondary infringement. Its wins were narrow, historic trade mark findings
about watermarks. Permission to appeal the secondary-infringement finding was granted.

6. "The UK court found that model weights do not contain copies of training data." Read
paragraph 11: Getty itself never alleged that Stable Diffusion stores copies. The court decided
a conceded point, on that record, about those models — not a general technical finding, and not
a finding about LLMs at all. The memorization literature cuts the other way.

7. "The EU AI Act bans training on copyrighted works" / "requires publishing the training
dataset." Article 53(1)(c)-(d) requires a copyright policy honoring Art. 4(3) DSM opt-outs and a
"sufficiently detailed summary" of training content on an AI Office template — a summary, not a
manifest, and not a ban. There is no fair use doctrine in EU law, so US fair-use reasoning does
not transfer. Also: the Commission's late-2025 "digital omnibus" package proposed changes to AI
Act timing and scope; check its current status before asserting any date.

8. "The Copyright Office concluded that AI training is not fair use." It is a PRE-PUBLICATION
report from May 2025 that was still not final as of Aug. 2026, it is not binding on any court,
it expressly declines a categorical rule, and its release was followed by upheaval at the Office
(verify the specifics before recounting them). Cite it as one agency's reasoning under contest,
not as law.

9. "The New York Times won" / "the Times lost." Judge Stein's April 2025 order largely denying
the motion to dismiss decided nothing about fair use. The Times and the Authors Guild cases are
handled together with the other S.D.N.Y. OpenAI actions in the consolidated MDL before Judge
Stein (In re OpenAI, Inc. Copyright Infringement Litigation, No. 1:25-md-03143); summary
judgment briefing runs into November 2026 and no trial date is set. There is no merits ruling to
describe.

10. Dollar figures for AI licensing deals. Reported per-year values are almost always leaks or
unconfirmed estimates; the agreements themselves are not public. Do not quote a number as fact,
and do not infer a market rate from one.

11. "Models learn the way humans do" and "it's compression, not copying." Both are analogies
doing argumentative work, not findings of fact. Alsup's schoolchildren analogy is a rhetorical
move that Chhabria and the Copyright Office explicitly refuse. Present them as contested
framings students can attack, never as background truth.

12. Getty's refiled US case: it was voluntarily dismissed in Delaware and refiled in N.D. Cal.
in August 2025, reportedly adding a dilution theory. The "reportedly" is load-bearing — this
comes from case-tracking journalism, not from a document I read. Do not characterize its claims
in detail.
