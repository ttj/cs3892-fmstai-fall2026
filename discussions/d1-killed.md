# D1 — Has AI Ever Killed Anyone? Cause, Contribution, and the Limits of Attribution

**Session 1 · Thu Aug 27 · week 1 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Sat Aug 29, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### What happened

At 9:58 p.m. on 18 March 2018, a modified 2017 Volvo XC90 struck and killed Elaine Herzberg, 49, as she pushed a bicycle midblock across N. Mill Avenue in Tempe, Arizona. Uber Technologies' Advanced Technologies Group (ATG) had fitted it with an experimental **automated driving system** (ADS) — software that steers, accelerates, and brakes on its own. The ADS was driving; a 44-year-old Uber employee sat in the driver's seat as a "vehicle operator," to watch the road and take over in emergencies.

### What the investigation found

The National Transportation Safety Board (NTSB), which investigates crashes but assigns no fault, reconstructed the final seconds from Uber's logs.

Radar detected Herzberg 5.6 seconds before impact and labeled her *vehicle*; the software then relabeled her — *other* (unknown), *vehicle*, *bicycle*. It never classified her as a pedestrian: "the system design did not include consideration for jaywalking pedestrians." On each reclassification the ADS discarded its **tracking history** — where the object had been — and re-predicted her path from scratch.

At 1.2 seconds it finally put her in the car's lane and registered an emergency. It did not brake. It began **action suppression**: a designed one-second window in which braking is withheld while the system verifies the hazard or the operator intervenes, added so false alarms would not cause violent maneuvers. No alert went to the operator. A second later the hazard remained; by design the ADS still did not brake hard, only alerting the operator and slowing gradually. The operator, who spent 34 percent of her moving time looking at a phone streaming a television show, took the wheel 0.02 seconds before impact, at 39 mph.

NTSB's *probable cause* — a statutory finding, not a criminal charge — was "the failure of the vehicle operator to monitor the driving environment ... because she was visually distracted throughout the trip by her personal cell phone." Uber ATG's safety culture was listed only as contributing. It also found an attentive operator "would likely have had sufficient time" to avoid the crash.

### Why it still matters

In March 2019 Arizona prosecutors found "no basis for criminal liability" for Uber. Safety driver Rafaela Vasquez was indicted for negligent homicide in September 2020, pleaded guilty in July 2023 to a lesser charge of endangerment, and got three years' probation. No engineer or executive was charged. Uber later changed the ADS to keep tracking history across reclassifications, brake hard for mitigation, and leave Volvo's emergency braking on; NTSB asked NHTSA to require developer safety self-assessments.

**Therac-25**: six patients received massive radiation overdoses between June 1985 and January 1987 from a machine that relied on software where earlier models had hardware interlocks; three died. **Tesla**: closing its Autopilot investigation in April 2024, NHTSA found 211 crashes where a Tesla's front struck something in its path (13 fatal, 14 deaths) and called Tesla an "industry outlier ... mismatching a weak driver engagement system with Autopilot's permissive operating capabilities." Note what the agency did *not* do: it issued no defect determination. Tesla had filed the recall (23V838) itself in December 2023, and NHTSA closed the investigation on the strength of it. Note too that those crashes "would have been avoidable by attentive drivers." **Chatbots**: in *Garcia v. Character Technologies*, after 14-year-old Sewell Setzer III's death, a federal judge in May 2025 let claims proceed treating the app as a defective product and declined to hold its output protected speech — while taking the plaintiff's account "as true for the purposes of this Order." Nothing has been proved.

### Timeline

| When | What |
|---|---|
| June 1985 – January 1987 | Six patients receive massive radiation overdoses from AECL's software-controlled Therac-25 radiotherapy machine; three die. The machine is recalled in 1987 for design changes, including hardware safeguards against software errors. |
| 18 March 2018 | An Uber ATG test vehicle — a modified 2017 Volvo XC90 under automated control — strikes and kills Elaine Herzberg, 49, on N. Mill Avenue in Tempe, Arizona. |
| March 2019 | The Yavapai County Attorney concludes there is "no basis for criminal liability" against Uber, and refers the safety driver's conduct back for further investigation. |
| 19 November 2019 | NTSB adopts HAR-19/03. Probable cause: the vehicle operator's failure to monitor the road while visually distracted by her personal cell phone. Uber ATG's safety culture is listed only as contributing. |
| September 2020 | A Maricopa County grand jury indicts safety driver Rafaela Vasquez on one count of negligent homicide. |
| July 2023 | Vasquez pleads guilty to one count of endangerment, a reduced charge, and is sentenced to three years' probation. |
| 25 April 2024 | NHTSA closes its Tesla Autopilot engineering analysis (EA22002): 956 crashes reviewed, 211 frontal-plane crashes, 13 fatal, 14 deaths; ODI calls Tesla an "industry outlier" in driver engagement. No defect determination is issued — Tesla had filed Recall 23V838 in December 2023, and ODI closes on that basis while opening a recall query (RQ24009) to test the remedy. |
| 21 May 2025 | In Garcia v. Character Technologies, a federal judge lets product-liability claims proceed and declines to hold that chatbot output is protected speech — while expressly taking all of the plaintiff's facts as alleged. |

