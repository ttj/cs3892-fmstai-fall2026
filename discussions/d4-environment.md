# D4 — What Does a Prompt Cost the Planet? Specifying AI's Environmental Impact

**Session 6 · Tue Sep 15 · week 4 · 30 minutes · think–pair–share**

## Framing

> Global data centres used about 485 TWh of electricity in 2025, and the IEA expects that to
> roughly double to 950 TWh by 2030, with 15 to 27 GW of on-site gas generation possibly attached
> to them, mostly in the United States. Measuring inside its own production fleet, Google reports
> that a median Gemini text prompt used 0.24 Wh and 0.26 mL of water in May 2025 — less energy
> than nine seconds of television — and that its per-prompt emissions had fallen 44-fold in the
> preceding twelve months. Over that same year Google's total electricity demand rose 37%, its
> supply-chain emissions rose 25%, and its own environmental report says reaching its climate
> targets is getting harder. Every one of those is a measured number rather than a guess, and the
> published estimates for the energy of a single prompt currently span from 0.1 to about 7 watt-
> hours; your job for the next half hour is to work out whether these figures actually disagree.

## Why this is in a formal-methods course

"Energy per query" is an underspecified predicate, and this packet contains the proof: Google's
own literature review lists published figures for that single named quantity at 0.10, 0.24, 0.3,
3, 4, and 1.83–6.95 Wh — roughly a 70x spread produced not by disagreement about physics but by
unstated choices over model, output length, batch size, utilisation, PUE boundary, idle
amortisation, embodied hardware, and market- versus location-based grid factors. That is
precisely the specification mismatch this course exists to catch: a proof is only as strong as
the property statement, and here every party is rigorously verifying a different property under
one name, then comparing results. Two further threads run straight into the syllabus — Google
can instrument while everyone else can only estimate, so the most accurate number is the least
independently checkable, which is attestation versus verification and points directly at runtime
monitoring and audit obligations; and the IEA reports 700–1,700 TWh for 2035, an interval rather
than a point, which is reachability over an uncertainty set rather than a single trajectory.

## Discussion questions

**1.** Google's 0.24 Wh is the only figure in this literature produced by instrumenting a real
production fleet, it is also the lowest number published, and no one outside Google can
reproduce it. Under what conditions should a number that only the measured party can produce
outrank an independent estimate that anyone can check — and what exactly would have to accompany
Google's number (an auditor? a released trace? a standard?) before you would treat it as
established rather than claimed?

**2.** Strubell et al.'s "five car lifetimes" was the neural-architecture-search row (626,155 lbs);
their row for actually training Transformer-big is 192 lbs. Patterson et al. later found the NAS
estimate 18.7x too high for an average organisation and 88x too high at Google's efficiency,
because the search used small proxy tasks that were assumed to be full-size. Strubell then went
on to co-author the careful inference measurements everyone now cites. Was the 2019 paper a bad
estimate that usefully forced the field's attention, a good estimate corrupted in transmission,
or something that should not have shipped in that form — and does your answer change if the
overstatement demonstrably accelerated the efficiency work that followed?

**3.** About 87% of Li et al.'s per-request water evaporates at power plants, not inside the data
centre; Google's 0.26 mL counts only cooling water on its own fleet. If AI's water footprint is
mostly a consequence of the electricity mix, is "AI's water use" a separable quantity at all, or
is it electricity use counted a second time? Whose interests does each boundary serve, and would
you draw the line the same way for beef, for Bitcoin, or for a hospital?

**4.** Data centres are around 1% of global electricity and 0.5% of global CO2, and will add less
demand between 2024 and 2030 than electric vehicles or air conditioning — but they are roughly
half of US electricity demand growth, and interconnection queues, gas turbines and capacity
prices are irreducibly local. When a technology is negligible in the global aggregate and
dominant in a specific grid, which number is the honest headline? Does your answer change
depending on whether you live next to one, and should it?

**5.** de Vries argues efficiency gains are absorbed by demand growth; Google reports a 44x reduction
in per-prompt emissions in twelve months alongside a 37% rise in its total electricity use. If
both are true, is per-unit efficiency reporting genuinely informative or is it a well-
constructed distraction? Name a per-unit metric you would accept as evidence that the problem is
actually shrinking — and say why a company could not game it.

## Readings

10 sources, 10 verified by direct fetch. Assign one; the rest are for students who want to go further, and for you when a claim gets challenged in the room.

