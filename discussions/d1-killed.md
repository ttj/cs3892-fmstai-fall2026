# D1 — Has AI Ever Killed Anyone? Cause, Contribution, and the Limits of Attribution

**Session 1 · Thu Aug 27 · week 1 · 30 minutes · think–pair–share**

## Framing

> On 18 March 2018 an Uber test vehicle struck and killed Elaine Herzberg in Tempe. The NTSB found
> that the automated driving system detected her 5.6 seconds before impact, never once classified
> her as a pedestrian, and then suppressed its own braking for a full second — not as a bug, but
> exactly as designed, while it waited for a human to take over. The Board's probable cause names
> the safety driver, not the software. So: did the AI kill her, did Uber, did the operator — or is
> "kill" simply the wrong verb to attach to a specification?

## Why this is in a formal-methods course

Every case in this packet is a specification story, and they fail at different layers. The Uber
ADS did not violate its specification — action suppression was designed behavior — but the
specification had a hole: "the system design did not include consideration for jaywalking
pedestrians," and tracking history was discarded whenever an object was reclassified, so no
amount of proving that the code refines the spec would have found it; MCAS is the adjacent
failure, where the software was retargeted from high-speed windup turns to low-speed pitch-up
while the safety assessment stayed where it was. That gap — between "the implementation refines
the specification" and "the specification refines the world" — is the spine of this course, and
it is why the chatbot and sepsis cases are the hardest of all: for those, nobody has written the
safety property down in the first place.

## Discussion questions

**1.** NTSB put probable cause on the Uber safety driver's phone use and listed the company's safety
culture as merely 'contributing.' NHTSA, looking at a structurally identical arrangement at
Tesla — a supervising human, permissive automation — landed on a defect finding in the driver-
engagement design. Same shape, opposite attribution. Which agency drew the line in the right
place, and what principle separates 'the human failed' from 'the design made human failure
predictable'?

**2.** Leveson argues that attributing a single cause to an accident is usually a serious mistake. If
she is right, 'did AI kill anyone' may have no answer even in principle. Does the system-
accident view dissolve responsibility or merely relocate it — and would you accept it as a
defense if Character Technologies offered it to a jury?

**3.** Therac-25 and MCAS killed people through code where every behavior was, at least in principle,
written down somewhere by someone. The chatbot cases involve outputs that no line of code
specifies and no engineer intended or foresaw. Which is harder to hold a person responsible for
— and does 'AI' name a genuinely new kind of killing, or just a new place for an old one to
hide?

**4.** Waymo's own peer-reviewed data reports 80% fewer injury crashes over 7.1 million miles, while
RAND's arithmetic says you would need 275 million failure-free miles before you could say
anything statistically about fatalities at all. So a deployed system may be saving lives nobody
can prove it saved while causing deaths that make the evening news. On what evidence, short of
the impossible number, should a regulator let it drive — and does your answer change if the
bargain is 'fewer deaths overall, but some new deaths a human driver would never have caused'?

**5.** Hundreds of hospitals ran the Epic sepsis model on a vendor-claimed AUC that independent
validation cut to 0.63, and no peer-reviewed source attributes a single death to it. Is 'no
attributable death' evidence that the model was harmless, or evidence that we possess no
instrument capable of detecting the harm? What would have to appear on a death certificate
before a model counts as having killed someone?

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **National Transportation Safety Board, "Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian, Tempe, Arizona, March 18, 2018," Highway Accident Report NTSB/HAR-19/03 (adopted 19 Nov 2019)** (primary, 2019)  
  <https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf>  
  The anchor document, and the one that cuts hardest against the framing's apparent thrust:
  the Board's probable cause is the operator's cell-phone distraction, with Uber ATG's safety
  culture only 'contributing' — even though the same report documents that the ADS 'never
  classified her as a pedestrian,' discarded tracking history on every reclassification, and
  initiated a designed 1-second 'action suppression' of braking. 78 pp: assign only the
  probable-cause statement (p. v) and §§1.5.5.3 and 1.5.6.1 (~8 pp, 25 min).

