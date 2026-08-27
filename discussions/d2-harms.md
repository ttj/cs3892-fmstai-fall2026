# D2 — A Survey of Harms: When Software and AI Hurt People

**Session 3 · Thu Sep 3 · week 2 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Sat Sep 5, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What happened

**Therac-25 (1985–87).** A computer-controlled radiation therapy machine from Atomic Energy of Canada Limited massively overdosed six patients. Some died; accounts differ on how many.

**Post Office Horizon (UK, from 1999).** The Post Office rolled out Horizon, a branch accounting system from ICL Pathway, later Fujitsu. Where Horizon showed a shortfall, the Post Office held the sub-postmaster — a branch's self-employed operator — personally liable and prosecuted many for theft or false accounting.

**Dutch childcare benefits (from 2013).** The Dutch tax authority used a "risk classification model" to flag childcare-benefit claims as possibly fraudulent. Flagged parents had payments stopped and were told to repay years of benefits at once. Amnesty International says tens of thousands were falsely accused.

**Robodebt (Australia, 2015–19).** The government raised welfare debts by averaging a person's annual tax-office income across fortnights, then asked recipients to disprove it.

**Gender Shades (2018).** Joy Buolamwini and Timnit Gebru audited three commercial systems that guess gender from a photograph.

**COMPAS (2016).** ProPublica obtained risk scores for 7,000+ people arrested in Broward County, Florida, and checked who was charged with a new crime within two years. Race is not among COMPAS's 137 inputs.

### What the investigators found

Nancy Leveson argues the Therac-25 lesson is *not* one concurrency bug: hardware interlocks that backstopped nearly identical software on earlier machines were removed, operators could not interpret the error messages, and no one independently reviewed the safety-critical software.

In *Bates v Post Office* (2019), Mr Justice Fraser tried the reliability question on evidence: Legacy Horizon "was not remotely robust," carrying "a significant and material risk of inaccuracy in branch accounts as a result of bugs, errors and defects." That is a finding about the system, not about anyone's guilt.

Robodebt's averaging computed exactly what policy instructed; the Royal Commission (July 2023) called it "a crude and cruel mechanism, neither fair nor legal." Amnesty found nationality was used as a risk factor in the Dutch model, amounting to racial profiling.

Gender Shades reported error rates up to 34.7% for darker-skinned women against 0.8% for lighter-skinned men — on gender classification, not on identifying who someone is. ProPublica found 44.9% of Black defendants who did not reoffend were labelled higher risk, versus 23.5% of white defendants; Northpointe answered that a given score means the same thing regardless of race. Kleinberg et al. and Chouldechova showed both can be true: when two groups reoffend at different underlying rates, no score can satisfy both criteria at once.

### Why it still matters

Sir Wyn Williams's 2025 inquiry report judges it "likely that approximately 1,000 persons were prosecuted and convicted" UK-wide on Horizon evidence, though he finds it "difficult to be precise"; about 10,000 are eligible for redress. The Post Office named 13 people whose families say Horizon drove them to take their own lives; Sir Wyn wrote he "cannot make a definitive finding" of a causal connection for all 13, but does "not rule it out as a real possibility." In May 2024 Parliament quashed a whole class of convictions by statute, not case by case. The Dutch cabinet resigned in January 2021 over the affair; Australia's Federal Court found Robodebt unlawful in late 2019, ending it.

Therac-25, Horizon and Robodebt involved no machine learning at all.

### Timeline

| When | What |
|---|---|
| June 1985 – January 1987 | The Therac-25, a computer-controlled radiation therapy machine made by Atomic Energy of Canada Limited, massively overdoses six patients. |
| September 1999 | The Post Office begins rolling out the Horizon accounting system to UK branches; rollout completes by early 2002, and prosecutions of sub-postmasters follow. |
| 23 May 2016 | ProPublica publishes "Machine Bias" on COMPAS; Kleinberg, Mullainathan and Raghavan (2016) and Chouldechova (2017) then prove the competing fairness criteria cannot all hold when base rates differ. |
| February 2018 | Buolamwini and Gebru present Gender Shades at the first Conference on Fairness, Accountability and Transparency. |
| 16 December 2019 | In Bates v Post Office (No. 6), Mr Justice Fraser finds Legacy Horizon "was not remotely robust" and carrying a material risk of inaccuracy in branch accounts. |
| January 2021 | The Dutch cabinet resigns over the childcare-benefits affair. |
| 7 July 2023 | The Royal Commission into the Robodebt Scheme delivers its final report, calling the scheme "a crude and cruel mechanism, neither fair nor legal." |
| 24 May 2024 | The Post Office (Horizon System) Offences Act 2024 receives Royal Assent, quashing a whole class of convictions by statute. |

## The question

