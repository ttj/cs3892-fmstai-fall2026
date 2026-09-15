# D4 — What Does a Prompt Cost the Planet? Specifying AI's Environmental Impact

**Session 6 · Tue Sep 15 · week 4 · 30 minutes in class · think–pair–share**

> **Before class:** read the assigned source (posted on Brightspace) and the background below.
> **After class:** one paragraph, 150–250 words, due **Thu Sep 17, 11:59 p.m.** — see
> [participation.md](participation.md).

## Background

### Where the debate comes from

Running an AI model consumes electricity, which carries emissions and water costs. Since 2019 researchers, companies and agencies have tried to put numbers on that, without converging. The International Energy Agency (IEA) estimates the world's data centres used about 485 TWh of electricity in 2025, and projects roughly 950 TWh by 2030. Data centres are not AI, though: the IEA tracks AI-focused facilities separately, growing about 50% in 2025 against 17% overall.

### What has actually been measured

Most per-query figures are estimated from public hardware specifications. One is not: in August 2025 Google measured inside its production fleet. The median Gemini Apps text prompt in May 2025 used 0.24 Wh, 0.03 gCO2e and 0.26 mL of water — by its own comparison, under nine seconds of television.

The accounting matters more than the number. Google sums four components: the AI accelerator chip (0.14 Wh, 58%), the host machine's CPU and memory (0.06 Wh, 25%), idle provisioned machines (0.02 Wh, 10%), and data-centre overhead — cooling and power conversion, a ratio called PUE, power usage effectiveness (0.02 Wh, 8%). Omit the last three, as most work does, and the same prompts measure 0.10 Wh. Google reports a 33x fall in energy per prompt and 44x in emissions over the preceding year. It notes 0.24 Wh is a daily median, not a mean — long prompts skew the distribution — and excludes reasoning, agentic and multimodal work. No outsider knows the 2026 figure.

### Why the published numbers disagree

Google's literature review lists "energy per prompt" at 0.10, 0.24, 0.3, 3, 4 and 1.83–6.95 Wh. Mostly they do not contradict; they measure different quantities under one name. De Vries's 3 Wh (2023) is model-based, inheriting a February 2023 assumption of 4,000 input and 2,000 output tokens — about 1,500 words. EcoLogits' 1.83–6.95 Wh is for a 50-output-token prompt. Emissions fork: Google's 2024 grid intensity was 345 gCO2e/kWh location-based (what the local grid emitted) against 94 market-based (after renewable certificates); 0.03 gCO2e uses the latter.

Water splits the same way. Li et al. estimate 16.9 mL per GPT-3 request at the US average, of which only 2.2 mL is on-site cooling; 14.7 mL evaporates at power plants. Their abstract says a 500 mL bottle covers "roughly 10 to 50" requests — the source of the "bottle of water per query" claim, and 10–50x off it. Google's 0.26 mL counts on-site cooling only; the two papers compute different functions.

### Why it still matters

Data centres are just over 1% of global electricity by Carbon Brief's count, about 1.5% by the IEA's — a gap about which facilities count — and 0.5% of global CO2. They will add less demand from 2024 to 2030 than electric vehicles or air conditioning, yet are roughly half of US demand growth, and grids are local. Training versus serving (running it for users) is contested too: Luccioni et al. found it takes 205–593 million inferences before serving energy matches training energy for BLOOMz models — after which serving dominates. Meanwhile Google's 2026 environmental report gives electricity demand up 37% in a year, supply-chain emissions up 25%, operational emissions down 2%, and says "reaching our climate moonshots is getting harder." Per-unit efficiency and total consumption move in opposite directions on one company's books.

### Timeline

| When | What |
|---|---|
| June 2019 | Strubell, Ganesh & McCallum (ACL) publish the first widely cited training-energy estimates — 192 lbs CO2e for Transformer-big, 626,155 lbs for a neural architecture search, the row that becomes the "five car lifetimes" headline. |
| April 2021 | Patterson et al. (Google) find that neural-architecture-search estimate 18.7x too high for an average organisation and 88x too high in emissions at Google's efficiency, because the search ran on small proxy tasks. |
| April 2023 | Li, Yang, Islam & Ren post "Making AI Less 'Thirsty'" (revised to v5 in March 2025), estimating 16.9 mL of water per GPT-3 request at the US average, only 2.2 mL of it on-site. |
| October 2023 | Alex de Vries publishes in Joule the ~3 Wh-per-query figure that becomes the debate's most repeated statistic. |
| February 2025 | Epoch AI estimates ~0.3 Wh for a typical GPT-4o query and traces the 3 Wh figure to a February 2023 estimate assuming 4,000 input and 2,000 output tokens. |
| August 2025 | Google publishes the first production-fleet measurement: a median Gemini Apps text prompt at 0.24 Wh under a comprehensive boundary, 0.10 Wh under a narrow one. |
| June 2026 | Google's 11th environmental report shows electricity demand up 37% in a year and supply-chain emissions up 25%, and says reaching its climate targets is getting harder. |
| 2026 | The IEA's "Key Questions on Energy and AI" puts data centres at 485 TWh in 2025 rising to ~950 TWh by 2030, close to the trajectory in its 2025 report. |