- **NHTSA Office of Defects Investigation, "Additional Information Regarding EA22002" (closing summary of the Tesla Autopilot engineering analysis), 25 April 2024** (primary, 2024)  
  <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf>  
  The agency's own account: 956 crashes reviewed, of which 211 frontal-plane crashes produced
  13 fatal crashes, 14 deaths and 49 injuries, and a finding that Tesla is an 'industry
  outlier in its approach to L2 technology by mismatching a weak driver engagement system with
  Autopilot's permissive operating capabilities.' Supports 'the design contributed' — but note
  ODI's own counterfactual, that those crashes 'would have been avoidable by attentive
  drivers,' pushes back the other way. ~11 pp; the best single undergraduate reading in the
  packet (20 min).

- **Joint Authorities Technical Review (JATR), "Boeing 737 MAX Flight Control System: Observations, Findings, and Recommendations," submitted to the FAA, 11 October 2019** (primary, 2019)  
  <https://www.faa.gov/sites/faa.gov/files/2021-08/Final_JATR_Submittal_to_FAA_Oct_2019.pdf>  
  The non-AI control case, and it refutes the lazy version of its own moral. JATR found MCAS
  'was not evaluated as a complete and integrated function in the certification documents' and
  rested on 'data, architecture, and assumptions that were reused from a previous aircraft
  configuration' — i.e. specification drift, not a system faithfully executing an analyzed
  spec. 71 pp: assign the cover letter (2 pp, which contains the 'evolution of MCAS from a
  relatively benign system to a much more aggressive system' passage) and Section 6 (~2 pp).

- **Nancy G. Leveson and Clark S. Turner, "An Investigation of the Therac-25 Accidents," IEEE Computer 26(7):18–41, July 1993 (doi:10.1109/MC.1993.274940)** (academic, 1993)  
  <https://www.se.rit.edu/~swen-342/resources/Leveson,%20Turner%20-%20An%20Investigation%20of%20the%20Therac-25%20Accidents%20-%20IEEE%20Computer%20v26n7%20-%201993-07.pdf>  
  The founding software-kills case — 'six known accidents involved massive overdoses' between
  June 1985 and January 1987, three documented deaths — and the source of the sentence the
  entire discussion turns on: 'To attribute a single cause to an accident is usually a serious
  mistake.' It cuts against every clean single-cause story students will bring, in both
  directions. 24 pp; assign pp. 18–24 plus the 'Causal factors' and 'Software engineering'
  subsections (~30 min). URL is a university mirror of the IEEE article.

- **Order on Motions to Dismiss, Garcia v. Character Technologies, Inc., No. 6:24-cv-1903-ACC-UAM (M.D. Fla.), Doc. 115, Conway, J., signed 20 May 2025 / filed 21 May 2025** (legal, 2025)  
  <https://storage.courtlistener.com/recap/gov.uscourts.flmd.433581/gov.uscourts.flmd.433581.115.0.pdf>  
  The court's own text rather than press coverage of it. Judge Conway wrote that she is 'not
  prepared to hold that Character A.I.'s output is speech,' and that 'Character A.I. is a
  product ... so far as Plaintiff's claims arise from defects in the Character A.I. app rather
  than ideas or expressions within the app'; IIED was dismissed without leave to amend and
  everything else survived. It also states outright that the facts 'are taken as true for the
  purposes of this Order' — so it supports 'courts are starting to treat models as products'
  while flatly undercutting 'a court found the chatbot killed him.' 49 pp; assign the First
  Amendment and 'product' sections (~12 pp).

- **Complaint, Raine v. OpenAI, Inc. and Samuel Altman, Superior Court of California, County of San Francisco, filed 26 August 2025 (Edelson PC / Tech Justice Law Project)** (legal, 2025)  
  <https://www.courthousenews.com/wp-content/uploads/2025/08/raine-vs-openai-et-al-complaint.pdf>  
  Seven causes of action arising from a 16-year-old's suicide, and — as of this packet — no
  ruling of any kind. The pedagogical point of assigning it next to the Garcia order is to
  make the difference between a pleading and a finding visible: the chat excerpts quoted
  everywhere in the press are exhibits to this document, not adjudicated facts. ~40 pp; skim
  the causes of action only (20 min).

- **Andrew Wong et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," JAMA Internal Medicine 181(8):1065–1070 (2021), doi:10.1001/jamainternmed.2021.2626** (academic, 2021)  
  <https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307>  
  AUC of 0.63 (95% CI 0.62–0.64) across 38,455 hospitalizations against the developer's
  reported 0.76–0.83, with 8 patients needing evaluation per sepsis case identified. Equally
  important for this discussion: it attributes no death to the model anywhere. Supports
  'deployment far outran validation' while refusing 'medical AI killed people.' 6 pp — the
  shortest and easiest reading here (15 min).

- **UN Security Council, Letter dated 8 March 2021 from the Panel of Experts on Libya established pursuant to resolution 1973 (2011), S/2021/229, paragraph 63** (primary, 2021)  
  <https://digitallibrary.un.org/record/3905159/files/S_2021_229-EN.pdf>  
  The actual text behind the endlessly repeated 'first AI kill.' Paragraph 63 says only that
  lethal autonomous weapons systems such as the STM Kargu-2 'were programmed to attack targets
  without requiring data connectivity between the operator and the munition: in effect, a true
  "fire, forget and find" capability' — a statement about capability, with no casualty
  attributed to autonomous engagement. Squarely against the framing's apparent thrust. 548 pp;
  assign paragraph 63 only (2 minutes).

- **Kristofer D. Kusano, John M. Scanlon, Yin-Hsiu Chen, Timothy L. McMurry, Ruoshu Chen, Tilia Gode, Trent Victor, "Comparison of Waymo rider-only crash data to human benchmarks at 7.1 million miles," Traffic Injury Prevention 25(sup1):S66–S77 (2024), doi:10.1080/15389588.2024.2380786** (academic, 2024)  
  <https://pubmed.ncbi.nlm.nih.gov/39485678/>  
  The strongest published 'automation reduces harm' result: 7.14 million rider-only miles,
  0.60 vs 2.80 any-injury-reported crashes per million miles (−80%) and 2.1 vs 4.68 police-
  reported (−55%). Two caveats the instructor must say aloud: every author is a Waymo
  employee, and the dataset contains no fatalities at all, so it is statistically silent on
  the question this class is actually asking. Verified via the PubMed record (abstract free;
  the full article is paywalled at Taylor & Francis).

- **Nidhi Kalra and Susan M. Paddock, "Driving to Safety: How Many Miles of Driving Would It Take to Demonstrate Autonomous Vehicle Reliability?" RAND Corporation, RR-1478-RC (2016)** (report, 2016)  
  <https://www.rand.org/content/dam/rand/pubs/research_reports/RR1400/RR1478/RAND_RR1478.pdf>  
  275 million failure-free miles — roughly 12.5 years under aggressive assumptions — merely to
  show a fatality rate better than the human 1.09 per 100 million miles, and 'billions to
  hundreds of billions of miles' to demonstrate small improvements. It cuts against both sides
  at once: neither the vendors claiming lives saved nor the critics counting deaths have the
  miles to support a statistical claim. Free PDF, 15 pp (25 min). Note: rand.org blocks some
  command-line fetchers; it opens normally in a browser.

## 30-minute run sheet

MATERIALS (prepare before class): one half-sheet per student, printed with (a) the three verdict
labels, (b) a six-case fact strip, (c) two blank lines. Board divided into six labeled columns,
one per case.

FACT STRIP (print verbatim so the think phase is spent judging, not recalling): THERAC-25 — six
massive-overdose accidents 1985-87, three deaths, no learned component; two known defects (a
race condition, a counter overflow), three accidents whose cause is undeterminable. MCAS — two
crashes, 346 deaths; software retargeted from high-speed windup turns to low-speed pitch-up
while the safety assessment was not updated. UBER / HERZBERG — detected 5.6 s out, never
classified as a pedestrian, 1 s of braking suppressed by design, no alert to the operator; NTSB
probable cause = the operator's phone. TESLA AUTOPILOT — NHTSA: 211 frontal-plane crashes, 13
fatal, 14 deaths; hazard visible >=5 s in 59 of 109 measurable cases; 'would have been avoidable
by attentive drivers.' CHARACTER.AI / SETZER — one death; a court has allowed product-liability
claims past a motion to dismiss while expressly taking all facts as alleged. EPIC SEPSIS MODEL —
deployed at hundreds of hospitals; external AUC 0.63 vs vendor 0.76-0.83; zero deaths attributed
in any peer-reviewed source.

0:00-3:00 FRAMING. Read the framing aloud, verbatim, and stop. Write the three verdict labels on
the board: (A) the software killed, (B) the software contributed, (C) the software is not the
right subject of that sentence. Do not define them further — the ambiguity is the exercise. Hand
out half-sheets.

3:00-9:00 THINK, SILENT. Each student assigns exactly one label to each of the six cases, then
writes one sentence defending their most confident call and one sentence naming the call they
are least sure of. Nothing is collected yet. Instructor stays silent and does not circulate
answering questions; if asked "what counts as contributed?", answer only "that's what you're
deciding."

9:00-17:00 PAIR. Pairs must produce a single joint ranking of all six cases, from "most
defensible to say AI killed" to "least." One ordering per pair, no ties. Where they cannot
agree, they write one line: "we split because ___." Announce at 14:00 that they have four
minutes and must have an ordering, split lines and all.

17:00-19:00 BOARD. Ask only two questions by show of hands: "who has Therac-25 at #1?" and "who
has Character.AI at #1?" Tally both under the case columns. Then ask for the split lines out
loud and write the recurring ones — expect variants of "she was jaywalking," "the driver was on
her phone," "nobody wrote a spec for a chatbot" — in a running list to the side. This list is
the real artifact of the session.

19:00-27:00 SHARE. Cold-call three pairs, chosen for maximum disagreement, in this order: a pair
that ranked Uber high, a pair that ranked Uber low, and any pair whose split line mentioned the
safety driver. After the third, read aloud exactly two sentences and nothing more — the NTSB
probable cause ("the failure of the vehicle operator to monitor the driving environment ...
because she was visually distracted throughout the trip by her personal cell phone"), and the
JATR line about "designing software for one scenario ... and then modifying the software for a
different scenario." Then ask: "does either sentence move your ordering, and if so which
direction?" Take two responses, no more. Do not adjudicate.

27:00-30:00 CLOSE. Write four words on the board: SPECIFICATION / IMPLEMENTATION / DEPLOYMENT /
ATTRIBUTION. Each student writes on the back of their half-sheet which of the four layers their
#1 case actually failed at, in one sentence. Collect the half-sheets at the door, ungraded.
Announce that these seed the next lecture on refinement and assume-guarantee reasoning, and that
the class will revisit whether verification could have caught any of the six. Do not offer a
correct ranking, and do not summarize the discussion — leave the disagreement standing.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

DO NOT ASSERT THESE FROM THE FRONT OF THE ROOM.

1. "A Kargu-2 autonomously killed people in Libya in 2020 — the first AI kill." S/2021/229 para
63 says only that such systems "were programmed to attack targets without requiring data
connectivity between the operator and the munition: in effect, a true 'fire, forget and find'
capability." That is a statement about capability. The report attributes no death to autonomous
target selection and does not say a machine chose a human target on its own. The NPR/Bulletin-
of-the-Atomic-Scientists coverage that popularized "first AI kill" outran the document; the
Bulletin's own headline hedged ("quite possibly").

2. "Autopilot is ~10x safer than a human driver." This traces to Tesla's own Quarterly Vehicle
Safety Report, not to any regulator or peer-reviewed study. Autopilot miles are overwhelmingly
divided highway; the human baseline is all road types. No matching for road class, weather, time
of day, driver age, or vehicle age, and Tesla changed its own denominator definitions across
quarters. Vendor marketing — do not cite it.

3. The mirror-image error: "NHTSA found Autopilot defective, so Autopilot killed 14 people."
ODI's defect finding is specifically about the driver-engagement design — Tesla "mismatching a
weak driver engagement system with Autopilot's permissive operating capabilities" — and ODI's
own counterfactual is that those crashes "would have been avoidable by attentive drivers." The
14 deaths sit inside the 211-crash frontal-plane subset where Autopilot was alleged to be
engaged. Structurally the same attribution problem as Uber, pointed the other way.

4. "The Epic sepsis model killed patients." No peer-reviewed source attributes a death to it.
Wong et al. establishes poor discrimination (AUC 0.63) and heavy alert burden, and that the
developer's 0.76-0.83 figure did not replicate — and that figure itself comes from vendor
documentation, not a published external validation. The defensible sentence is "deployed at
scale on unvalidated performance claims," not "killed."

5. "MCAS did exactly what it was specified to do." The interesting half of this is false. MCAS
as shipped — single AoA input, repeated activation, expanded authority — had drifted from the
configuration the safety analysis covered. JATR: it "was not evaluated as a complete and
integrated function in the certification documents" and reused "data, architecture, and
assumptions ... from a previous aircraft configuration." Spec drift, not faithful execution of
an analyzed spec.

6. "A court found Character.AI responsible for Sewell Setzer's death." No court has found
anything of the sort. Judge Conway's order states that "Plaintiff's facts and allegations are
taken as true for the purposes of this Order." She declined to hold at that stage that
Character.AI's output is speech and held the app is a product only "so far as Plaintiff's claims
arise from defects in the Character A.I. app rather than ideas or expressions within the app."
Raine v. OpenAI has no ruling at all — every statement drawn from it must be "plaintiffs
allege," including the widely reproduced chat excerpts, which are exhibits to a complaint.

7. "Chatbots will tell a suicidal teenager how to die." McBain et al., Psychiatric Services
76(11):944-950 (2025), doi:10.1176/appi.ps.20250086, tested three chatbots on 30 expert-risk-
rated questions, 100 repetitions each: ChatGPT and Claude gave direct responses 0% of the time
to very-high-risk queries (and 100% to very-low-risk); Gemini was more variable. The real,
narrower finding is that none of them "meaningfully distinguish among intermediate risk levels."
State that, not the blanket claim.

8. "The Uber safety driver was watching The Voice on Hulu." The show title comes from Tempe PD,
not NTSB; the Board's own finding is that phone records show she was streaming a television show
via an app and that she was visually distracted by her personal cell phone. Related: do not say
she "disabled the Volvo AEB." The factory ADAS "was designed to deactivate during ADS testing" —
an Uber ATG design decision, which NTSB criticized as removing "a layer of safety redundancy."

9. "Therac-25 was a race condition." Partly. The race condition explains the Tyler accidents;
the second Yakima accident had a different cause (a counter overflow). Leveson and Turner state
plainly that the causes of the Kennestone, Hamilton and first Yakima accidents cannot be
determined. Also handle the death count carefully: three deaths are documented, one of them a
man already terminally ill whose survivors alleged only that he "died sooner than he would
have."

10. Aggregate "AI has killed N people" counts from incident trackers (AI Incident Database,
tesladeaths.com and similar) are compilations of press reports with no adjudicated causation and
heavy double-counting risk. Useful for finding cases; not usable as a number.