- **International Energy Agency, "Key Questions on Energy and AI — Executive summary," World Energy Outlook Special Report** (report, 2026)  
  <https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary>  
  The most current authoritative aggregate and the packet's anchor for the "real" side: 485
  TWh of data-centre electricity in 2025 rising to ~950 TWh by 2030, 17% growth in 2025
  against 50% for AI-focused sites, and 15–27 GW of on-site natural gas possibly serving data
  centres by 2030. It also cuts against a claim students will bring in — it says the central
  projection "remains close to the trajectory set out in the IEA's 2025 report," i.e. the
  forecasts are not being serially revised upward. Executive summary only, ~10 minutes; the
  415 TWh / ~1.5% figure for 2024 comes from the earlier April 2025 Energy and AI report, not
  this one.

- **Josh Gabbatiss, "AI: Five charts that put data-centre energy use – and emissions – into context," Carbon Brief** (news, 2025)  
  <https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context>  
  ASSIGN THIS ONE as pre-class reading — ~15 minutes, five charts, and it holds the tension
  rather than resolving it. Data centres are just over 1% of global electricity and 0.5% of
  CO2, and add less 2024–2030 demand than electric vehicles (838 TWh) or air conditioning (651
  TWh); yet they are ~25% of advanced-economy demand growth and about half of US and Japanese
  growth. Its fifth chart — 2030 forecasts spanning ~700 to over 4,000 TWh — is the single
  most useful image in the packet. Note it reports "just over 1%" for 2024 where the IEA says
  1.5%; that discrepancy is a definitional boundary question, not an error, and is worth
  surfacing.

- **Emma Strubell, Ananya Ganesh, Andrew McCallum, "Energy and Policy Considerations for Deep Learning in NLP," Proceedings of ACL 2019 (arXiv:1906.02243)** (academic, 2019)  
  <https://arxiv.org/abs/1906.02243>  
  The origin of the entire debate and of the "five car lifetimes" meme. Have students read
  Table 1 and Table 3 side by side: training Transformer-big is 192 lbs CO2e, less than 2% of
  one American's annual footprint, while the famous 626,155 lbs figure is the neural
  architecture search (car lifetime incl. fuel = 126,000 lbs). Nine pages, well under 30
  minutes. Supports the "impacts are real" side and is simultaneously the packet's best object
  lesson in how a correct table becomes a wrong headline.

- **David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, Jeff Dean, "Carbon Emissions and Large Neural Network Training," arXiv:2104.10350** (academic, 2021)  
  <https://arxiv.org/abs/2104.10350>  
  The direct rebuttal. Section 4.1 finds Strubell et al.'s NAS energy estimate 18.7x too high
  for an average organisation and 88x too high in emissions at Google-level efficiency,
  because the search ran on small proxy tasks that were assumed to be full-size, and notes NAS
  runs once per problem domain and search space rather than once per model trained. It is also
  the source of the widely repeated "choice of model, chip and datacentre gives ~100–1000x."
  Long (~25 pp) — assign §4.1 and Table 4 only. Google-authored; flag that from the front of
  the room.

- **Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell, "Power Hungry Processing: Watts Driving the Cost of AI Deployment?", ACM FAccT '24 (arXiv:2311.16863)** (academic, 2024)  
  <https://arxiv.org/abs/2311.16863>  
  The careful independent inference measurements. Per 1,000 inferences: text classification
  0.002 kWh, text generation 0.047 kWh, image generation 2.907 kWh — a spread of more than
  1,000x under one heading — and Table 5's cost-parity analysis showing 205–593 million
  inferences before inference energy matches training energy for BLOOMz models, which at
  ChatGPT scale is weeks. Point out to the room that Strubell co-authors this: the author of
  the most-criticised 2019 estimate did the careful measurement work, which kills "Strubell
  was just wrong" as a cheap dunk. Assign §5 and Table 5, ~20 minutes.

- **Pengfei Li, Jianyi Yang, Mohammad A. Islam, Shaolei Ren, "Making AI Less 'Thirsty': Uncovering and Addressing the Secret Water Footprint of AI Models," arXiv:2304.03271 (v1 Apr 2023, v5 Mar 2025)** (academic, 2025)  
  <https://arxiv.org/abs/2304.03271>  
  The primary source behind essentially every water claim in circulation — read it rather than
  the coverage of it. Table 1 is the whole argument: 16.9 mL per GPT-3 medium-sized request at
  US average, of which 14.7 mL is off-site power-plant evaporation, ranging 7.1 mL (Ireland)
  to 47.5 mL (Washington); 500 mL covers 10–50 requests, i.e. 29.6 at US average. Assign §3.3
  and Table 1, ~15 minutes. It supports the "real" side on water and simultaneously disproves
  the meme built on top of it.

