# D2 — A Survey of Harms: When Software and AI Hurt People

**Session 3 · Thu Sep 3 · week 2 · 30 minutes · think–pair–share**

## Framing

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

## Discussion questions

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

## Readings

10 sources, 8 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **Joy Buolamwini and Timnit Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," Proceedings of the 1st Conference on Fairness, Accountability and Transparency, PMLR vol. 81** (academic, 2018)  
  <https://proceedings.mlr.press/v81/buolamwini18a.html>  
  The audit that founded the field and the best candidate for the assigned reading (~15 pages,
  undergraduate-readable): error rates up to 34.7% for darker-skinned women against 0.8% for
  lighter-skinned men on three commercial APIs. Supports the framing's disparity claim, but
  note it measures gender classification, not identification.

- **Patrick Grother, Mei Ngan and Kayee Hanaoka, "Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects," NISTIR 8280, National Institute of Standards and Technology, December 2019** (report, 2019)  
  <https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf>  
  Cuts against the simple reading: across 189 algorithms from 99 developers and 18.27 million
  images, NIST confirms false-positive differentials of 10x to beyond 100x, but also finds the
  effect reversed on East Asian faces for a number of China-developed algorithms and that the
  most accurate algorithms produce the smallest differentials. Assign only the four-page
  Executive Summary.

- **Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, "Machine Bias," ProPublica, 23 May 2016** (news, 2016)  
  <https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing>  
  The journalism that set the terms of the entire fairness debate (44.9% of Black defendants
  who did not reoffend were labelled higher risk against 23.5% of white defendants), and the
  specific claim the next two references dispute; about 20 minutes to read.

- **Anthony W. Flores, Kristin Bechtel and Christopher T. Lowenkamp, "False Positives, False Negatives, and False Analyses: A Rejoinder to 'Machine Bias: There's Software Used Across the Country to Predict Future Criminals. And It's Biased Against Blacks,'" Federal Probation 80(2), September 2016** (academic, 2016)  
  <https://www.uscourts.gov/sites/default/files/80_2_6_0.pdf>  
  The required counterweight and the one to assign alongside ProPublica: argues the analysis
  was methodologically unsound (COMPAS applied outside the post-disposition population it was
  built for, pretrial-only sample, unexplained exclusion of probation and parole subjects) and
  that the honest baseline is unstructured judicial judgment rather than perfection. Short and
  readable; the authors state they are not endorsing COMPAS.

- **Jon Kleinberg, Sendhil Mullainathan and Manish Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," arXiv:1609.05807** (academic, 2016)  
  <https://arxiv.org/abs/1609.05807>  
  The impossibility result in its strongest form: three fairness conditions cannot hold
  simultaneously except in highly constrained special cases. This is what makes the COMPAS
  dispute unresolvable rather than merely unresolved. Assign the abstract and introduction
  only; the proofs are graduate-level.

- **Alexandra Chouldechova, "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments," Big Data 5(2):153-163, 2017 (preprint arXiv:1703.00056)** (academic, 2017)  
  <https://arxiv.org/abs/1703.00056>  
  The undergraduate-readable statement of the same impossibility (when base rates differ,
  equal predictive value and balanced error rates cannot both hold), and the paper to assign
  if you assign only one piece of fairness mathematics; under 30 minutes. Published venue
  confirmed via Crossref (DOI 10.1089/big.2016.0047); the arXiv page is the version I
  retrieved.

- **Nancy G. Leveson, "Medical Devices: The Therac-25," Appendix A of Safeware: System Safety and Computers (Addison-Wesley, 1995)** (academic, 1995)  
  <http://sunnyday.mit.edu/papers/therac.pdf>  
  The canonical body-count case, and the strongest rebuttal in the packet to the 'find the
  bug' reflex: Leveson's argument is that removed hardware interlocks, software reused from
  machines whose hardware still backstopped it, unusable error reporting and the absence of
  independent review mattered more than any single race condition. 49 pages; assign the
  introduction and the East Texas accidents. IMPORTANT: this is the Safeware appendix by
  Leveson alone, routinely miscited as the 1993 IEEE Computer article by Leveson and Turner.