## The question

> On 18 March 2018 an Uber test vehicle struck and killed Elaine Herzberg in Tempe. The NTSB found
> that the automated driving system detected her 5.6 seconds before impact, never once classified
> her as a pedestrian, and then suppressed its own braking for a full second — not as a bug, but
> exactly as designed, while it waited for a human to take over. The Board's probable cause names
> the safety driver, not the software. So: did the AI kill her, did Uber, did the operator — or is
> "kill" simply the wrong verb to attach to a specification?

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

**1.** NTSB put probable cause on the Uber safety driver's phone use and listed the company's safety
culture as merely 'contributing.' NHTSA, looking at a structurally identical arrangement at
Tesla — a supervising human, permissive automation — pointed at the driver-
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

## Readings

10 sources, 10 verified by direct fetch. You will be assigned one; the rest are here if you want to go further, or if you want to check a claim that gets made in the room.

- **National Transportation Safety Board, "Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian, Tempe, Arizona, March 18, 2018," Highway Accident Report NTSB/HAR-19/03 (adopted 19 Nov 2019)** (primary, 2019)  
  <https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf>  
  The anchor document, and the one that argues hardest against blaming the software: the
  Board's probable cause is the operator's cell-phone distraction, with Uber ATG's safety
  culture only 'contributing' — even though the same report documents that the ADS 'never
  classified her as a pedestrian,' discarded tracking history on every reclassification, and
  initiated a designed 1-second 'action suppression' of braking. It runs 78 pp, but the part
  you need is the probable-cause statement (p. v) and §§1.5.5.3 and 1.5.6.1 (~8 pp, 25 min).

- **NHTSA Office of Defects Investigation, "Additional Information Regarding EA22002" (closing summary of the Tesla Autopilot engineering analysis), 25 April 2024** (primary, 2024)  
  <https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf>  
  The agency's own account: 956 crashes reviewed, of which 211 frontal-plane crashes produced
  13 fatal crashes, 14 deaths and 49 injuries, and a finding that Tesla is an 'industry
  outlier in its approach to L2 technology by mismatching a weak driver engagement system with
  Autopilot's permissive operating capabilities.' It supports 'the design contributed' — but
  watch ODI's own counterfactual, that those crashes 'would have been avoidable by attentive
  drivers,' which pushes back the other way. 6 pp, 15 min; if you read only one thing on this
  list, make it this one.