- **Cooper Elsworth, Keguo Huang, David Patterson, Ian Schneider, Robert Sedivy, Savannah Goodman, Ben Townsend, Parthasarathy Ranganathan, Jeff Dean, Amin Vahdat, Ben Gomes, James Manyika, "Measuring the environmental impact of delivering AI at Google Scale," arXiv:2508.15734** (academic, 2025)  
  <https://arxiv.org/abs/2508.15734>  
  The only production-instrumented measurement in existence: median Gemini Apps text prompt at
  0.24 Wh, 0.03 gCO2e, 0.26 mL (May 2025), against 0.10 Wh under a narrow boundary. This is
  the reference that cuts hardest against the framing's alarm side. Assign §3.3–§4.2 plus
  Table 2, ~15 minutes, and make students find the boundary choices themselves: market-based
  carbon, ISO WUE Category 2 (on-site cooling water only), daily median not mean. Its §2
  literature table — de Vries 3 Wh, Epoch 0.3 Wh, EcoLogits 1.83–6.95 Wh, Luccioni BLOOM 4 Wh,
  Samsi LLaMA-65B 0.3 Wh — is the best single artefact for the specification point. Vendor-
  authored, not peer reviewed, not independently reproducible; that is discussion material,
  not a disqualification.

- **Josh You, "How much energy does ChatGPT use?", Epoch AI, Gradient Updates, 7 February 2025** (report, 2025)  
  <https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use>  
  The independent, non-vendor rebuttal to the 3 Wh figure, and the packet's cleanest piece of
  provenance work: ~0.3 Wh for a typical GPT-4o query, and it traces the 3 Wh number to de
  Vries (2023) relying on a February 2023 SemiAnalysis estimate that assumed 4,000 input and
  2,000 output tokens (~1,500 words), and the 0.3 Wh Google-search comparator to "a very old
  estimate from Google in 2009." Honest about its own limits: long-context queries run 2.5–40
  Wh and reasoning models much higher. ~10 minutes. Along with Carbon Brief this is the
  reference that most cuts against the framing's apparent thrust.

- **Google, "Read our 11th annual Environmental Report," The Keyword, 30 June 2026** (primary, 2026)  
  <https://blog.google/company-news/outreach-and-initiatives/sustainability/2026-environmental-report/>  
  Google's own accounting set directly against the same company's per-prompt optimism:
  operational Scope 1+2 (market-based) emissions down 2%, supply-chain Scope 3 up 25%, total
  electricity demand up 37% in a single year, 100% of electricity matched with renewable
  purchases for a ninth consecutive year, ~7.7 billion gallons replenished (~78% of freshwater
  consumption), and an explicit statement that "reaching our climate moonshots is getting
  harder." ~10 minutes. Pair it with the Gemini measurement paper — same company, opposite
  mood — and use it to teach market-based versus location-based accounting.

- **Alex de Vries, "The growing energy footprint of artificial intelligence," Joule 7(10):2191–2194, doi:10.1016/j.joule.2023.09.004** (academic, 2023)  
  <https://research.vu.nl/en/publications/daca1753-5603-416f-8fad-36460dc944c4>  
  The origin of the 3 Wh-per-query figure, the 85–134 TWh-by-2027 projection, and the clearest
  statement of the Jevons-paradox argument that efficiency gains get absorbed by demand — the
  strongest reply to Google's 44x improvement claim. VERIFICATION NOTE: cell.com and
  sciencedirect return HTTP 403 to automated fetch; the URL given is the VU Amsterdam
  research-portal record for the article, which I fetched and which confirms title, author,
  journal, volume, pages and DOI but carries no full text. The headline figures above were
  confirmed from the Cell Press release, and the 3 Wh attribution is independently confirmed
  in Epoch AI's piece; get the four-page PDF through the Vanderbilt library before quoting
  anything else from it.

## 30-minute run sheet