- **Bates and Others v Post Office Ltd [2019] EWHC 3408 (QB), Judgment (No. 6) "Horizon Issues", Mr Justice Fraser, 16 December 2019** (legal, 2019)  
  <https://www.judiciary.uk/wp-content/uploads/2019/12/bates-v-post-office-judgment.pdf>  
  The rare case where 'is this software reliable?' was actually tried on evidence: Fraser J
  finds Legacy Horizon 'was not remotely robust' and a 'material risk of inaccuracy in branch
  accounts as a result of bugs, errors and defects,' while also finding the 2019 system far
  more robust. 313 pages; assign paragraphs 1-30 and the Horizon Issues answers (from para.
  968) only.

- **Royal Commission into the Robodebt Scheme, Report (Commissioner Catherine Holmes), delivered 7 July 2023, Commonwealth of Australia** (primary, 2023) ⚠️ *not fetch-verified*  
  <https://robodebt.royalcommission.gov.au/publications/report>  
  NOT VERIFIED FROM THIS ENVIRONMENT: the Commission's CDN reset every connection I made
  (HTTP/1.1, HTTP/2, and the Wayback Machine all failed), so I am citing the official
  publication page without having retrieved the document. Existence, date and the
  Commissioner's description of the scheme as 'a crude and cruel mechanism, neither fair nor
  legal' were independently confirmed from the Australian Prime Minister's official statement
  of 7 July 2023 (https://www.pm.gov.au/media/final-report-royal-commission-robodebt-scheme),
  which I did fetch. About 1,000 pages in three volumes; assign the report overview only.

- **Alexandra Chouldechova and Daniel J. Hemel, "Race-conscious admissions algorithms and the law," Proceedings of the National Academy of Sciences 123(30), 20 July 2026, DOI 10.1073/pnas.2509764123** (academic, 2026) ⚠️ *not fetch-verified*  
  <https://doi.org/10.1073/pnas.2509764123>  
  NOT VERIFIED BY PAGE RETRIEVAL: pnas.org returns 403 to automated clients, so I confirmed
  title, both authors, venue, volume/issue, date and the full abstract from publisher-
  deposited Crossref metadata for this DOI rather than from the landing page. Substantively it
  is the admissions reference the discussion needs: it maps Students for Fair Admissions v.
  Harvard onto machine learning by distinguishing first- and second-order race consciousness
  at training and at prediction time, which turns 'the model never sees race' from a defence
  into a live legal question.

## 30-minute run sheet

PREP: on the board draw two columns, 'adjudicated / countable' and 'contested / uncounted'. Have
an 11-line case card ready (project or print): Therac-25, Ariane 501, Knight Capital, 737 MAX,
Post Office Horizon, Robodebt, Dutch toeslagenaffaire, UK A-levels 2020, COMPAS, Gender Shades,
Amazon hiring tool -- one sentence each, no adjectives.

0:00-0:03 Instructor reads the framing aloud once, verbatim, and says nothing else. Hands out
the case card.

0:03-0:08 SILENT INDIVIDUAL THINK, written, no laptops. Each student picks the single case they
would call the worst harm and writes exactly two lines: (a) 'This is the worst because ___'; (b)
'A property that, if written down in advance, would have caught it: ___'. Instructor does not
circulate or comment.

0:08-0:10 Fast tally. Instructor reads the eleven case names; hands up once each; writes counts
on the board in BLACK. No discussion, no justification. 90 seconds, hard stop.

0:10-0:18 PAIR. Rule enforced by the instructor: you must pair with someone who chose a
different case. FALLBACK: Therac-25 will probably dominate the tally; if fewer than four cases
drew votes, the instructor assigns each pair a second case off the card so every pair still has
two to rank. Task: rank your two cases against each other and write down the ONE criterion that
decided it. Instructor circulates and writes overheard criteria in the margin -- expect
severity, number affected, reversibility, intent, foreseeability, whether anyone was held
liable, whether a specification existed. Instructor writes the criteria, not the verdicts.

0:18-0:20 Silent re-vote on the same eleven cases with the criteria now visible. Instructor
writes the new counts in RED next to the black ones. Do not explain the movement; let the two
colours sit there.

0:20-0:28 SHARE. Call on pairs by criterion, not by case: 'who decided on foreseeability?' --
take three, then 'who decided on whether anyone was held liable?' -- take two. Then put prompt 1
(impossibility) to the room and take two volunteers on opposite sides, three minutes total. Then
prompt 2 (Ariane and Robodebt: where exactly did the failure live?) and take two more. The
instructor does not adjudicate and does not summarise; if the room converges, the instructor
argues the vacated side. EXPECTED CHALLENGE: someone will point out that the Dutch
toeslagenaffaire is on the card, involved an automated risk-classification system, and destroyed
families -- which cuts directly against the framing's opening line. Take it, say so, and put it
on the board; the framing says 'almost every', and a student who punctures it in thirty seconds
has done the session's work for you.

0:28-0:30 CLOSE AND COLLECT. Exit ticket, collected at the door: 'Name one property from today's
cases you could state precisely enough for a machine to check, and one you could not. One
sentence each.' Instructor says only that these become the first specification-writing exercise,
and leaves the two-colour tally on the board for the next session.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

Do not assert any of the following from the front of the room.

1. 'Gender Shades proved face recognition misidentifies Black people.' It measured GENDER
CLASSIFICATION on three commercial APIs -- not one-to-one verification and not one-to-many
identification. The identification evidence is NISTIR 8280, and it is more textured: false-
positive differentials of 10x to beyond 100x, but reversed on East Asian faces for a number of
China-developed algorithms, larger for women than men but by less than the race effect, and
smallest in the most accurate algorithms. 'Bias is a property of face recognition' is not what
either document says.

2. 'COMPAS uses race as an input.' It does not, and ProPublica never claimed it did. The dispute
is about outcome measures, not features.

3. 'ProPublica proved COMPAS is racist' or 'Northpointe was debunked.' Both parties are
arithmetically correct about different quantities; that is the content of the impossibility
results. Flores, Bechtel and Lowenkamp raise concrete methodological objections (pretrial-only
sample, unexplained exclusion of probation and parole subjects, instrument used outside its
intended decision point). Present as unresolved, not as one side winning. If you quote
Northpointe's own rebuttal (Dieterich, Mendoza and Brennan, 2016) rather than paraphrasing
predictive parity, source that document directly -- it is not in this packet's verified set.

4. 'Dressel and Farid showed COMPAS is no better than untrained people on Mechanical Turk.'
Contested. That study (Science Advances, 2018) used a seven-feature subset, and Lin, Jung, Goel
and Skeem (Science Advances, 2020) argue the result is sensitive to the information and feedback
conditions. Flag as disputed; do not build an argument on it.

5. 'Amazon's AI rejected women's resumes.' Every specific detail traces to a single Reuters
story by Jeffrey Dastin (October 2018) built on anonymous sources. The tool was experimental,
reportedly never the operative screen, was never externally audited, and no artefact was ever
published. It is a single-weak-source claim, which is itself the useful teaching point -- do not
present it as an audited finding.

6. 'The 2020 A-level fiasco was an AI failure' / 'the mutant algorithm.' Ofqual's direct centre-
level performance approach was statistical standardisation over historical centre results and
prior attainment, not machine learning. 'Mutant algorithm' was a politician's phrase, not a
technical description. And Ofqual did run model testing and a centre-level equalities analysis
before selecting its approach, and set both out in its interim report -- the failure was not an
absence of testing, which is precisely why the case is hard. (The interim report itself appeared
at results time, so do not claim the analysis was published in advance.)

7. 'Robodebt was a software bug.' The finding was about a policy and legal choice -- raising
debts by averaging annual tax-office income across fortnights and reversing the onus onto
recipients -- not a coding defect. Also treat the human toll carefully: the harm is documented
and grave, but attributing specific deaths to the scheme is a causal claim the Commission
handled with care, and the instructor should not sharpen it.

8. 'Therac-25 was a race condition that killed six people.' Leveson's own argument is that
reducing it to one concurrency bug is the wrong lesson; she emphasises removed hardware
interlocks, software carried over from Therac-6/20 where hardware still backstopped it, unusable
error reporting, no independent review, and a manufacturer and regulator response that let it
recur. Her text describes six massive overdoses; the death count is variously given as three or
four depending on attribution, so do not state a crisp number.

9. 'Horizon was broken software that convicted hundreds.' Fraser J's findings are time-sliced:
Legacy Horizon 'was not remotely robust', HNG-X only slightly better, and the 2019 system
'relatively robust'. He found a material risk of inaccuracy in branch accounts from bugs, errors
and defects -- that is a finding about the system, not a per-claimant or per-conviction
attribution, which has been handled through separate appeals, the statutory inquiry and
subsequent legislation. Do not state a settled count of convictions caused by the software.

10. 'Knight Capital lost $440 million because of a bug.' The SEC order (Release 34-70694, 16 Oct
2013) describes controls failures: dead 'Power Peg' code left callable, a flag repurposed
instead of the old code deleted, a deployment that reached seven of eight servers with no
second-technician review and no written procedure requiring one, and 97 automated 'Power Peg
disabled' reject e-mails that were never designed as alerts and were not read. Note also that
the order states a loss of more than $460 million while $440 million circulates from Knight's
own disclosure -- say which document your number came from.

11. 'Vendor X's admissions or hiring tool is unbiased / bias-audited.' Claims of this form are
marketing unless a specific audit is public. Pyle and Andalibi (Proc. ACM Human-Computer
Interaction, CSCW, 2025) document exactly this gap between admissions-technology vendors'
claimed benefits and applicants' perceived harms. Relatedly, do not tell students that AI in
college admissions is currently 'illegal' or 'legal' -- Chouldechova and Hemel treat it as an
open question that courts have not yet resolved, and the U.S. disparate-impact regulatory
picture has been unstable enough that any confident statement of current law should be checked
against the date you are teaching.

12. 'Ariane 5 was a unit-conversion error' or 'Ariane 5 proves the code was fine and only the
spec was wrong.' The units story is the Mars Climate Orbiter. The Lions board found an Operand
Error converting a 64-bit float to a 16-bit signed integer in the horizontal-bias variable BH;
three of seven at-risk variables were left unprotected on a margin argument that 'in the case of
the variable BH turned out to be faulty'; the routine was still running forty seconds into
flight on an Ariane 4 timing requirement; and the board nonetheless called it 'a systematic
software design error.' The clean 'code correct, spec wrong' story is contestable on the board's
own text, which is why it makes a good prompt rather than a good assertion.

13. '737 MAX was a software bug' or 'MCAS was badly coded.' Do not say this. The contested
ground is requirements and safety assessment -- what the system was permitted to command, what
sensor input it was allowed to rely on, what crew recognition and response was assumed -- and
the certification and delegation process around them. Specific hazard classifications, assumed
response times and delegation details are matters of record in the accident and congressional
reports; cite whichever report you use rather than asserting them from memory. No 737 MAX
document is in this packet's verified set.

14. 'An algorithm brought down the Dutch government.' The Rutte cabinet did resign in January
2021 over the childcare-benefits affair, but the findings faulted institutional conduct across
the tax administration, the courts and parliament, with the risk-classification system one
component of a much larger failure. The verified narrow claim is that nationality was used as a
risk factor in assessing benefit applications (Amnesty International, 'Xenophobic Machines:
Discrimination through unregulated use of algorithms in the Dutch childcare benefits scandal',
EUR 35/4686/2021, 25 October 2021 -- fetched and confirmed, but not in the reference list
above). If you want to call the system 'self-learning' or 'machine learning', source that
separately; this packet did not verify it.

15. Selection bias in the survey itself. Any list of harms, this one included, is a convenience
sample of incidents that were noticed, litigated, or reported in English. Do not let the class
treat the absence of a case from the list as evidence that no harm occurred there.