## The question

**Does anyone know what a prompt costs the planet?**

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

## Discussion questions

You will be assigned one of these in class. Come having thought about at least two.

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

## Readings

10 sources. One of them is assigned before class; the rest are here if you want to go further, or to check a claim that comes up in discussion.

- **International Energy Agency, "Key Questions on Energy and AI — Executive summary," World Energy Outlook Special Report** (report, 2026)  
  <https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary>  
  The most current authoritative aggregate, and the anchor for the "impacts are real" side:
  485 TWh of data-centre electricity in 2025 rising to ~950 TWh by 2030, 17% growth in 2025
  against 50% for AI-focused sites, and 15–27 GW of on-site natural gas possibly serving data
  centres by 2030. It also undercuts an easy assumption — that these forecasts get revised
  upward every year: the central projection here "remains close to the trajectory set out in
  the IEA's 2025 report." Read the executive summary only, ~10 minutes. Note that the
  415 TWh / ~1.5% figure for 2024 comes from the earlier April 2025 Energy and AI report, not
  this one.

- **Josh Gabbatiss, "AI: Five charts that put data-centre energy use – and emissions – into context," Carbon Brief** (news, 2025)  
  <https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context>  
  This is the one to read before class — ~15 minutes, five charts, and it holds the tension
  rather than resolving it. Data centres are just over 1% of global electricity and 0.5% of
  CO2, and add less 2024–2030 demand than electric vehicles (838 TWh) or air conditioning (651
  TWh); yet they are ~25% of advanced-economy demand growth and about half of US and Japanese
  growth. Its fifth chart — 2030 forecasts spanning ~700 to over 4,000 TWh — is the single
  most useful image in this whole reading list. Watch one detail: it reports "just over 1%"
  for 2024 where the IEA says 1.5%. That discrepancy is a definitional boundary question, not
  an error, and it is worth raising in discussion.

- **Emma Strubell, Ananya Ganesh, Andrew McCallum, "Energy and Policy Considerations for Deep Learning in NLP," Proceedings of ACL 2019 (arXiv:1906.02243)** (academic, 2019)  
  <https://arxiv.org/abs/1906.02243>  
  The origin of the entire debate and of the "five car lifetimes" meme. Read Table 1 and
  Table 3 side by side: training Transformer-big is 192 lbs CO2e, less than 2% of one
  American's annual footprint, while the famous 626,155 lbs figure is the neural architecture
  search (car lifetime incl. fuel = 126,000 lbs). Nine pages, well under 30 minutes. It
  supports the "impacts are real" side and is at the same time the best object lesson here in
  how a correct table becomes a wrong headline.

- **David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, Jeff Dean, "Carbon Emissions and Large Neural Network Training," arXiv:2104.10350** (academic, 2021)  
  <https://arxiv.org/abs/2104.10350>  
  The direct rebuttal. Section 4.1 finds Strubell et al.'s NAS energy estimate 18.7x too high
  for an average organisation and 88x too high in emissions at Google-level efficiency,
  because the search ran on small proxy tasks that were assumed to be full-size, and notes NAS
  runs once per problem domain and search space rather than once per model trained. It is also
  the source of the widely repeated "choice of model, chip and datacentre gives ~100–1000x."
  It is long (~25 pp), but you only need §4.1 and Table 4. Note that it is Google-authored.

- **Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell, "Power Hungry Processing: Watts Driving the Cost of AI Deployment?", ACM FAccT '24 (arXiv:2311.16863)** (academic, 2024)  
  <https://arxiv.org/abs/2311.16863>  
  The careful independent inference measurements. Per 1,000 inferences: text classification
  0.002 kWh, text generation 0.047 kWh, image generation 2.907 kWh — a spread of more than
  1,000x under one heading — and Table 5's cost-parity analysis showing 205–593 million
  inferences before inference energy matches training energy for BLOOMz models, which at
  ChatGPT scale is weeks. Note the author list: Strubell co-authored the most-criticised 2019
  estimate and also did this careful measurement work, which rules out "Strubell was just
  wrong" as a cheap dunk. Read §5 and Table 5, ~20 minutes.