BEFORE CLASS: assign Carbon Brief (ref 2), ~15 min. Print a one-page handout with three excerpts
only — Carbon Brief's chart 5 (2030 forecasts, ~700 to >4,000 TWh); Google's Table 2 (0.10 vs
0.24 Wh, 0.12 vs 0.26 mL); Li et al.'s Table 1 "U.S. Average" row (2.2 mL on-site / 14.7 off-
site / 16.9 total / 29.6 requests per 500 mL). Bring index cards.

0–3 — Read the framing aloud. Write exactly three numbers on the board and nothing else: 0.24 Wh
(Google, instrumented), 3 Wh (de Vries 2023, model-based), 500 mL per 10–50 requests (Li et
al.). Offer no commentary on which is right.

3–4 — Distribute the three-excerpt handout. Assign prompts by seating row: row 1 takes P1, row 2
P2, row 3 P3. Hold P4 and P5 back (deployed at 19–27).

4–9 — Silent individual think, no laptops. Each student writes two sentences on an index card:
"The number I trust least is ___ because ___" and "What would change my mind is ___." Tell them
the cards are collected at the door, not now — this keeps them writing for themselves.

9–17 — Pairs. Each pair produces ONE written artefact: a "boundary spec" listing at least four
things that must be pinned down before "energy per query" is a well-defined quantity. Instructor
circulates and boards items as overheard, unattributed. Expect to collect: model and version,
output length, batch size, GPU utilisation, PUE boundary, idle-capacity amortisation, embodied
hardware, market- vs location-based grid factor, median vs mean, on-site vs off-site water.

17–19 — Consolidate the boarded items into a single column headed FREE VARIABLES. Say only one
thing: "this is the list; no published number states all of it."

19–27 — Share. Cold-call four or five pairs for one item each. On the other half of the board
run two columns: WE COULD CHECK THIS OURSELVES / WE MUST TRUST SOMEONE. Every figure anyone
names gets placed in one column, including Google's, Li's and de Vries's. If the room converges
too quickly on "it's all overstated" or "it's all fine," deploy P4 (negligible globally,
dominant in a single grid) to break the consensus, or P5 (44x per-prompt gain against +37% total
electricity) to reopen it. Hand P4 or P5 to any pair that finished the boundary spec early.

27–30 — Close. State the one result the class established: the disagreement does not live in the
arithmetic, it lives in the right-hand column. Assign the take-home — write a specification for
"energy per query" precise enough that two independent labs would compute the same number, and
name what an auditor would need access to in order to check a vendor's claim against it. Two
pages, due next class. Collect the index cards at the door and skim them before the next
session; the "what would change my mind" halves are the best available read on where the room
actually is.

## Do not assert these

Claims that circulate widely about this topic but are wrong, contested, or traceable only to a single weak source. Getting one of these wrong from the front of the room, in a course about verification, costs more than it would anywhere else.

DO NOT ASSERT, EACH WITH THE REASON:

1. "One ChatGPT query equals a bottle of water." Wrong by 10–50x even by its own source. Li et
al.'s Table 1 gives ~16.9 mL per GPT-3 medium-sized request at US average — 29.6 requests per
500 mL bottle — and their abstract says "roughly 10 to 50" requests. About 87% of that (14.7 of
16.9 mL) evaporates at power plants, not in the data centre. The per-prompt version traces to a
Washington Post rendering that additionally assumed roughly ten ChatGPT queries per email.

2. But do NOT assert the reverse — that Google's 0.26 mL "refutes" Li et al. Google writes that
0.26 mL is "orders of magnitude less than previous estimates of 45 to 50 mL," and its reference
for the 50 mL is Li et al. — but 50 mL is simply 500/10, the worst end of Li's 10–50 range, and
it includes off-site power-plant water. Google's 0.26 mL is a median prompt, on-site cooling
only (ISO WUE Category 2), on Google's own unusually low-WUE fleet. Li's own US-average on-site
figure is 2.2 mL for a much larger GPT-3 request. On-site to on-site the gap is roughly 8x, not
orders of magnitude. The two papers compute different functions; only the bottle-per-query claim
is actually refuted.

3. "A ChatGPT query uses ten times a Google search — 3 Wh versus 0.3 Wh." Both endpoints are
weak. The 3 Wh traces to de Vries (2023), which relied on a February 2023 SemiAnalysis estimate
assuming 4,000 input and 2,000 output tokens (~1,500 words). Epoch AI states the 0.3 Wh search
comparator "comes from a very old estimate from Google in 2009." No current, well-sourced figure
exists for either side of that ratio, and this is the single most-repeated statistic in the
debate.