- **Joint Authorities Technical Review (JATR), "Boeing 737 MAX Flight Control System: Observations, Findings, and Recommendations," submitted to the FAA, 11 October 2019** (primary, 2019)  
  <https://www.faa.gov/sites/faa.gov/files/2021-08/Final_JATR_Submittal_to_FAA_Oct_2019.pdf>  
  The non-AI control case, and it undercuts the easy version of its own moral. JATR found MCAS
  'was not evaluated as a complete and integrated function in the certification documents' and
  rested on 'data, architecture, and assumptions that were reused from a previous aircraft
  configuration' — i.e. specification drift, not a system faithfully executing an analyzed
  spec. It runs 71 pp; read the cover letter (2 pp, which contains the 'evolution of MCAS from
  a relatively benign system to a much more aggressive system' passage) and Section 6 (~2 pp).

- **Nancy G. Leveson and Clark S. Turner, "An Investigation of the Therac-25 Accidents," IEEE Computer 26(7):18–41, July 1993 (doi:10.1109/MC.1993.274940)** (academic, 1993)  
  <https://www.se.rit.edu/~swen-342/resources/Leveson,%20Turner%20-%20An%20Investigation%20of%20the%20Therac-25%20Accidents%20-%20IEEE%20Computer%20v26n7%20-%201993-07.pdf>  
  The founding software-kills case — 'six known accidents involved massive overdoses' between
  June 1985 and January 1987, three documented deaths — and the source of the sentence the
  entire discussion turns on: 'To attribute a single cause to an accident is usually a serious
  mistake.' It cuts, in both directions, against every clean single-cause story it is tempting
  to tell. 24 pp; read pp. 18–24 plus the 'Causal factors' and 'Software engineering'
  subsections (~30 min). URL is a university mirror of the IEEE article.

- **Order on Motions to Dismiss, Garcia v. Character Technologies, Inc., No. 6:24-cv-1903-ACC-UAM (M.D. Fla.), Doc. 115, Conway, J., signed 20 May 2025 / filed 21 May 2025** (legal, 2025)  
  <https://storage.courtlistener.com/recap/gov.uscourts.flmd.433581/gov.uscourts.flmd.433581.115.0.pdf>  
  The court's own text rather than press coverage of it. Judge Conway wrote that she is 'not
  prepared to hold that Character A.I.'s output is speech,' and that 'Character A.I. is a
  product ... so far as Plaintiff's claims arise from defects in the Character A.I. app rather
  than ideas or expressions within the app'; IIED was dismissed without leave to amend and
  everything else survived. It also states outright that the facts 'are taken as true for the
  purposes of this Order' — so it supports 'courts are starting to treat models as products'
  while flatly undercutting 'a court found the chatbot killed him.' 49 pp; read the First
  Amendment and 'product' sections (~12 pp).

- **Complaint, Raine v. OpenAI, Inc. and Samuel Altman, Superior Court of California, County of San Francisco, filed 26 August 2025 (Edelson PC / Tech Justice Law Project)** (legal, 2025)  
  <https://www.courthousenews.com/wp-content/uploads/2025/08/raine-vs-openai-et-al-complaint.pdf>  
  Seven causes of action arising from a 16-year-old's suicide, and — as of this writing — no
  ruling of any kind. Read it next to the Garcia order and the difference between a pleading
  and a finding becomes visible: the chat excerpts quoted everywhere in the press are exhibits
  to this document, not adjudicated facts. ~40 pp; skim the causes of action only (20 min).

- **Andrew Wong et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," JAMA Internal Medicine 181(8):1065–1070 (2021), doi:10.1001/jamainternmed.2021.2626** (academic, 2021)  
  <https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307>  
  AUC of 0.63 (95% CI 0.62–0.64) across 38,455 hospitalizations against the developer's
  reported 0.76–0.83, with 8 patients needing evaluation per sepsis case identified. Equally
  important here: it attributes no death to the model anywhere. It supports 'deployment far
  outran validation' while refusing 'medical AI killed people.' 6 pp — the shortest and
  easiest reading on this list (15 min).
  **Read the correction with it.** *Errors in Table 2 and Results*, JAMA Internal Medicine
  181(8):1144, doi:10.1001/jamainternmed.2021.3907 — "the number needed to evaluate that is
  presented in Table 2 and the Results should be **8, not 15**." The figure quoted above is the
  corrected one; the version of Table 2 you will see if you skim the original PDF is not. That
  is worth two minutes of your attention in a course about the difference between a number that
  is checked and a number that is repeated.

- **UN Security Council, Letter dated 8 March 2021 from the Panel of Experts on Libya established pursuant to resolution 1973 (2011), S/2021/229, paragraph 63** (primary, 2021)  
  <https://digitallibrary.un.org/record/3905159/files/S_2021_229-EN.pdf>  
  The actual text behind the endlessly repeated 'first AI kill.' Paragraph 63 says only that
  lethal autonomous weapons systems such as the STM Kargu-2 'were programmed to attack targets
  without requiring data connectivity between the operator and the munition: in effect, a true
  "fire, forget and find" capability' — a statement about capability, with no casualty
  attributed to autonomous engagement. This one argues the other way. 548 pp; read paragraph
  63 only (2 minutes).

- **Kristofer D. Kusano, John M. Scanlon, Yin-Hsiu Chen, Timothy L. McMurry, Ruoshu Chen, Tilia Gode, Trent Victor, "Comparison of Waymo rider-only crash data to human benchmarks at 7.1 million miles," Traffic Injury Prevention 25(sup1):S66–S77 (2024), doi:10.1080/15389588.2024.2380786** (academic, 2024)  
  <https://pubmed.ncbi.nlm.nih.gov/39485678/>  
  The strongest published 'automation reduces harm' result: 7.14 million rider-only miles,
  0.60 vs 2.80 any-injury-reported crashes per million miles (−80%) and 2.1 vs 4.68 police-
  reported (−55%). Two caveats to carry with those numbers: every author is a Waymo employee,
  and the dataset contains no fatalities at all, so it is statistically silent on the question
  this discussion is actually asking. Verified via the PubMed record (abstract free; the full
  article is paywalled at Taylor & Francis).

- **Nidhi Kalra and Susan M. Paddock, "Driving to Safety: How Many Miles of Driving Would It Take to Demonstrate Autonomous Vehicle Reliability?" RAND Corporation, RR-1478-RC (2016)** (report, 2016)  
  <https://www.rand.org/content/dam/rand/pubs/research_reports/RR1400/RR1478/RAND_RR1478.pdf>  
  275 million failure-free miles — roughly 12.5 years under aggressive assumptions — merely to
  show a fatality rate better than the human 1.09 per 100 million miles, and 'billions to
  hundreds of billions of miles' to demonstrate small improvements. It cuts against both sides
  at once: neither the vendors claiming lives saved nor the critics counting deaths have the
  miles to support a statistical claim. Free PDF, 15 pp (25 min). Note: rand.org blocks some
  command-line fetchers; it opens normally in a browser.

## What you submit

One paragraph, 150–250 words, by **Sat Aug 29, 11:59 p.m.**, to the `D1` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
