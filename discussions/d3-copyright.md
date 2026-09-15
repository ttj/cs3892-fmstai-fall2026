# D3 — Are LLMs Theft? Training Data, Copyright, and Fair Use (status as of August 2026)

**Session 4 · Tue Sep 8 · week 3 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Thu Sep 10, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What happened

Since 2023, authors, news organizations, visual-media companies, and music publishers have sued companies building generative AI models for copyright infringement. The complaints separate three acts; a defendant can lose one and win the others: **acquisition** — how the copies were obtained, and several defendants bulk-downloaded books from pirate "shadow libraries" like LibGen and Anna's Archive; **training** — using the works to fit model weights; and **output** — whether the finished system reproduces protected expression.

The main U.S. defense is **fair use**, a statutory exception (17 U.S.C. § 107) making some unauthorized copying lawful. Courts weigh four factors: the purpose and character of the use, including whether it is "transformative"; the nature of the work; how much was taken; and the effect on the original's market — often decisive. Fair use is a U.S. doctrine; the EU and UK use narrower, enumerated exceptions instead.

### What the courts found

In February 2025, Judge Stephanos Bibas (D. Del.) rejected Ross Intelligence's fair use defense for copying Westlaw headnotes to build a competing legal-research tool — while cautioning that "only non-generative AI is before me today," and revising his own 2023 ruling: "That is why I have changed my mind."

Four months later, one San Francisco courthouse produced two rulings two days apart. Judge William Alsup (*Bartz v. Anthropic*, June 23, 2025) granted Anthropic summary judgment that training was fair use — "exceedingly transformative" — and rejected the authors' market-flooding theory: it is "no different" than complaining "that training schoolchildren to write well would result in an explosion of competing works." But he denied summary judgment on the pirated copies Anthropic kept in a permanent "central library," sending those to trial. Judge Vince Chhabria (*Kadrey v. Meta*, June 25, 2025) reasoned the opposite way on both: Meta's shadow-library downloads shared training's transformative purpose, yet "market dilution will often cause plaintiffs to decisively win the fourth factor." He ruled for Meta only because these thirteen plaintiffs "barely give this issue lip service, and they present no evidence," adding that the ruling "does not stand for the proposition that Meta's use of copyrighted materials to train its language models is lawful."

### Why it still matters

Very little is settled. Anthropic settled the pirated-acquisition claim for $1.5 billion, approved in July 2026 at roughly $3,000 per work — but a settlement is not a judgment, carries no liability finding, and ended the case before appeal. No U.S. appellate court has ruled: the Third Circuit heard argument in Ross on June 11, 2026 and has not decided; the consolidated OpenAI cases before Judge Stein, including The New York Times's, are in summary-judgment briefing into November 2026. In the UK, Getty abandoned its training claim against Stability AI for want of evidence that training happened there — a territoriality failure, not a ruling on whether training infringes — and never alleged the model stores copies.

At stake is the field's cost structure: whether training data must be licensed, what provenance must be logged, what a court could order done to a model. Every contested question — does the model contain the work, do its outputs dilute a market, was this copy used only for training — is a claim about a program that none of these courts had a reproducible way to measure.

### Timeline

| When | What |
|---|---|
| Feb 11, 2025 | Judge Bibas (D. Del.) rejects Ross Intelligence's fair use defense in Thomson Reuters v. Ross, revising his own 2023 ruling and noting that "only non-generative AI is before me today." |
| May 2025 | U.S. Copyright Office releases its pre-publication Part 3 report: AI outputs "can dilute the market for works similar to those found in its training data," and where licensing is feasible that "will disfavor fair use." Non-binding; still not final as of Aug. 2026. |
| June 23, 2025 | Judge Alsup, Bartz v. Anthropic: training was "exceedingly transformative" and fair use; summary judgment denied as to the pirated central-library copies, which are set for trial. |
| June 25, 2025 | Judge Chhabria, Kadrey v. Meta: summary judgment for Meta on this record, while holding that market dilution "will often cause plaintiffs to decisively win the fourth factor"; ruling expressly limited to these thirteen plaintiffs. |
| Nov 4, 2025 | UK High Court, Getty Images v Stability AI: the training and outputs claims are abandoned before judgment, secondary infringement fails, and the trade mark findings are "historic and extremely limited in scope." |
| June 11, 2026 | Third Circuit hears argument in Thomson Reuters v. Ross (No. 25-2153), the first U.S. appellate argument on AI training and fair use. Undecided. |
| July 2026 | Judge Martinez-Olguin grants final approval to Anthropic's $1.5B settlement of the pirated-acquisition claim (roughly $3,000 per work). A settlement, not a judgment; no liability finding. |
| November 2026 (scheduled) | Summary-judgment briefing closes in the consolidated OpenAI cases before Judge Stein (In re OpenAI, No. 1:25-md-03143). No trial date set. |

## The question

**Does deleting the pirated books after training make it okay?**

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

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

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

## Readings

10 sources. You will be assigned one; the rest are here if you want to go further, or if you want to check a claim you hear in the room.