4. "Training one AI model emits as much as five cars over their lifetimes." That is the neural-
architecture-search row of Strubell et al.'s Table 1 (626,155 lbs against 126,000 lbs for a car
lifetime). Their Transformer-big training row is 192 lbs. Patterson et al. §4.1 further found
the NAS estimate 18.7x too high for an average organisation and 88x too high at Google
efficiency, because the search ran on small proxy tasks that were assumed to be full-size; and
NAS is run once per problem domain and search space, not once per model trained.

5. "Google's data centres run on renewables." Google matched 100% of its electricity with
renewable PURCHASES for a ninth consecutive year — annual, market-based certificate matching,
not hourly clean supply. Google's own paper gives its 2024 location-based grid factor as 345
gCO2e/kWh against a net market-based 94 gCO2e/kWh after carbon-free-energy procurement. The
published 0.03 gCO2e per prompt uses the market-based number; on a location-based basis the
operational share would be several times higher.

6. Replenishment is not non-consumption. Google reports replenishing ~7.7 billion gallons,
"roughly 78% of freshwater consumption"; Microsoft's 2026 report says it "replenished over 14.2
million m³ ... more than we withdrew." Replenishment credits are frequently in different
watersheds from the withdrawal, and water is a local resource. Do not describe either firm as
water-neutral in the places where it operates. (This packet did not verify Microsoft's emissions
figures against its 2020 baseline — do not quote them from the front of the room.)

7. 0.24 Wh is a May 2025 MEDIAN, not today's average. Google explicitly chooses the daily median
because the distribution is right-skewed by long-context and low-utilisation prompts, and
reports a 33x energy improvement over the preceding twelve months — so by Fall 2026 the figure
is sixteen months old and nobody outside Google knows the current one, in either direction. It
also excludes reasoning, agentic and multimodal workloads; Epoch notes long-input queries run
2.5–40 Wh.

8. "Total data-centre electricity is AI's footprint." It is not. The IEA tracks AI-focused data
centres separately and reports them growing ~50% in 2025 against 17% for data centres overall.
Related: the share-of-global-electricity figure is itself contested by definition — IEA says
~1.5% for 2024, Carbon Brief reports "just over 1%." That gap is about which facilities count,
not arithmetic, and students will spot it.

9. "The IEA keeps revising its projections upward." Not supported. The 2026 Key Questions report
says the central data-centre trajectory "remains close to the trajectory set out in the IEA's
2025 report" (~945 versus ~950 TWh for 2030). What is large is the spread, not the drift: IEA's
own 2035 cases span 700–1,700 TWh and the wider literature Carbon Brief surveys spans ~700 to
over 4,000 TWh for 2030. Present a range, never a point forecast.

10. "Energy use scales with compute." Masanet, Shehabi, Lei, Smith and Koomey, Science
367(6481):984–986 (2020), doi:10.1126/science.aba3758, found data-centre energy growth had
decoupled sharply from compute growth through 2018. IMPORTANT: this packet could NOT retrieve
that paper — science.org returns 403, Semantic Scholar reports it closed with no open-access
PDF, and only the bibliographic record was confirmed (via OpenAlex, Crossref and Semantic
Scholar). Do not quote a precise "compute +550%, energy +6%" figure without pulling the paper
first. And do not assert the converse either: that window closed before the generative-AI
buildout, and Google's own 37% single-year electricity increase suggests the historical
decoupling is not currently holding.

11. Sourcing hygiene on the pushback. Andy Masley's widely shared "The AI water issue is fake"
is a personal blog, not peer-reviewed work. His provenance tracing (bottle-per-prompt to the
Washington Post to Li et al.) is checkable and holds up; his headline framing is advocacy and
should be attributed as such rather than cited as a finding. Do not present him as the
scientific counterweight to Li et al. Symmetrically, self-reported AI-emissions-SAVINGS claims —
including Google's "nine AI solutions reduced an estimated 41 million tCO2e" — are vendor
counterfactual modelling with no independent replication, and must not be netted against
measured emissions.

12. The "4Ms" framing and the claim that ML held "under 15% of Google's total energy use" come
from Patterson et al. (2022) — Google-authored, and covering a period that ended before the
generative-AI buildout. Do not present it as a current fact about the industry.