> Almost every case on today's list in which someone died, went to prison, or lost a house
> involved no machine learning at all: a radiation therapy machine, a rocket's inertial reference
> unit, a Post Office accounting package, a welfare debt calculator that averaged annual income
> across fortnights. Meanwhile the cases that dominate AI-ethics syllabi have harms that are real
> but contested, unquantified, or in one instance never deployed: a hiring model known to us only
> through anonymous sources, a recidivism score whose bias depends on which fairness definition
> you adopt, a gender classifier that does not perform face identification. One reading is that we
> are studying the wrong failures because the new ones photograph better. Another is that the old
> failures are simply the ones that have finished being adjudicated, and that we are looking at
> the early photographs of the next Horizon.

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

**1.** Kleinberg et al. and Chouldechova prove that calibration and equal error rates across groups
cannot all hold when base rates differ. Northpointe's defence was that COMPAS satisfies
predictive parity -- a given risk score carries the same probability of reoffending regardless
of race -- while ProPublica measured error-rate balance instead. Does an impossibility theorem
license deployment (no system could have done better, so ours is not unfair) or forbid it (there
is no coherent specification, so nothing was ever verified)? Argue the side you find less
comfortable.

**2.** The Ariane 501 board found that the fatal conversion was in an alignment routine that 'serves no
purpose' after lift-off, kept running for forty seconds on a timing requirement inherited from
Ariane 4, and that the partners had 'jointly agreed not to include the Ariane 5 trajectory data
in the SRI requirements and specification' -- while the shutdown that killed both units was the
specified exception behaviour. The board still called the result 'a systematic software design
error.' Robodebt's income averaging likewise computed exactly what policy instructed. So: was
Ariane a code failure, a specification failure, or a reuse-without-revalidation failure -- and
for each answer, name the artifact a verification tool could have been pointed at.

**3.** ProPublica compared COMPAS against ground truth. Flores et al. argue the right comparison is the
judges COMPAS was meant to inform. If a tool is measurably biased but less biased than the
humans it displaces, is deploying it a harm? Who carries the burden of proof, the vendor or the
critic -- and does your answer change if the vendor's model is a trade secret?

**4.** Robodebt and the 2020 A-level standardisation used no machine learning, and Ofqual ran model
testing and a centre-level equalities analysis before choosing its approach. Does 'we specified
it, tested it, and wrote the analysis down' make those outcomes more defensible or less? Compare
with the Amazon hiring tool, which was scrapped before it ever decided anything.

**5.** Chouldechova and Hemel distinguish first- from second-order race consciousness in admissions
models. If a system never sees race but learns ZIP code, high school, and surname, has it
decided 'on the basis of race'? Would you give the same answer if the disparate effect ran in
the opposite direction, and what does that tell you about whether the objection is to the
mechanism or to the outcome?

## Why this is in a formal-methods course

Most of these cases fail somewhere other than implementation correctness: the Ariane 501 board
found the Ariane 5 trajectory data had been deliberately left out of the SRI requirements and
specification and that the offending routine ran on an inherited Ariane 4 timing requirement,
Robodebt's averaging computed precisely what policy instructed, and the Kleinberg/Chouldechova
results say the fairness specification students most want to write does not exist for any system
whose base rates differ across groups. Verification presupposes a specification, so the point of
this session is to make students feel the gap between 'the code is right' and 'the right thing
was built' before the course starts teaching them to discharge proof obligations. The exit
tickets sort the semester's cases into checkable and uncheckable properties, and that sorting is
the first specification-writing exercise rather than a rhetorical flourish.

## Readings

10 sources, 8 verified by direct fetch. One of them will be assigned to you; the rest are here if you want to go further, or if you want to check a claim someone makes in class.

- **Joy Buolamwini and Timnit Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," Proceedings of the 1st Conference on Fairness, Accountability and Transparency, PMLR vol. 81** (academic, 2018)  
  <https://proceedings.mlr.press/v81/buolamwini18a.html>  
  The audit that founded the field and the one most likely to be assigned to you (~15 pages,
  undergraduate-readable): error rates up to 34.7% for darker-skinned women against 0.8% for
  lighter-skinned men on three commercial APIs. It supports the claim that these systems fail
  unevenly across groups, but watch the scope — it measures gender classification, not
  identification.

- **Patrick Grother, Mei Ngan and Kayee Hanaoka, "Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects," NISTIR 8280, National Institute of Standards and Technology, December 2019** (report, 2019)  
  <https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf>  
  This one argues the other way. Across 189 algorithms from 99 developers and 18.27 million
  images, NIST confirms false-positive differentials of 10x to beyond 100x, but also finds the
  effect reversed on East Asian faces for a number of China-developed algorithms and that the
  most accurate algorithms produce the smallest differentials. Read only the four-page
  Executive Summary.

- **Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, "Machine Bias," ProPublica, 23 May 2016** (news, 2016)  
  <https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing>  
  The journalism that set the terms of the entire fairness debate (44.9% of Black defendants
  who did not reoffend were labelled higher risk against 23.5% of white defendants). It is
  also the specific claim the next two sources dispute, so read it before them; about 20
  minutes.