- **Pengfei Li, Jianyi Yang, Mohammad A. Islam, Shaolei Ren, "Making AI Less 'Thirsty': Uncovering and Addressing the Secret Water Footprint of AI Models," arXiv:2304.03271 (v1 Apr 2023, v5 Mar 2025)** (academic, 2025)  
  <https://arxiv.org/abs/2304.03271>  
  The primary source behind essentially every water claim in circulation — read it rather than
  the coverage of it. Table 1 is the whole argument: 16.9 mL per GPT-3 medium-sized request at
  US average, of which 14.7 mL is off-site power-plant evaporation, ranging 7.1 mL (Ireland)
  to 47.5 mL (Washington); 500 mL covers 10–50 requests, i.e. 29.6 at US average. Read §3.3
  and Table 1, ~15 minutes. It supports the "real" side on water and simultaneously disproves
  the meme built on top of it.

- **Cooper Elsworth, Keguo Huang, David Patterson, Ian Schneider, Robert Sedivy, Savannah Goodman, Ben Townsend, Parthasarathy Ranganathan, Jeff Dean, Amin Vahdat, Ben Gomes, James Manyika, "Measuring the environmental impact of delivering AI at Google Scale," arXiv:2508.15734** (academic, 2025)  
  <https://arxiv.org/abs/2508.15734>  
  The only production-instrumented measurement in existence: median Gemini Apps text prompt at
  0.24 Wh, 0.03 gCO2e, 0.26 mL (May 2025), against 0.10 Wh under a narrow boundary. This is
  the strongest measured evidence on the side that says the alarm is overstated. Read
  §3.3–§4.2 plus Table 2, ~15 minutes, and find the boundary choices yourself before you
  accept the number: market-based carbon, ISO WUE Category 2 (on-site cooling water only),
  daily median not mean. Its §2 literature table — de Vries 3 Wh, Epoch 0.3 Wh, EcoLogits
  1.83–6.95 Wh, Luccioni BLOOM 4 Wh, Samsi LLaMA-65B 0.3 Wh — is the best single artefact for
  the specification point. It is vendor-authored, not peer reviewed and not independently
  reproducible; that is something to argue about, not a reason to dismiss it.

- **Josh You, "How much energy does ChatGPT use?", Epoch AI, Gradient Updates, 7 February 2025** (report, 2025)  
  <https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use>  
  The independent, non-vendor rebuttal to the 3 Wh figure, and the cleanest piece of
  provenance work in this list: ~0.3 Wh for a typical GPT-4o query, and it traces the 3 Wh
  number to de Vries (2023) relying on a February 2023 SemiAnalysis estimate that assumed
  4,000 input and 2,000 output tokens (~1,500 words), and the 0.3 Wh Google-search comparator
  to "a very old estimate from Google in 2009." Honest about its own limits: long-context
  queries run 2.5–40 Wh and reasoning models much higher. ~10 minutes. If you read only one
  thing on where the 3 Wh number came from, make it this; with Carbon Brief, it is the
  strongest source here that argues the other way with no vendor behind it.

- **Google, "Read our 11th annual Environmental Report," The Keyword, 30 June 2026** (primary, 2026)  
  <https://blog.google/company-news/outreach-and-initiatives/sustainability/2026-environmental-report/>  
  Google's own accounting set directly against the same company's per-prompt optimism:
  operational Scope 1+2 (market-based) emissions down 2%, supply-chain Scope 3 up 25%, total
  electricity demand up 37% in a single year, 100% of electricity matched with renewable
  purchases for a ninth consecutive year, ~7.7 billion gallons replenished (~78% of freshwater
  consumption), and an explicit statement that "reaching our climate moonshots is getting
  harder." ~10 minutes. Read it alongside the Gemini measurement paper — same company,
  opposite mood — and note that it is also the clearest illustration of market-based versus
  location-based accounting.

- **Alex de Vries, "The growing energy footprint of artificial intelligence," Joule 7(10):2191–2194, doi:10.1016/j.joule.2023.09.004** (academic, 2023)  
  <https://research.vu.nl/en/publications/daca1753-5603-416f-8fad-36460dc944c4>  
  The origin of the 3 Wh-per-query figure, the 85–134 TWh-by-2027 projection, and the clearest
  statement of the Jevons-paradox argument that efficiency gains get absorbed by demand — the
  strongest reply to Google's 44x improvement claim. The link goes to the VU Amsterdam
  research-portal record, which carries the full citation but not the article text. The
  figures quoted above are confirmed from the Cell Press release, and the 3 Wh number
  independently from the Epoch AI piece. **Get the four-page PDF through the Vanderbilt
  library before quoting anything else from it.**

## What you submit

One paragraph, 150–250 words, by **Thu Sep 17, 11:59 p.m.**, to the `D4` assignment folder on
Brightspace. Answer three things: where you landed and why, what the strongest argument against you
was, and what would change your mind. Scored 0–2; lowest of the nine is dropped. Full details and
the rubric are in [participation.md](participation.md).