- **Bartz v. Anthropic PBC, No. 3:24-cv-05417-WHA, Dkt. 231, "Order on Fair Use" (N.D. Cal. June 23, 2025) (Alsup, J.)** (primary, 2025)  
  <https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.231.0_1.pdf>  
  The strongest judicial statement for the AI-company side — training was "exceedingly
  transformative," print-to-digital conversion was fair use — and simultaneously the strongest
  for the rights-holder side on acquisition: the pirated central library was not fair use and
  was headed to trial. It also contains the flat rejection of market dilution ("training
  schoolchildren to write well") that the Copyright Office and Judge Chhabria contradict. 32
  pages; the part you need is pp. 1-2 (Introduction) and the factor-four passage at p. 30.

- **Kadrey v. Meta Platforms, Inc., No. 3:23-cv-03417-VC, Dkt. 598, Order Denying Plaintiffs' Motion for Partial Summary Judgment and Granting Meta's Cross-Motion (N.D. Cal. June 25, 2025) (Chhabria, J.)** (primary, 2025)  
  <https://chatgptiseatingtheworld.com/wp-content/uploads/2025/06/Judge-Chhabria-Fair-Use-decision-in-Kadrey-v.-Meta-June-25-2025.pdf>  
  Decided two days after Bartz and reasoning the opposite way on both contested points:
  shadow-library downloads ride along with training, but market dilution "will often cause
  plaintiffs to decisively win the fourth factor." Nominally a win for Meta, doctrinally a
  roadmap for authors — it supports neither side cleanly, so read it for the reasoning rather
  than the outcome. 40 pages; pp. 1-5 carry the whole argument. (This is an ECF-stamped copy
  of Dkt. 598 mirrored on a case-tracking blog; I confirmed the caption, case number, docket
  number, filing stamp and page count from the file itself.)

- **Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence Inc., No. 1:20-cv-613-SB, Dkt. 770 (D. Del. Feb. 11, 2025) (Bibas, J.)** (primary, 2025)  
  <https://chatgptiseatingtheworld.com/wp-content/uploads/2025/02/Judge-Bibas-SJ-order-rejects-fair-use-defense.pdf>  
  If you read only one court opinion on this, make it this one — the clearest anti-fair-use
  holding, 23 pages, ~6,700 words, plain prose. It supports the rights-holder side, but limits
  itself expressly ("only non-generative AI is before me today") and openly revises the judge's
  own 2023 ruling ("That is why I have changed my mind"), so distinguish it before you
  generalize from it. This is the case argued to the Third Circuit on June 11, 2026 and still
  undecided. (Blog-mirrored ECF-stamped copy; caption, docket number and filing stamp verified
  from the file.)

- **Getty Images (US) Inc & Ors v Stability AI Ltd [2025] EWHC 2863 (Ch), Case No. IL-2023-000007 (Mrs Justice Joanna Smith DBE, 4 Nov. 2025)** (primary, 2025)  
  <https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf>  
  Reported as a sweeping win for AI developers; read directly, it mostly supports neither side
  and teaches procedure over doctrine. Getty abandoned the training claim for want of evidence
  that training happened in the UK (¶9), abandoned the outputs claim, lost secondary
  infringement, and won only "historic and extremely limited" trade mark findings (¶757) — and
  ¶11 records that Getty never alleged the model stores copies at all. 199 pages; read
  ¶¶8-14 and ¶¶757-758 only.

- **U.S. Copyright Office, Copyright and Artificial Intelligence, Part 3: Generative AI Training (Pre-Publication Version), Report of the Register of Copyrights, May 2025** (report, 2025)  
  <https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf>  
  The institutional case for the rights-holder side, and the source of the factor-four
  circularity problem: outputs "can dilute the market for works similar to those found in its
  training data," and "[w]here licensing options exist or are likely to be feasible, this
  consideration will disfavor fair use." Non-binding, still pre-publication as of Aug 2026.
  108 pages; read the Executive Summary plus the market-effects discussion around pp. 60-75.

- **Mark A. Lemley & Bryan Casey, "Fair Learning," 99 Texas Law Review 743 (2021)** (academic, 2021)  
  <https://texaslawreview.org/fair-learning/>  
  The strongest argument on the other side: ML training should be presumptively fair because
  systems take unprotectable facts and ideas rather than protected expression. Written years
  before this litigation, so it is free of litigation posture. Read it against the Copyright
  Office report and find the exact point where the two disagree about what a model "takes."

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
  applicable to GPAI providers from 2 Aug. 2025. Read it for the contrast: the EU regulates
  provenance disclosure while the US litigates outcomes. (This is an unofficial consolidated
  presentation; I separately fetched EUR-Lex CELEX 32024R1689 and confirmed the regulation's
  official title and date of 13 June 2024.)

- **JURIST, "Judge approves record $1.5 billion AI copyright settlement involving Anthropic" (July 2026)** (news, 2026)  
  <https://www.jurist.org/news/2026/07/judge-approves-record-1-5-billion-settlement-involving-anthropic/>  
  The detail most people get wrong here is procedural, and getting it right cuts against the
  "authors won" narrative: the $1.5B is a settlement given final approval by Judge
  Martínez-Olguín in July 2026 (~$3,000 per work), not a judgment, with no liability finding —
  and it left Alsup's pro-Anthropic training holding standing while ending the case before any
  appellate review of it. Two-minute read.

- **Murray Stassen, "Music publishers file amended lyrics lawsuit against Anthropic — just as AI firm's separate $1.5bn settlement with authors wins court approval," Music Business Worldwide (July 2026)** (news, 2026)  
  <https://www.musicbusinessworldwide.com/music-publishers-file-amended-lyrics-lawsuit-against-anthropic-just-as-ai-firms-separate-1-5b-piracy-settlement-with-authors-wins-court-approval/>  
  The Anthropic story is not closed, and this is where discussion question 5 on remedies comes
  from: Judge Eumi Lee denied the publishers' preliminary injunction on training in March 2025
  partly over the enforceability of an order governing future models; publishers moved for
  partial summary judgment against fair use in March 2026 and filed a second amended complaint
  on 22 July 2026, with a separate January 2026 suit over 20,000+ songs seeking $3B+.
  Journalism, not a court document — cite it for posture, never for holdings.

## What you submit

One paragraph, 150–250 words, by **Thu Sep 10, 11:59 p.m.**, to the `D3` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