- **Anthony W. Flores, Kristin Bechtel and Christopher T. Lowenkamp, "False Positives, False Negatives, and False Analyses: A Rejoinder to 'Machine Bias: There's Software Used Across the Country to Predict Future Criminals. And It's Biased Against Blacks,'" Federal Probation 80(2), September 2016** (academic, 2016)  
  <https://www.uscourts.gov/sites/default/files/80_2_6_0.pdf>  
  The counterweight to ProPublica; read the two next to each other. It argues the analysis
  was methodologically unsound (COMPAS applied outside the post-disposition
  population it was built for, pretrial-only sample, unexplained exclusion of probation and
  parole subjects) and that the honest baseline is unstructured judicial judgment rather than
  perfection. Short and readable; the authors state they are not endorsing COMPAS.

- **Jon Kleinberg, Sendhil Mullainathan and Manish Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," arXiv:1609.05807** (academic, 2016)  
  <https://arxiv.org/abs/1609.05807>  
  The impossibility result in its strongest form: three fairness conditions cannot hold
  simultaneously except in highly constrained special cases. This is what makes the COMPAS
  dispute unresolvable rather than merely unresolved. Read the abstract and introduction
  only; the proofs are graduate-level.

- **Alexandra Chouldechova, "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments," Big Data 5(2):153-163, 2017 (preprint arXiv:1703.00056)** (academic, 2017)  
  <https://arxiv.org/abs/1703.00056>  
  The undergraduate-readable statement of the same impossibility (when base rates differ,
  equal predictive value and balanced error rates cannot both hold); if you read only one
  thing on the fairness mathematics, make it this. Under 30 minutes. Published venue
  confirmed via Crossref (DOI 10.1089/big.2016.0047); the arXiv page is the version I
  retrieved.

- **Nancy G. Leveson, "Medical Devices: The Therac-25," Appendix A of Safeware: System Safety and Computers (Addison-Wesley, 1995)** (academic, 1995)  
  <https://web.archive.org/web/20260820015352/http://sunnyday.mit.edu/papers/therac.pdf>  
  (MIT's copy at `sunnyday.mit.edu` stopped answering in August 2026; this is the Internet
  Archive's snapshot of the same PDF.)  
  The canonical body-count case, and the strongest rebuttal on this list to the 'find the
  bug' reflex: Leveson's argument is that removed hardware interlocks, software reused from
  machines whose hardware still backstopped it, unusable error reporting and the absence of
  independent review mattered more than any single race condition. 49 pages; read the
  introduction and the East Texas accidents. IMPORTANT: this is the Safeware appendix by
  Leveson alone, routinely miscited as the 1993 IEEE Computer article by Leveson and Turner.

- **Bates and Others v Post Office Ltd [2019] EWHC 3408 (QB), Judgment (No. 6) "Horizon Issues", Mr Justice Fraser, 16 December 2019** (legal, 2019)  
  <https://www.judiciary.uk/wp-content/uploads/2019/12/bates-v-post-office-judgment.pdf>  
  The rare case where 'is this software reliable?' was actually tried on evidence: Fraser J
  finds Legacy Horizon 'was not remotely robust' and a 'material risk of inaccuracy in branch
  accounts as a result of bugs, errors and defects,' while also finding the 2019 system far
  more robust. 313 pages; the parts you need are paragraphs 1-30 and the Horizon Issues
  answers (from para. 968).

- **Royal Commission into the Robodebt Scheme, Report (Commissioner Catherine Holmes), delivered 7 July 2023, Commonwealth of Australia** (primary, 2023) ⚠️ *not fetch-verified*  
  <https://robodebt.royalcommission.gov.au/publications/report>  
  NOT VERIFIED FROM THIS ENVIRONMENT: the Commission's CDN reset every connection I made
  (HTTP/1.1, HTTP/2, and the Wayback Machine all failed), so I am citing the official
  publication page without having retrieved the document. Existence, date and the
  Commissioner's description of the scheme as 'a crude and cruel mechanism, neither fair nor
  legal' were independently confirmed from the Australian Prime Minister's official statement
  of 7 July 2023 (https://www.pm.gov.au/media/final-report-royal-commission-robodebt-scheme),
  which I did fetch. About 1,000 pages in three volumes; read the report overview only.

- **Alexandra Chouldechova and Daniel J. Hemel, "Race-conscious admissions algorithms and the law," Proceedings of the National Academy of Sciences 123(30), 20 July 2026, DOI 10.1073/pnas.2509764123** (academic, 2026) ⚠️ *citation confirmed via DOI resolution — title, authors, journal, volume and date all match; full text not fetch-verified, PNAS 403s automated fetchers*  
  <https://doi.org/10.1073/pnas.2509764123>  
  NOT VERIFIED BY PAGE RETRIEVAL: pnas.org returns 403 to automated clients, so I confirmed
  title, both authors, venue, volume/issue, date and the full abstract from publisher-
  deposited Crossref metadata for this DOI rather than from the landing page. Substantively it
  is the source behind discussion question 5: it maps Students for Fair Admissions v.
  Harvard onto machine learning by distinguishing first- and second-order race consciousness
  at training and at prediction time, which turns 'the model never sees race' from a defence
  into a live legal question.

## What you submit

One paragraph, 150–250 words, by **Sat Sep 5, 11:59 p.m.**, to the `D2` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
