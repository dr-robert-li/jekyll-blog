# Collective Delay in the Face of Foreseen Global Challenges
## Premise check, explanatory literature, the mathematics of sentiment tipping, downstream harms, and the causal-AI response

**Prepared:** 10 October 2026
**Context:** Follow-up to the author's essay "The Cycle of Order and Disorder & the Challenge of LLMs" (26 March 2025), summarised in Appendix E.
**Research question.** Three foreseen global challenges are converging: record public debt, accelerating climate change, and pushback against AI ethics and safety. Why do societies delay addressing such challenges until the last moment, even when the threat is foreseen and its harms fall unevenly? The hypothesis under test is that individuals keep supporting a system while the benefit it gives them and their circle of trust exceeds the generalised harm they perceive, and act only at the crossover (B.1). The report asks whether an established term exists for this, how the sentiment change needed for action scales with population size, and how large the hidden "iceberg" of private support is beneath visible protest.
**Method:** I tried to refute every substantive claim against a primary or authoritative source before tagging it:
- `[admit: source]`: confirmed this session in an authoritative source for this specific claim, and the refutation attempt failed.
- `[refute: source]`: an authoritative source contradicts the claim. The correction is given.
- `[abstain: reason]`: I could not verify the claim this session, the only source is non-authoritative, or credible sources conflict. Reasons are limited to `unverifiable`, `source-vs-prior conflict`, `non-authoritative source`, or `tier-floor: unearned confidence`.

**A note on framing.** The essay's explicit frameworks are Actor-Network Theory (Callon and Latour's "translation"), reification, simulacra, and Brian Klaas's *sandpile* or self-organised-criticality metaphor ("a single additional grain can trigger an avalanche"). That matters for this report. The sandpile metaphor is the physical cousin of the threshold-cascade models in Part C. Those models make the essay's intuition precise: a system can sit near a critical state for a long time and then reorganise suddenly.

---

## Executive summary

1. **The premise mostly holds, with important corrections.**
   - **Debt.** Debt is at record dollar levels, and *public* debt/GDP is rising toward 100% of world GDP by 2029, a level last seen after WWII. However, *total* debt/GDP is about 23 percentage points below its 2020 peak, and private debt/GDP is at its lowest since 2015. The famous "debt thresholds" that would make debt harmful (Reinhart and Rogoff's 90% figure) have been refuted. "Too much finance" thresholds (private credit around 100% of GDP) are contested.
   - **Climate.** Warming is unambiguous: 2023–25 were the three warmest years, and 2024 was about 1.55 °C above pre-industrial. A very strong, possibly record, El Niño is under way in 2026. Projections of how ENSO changes under warming, and whether the AMOC has *already* declined or *when* it might collapse, are genuinely contested in the peer-reviewed literature.
   - **AI safety pushback.** The pushback is well documented in the US and UK in 2025–26: the US and UK safety institutes were renamed, the Biden-era AI executive order was revoked, the US moved to pre-empt state laws, and the Pentagon designated Anthropic a "supply chain risk". The EU AI Act's high-risk obligations were also delayed. Counter-movements exist too: the US Senate voted 99–1 against a moratorium on state AI laws, California enacted SB 53, and public majorities in the US want *more* regulation.
2. **The explanation is largely already in the literature, spread across disciplines.** The author's "local benefit vs generalised pain crossover" is, almost word for word, how Granovetter (1978) defines an individual's *threshold*: "the point where net benefits begin to exceed net costs for that particular actor". In political economy, the nearest named theory is the **crisis hypothesis of reform** (Drazen and Grilli 1993), built on the **war-of-attrition model of delayed stabilisation** (Alesina and Drazen 1991). In that model, reform comes only when the welfare loss from the status quo "dwarfs" each group's distributional loss from reform. The "personal circle" component maps onto **particularised trust** (Uslaner), the **radius of trust** (Fukuyama; Delhey, Newton and Welzel 2011) and, in its extreme form, **amoral familism** (Banfield 1958). The "foreseen yet ignored" component is a **predictable surprise** (Bazerman and Watkins), and on the time axis it is a **tragedy of the horizon** (Carney) and a **super wicked problem** (Levin et al. 2012).
   - **No single established term** combines "the benefit is computed inside the trust radius" with "act only at the crossover against generalised harm". The closest composite is *crisis-induced reform under particularised trust*. I found no precise named term, but that is an absence of evidence, so it is tagged abstain.
3. **The evidence partly contradicts the hypothesis, and the model in B.4 is built around these corrections.** Majorities *already* privately support climate action (69% of people worldwide are willing to give 1% of income; 89% want more political action). Yet people underestimate how many others share that view by about 26 percentage points. That pattern is **pluralistic ignorance**, not a calculation of individual benefit. So the binding constraint is often *coordination and perception* plus *elite insulation* (Diamond; Alesina–Drazen), not individuals' net-benefit sums. Local pain moves opinion only modestly, briefly, and through a partisan filter: wildfire exposure raised pro-climate votes by 5–6 points within 5 km, mostly in Democratic areas. Baselines also renormalise within 2–8 years.
4. **Scaling with population (Part C).** In the canonical models (Granovetter mean-field thresholds; committed-minority naming games; Centola's convention experiments) the *critical fraction* does **not** depend on N, so the *absolute* number required grows roughly linearly with N. Three qualifications matter:
   - (a) The *time* to tip does depend on N. Below the critical committed fraction, consensus time grows **exponentially** in N; above it, only as ln N (Xie et al. 2011).
   - (b) On networks, what matters is local neighbourhood fractions and the degree distribution, not N (Watts 2002).
   - (c) If people react to *absolute* counts, as Granovetter allows, the required *fraction* falls roughly as 1/N. Olson's claim that groups fail as they grow holds only when costs rise with group size (Oliver and Marwell 1988). Laboratory evidence contradicts it for large groups (Isaac, Walker and Williams 1994).

   Chenoweth's 3.5% is a descriptive rule of thumb drawn from *maximalist* campaigns. It is not a law: 83% of successful campaigns stayed below 3.5%, and Bahrain failed at more than 6%.
5. **The "iceberg" is real and has a name.** Chenoweth herself writes that peak participation "is usually the tip of the iceberg". Kuran's **preference falsification** and the survey literature on **pluralistic ignorance** quantify the hidden mass. One 2026 finding complicates it: people *overestimate* rare costly behaviours such as donating and political engagement, and correcting misperceptions did not change actual donations (Tiede et al. 2026).

6. **Deep history: Montreal is an exception for *novel, global* threats, and only partly pre-emptive (Part D).**
   - Pre-emption is common against *recurrent, local, visible* hazards on a bounded commons: water boards, quarantine, alpine commons, granaries.
   - It is rare (an estimated 5–25%, a judgement rather than a measurement) against novel, diffuse threats whose costs fall outside the decision-makers' circle.
   - Ostrom's enduring commons are precisely the cases where the trust radius **encompasses** the commons. That is consistent with the radius-bounded mechanism, but Ostrom selected long-enduring cases and measured membership boundaries, not trust, so it is supporting rather than confirming evidence (App. A §6).
7. **Generality: the mechanism describes a plurality, and probably a majority, of slow-onset, diffuse-harm, concentrated-benefit problems. It does not describe all civilisational systems (Part E).**
   - In a 33-case, 10-domain catalogue, 79% were late, failed or ongoing. The full four-term mechanism is clearly needed in about a third of cases.
   - In another two-fifths, incumbent benefit plus a veto among *few* deciders suffices.
   - Systems with immediate, attributable feedback, such as aviation safety and drug recalls, mostly succeed quietly.
8. **Crisis is neither necessary nor sufficient (Parts D and E).**
   - Reform is uncorrelated with crisis severity in CrisisDB, where only 31% of crises saw any reform, and in a global disaster-policy panel.
   - Under partisan filtering, a crisis can *raise* the veto (mass shootings → loosening laws).
   - The model in B.4.1 proposes instead that reform follows when harm **enters the veto players' own radius**. Case evidence fits (the Great Stink, the Dust Bowl, Montreal), but this is a hypothesis, untested on unselected data (P4).
9. **Downstream harms and accreted wickedness (Part G).**
   - Unresolved root causes produce harms down causal chains that cross domains. Attribution decays with each link, and the people who bear downstream costs hold no veto at the root. In all four current chains coded (French debt, California wildfire, social media, obesity), most enacted policy sits at the nearest attributable, lowest-veto link. That is a pattern in non-random cases, not a measured rate.
   - In the resolved historical chains (tobacco, lead, CFCs), root action followed a **carrier** that moved costs into the veto holders' radius: state Medicaid suits and the 1998 settlement, independent lead research, a US skin-cancer valuation of ozone loss.
   - Each symptomatic response creates beneficiaries who join the veto. In aggregate the layers can turn a tractable problem into a wicked one. No source names this "accreted wickedness", though each component is established (Pierson's policy feedback, layering, Adam et al.'s policy accumulation).
   - No study measures how often accumulated policy is unwound comprehensively without a crisis. Unit-level termination is measured: about 10% of US domestic programmes end within a decade.
10. **Causal AI as a way out, and its cost (Part H).**
   - Causal models, causal discovery and digital twins (used here as names of a model class, not as a commitment to causes as things) could slow attribution decay along chains, do part of the work of a spanning mandate, and hold institutional memory. Attribution tools already create carriers: extreme-event attribution won recognition of emitter liability in principle (*Lliuya v RWE*, 2025), though no damages award yet, and pharmacovigilance detects drug-safety signals routinely. Where harm is delayed and incumbent benefit large, detection is rarely the bottleneck: rofecoxib's heart-attack signal preceded its withdrawal by four years.
   - Two limits are ceilings: observational data cannot settle interventional questions without assumptions or interventions, and retraining on a world the model has shaped converges to performatively stable points that need not be true. Partisan filtering, capture, binding vetoes and data silos are governance risks.
   - The central risk is intrinsic to success. A large, continuously updated causal model is opaque by scale, updating to fix drift removes the stable referent that tracing needs, and the human capacity to trace atrophies, as automation research predicts (Bainbridge 1983; AF447; endoscopists' adenoma detection falling from 28.4% to 22.4% after AI exposure, an observational finding). Maintaining that capacity is M, which the model predicts will be cut under fiscal pressure; US manual-flying guidance is advisory and its uptake was never measured. The model then becomes the most complete accreted layer, and its operators the obligatory passage point for what counts as a cause.
   - This is Latour's blackboxing, technical work "made invisible by its own success" (1999), traced through Law, Callon, Akrich, Star, and Callon and MacKenzie on performativity. It also fixes the report's ontology: V, L^R, the trust radius and M are punctualised network effects, and carriers are the actants that reopen them.

### Status of the report's claims relative to existing research

**1. Novel claims (no precedent found; novelty is an absence-of-evidence judgement, not proof).**
- *The trust radius as the domain of the private benefit term*, so that its size sets the timing of the crossover. Nearest: Uslaner; Delhey et al. 2011; Drazen & Grilli. (B.3, B.4)
- *The trust radius enters three terms at once* (L's domain, φ's distance decay, the silence bias δ). Nearest: Matthes et al. 2018 on silencing within close circles. (B.4)
- *The formal micro composite*: cascade threshold, biased r̂, radius-bounded L, endogenous elite veto and N-scaling of time to tip. Nearest: Platt 1973; Kuran 1995; Søgaard Jørgensen et al. 2024. (Part E; App. B §6)
- *Accreted wickedness*: symptomatic layers plus a growing beneficiary veto turn a tractable problem into a wicked one. Nearest: Adam et al. 2019; Pierson 1993; Howlett & Rayner 2009; Wildavsky 1979. (G.2; App. C §7)
- *Carriers* as the actors who decide when a root cause is reached. Nearest: Birkland's focusing events; Alesina & Drazen's cost of delay to groups. (G.1)
- *The successful causal model as the most complete accreted layer*: opaque by scale, untraceable because it updates, served by an atrophying reserve of human tracing (M), with its operators as the obligatory passage point for what counts as a cause. Nearest: Bainbridge 1983; Latour 1999; Callon 1986; Sculley et al. 2015; Messeri & Crockett 2024. (H.3, H.4; App. D N1)

**2. Claims that extend existing research or doctrine.**
- *The veto depends on elite exposure*, V = V₀ − γH_elite + δL^R_elite + σΠ. Builds on Alesina & Drazen 1991, Drazen & Grilli 1993 and Diamond's elite insulation; adds which costs count and the polarisation term. (B.4.1)
- *An institutional-memory term M* in φ that resists shifting baselines. Builds on Pauly 1995, Moore et al. 2019 and Riris et al. 2024. (B.4.1)
- *An exit branch*: reform may never come; displacement or collapse can replace it. Builds on Hirschman 1970 and CrisisDB (Hoyer et al.). (B.4.1)
- *N-scaling of time to tip as a formal "last moment"*. Builds on Xie et al. 2011. (B.4, C.2)
- *The iceberg ratio I = s/a* with a pluralistic-ignorance discount. Builds on Granovetter, Kuran and Chenoweth. (C.3)
- *Radius alignment explains enduring commons, and its breach explains decay*. Builds on Ostrom 1990 and van Bavel et al. 2018. (App. A §6; P10)
- *Externality leakage*: pre-emption inside a radius exports harm. Builds on maladaptation (Barnett & O'Neill 2010). (B.4.1; P12)
- *Attribution decays multiplicatively along multi-link, cross-domain chains with an unaddressed policy root, mainly at intervening agents, and responses settle at the lowest-veto attributable link*. Builds on Arnold 1990 (traceability), Engelmann & Waldmann 2022 (chain length lowers blame) and Hilton et al. 2010 (attribution passes through physical links), with Senge and Kahn for the response side. (G.1; P14)
- *The lateral-connection problem as M-erosion*. Builds on the 9/11 Commission, Vaughan 1996 and Tett 2015. (G.3)
- *The drift–traceability trade-off*: updating a model to track drift removes the stable referent that tracing needs, and no update rate avoids both costs. Builds on Sculley et al. 2015 (CACE) and concerns about auditing continual learning; not novel as an engineering observation. (H.3)
- *Reification as the cost of success, through M-erosion*: reserve tracing capacity is a standing cost cut under fiscal pressure. Builds on Bainbridge 1983, Latour 1999 and B.4.1's late-Qing and OTA cases. (H.3)
- *The model's variables as punctualisations*: V, L^R, the trust radius and M are punctualised network effects, and carriers are actants that reopen them. Builds on Law 1992, Latour 1986 and Callon & Latour 1981. (H.4)

**3. Claims that align with existing research but do not extend it.**
- The private crossover is Granovetter's threshold. (B.2)
- Delay until status-quo costs exceed distributional losses is the war of attrition and the crisis hypothesis. (B.2)
- Majorities underestimate support for climate action (pluralistic ignorance). (C.3; Andre et al. 2024; Sparkman et al. 2022) This holds for broad support. For rare, costly behaviours (donating, political engagement) the share acting is *over*estimated (Tiede et al. 2026).
- Attribution weakens as a causal chain lengthens, and legislators anticipate traceability. (G.1; Arnold 1990; Mildenberger & Sahn 2025; Engelmann & Waldmann 2022)
- Shifting baselines and distance decay filter perceived harm. (B.2; Pauly; Moore et al.; Hazlett & Mildenberger)
- The critical fraction is independent of N in proportional models. (C.2)
- Policy change is "delay, then lurch". (App. B §4.3; Jones et al. 2009)
- Incumbents depress φ by manufacturing doubt. (B.4.1; Oreskes & Conway 2010)
- Montreal succeeded because its parameters were unusually favourable. (Part D; Sunstein 2007; Barrett 2003)
- Financial crises are predictable yet unprevented. (App. B; Greenwood et al. 2022)
- Revisions of Norse, Rapa Nui and Angkor "collapse". (App. A §4.1; Dugmore et al.; Moreno-Mayar et al.; Penny et al.)
- Retraining addresses drift but converges to performatively stable, not necessarily optimal, points. (H.2; Perdomo et al. 2020)
- Observational data alone cannot settle interventional questions. (H.2; Bareinboim et al. 2022)
- Automation erodes unused skill and induces complacency and bias. (H.3; Bainbridge 1983; Parasuraman & Manzey 2010)
- Practising with an AI model impairs the formation of unassisted skill, and cognitive skills decay with disuse faster than physical ones. (H.3; Bastani et al. 2025; Arthur et al. 1998; Casner et al. 2014)
- Performative prediction belongs with Barnesian performativity. (H.4; MacKenzie 2006; Hardt & Mendler-Dünner 2023)
- Where harm is delayed and incumbent benefit large, detection is rarely the bottleneck for action. (H.2; rofecoxib; App. C tobacco chain; App. B boundary conditions)

**4. Defensible claims that oppose existing research or doctrine, subject to testing.**
- *Against Olson's group-size law as general*: larger groups are not generally less able to act. Test: group-size effects should appear only where the cost of the good rises with N (P5; large-N public-goods experiments). (C.2)
- *Against Chenoweth's 3.5% as a law*: it is descriptive, for maximalist campaigns. Test: out-of-sample campaigns after 2010 with peak participation above 3.5% that failed. (C.2)
- *Against crisis severity as the reform trigger* (Drazen–Grilli extrapolated): reform follows harm entering the veto radius. Test: P4 and P16, elite exposure and carrier emergence vs severity. (B.4.1; App. A §5.1)
- *Against Rittel & Webber's intrinsic wickedness*: some wickedness is made by policy layers. Test: P17 and P20, wickedness indicators and unwind failure rising with layer count within a domain. (G.2)
- *Against "the polycrisis has no shared mechanism" as a reading of Lawrence et al. 2024*: one micro-mechanism of delay operates across systems. Test: P1, ex-ante parameter coding across domains. (Part E; App. B §6)
- *Against Diamond's collapse cases*: Rapa Nui, the Norse and Angkor are adaptation or gradual change, not chosen failure. Test: further genomic and archaeological dating. (App. A §4)
- *Against Sen's no-famine law as absolute*: a free press and elections lower V but are not sufficient. Test: famine incidence in electoral democracies with a free press. (App. B B5)
- *Against "causal AI opens the black box"* (advocacy, e.g. *SSIR*): an explicit graph is transparent by design but opaque by scale and update rate. Test: P23, and measured time and success of human tracing of outputs from deployed large causal models. (H.3; App. D N3)
- *Against better attribution as a direct route to root reform* (the premise of much causal-AI and digital-twin advocacy): attribution speeds carriers, while reform still waits for V conditions. Test: P22. (H.1, H.5; App. D AT3, AT8)
- *Against social-norms correction as a general lever*: correcting misperceived support raises action only where the barrier is social, the step is cheap and the target is below the norm. Evidence: null or backfire in pensions (Beshears et al. 2015), actual climate donations (Tiede et al. 2026), college drinking (Foxcroft et al. 2015 Cochrane) and health messaging after bias correction (Papakonstantinou et al. 2025). The report's own B.4 and executive point 3 lean on correction of \(\hat r\) as a lever, so this qualifies the report as well as the advocacy literature. Test: P3. (B.4; C.3)

**Tag totals across the main body and Appendices A, B, C and D (see the ledger):** admit 356 · refute 26 · abstain 109. Main body alone: admit 80 · refute 5 · abstain 20.

---

## PART A — Validating the premise

### A.1 Debt and financialisation

| # | Finding | Tag |
|---|---|---|
| A1 | IMF Global Debt Database (Sept 2025, data for 2024): total global debt "just above 235 percent" of world GDP. Public debt is "nearly 93 percent" and private debt "under 143 percent", the lowest since 2015. Total debt peaked at 258% in 2020. In dollars: $251T total, of which $99.2T public. US general government debt is 121% of GDP. | [admit: IMF blog "Global Debt Remains Above 235% of World GDP", 17 Sep 2025, imf.org] |
| A2 | IMF *Fiscal Monitor* (Apr 2026): global public debt was 93.9% of GDP in 2025. It is projected at 95.3% in 2026 and 100% in 2029, a level previously reached only after WWII. Interest costs are about 3% of global GDP, up from 2% four years earlier, and the global "fiscal buffer" has fallen to near zero. Debt-at-risk is approaching 117% of GDP. | [admit: IMF Fiscal Monitor April 2026, "Fiscal Policy under Pressure: High Debt, Rising Risks"] |
| A3 | IIF Global Debt Monitor (23 Sep 2026): global debt hit a record $365.5T in H1 2026. Debt/GDP is about 25 pp below its 2021 peak, mainly because of nominal-GDP inflation. Emerging-market government debt is 76.8% of GDP. | [abstain: non-authoritative source — IIF report is paywalled; figures seen only via press summaries (Investing.com, bne IntelliNews)] |
| A4 | The premise as stated, "debt/GDP is ballooning", is **partly wrong**. *Public* debt/GDP is rising. *Total* debt/GDP has fallen since 2020 and *private* debt/GDP is at a decade low. The correct framing is: public debt is rising toward post-war records, dollar totals are at record highs, and debt-service burdens are rising. | [refute: IMF Global Debt Database 2025 — total debt/GDP below the 2020 peak] |
| A5 | **Definition of financialisation.** Krippner: "a pattern of accumulation in which profits accrue primarily through financial channels rather than through trade and commodity production" (*Socio-Economic Review* 3(2):173–208, p. 174). | [admit: Krippner 2005] |
| A6 | **"Too much finance."** Financial depth starts to reduce output growth when private credit reaches about 100% of GDP. The 2012 working paper gives 80–100%. A "redux" on 1960–2019 data puts the turning point at 70–120%. | [admit: Arcand, Berkes & Panizza 2015, J Econ Growth 20:105–148] |
| A7 | Whether excess finance *causally* lowers growth is contested. Cline (PIIE 2015) shows that any variable rising with income will spuriously show a quadratic "too much" turning point; his analogy is "too many doctors". The authors replied that the result is robust. | [abstain: source-vs-prior conflict — Cline 2015 vs Berkes/Panizza/Arcand 2015 reply] |
| A8 | Reinhart and Rogoff's claim that growth falls sharply once public debt exceeds 90% of GDP. A reanalysis of their own data found coding and weighting errors, a gentler negative relationship, and **no identifiable threshold**. | [refute: Herndon, Ash & Pollin 2014, Camb J Econ 38(2):257–279] |

**Well-established:** record nominal debt; public debt rising toward 100% of GDP; rising interest burdens; the empirical shift of profits toward financial channels in the US since the 1970s (Krippner).
**Contested:** whether there are *thresholds* beyond which debt or finance becomes harmful; whether *total* leverage is still "ballooning" (it is not, relative to GDP); and causal identification in finance–growth regressions.

### A.2 Global warming, ENSO and the AMOC

| # | Finding | Tag |
|---|---|---|
| A9 | 2024 is the warmest year on record, about 1.55 °C ±0.13 above 1850–1900. 2025 was about 1.43 °C, second or third warmest depending on dataset, *despite* La Niña. 2015–2025 are the 11 warmest years, and 2023–25 average about 1.48 °C. Earth's energy imbalance reached a record in 2025. | [admit: WMO State of the Global Climate 2025 (released 23 Mar 2026); WMO COP30 update] |
| A10 | **2026 El Niño.** WMO declared onset on 2 June 2026. On 3 Sep 2026 WMO gave a likelihood of "nearly 100%" that it persists through Feb 2027 and said it would reach "very strong intensity", possibly "off the charts". On 10 Sep, NOAA CPC gave a >90% chance of a very strong event and a 75% chance of a "historic" event exceeding all events since 1950 in Oct–Dec 2026. | [admit: WMO El Niño/La Niña Update, 3 Sep 2026; NOAA CPC ENSO discussion, Sep 2026] |
| A11 | **ENSO under warming (IPCC).** "No model consensus for a systematic change in intensity of ENSO SST variability" (*medium confidence*). However, ENSO *rainfall* variability will *very likely* increase in the second half of the century under SSP2-4.5 and higher. | [admit: IPCC AR6 WG1 Ch. 4 & SPM B.3.2] |
| A12 | Models project that extreme (rainfall-defined) El Niño events roughly double under RCP8.5. | [admit: Cai et al. 2014, Nat Clim Change 4:111–116; Cai et al. 2017 GRL] |
| A13 | Whether the *observed* tropical Pacific is moving toward an El Niño-like state is disputed. Observations show a *strengthening* zonal SST gradient (La Niña-like), which most CMIP models fail to reproduce. Explanations include model cold-tongue bias, internal variability, and Atlantic teleconnections. | [abstain: source-vs-prior conflict — Seager et al. 2019 NCC vs CMIP6 projections; 2026 Nat Commun] |
| A14 | **AMOC (IPCC).** The AMOC "will very likely decline over the 21st century for all SSP scenarios. There is medium confidence that the decline will not involve an abrupt collapse before 2100." Projected 2100 decline: 24% (range 4–46%) under SSP1-2.6, up to 39% (17–55%) under SSP5-8.5. | [admit: IPCC AR6 WG1 Ch. 9 (Fox-Kemper et al. 2021); SPM C.3.4] |
| A15 | *Has the AMOC already weakened?* SST-fingerprint studies say yes (Caesar et al. 2018, about 70-year decline). Terhaar, Vogt and Foukal (2025), using air–sea heat fluxes, find "no decline since the 1960s" in the decadal-mean AMOC at 26.5°N, though reanalysis uncertainty is large. | [abstain: source-vs-prior conflict — Terhaar et al. 2025 Nat Commun 16:222 vs SST-proxy literature] |
| A16 | Ditlevsen and Ditlevsen (2023) estimate a collapse between 2025 and 2095 (95% interval), central estimate 2057. Their proxy and statistical assumptions have drawn substantial criticism (Reschenhofer; experts quoted by the Science Media Centre). | [abstain: source-vs-prior conflict — Nat Commun 14:4254 vs Baker et al. 2025; methodological critiques] |
| A17 | Baker et al. (2025, *Nature* 638:987–994) find that CMIP models show no full AMOC collapse before 2100 even under extreme forcing, because wind-driven Southern Ocean upwelling sustains some North Atlantic sinking. Large weakening still occurs. | [admit: Baker et al. 2025] |
| A18 | Drijfhout et al. (2025, *ERL* 20:094062): in extended CMIP6 runs, deep convection collapses and the northern AMOC shuts down **after 2100** in 67% of very-high-emission runs, 30% of medium and 25% of low. The authors argue AR6's "low-likelihood" framing needs revision in AR7. | [admit: Drijfhout et al. 2025] |
| A19 | van Westen, Börner and Dijkstra (2026, *Nat Clim Change*) show **rate-induced** tipping. With a slow CO₂ ramp the AMOC stays stable to +5.5 °C. With fast ramps it collapses at about +2 °C. So a single "temperature threshold" may be misleading. | [admit: van Westen et al. 2026, doi:10.1038/s41558-026-02730-w] |
| A20 | Global Tipping Points Report 2025: warm-water coral reefs are "crossing" their thermal tipping point (central estimate 1.2 °C, range 1–1.5 °C). The International Coral Reef Society says the point of no return has not yet been reached. | [abstain: source-vs-prior conflict — GTR 2025 (non-journal assessment) vs ICRS statement] |
| A21 | **Polycrisis.** "Global polycrisis" has a scholarly definition: "the causal entanglement of crises in multiple global systems in ways that significantly degrade humanity's prospects". It works through common stresses, domino effects and inter-systemic feedbacks. This is the named concept for the author's "several simultaneous global challenges". | [admit: Lawrence, Homer-Dixon et al. 2024, Global Sustainability 7:e6] |

**Well-established:** warming of about 1.4–1.55 °C; record recent years; a very strong 2026 El Niño; *projected* AMOC weakening this century; amplified ENSO rainfall variability.
**Contested, and presented honestly:**
- the sign of the *observed* tropical Pacific trend and the forced ENSO amplitude;
- whether the AMOC has *already* declined;
- whether a *full collapse* happens this century (Ditlevsen: likely; Baker: no; Drijfhout: shutdown after 2100 is common under high emissions; van Westen: depends on the *rate* of forcing).

The AMOC literature is moving toward "substantial weakening is likely, full collapse is a real but uncertain tail risk, and timing depends on emission rates". That is a different claim from either "imminent collapse" or "nothing to see".

### A.3 Pushback against AI ethicists and safety experts

| # | Finding | Tag |
|---|---|---|
| A22 | **Google.** Timnit Gebru was dismissed on 2 Dec 2020 after a dispute over the "Stochastic Parrots" paper (FAccT 2021, doi:10.1145/3442188.3445922). Google said it "accepted her resignation". Margaret Mitchell was fired on 19 Feb 2021. | [admit: Bender 2022 timeline; MIT Technology Review 4 Dec 2020] |
| A23 | **OpenAI, May 2024.** Superalignment co-lead Jan Leike resigned, writing that "safety culture and processes have taken a backseat to shiny products". The team was disbanded within days. | [admit: Leike's X statement, 17 May 2024, as reported by Wired/IEEE Spectrum] |
| A24 | **US executive branch.** EO 14148 (20 Jan 2025) revoked Biden's EO 14110. EO 14179 (23 Jan 2025), "Removing Barriers to American Leadership in AI", ordered reviews of actions taken under 14110 and required an AI Action Plan (published July 2025). | [admit: EO texts via Federal Register/White House as summarised by OECD.AI & law firms] |
| A25 | **Rhetoric.** At the Paris AI Action Summit (11 Feb 2025), JD Vance said: "The AI future is not going to be won by hand-wringing about safety." He also said: "this doesn't mean... that all concerns about safety go out the window". The US declined to sign the summit declaration. | [admit: U.S. Embassy transcript] |
| A26 | **Renaming the institutes.** The UK AI Safety Institute became the AI *Security* Institute on 14 Feb 2025, dropping bias and freedom-of-speech work. The US AISI became the Center for AI Standards and Innovation on 3 Jun 2025. Lutnick: "censorship and regulations have been used under the guise of national security." | [admit: UK Parliament written statement HCWS462; U.S. Commerce press release 3 Jun 2025] |
| A27 | **Pre-emption.** EO "Ensuring a National Policy Framework for AI" (11 Dec 2025) created a DOJ "AI Litigation Task Force" to challenge state AI laws and tied some federal grants to states avoiding "onerous" AI laws. In March 2026 the White House sent Congress a legislative framework proposing broad pre-emption. | [admit: EO text as summarised by Mayer Brown, Latham & Watkins, Lawfare] |
| A28 | **Anthropic.** On 27 Feb 2026 the Defense Secretary designated Anthropic a "supply chain risk" after it refused uses for mass domestic surveillance and fully autonomous weapons. The President ordered agencies to stop using Anthropic's models. The designation was formalised in March. | [admit: CBS News, Axios, Mayer Brown, Venable] |
| A29 | A divided D.C. Circuit panel reportedly upheld that designation (2–1, Katsas J.) around late Sep 2026. | [abstain: non-authoritative source — single low-reliability outlet] |
| A30 | **OpenAI, Oct 2026.** OpenAI fired safety researchers Korbak, Balesni and Wang. The researchers say they were dismissed for raising safety concerns and contacting METR. OpenAI cites a "significant breach of trust" and says the dismissals were "not about raising safety concerns". | [abstain: unverifiable — facts actively disputed between parties] |
| A31 | **EU.** The Digital Omnibus on AI (provisionally agreed 7 May 2026, final EP vote 16 Jun 2026) delays Annex III high-risk obligations to 2 Dec 2027 and Annex I obligations to 2 Aug 2028. Article 50 transparency obligations keep the Aug 2026 date. This is *delay*, not repeal. | [admit: Gibson Dunn; Morgan Lewis; Hogan Lovells analyses of adopted text] |
| A32 | **Counter-evidence.** The Senate struck the 10-year state-law moratorium 99–1 (1 Jul 2025), with opposition from 17 Republican governors and 40 attorneys general. California's SB 53 (frontier AI transparency) was signed 29 Sep 2025 and took effect 1 Jan 2026. | [admit: Senate Commerce Committee release; FPF/White & Case analyses] |
| A33 | **Public opinion.** About 6 in 10 US adults and 56% of AI experts worry more that government will *not go far enough* in regulating AI than that it will go too far (surveys fielded in 2024). A Sept 2025 Pew poll found 57% rate AI's societal risks as high. | [admit: Pew Research Center, 3 Apr 2025] |
| A34 | Describing this as a *global* pushback overstates it. The evidence is concentrated in the US federal executive, with UK alignment and an EU delay. China signed the Paris declaration, and US states and Congress have partly resisted. | [abstain: unverifiable — no systematic cross-national dataset consulted] |

**Well-established:** documented dismissals and departures (2020–24); a sharp change of US federal posture and vocabulary in 2025–26 ("safety" replaced by "security", "innovation" and "dominance"); renamed institutes; a federal pre-emption campaign; the Anthropic designation; EU delays.
**Contested:** motives behind specific firings; whether this is "anti-safety" or "anti-regulation/anti-'woke' AI" (officials say the latter); whether it is global or largely American. It is also contested whether pushback reflects the public: it does not, since US majorities want more regulation. That supports the author's broader claim that *elites insulated from consequences* can delay action against majority preference (see B-table: Diamond; Alesina–Drazen).

---

## PART B — Why societies wait until the last moment

### B.1 The author's hypothesis, stated formally

Paraphrasing: individual *i* keeps supporting a system (credit, fossil energy, an AI tool) while the **localised net benefit** \(L_i(t)\), accrued inside *i*'s circle of particularised trust, exceeds the **perceived generalised harm** \(H_i(t)\) of the wider challenge. Collective action begins only when, for enough people, \(H_i(t) > L_i(t)\). This holds even though (a) harms and benefits are unevenly distributed, (b) the threat was foreseen, and (c) distant others face existential consequences.

A compact model that combines the author's terms with Granovetter's:

$$
\text{act}_i(t) = \mathbb{1}\big[\, \underbrace{H_i(t) - L_i(t)}_{\text{private crossover}} \;+\; \beta\, \hat r_i(t) \;>\; \kappa_i \,\big]
$$

- \(\hat r_i(t)\) is *i*'s perceived share of others already acting (the social component).
- \(\beta\) is susceptibility to that social signal.
- \(\kappa_i\) is the personal cost of acting.
- Each term corresponds to a literature below:
  - \(L_i\) restricted to the trust radius: Uslaner, Fukuyama, Banfield.
  - \(H_i\) discounted by distance and time: Carney, Weber, Gardiner.
  - The baseline against which \(H_i\) is judged drifts: Pauly, Moore et al.
  - \(\hat r_i\) is biased downward: Kuran, Sparkman, Andre.
  - Elites with large \(L_i\) and small \(H_i\) can veto: Diamond, Alesina–Drazen.

### B.2 Mapping each element of the hypothesis to named concepts

| Element of the author's hypothesis | Closest named concept(s) | What the source actually says | Fit | Tag |
|---|---|---|---|---|
| Act only when net benefit of acting turns positive | **Threshold** (Granovetter 1978) | Threshold = "the number or proportion of others who must make one decision before a given actor does so; this is the point where net benefits begin to exceed net costs for that particular actor" (AJS 83:1420). | Very close; adds the social term | [admit: Granovetter 1978, read in full this session] |
| Reform delayed until status-quo costs rise enough | **War of attrition / delayed stabilisation** (Alesina & Drazen 1991) | Groups try to shift the burden of stabilisation onto others; stabilisation happens "only when one group concedes". Higher costs of instability bring the date forward. Delay requires incomplete information about others' costs. | Very close on mechanism (distributional) | [admit: Alesina & Drazen 1991, AER 81(5):1170–88] |
| Pain must exceed *one's own* distributional loss | **Crisis hypothesis** (Drazen & Grilli 1993) | In a crisis, "the extreme welfare loss each agent suffers dwarfs the loss he may associate with an unfavorable distribution of the burden" of reform. The authors warn crises are not socially desirable if policymakers are biased. | **Closest formal statement** of the author's crossover | [admit: Drazen & Grilli 1993, AER 83(3):598–607 (quoted via J. Dev. Studies 2010)] |
| …and empirically, only at extremes | Crisis-induces-reform tests | Evidence for the hypothesis appears only at *extreme* inflation or black-market premia, not for deficits or recessions. Crises must be "very deep". | Supports "last moment" for modern macro stabilisation only; it does not show that reform needs an extreme crisis in general (see B.4.1) | [admit: Drazen & Easterly 2001, Econ & Politics 13(2):129–58] |
| Uncertain winners resist reform | **Status-quo bias from individual-specific uncertainty** (Fernandez & Rodrik 1991) | Reforms that would win ex post fail ex ante when individual gainers cannot be identified; this needs no risk aversion or irrationality. About 1,160 citations (Semantic Scholar). | Explains uneven distribution | [admit: Fernandez & Rodrik 1991, AER 81(5):1146–55] |
| Benefits computed inside personal circles | **Particularised vs generalised trust** (Uslaner 2002) | Particularised trust is faith "only... in people like ourselves" and "restricts the size of our moral community"; generalised trust is that "most people can be trusted". Uslaner compares the split to Putnam's bonding vs bridging. | Direct match | [admit: Uslaner, *Moral Foundations of Trust*, CUP 2002, ch. 2] |
| Size of that circle | **Radius of trust** (Fukuyama 1999/2001; Delhey, Newton & Welzel 2011) | In 41 of 51 countries "most people" means out-groups, but the radius varies widely. "Trust is only civic in nature when the radius is wide." | Direct match; measurable | [admit: Delhey et al. 2011, ASR 76(5):786–807] |
| Extreme particularism | **Amoral familism** (Banfield 1958) | "Maximize the material, short-run advantage of the nuclear family; assume that all others will do likewise." | Concept matches; its empirical basis is disputed (Miller 1974 failed to support it) | [admit: concept, Banfield 1958] |
| Short-termism and future victims | **Tragedy of the horizon** (Carney 2015) | Climate change "imposes a cost on future generations that the current one has no direct incentive to fix"; impacts fall "beyond the traditional horizons of most actors". | Close (time axis) | [admit: Carney, BoE speeches 2015/2018] |
| Foreseen but not acted on | **Predictable surprise** (Bazerman & Watkins 2003/2004) | Disasters leaders had the information to anticipate. Failure can occur at Recognition, Prioritisation or Mobilisation, with cognitive, organisational and political roots (special interests). | Close (foreseen threat) | [admit: Watkins & Bazerman, HBR 81(3):72–80; HBS Press 2004] |
| Same | **Gray rhino** (Wucker 2016) | High-probability, high-impact, neglected threat. | Close | [abstain: unverifiable — not checked this session] |
| Causers are also the solvers; no central authority; time running out | **Super wicked problems** (Levin et al. 2012) | Four features: time is running out; those causing the problem seek to solve it; central authority is weak or absent; policies "discount the future irrationally". | Close (structural) | [admit: Levin et al. 2012, Policy Sci 45:123–152] |
| Global, intergenerational, theoretical dispersion; self-serving rationalisation | **Perfect moral storm / moral corruption** (Gardiner 2006, 2011) | Dispersion of causes and effects, fragmentation of agency, institutional inadequacy, plus "generational buck-passing". These make us vulnerable to "moral corruption". | Close (ethics) | [admit: Gardiner 2006, Env Values 15(3):397–413] |
| Elites benefit while others pay | **Rational bad behaviour; elite insulation** (Diamond 2005, ch. 14) | "Some people may reason correctly that they can advance their own interest by behavior harmful to other people." It is especially bad when elites are insulated from the consequences. Road map: failure to anticipate, failure to perceive, failure to try, failure of solutions. | Direct for the "uneven distribution" clause | [abstain: non-authoritative source — quoted via reading notes and summaries only; see App. B M34] |
| Slow change goes unnoticed | **Creeping normalcy / landscape amnesia** (Diamond); **shifting baseline syndrome** (Pauly 1995) | Each generation "accepts as a baseline the stock size... that occurred at the beginning of their careers". About 1,560 references in 25 years (WoS, per Alleway 2023). | Explains why \(H_i\) is under-perceived | [admit: Pauly 1995, TREE 10(10):430] |
| Measured baseline drift | Empirical shifting baseline | The reference for "normal" weather is weather experienced **2–8 years** earlier. Extreme temperatures become less *remarkable* but not less *negative* (the "boiling frog"). | Strong empirical support | [admit: Moore et al. 2019, PNAS 116:4905–10] |
| Experience vs description | **Experience-based risk perception; finite pool of worry** (Weber 2006) | Visceral reactions depend on personal experience, so description-based climate risk feels low. Concern for one risk may crowd out others. | Explains low \(H_i\) | [admit: Weber 2006, Clim Change 77:103–120] |
| Local pain moves behaviour | Disaster-exposure effects | Wildfire within 5 km raised support for costly climate ballot measures by 5–6 pp, decaying to about 0 beyond 15 km, and **only in Democratic areas**. | Supports the "local" clause, but shows a partisan filter | [admit: Hazlett & Mildenberger 2020, APSR 114(4):1359–65] |
| …but the effect is modest | Systematic review | "Modest support" for the link between weather experience and climate opinion (73 studies). | Weakens the "pain will tip it" clause | [admit: Howe et al. 2019, ERL 14:113001] |
| Defending the system that benefits me | **System justification** (Jost) | System-justification tendencies mediate environmental denial. The intervention framing change as "patriotic" failed to replicate robustly. | Explains attachment to \(L_i\) | [admit: Feygina, Jost & Goldsmith 2010, PSPB 36:326–38; IRSP replication] |
| Finance: good times breed fragility | **Financial instability hypothesis** (Minsky) | "Over periods of prolonged prosperity, the economy transits from financial relations that make for a stable financial system to financial relations that make for an unstable system" (hedge → speculative → Ponzi finance). | The credit version of the hypothesis | [admit: Minsky 1992, Levy WP 74, p. 8] |
| Finance: forgetting the last disaster | **Disaster myopia** (Guttentag & Herring) | Lenders' subjective default probabilities decline during long favourable periods: "the worst of loans are made in the best of times". | Close (credit) | [admit: Guttentag & Herring 1986, Princeton Essays in Int'l Finance 164; Herring 2017] |
| When complexity stops paying, people defect | **Declining marginal returns to complexity** (Tainter 1988) | When the marginal cost of complexity becomes too high, parts of society increase resistance or try to break away. | Matches "benefit erodes, then exit" | [admit: Tainter 1988 (via Schumacher Center excerpts)] |
| Group size defeats action | **Logic of collective action** (Olson 1965) | "Unless the number of individuals in a group is quite small, or unless there is coercion... rational, self-interested individuals will not act to achieve their common or group interests" (p. 2). | Classic, but not general (see C) | [admit: Olson 1965 p. 2 (wording)] |
| Others will act, so I won't | **Diffusion of responsibility / volunteer's dilemma** | Diekmann formalises Darley and Latané. In equilibrium, individual volunteering falls with N. Darley and Latané's own data showed a *slightly increasing* chance that *someone* helps. | Partly supports | [admit: Diekmann 1985, J Conflict Resolution 29:605–10] |
| Commons are destroyed | Tragedy of the commons (Hardin 1968) vs **Ostrom** (1990, 2010): communities with appropriate institutions and polycentric governance can manage commons | Ostrom 2010 Nobel lecture (AER 100(3):641–72) confirmed as source. I did not re-read its specific Hardin critique this session. | Ostrom shows the outcome is *not* inevitable | [abstain: unverifiable — Hardin text and Ostrom's design principles not read this session] |
| Too late to steer technology | **Collingridge dilemma** (1980) | "When change is easy, the need for it cannot be foreseen; when the need for change is apparent, change has become expensive, difficult and time consuming." | Exact for AI | [admit: quoted via Morozov 2012/Liebert & Schmidt 2010] |
| Fear of isolation silences dissent | **Spiral of silence** (Noelle-Neumann 1974) | Meta-analysis: very small effect (r ≈ .05). An updated meta-analysis finds r ≈ .10, with the strongest silencing (r ≈ .34) among **family, friends and neighbours**. | Interesting: silence is strongest *inside* particularised-trust circles | [admit: Glynn, Hayes & Shanahan 1997 POQ 61:452; Matthes et al. 2018 Comm Res] |
| Hidden private dissent | **Preference falsification** (Kuran 1991, 1995) | Public vs private preferences diverge under social pressure, so revolutions surprise. The same falsification hides the forces at work afterwards. | Core of the "iceberg" | [admit: Kuran 1991 World Politics 44(1):7–48] |
| Bystander effect, loss aversion, status-quo bias, hyperbolic discounting | Darley & Latané 1968; Kahneman & Tversky 1979; Samuelson & Zeckhauser 1988; Laibson 1997 | Standard behavioural mechanisms that raise \(\kappa_i\) and discount \(H_i\). | Supporting | [abstain: unverifiable — classics, not re-checked this session] |
| Punctuated change | Baumgartner & Jones 1993 (punctuated equilibrium); Kingdon 1984 (policy windows); Overton window | Long stasis, then rapid change when attention and coupled "streams" align. | Describes the *shape* of delay-then-rush | [abstain: unverifiable — not re-checked] |
| Risk society, denial, exit/voice | Beck 1986/1992; Norgaard 2011; Jamieson 2014; Hirschman 1970; Putnam 2000; Fukuyama 1995; Olson 1982 | Manufactured risk; socially organised denial; exit vs voice when quality declines; bonding vs bridging capital; distributional coalitions. | Supporting | [abstain: unverifiable — not re-checked] |

### B.3 Does a precise named term exist?

- **No single canonical term** captures "benefit computed within particularised trust; act only when generalised harm exceeds it". [abstain: unverifiable — absence of evidence; I searched for it but cannot prove a negative]
- **Closest single terms, by discipline:**
  - *Economics:* **crisis hypothesis** (Drazen & Grilli 1993), with **war of attrition** (Alesina & Drazen 1991) as the mechanism. This is the most precise match for "wait until the pain exceeds one's own distributional gain".
  - *Sociology/complexity:* **threshold** (Granovetter), defined as the net-benefit crossover.
  - *Political science/management:* **predictable surprise**; **super wicked problem**.
  - *Trust literature:* **radius of trust** / **particularised trust** for the "circle".
  - *Ethics:* **moral corruption** within a **perfect moral storm**.
- **Suggested coinage** if the author wants one: a *radius-bounded crisis threshold*. That is a Granovetter-type threshold where the private benefit term is summed only over the trust radius, as in Delhey et al., and the trigger follows the Drazen–Grilli crossover.

### B.4 The radius-bounded threshold model

**Starting point.**
- The crossover hypothesis makes the *private crossover* \(H_i > L_i\) the binding constraint.
- The evidence shows majorities often *already* privately favour action. So the crossover is one term, but not the sole bottleneck.
- Three further constraints complete the model:
  - a **perception filter** on harm;
  - a **socially biased coordination term**;
  - an **elite or institutional veto**.
- Population size governs **time to tip**, not the required fraction.

**Restated in prose.** Societies delay addressing foreseen global challenges because of four compounding mechanisms, not chiefly because individuals privately value the incumbent system more than they fear the wider harm:
1. **Filtered harm.** Each person perceives generalised harm through a filter. The filter discounts distance, resets to a shifting baseline within a few years, and passes through partisan and identity screens. Private concern therefore rarely becomes a *felt* crossover.
2. **Misperceived peers.** People underestimate how many others share their concern (pluralistic ignorance). Silence is strongest *inside* circles of particularised trust. So the social term that would tip them stays below threshold.
3. **Vetoes held by the insulated.** Those with the largest localised benefit and the least exposure to harm hold veto power. Reform tends to arrive when a crisis raises the cost of the status quo *to them*, as in a war of attrition and the crisis hypothesis, or when they are displaced (B.4.1). It does not arrive when the median citizen's crossover occurs.
4. **Metastability scales with size.** The *fraction* needed to tip a population does not depend on its size. But the *time* to tip from just below critical mass grows exponentially with size. Large societies can stay stuck for a long time and then reorganise abruptly, which is a formal account of "the last moment".

**Formal model.**

Individual decision:

$$
\text{act}_i(t) = \mathbb{1}\Big[\, \underbrace{\varphi_i\big(d_i,\; t - t^{\text{base}}_i,\; \pi_i\big)\, H_i(t)}_{\text{filtered generalised harm}} \;-\; \underbrace{L_i^{R_i}(t)}_{\text{benefit within trust radius } R_i} \;+\; \beta\, \underbrace{\big(r(t) - \delta_i\big)}_{\hat r_i:\ \text{perceived peers}} \;>\; \kappa_i \,\Big]
$$

- \(\varphi_i \in [0,1]\) is the perception filter. It falls with distance \(d_i\) (wildfire effects vanish beyond about 15 km). It resets as the baseline \(t^{\text{base}}_i\) renormalises (2–8 years). It is gated by partisan or identity alignment \(\pi_i\). [admit: Hazlett & Mildenberger 2020; Moore et al. 2019; Howe et al. 2019]
- \(\delta_i > 0\) is the pluralistic-ignorance bias: true support is underestimated by about 26 pp worldwide. [admit: Andre et al. 2024; Sparkman et al. 2022]
- \(L_i^{R_i}\) is summed only over \(i\)'s radius of particularised trust. [admit: Uslaner 2002; Delhey et al. 2011 for the radius concept]

Collective reform time:

$$
t^{*} = \min\big\{\, t \;:\; r(t) \ge r_c \;\;\wedge\;\; P\big(r(t)\big) > V(t) \,\big\}
$$

- \(r(t)\) is the share actually acting, and \(r_c\) is the critical fraction for a cascade.
- \(P\) is the political pressure the cascade generates.
- \(V(t)\) is the veto held by actors with large \(L^{R}\) and small \(\varphi H\).
- In the war-of-attrition reading, \(V(t)\) falls only as the cost of the status quo to the veto players rises. B.4.1 specifies which costs count. [admit: Alesina & Drazen 1991; Drazen & Grilli 1993; Drazen & Easterly 2001. Diamond 2005 ch. 14 is abstained in B.2]

Scaling:

$$
r_c \perp N, \qquad n_c = r_c N, \qquad
\mathbb{E}[T_{\text{tip}}] \sim
\begin{cases}
e^{\,cN} & p < p_c \ \ (\text{committed minority below critical})\\[2pt]
\ln N & p > p_c
\end{cases}
$$

[admit: Granovetter 1978; Xie et al. 2011; Centola et al. 2018. On networks, local structure dominates N: Watts 2002]

**Reading the variables.** V, L^R, the trust radius R and M are punctualisations (Law 1992): summaries of networks of associations that are continually performed and maintained, not pre-given structural forces. The formal model is a black-boxed description of network effects, and each variable's value has to be traced case by case (H.4 point 3).

**What the crossover intuition contributes.**
1. *The localised-benefit term still matters.* It now does its work mainly through the **veto players**, whose \(L^{R}\) is large and whose \(\varphi H\) is small, and through the marginal actors near threshold. It does not work through the median citizen.
2. *The trust radius now enters three terms, not one.* This strengthens the author's intuition.
   - It sets the domain of \(L\).
   - It partly sets the distance decay in \(\varphi\), because social distance compounds geographic distance.
   - It shapes the bias \(\delta\). The spiral-of-silence meta-analysis finds silencing strongest among family, friends and neighbours (r ≈ .34 vs ≈ .10 overall). [admit: Matthes et al. 2018]
   - So a narrow trust radius both inflates the benefit that is defended and hides the support that would overturn it. [abstain: unverifiable — novel synthesis, untested]
3. *"Even if they see it coming"* is now explained without irrationality. Foresight raises \(H\), but \(\varphi\) and \(\delta\) keep that foresight from becoming a felt crossover or a visible cascade, and \(V\) blocks the cascade that does form.

#### B.4.1 Extensions from deep history and cross-system evidence

Appendices A and B support the core model and require four further elements.

1. **The veto depends on elite exposure.** The veto is not a fixed obstacle that crisis pressure must overcome. It depends on harm inside the elite's own radius, on the elite's incumbent benefit, and on identity sorting:

$$
V(t) = V_0 \;-\; \gamma\, H_{\text{elite}}(t) \;+\; \delta\, L^{R}_{\text{elite}}(t) \;+\; \sigma\, \Pi(t)
$$

   - When harm reaches the veto holders, or their incumbent benefit turns negative (cheap substitutes), \(V\) falls and can reverse sign. The elite then becomes the *initiator*, as with the Great Stink, the Dust Bowl, Tokugawa forestry, Venice and Montreal.
   - \(\Pi\) is partisan or identity polarisation. Under high \(\Pi\), a crisis can *raise* \(V\).
   - Sources: Synthesis across findings admitted in App. A §4–6 and App. B B2, B8 (Luca et al. 2020; Graham & Svolik 2020). The elite-exposure clause is a hypothesis tested by P4.
2. **Institutional memory resists shifting baselines.**

$$
\varphi_i = \varphi_0\, e^{-\lambda\,(t - t^{\text{base}}_i)} + M
$$

   - \(M\) is built by past disasters and maintained by standing institutions.
   - It explains why *recurrent* hazards are routinely pre-empted and *first-encounter* hazards are not. It also predicts that \(M\) erodes as fiscal capacity falls (late-Qing granaries).
   - \(\varphi\) is also **endogenous to \(V\)** when incumbents control information: leaded petrol, tobacco, the doubt merchants.
   - Sources: [admit: Riris et al. 2024; Will & Wong 1991; EEA 2013; Oreskes & Conway 2010].
3. **Exit branch.** Reform is not guaranteed eventually:

$$
t^{*} = \min\big\{\, t : \big[r(t) \ge r_c \wedge P(r(t)) > V(t)\big] \;\vee\; V(t)\to 0 \text{ exogenously} \,\big\}
$$

   - The historical alternatives to cascade-driven reform are **elite displacement, collapse or exit**, as when Angkor's elites left first.
   - Pressure can remain below \(V\) indefinitely.
   - Sources: [admit: Hoyer et al. 2024/25 CrisisDB; Penny et al. 2019].
4. **Externality leakage.** Pre-emption *within* a radius can export harm beyond it: Venice protected the lagoon at the mainland's expense. Radius-bounded success is not the same as welfare-improving success overall. [Synthesis, App. A §7.2]

**Reconciling the crisis evidence.**
- Drazen & Easterly (2001) find that crises are associated with *modern macroeconomic* reform only at *extreme* levels (hyperinflation, very high black-market premia). They do not show that reform requires an extreme crisis.
- CrisisDB (pre-modern societies) and Nohrstedt et al. (2021, 85 countries) find reform uncorrelated with severity.
- These are compatible: the condition the crisis meets is not severity as such. Hyperinflation and black-market premia are crises that fall directly on governing elites and their fiscal base. Many disasters fall elsewhere.
- So the model's hypothesis is: **crisis triggers reform when, and to the extent that, it enters the veto holders' radius.** [Synthesis across admitted findings; untested as a general law, see P4]

**Scope.**
- The model is the dominant route to delay for **commons and mass-behaviour problems**: slow-onset, diffuse harm, concentrated benefit, large N.
- Where few decision-makers decide (regulatory capture, organisational incubation), \(L^R\) plus \(V\) suffices and the \(\hat r\) cascade term is idle.
- Where the bottleneck is signal detection inside an expert organisation (Pearl Harbor, 9/11), the model is the wrong tool. [admit: App. B §4–5]

Testable predictions and falsification tests are consolidated in **Part F**.

---

## PART C — The mathematics of required sentiment change

### C.1 Granovetter's threshold cascade (1978)

Let \(F(x)\) be the CDF of thresholds, the share of the population whose threshold is ≤ \(x\). Let \(r(t)\) be the share acting at time \(t\). Then:

$$ r(t+1) = F\big(r(t)\big) $$

"It follows immediately that the process is described by the difference equation r(t+1) = F[r(t)]" (p. 1425).

- **Equilibrium:** \(r^\* = F(r^\*)\). Starting from \(r_0\), the process stops at the **first crossing of F with the 45° line from above**. A full cascade requires \(F(r) > r\) for all \(r \in [r_0, 1)\).
- **Stability:** a fixed point is stable if \(F'(r^\*) < 1\).
- **Fragility:** with uniform thresholds \(\{0,1,…,99\}\) everyone joins. Replace the threshold-1 person with a second threshold-2 person and **only one** person acts (p. 1424–5). Near-identical populations can produce opposite outcomes. This is the formal version of the essay's sandpile metaphor.
- **Fraction or count:** footnote 3 says "thresholds may usefully be described as either proportions or absolute numbers. The mathematical analysis is the same in either case."
- **Misperception:** Granovetter explicitly models people who "systematically misperceive the proportion of others who have... joined" (p. 1437). This is where pluralistic ignorance enters.

[admit: Granovetter 1978, AJS 83(6):1420–1443, PDF read this session]

### C.2 Does the required fraction scale with N?

**Case 1: proportional thresholds (mean-field).** \(F\) is defined on fractions, so the critical fraction \(r_c\) (the smallest seed that leads to a full cascade) is **independent of N**. The required absolute number is \(A_c = r_c N\), which grows linearly with N. [admit: follows directly from C.1 definitions]

**Case 2: absolute thresholds.** If individual *i* needs to see \(k_i\) others act, a proportional representation is \(\theta_i = k_i/N\). For a fixed distribution of \(k\), every \(\theta_i \to 0\) as \(N\) grows. In large populations, cascades become *easier* and the required fraction falls roughly as \(1/N\). This becomes realistic once mass media make absolute crowd counts visible: Lohmann's Leipzig turnout signals, or Chenoweth's "11 million". [admit: derivation from Granovetter fn. 3; whether people actually use absolute counts is an empirical question → see C.5]

**Case 3: networks (Watts 2002).** A node with degree \(k\) is *vulnerable* if its threshold \(\phi \le 1/k\), with probability \(\rho_k = P(\phi \le 1/k)\). Global cascades are possible only if the vulnerable cluster percolates:

$$ \sum_k k(k-1)\,\rho_k\, p_k \;>\; z, \qquad z=\langle k\rangle $$

The condition depends on the **degree distribution and threshold distribution, not on N**. More heterogeneous thresholds increase vulnerability; more heterogeneous degree decreases it. [admit: Watts 2002, PNAS 99:5766–71 — percolation condition confirmed; expanded summation form is the standard rendering of his eq. 5 (G₀″(1)=z boundary)]

**Case 4: committed minorities (binary-agreement naming game).** A fraction \(p\) of agents never changes opinion. In the mean-field case there is a critical \(p_c \approx 10\%\):

$$ T_c \sim e^{\alpha(p)N}\ \ (p<p_c), \qquad T_c \sim \ln N\ \ (p>p_c) $$

The *fraction* is scale-free, but **below the critical fraction, the time for a larger society to flip grows exponentially with its size**. This is the most important scaling result for the author. A large society can stay "stuck" for an effectively unbounded time just below the critical mass, then flip quickly once over it. [admit: Xie et al. 2011, PRE 84:011130, abstract read verbatim]

**Case 5: experimental conventions (Centola et al. 2018).** A committed minority of about **25%** tipped the convention (largest failed minority 21%, smallest successful 25%; about 72% uptake above the threshold). The predicted critical mass **rises with agents' memory length** M and stays below 50%. The authors say 25% is "not expected to be a universal value". [admit: Centola, Becker, Brackbill & Baronchelli 2018, Science 360:1116–19] Group sizes in the experiment were small, roughly 20–30 per group. [abstain: unverifiable — exact N not confirmed this session]

**Case 6: Olson, and its refutation as a general law.** Olson's free-rider logic, simplified: *i* contributes iff \(F_i V_g(T) - C(T) > 0\), where \(F_i\) is *i*'s share of the group's gain. If \(F_i \approx 1/N\) and the cost of the good grows with N (zero jointness of supply), contributions fail as N grows.
- Oliver & Marwell show the sign depends on costs. If the costs of the collective good vary little with group size, "larger groups should exhibit more collective action", because they are more likely to contain a critical mass of highly interested, resourceful actors. This effect is stronger with heterogeneity and non-random social ties. [admit: Oliver & Marwell 1988, ASR 53:1–8]
- In VCM experiments with N = 4, 10, 40 and 100, "groups of 40 and 100 provided the public good more efficiently than groups of 4 and 10". [admit: Isaac, Walker & Williams 1994, J Pub Econ 54:1–36]
- The blanket claim "larger groups are less able to act collectively" is therefore false as a general law. [refute: Oliver & Marwell 1988; Isaac et al. 1994]

**Case 7: volunteer's dilemma (diffusion of responsibility).** With \(m+1\) players and normalised cost \(c<1\), the symmetric mixed equilibrium is:

$$ p^\* = 1-c^{1/m}, \qquad P(\text{provided}) = 1 - c^{(m+1)/m} \;\to\; 1-c \text{ as } m\to\infty $$

Individual effort falls with group size and the chance that *nobody* acts rises toward \(c\). Lab evidence does not show a clean monotonic effect. [admit: Diekmann 1985 as restated by Konrad 2025; Tinbergen large-N experiment]

**Case 8: the 3.5% rule (Chenoweth & Stephan).** No government withstood a campaign whose **peak** event mobilised 3.5% of the population. Chenoweth's own caveats (2020):
- it is "descriptive... not necessarily prescriptive";
- it applies only to *maximalist* campaigns (overthrowing a government or winning independence);
- only 17 of 169 nonviolent campaigns (10%) reached 3.5%;
- "among all maximalist nonviolent campaigns that did succeed, **83% did so without crossing** the 3.5% threshold";
- Bahrain (2011–14) failed at over 6%;
- "it's a rule, not a law";
- whether it applies to climate or other reformist campaigns: "No one knows."

[admit: Chenoweth 2020, Carr Center DP 2020-005, read this session]
- She notes that 3.5% "is a large absolute number... In the U.S. today, 3.5% would be well over 11 million". The 2017 Women's March was 1–1.6%. So she treats the threshold as a fraction while recognising the absolute logistics. [admit: same]
- Success rates of nonviolent revolutions fell from about 65% in the 1990s to **below 34% since 2010**. [admit: Chenoweth 2020, J Democracy 31(3):69–84]
- Treating 3.5% as a law or a sufficient condition is wrong. [refute: Chenoweth 2020 Carr Center DP]

**Case 9: social tipping in climate.** Otto et al. (2020) identify six social tipping elements: energy, settlements, financial markets, norms, education, and information feedbacks. [admit: Otto et al. 2020, PNAS 117:2354–65] The concept is widely overused, with premature labelling, missing system boundaries, and missing evidence of feedbacks or multistability. [admit: Milkoreit 2023, WIREs Clim Change 14:e813] Whether these interventions *will* stabilise climate by 2050 is unproven. [abstain: source-vs-prior conflict — Smith et al. 2020 PNAS letter; Milkoreit 2023]

**Verdict on scaling.**
1. In all canonical *proportional* models (Granovetter, naming-game committed minorities, Centola), the **critical fraction is scale-invariant**, so the **absolute number scales ~linearly with N**. [admit: Granovetter 1978; Xie 2011; Centola 2018]
2. The **time** to reach consensus scales with N, exponentially below the critical fraction and logarithmically above it. Large populations just short of critical mass can stay stuck indefinitely. [admit: Xie et al. 2011]
3. On networks, **structure (degree, clustering, threshold heterogeneity) dominates N**. [admit: Watts 2002]
4. If people react to **absolute counts**, the required *fraction* falls as N grows. Olson-type cost scaling makes it rise. The net direction is empirical. [admit: Granovetter fn. 3; Oliver & Marwell 1988]
5. **No universal fraction exists for real societies.** The candidates are about 10% (Xie, theoretical), about 25% (Centola, experimental, memory-dependent) and 3.5% (Chenoweth, descriptive, peak participation, maximalist campaigns only). They measure different things and should not be compared directly. [refute: claim of a universal tipping fraction — Centola 2018 ("not universal"), Chenoweth 2020 ("rule, not law"), Bahrain case]

### C.3 Pluralistic ignorance, spiral of silence and preference falsification: the "iceberg"

| # | Finding | Tag |
|---|---|---|
| C1 | Chenoweth: "large-scale participation is usually **the tip of the iceberg**, and there is usually much broader public support for the movement than the people who are active in the streets… there is no way to calculate how much popular support is needed… without comprehensive opinion polling." She also warns that organising only for turnout benchmarks "may create a loud but wildly unpopular minority". | [admit: Chenoweth 2020 Carr Center DP, p. 3] |
| C2 | USA (N = 6,119): "While 66–80% Americans support these policies, Americans estimate the prevalence to only be between 37–43% on average." 80–90% of people underestimate support. The authors call this a "false social reality". | [admit: Sparkman, Geiger & Weber 2022, Nat Commun 13:4779] |
| C3 | World (125 countries, ~130,000 people): 69% willing to contribute 1% of income; 86% endorse pro-climate norms; 89% demand more political action. People "systematically underestimate" others' willingness, and conditional cooperation means this misperception suppresses action. | [admit: Andre, Boneva, Chopra & Falk 2024, Nat Clim Change 14:253–59] |
| C4 | The size of that global perception gap is 26 percentage points: 69% actually willing vs 43% perceived. | [admit: Andre et al. 2024 full text (PDF); University of Bonn release on the paper] |
| C5 | **Complication.** In five preregistered experiments (N = 5,081), people **overestimated rare actual behaviours** (others' donating and political engagement) while underestimating broad support. Correcting misperceptions changed *stated* donation willingness but **not actual donations**. | [admit: Tiede, Maur, Betsch et al. 2026, Nat Clim Change, doi:10.1038/s41558-026-02668-z] |
| C6 | Kuran: hidden private opposition plus threshold-based public expression produce sudden, unpredictable cascades. 1989 is the paradigm case. | [admit: Kuran 1991] |
| C7 | Lohmann: each turnout reveals hidden private information about the regime. Cascades end as their informational role is exhausted (Leipzig, 42 Monday demonstrations). | [admit: Lohmann 1994, World Politics 47(1):42–101] |
| C8 | Spiral-of-silence effects are small on average (r ≈ .05–.10). The largest effect (r ≈ .34) is **within family, friends and neighbours**. | [admit: Glynn et al. 1997; Matthes et al. 2018] |

**A worked "iceberg" formulation.**

Let \(N\) be the population, \(s\) the share of **latent sympathisers** (private preference for change), and \(a\) the share **actively participating**. Define the iceberg ratio as

$$ I = \frac{s}{a}. $$

Among sympathisers, let \(G(\cdot)\) be the CDF of *participation thresholds* over **perceived** participation \(\hat a\). Participation then follows Granovetter's dynamics, restricted to the iceberg:

$$ a(t+1) = s \cdot G\big(\hat a(t)\big), \qquad \hat a(t) = \lambda\, a(t) $$

- \(\lambda<1\) is the *pluralistic-ignorance discount* (underestimation).
- At a fixed point, \(a^\* = s\,G(\lambda a^\*)\), so \(I^\* = s/a^\* = 1/G(\lambda a^\*)\).
- The iceberg ratio is simply the reciprocal of the share of sympathisers whose threshold has been met.

A cascade from seed \(a_0\) requires \(s\,G(\lambda a) > a\) for all \(a \in [a_0, s)\). Three levers follow, each tied to a literature:
1. raise \(s\): persuasion, or experienced harm (Weber; Hazlett & Mildenberger);
2. raise \(\lambda\) toward 1: correct misperception (Sparkman; Andre), which Tiede et al. show is not always enough;
3. shift \(G\) left by lowering costs or raising the salience of absolute counts (Chenoweth; Lohmann).

**Illustrative numbers** (assumptions, not estimates):
- With \(s = 0.69\) (Andre et al.) and \(\lambda\) implied by perceived ≈ 0.43 vs actual 0.69, so \(\lambda \approx 0.62\) applied to the *support* signal:
  - A Chenoweth-scale peak of \(a = 0.035\) implies \(I \approx 20\).
  - A Women's-March-scale \(a \approx 0.013\) implies \(I \approx 53\).
- Chenoweth's own heuristic, 3.5% active with probable majority support, gives \(I \gtrsim 14\).
- The author's intuition that visible protesters are one or two orders of magnitude smaller than the latent sympathetic population is therefore **consistent with the data**. The hard part is that \(G\) (costly action) is very right-skewed, so a large \(s\) does not automatically produce a large \(a\) (Tiede et al.). [abstain: tier-floor: unearned confidence — illustrative calibration combining different measures (willingness-to-pay vs protest participation)]

---

## PART D — Historical horizon: is the Montreal Protocol the exception? (summary of Appendix A)

**Montreal.**
- It was pre-emptive in that no significant mid-latitude ozone loss had been measured at signing. But the ozone hole and NASA imagery catalysed it, the 1987 terms were weak (a 50% cut), and the phase-out came only in 1990–92.
- It succeeded because every variable was favourable:
  - few producers, so a small veto;
  - DuPont expected to profit from substitutes, so the incumbent's \(L^R\) flipped sign;
  - the US gained unilaterally, so \(H\) fell inside the veto holder's radius;
  - trade sanctions on non-parties corrected \(\hat r\) and removed free-riding.
- [admit/refute: App. A §2; refute: "ozone hole played no role" — Grevsmühl & Briday 2023]

**Deep history (≈25 pre-modern cases, Bronze Age to the Little Ice Age).** The record splits sharply.
- **Recurrent, local, visible hazards on bounded commons** were often handled by long-lived anticipatory institutions, usually founded after a first disaster:
  - Dutch and Flemish water boards;
  - Ragusa's 1377 quarantine;
  - the Törbel alp statutes;
  - Japanese *iriai* forests;
  - the Valencian huertas;
  - Qing ever-normal granaries;
  - Tokugawa forestry.
- **Novel, diffuse, slow threats whose costs fall outside the deciders' circle** were usually met late, reactively or under elite obstruction: the Gracchan land crisis, England's labour statutes after 1349, Mamluk Egypt, late Flemish flood defence, 17th-century Italian plague.
- Collapse revisionism removes several canonical "chose to fail" cases. The Norse adapted, Rapa Nui had no pre-contact demographic collapse, and Angkor declined gradually. [refute: Dugmore et al. 2012; Moreno-Mayar et al. 2024; Penny et al. 2019]

**Base rate.**
- No study measures the base rate directly.
- CrisisDB (n = 168 crises) shows only about 31% saw any welfare-enhancing reform, and reform was uncorrelated with severity. [admit/refute: Hoyer et al. 2024/25]
- The appendix's judgement is **about 5–25% pre-emptive** for novel slow threats with concentrated incumbent benefits. [abstain: judgemental estimate]

**What distinguishes pre-emptive successes, mapped to model variables:**
1. The trust radius coincides with the commons, so \(L^R\) and \(H\) are summed over the same people (Ostrom principles 1 and 3).
2. Harm falls inside the veto holders' own radius, or their \(L^R\) turns positive.
3. There are few decision-makers, or the polity is small.
4. Mutual monitoring corrects \(\hat r\).
5. Recurrence plus institutional memory maintains \(\varphi\).
6. Cheap substitutes exist.
7. The state has capacity and fiscal health.
8. The harm is visible and can be pictured.

**Verdict.** Montreal is the exception for *novel, global* threats, and deep history explains why. Pre-emption happens when veto holders are inside the radius of harm, when those who pay are those who decide, and when memory of past disaster is institutionalised. Climate change and AI risk currently satisfy none of the three. That is the radius-bounded mechanism's prediction, and the historical record broadly confirms it.

---

## PART E — Does the micro-mechanism generalise across civilisational systems? (summary of Appendix B)

**Verdict: yes, with bounds.**
- The mechanism describes a plurality, and probably a majority, of documented cases where harm is slow-onset, diffuse or delayed and benefits are concentrated.
- That class includes chemical and occupational hazards, fisheries and land commons, financial booms, pensions and demographics, infrastructure maintenance, antimicrobial resistance, and parts of democratic erosion.
- It does **not** describe most systems with routine, acute, attributable feedback, such as aviation safety, food recalls and acute drug toxicity. Their success is quiet and leaves no case record.

**Catalogue (33 cases, 10 domains; a convenience sample biased toward famous failures).**
- Outcomes: 21% prompt or pre-emptive · 33% late · 30% prevention failed · 15% ongoing with no adequate action. **79% were late, failed or ongoing.**
- Fit of the full four-term mechanism: strong in 33%, partial in 39%, weak or another mechanism dominant in 27%.
- [admit: App. B §4.1; selection-bias caveat §4.2]

**Population-scale evidence that is not selected on outcome.**
- Public budgets in every Comparative Agendas Project dataset are leptokurtic: delay, then lurch. [admit: Jones et al. 2009]
- Financial crises are frequent (164 since 1970) and predictable, yet unprevented. [admit: Laeven & Valencia; Greenwood et al.]
- Disaster severity does not predict disaster-policy reform (85 countries, 10,976 events). [admit: Nohrstedt et al. 2021]

**Boundary conditions where delay collapses, mapped to model variables:**
- immediate, attributable harm (\(\varphi \to 1\); thalidomide was withdrawn within about 10 days);
- harm inside the veto holders' radius (\(V\) falls; the Great Stink, dust reaching Washington);
- cheap substitutes (\(L^R\) small);
- few decision-makers who monitor each other (\(\hat r\) accurate);
- a free press plus electoral accountability (\(\varphi\) up, \(V\) down). This holds as a tendency only: Sen's no-famine law is refuted as absolute by Malawi 2002 and Niger 2005. [refute: Rubin 2008/09; admit: Besley & Burgess 2002]

**Existing domain-general theories of delay.**
- Platt's *social traps* (micro);
- Kuran's *preference falsification* (micro; the \(\hat r\) term);
- *institutional friction* / punctuated equilibrium (meso; quantitatively validated);
- path dependence and *carbon lock-in* (Pierson; Unruh);
- Geels's *regime resistance*;
- the Collingridge dilemma;
- disaster incubation;
- predictable surprises;
- the ostrich paradox;
- Anthropocene *evolutionary traps* (Søgaard Jørgensen et al. 2024).

None combines the cascade threshold, biased \(\hat r\), radius-bounded \(L\), endogenous elite veto and N-scaling (see "Status of the report's claims" in the executive summary).

---

## PART F — Consolidated testable predictions and falsification tests

The model explains prompt cases by parameter values: high \(\varphi\), low \(L^R\), low \(V\). It therefore risks being unfalsifiable **unless the parameters are coded before the outcomes are known.** Every test below is framed that way. [abstain: unverifiable — proposed, not yet tested]

| # | Prediction | Model term tested | What would falsify it | Data or design | Source |
|---|---|---|---|---|---|
| P1 | **Ex-ante lag ranking.** Coding \(\varphi\) (latency, visibility, attributability), \(L^R\) concentration, \(V\) (veto points, incumbent lobbying share) and the \(\hat r\) bias for a pre-registered set of current hazards predicts the rank order of response lags. | Whole model | A rank correlation near zero | Pre-registered panel of live hazards (e.g. PFAS, AMR, microplastics, AI incidents) | App. B F1 |
| P2 | **Trust radius → speed.** Societies with a wider trust radius act sooner after equivalent warnings or shocks. | \(L^{R}\) radius | No relationship | Delhey et al. radius scores × adoption lags for the same EU directive or WHO guideline | B.4; App. B F2 |
| P3 | **Correcting misperceived support works where the barrier is social, the step is cheap, and the target is below the true norm.** Publicising true private *support* (who thinks the behaviour should happen) raises actual behaviour more than equally vivid harm information when three conditions hold: the behaviour is low-cost or a first step; others' disapproval is what holds it back; and the target underestimates support. This applies in climate and outside it (AMR prescribing, pension enrolment, platform-use coordination). For costly or rare behaviours the effect on *actual* behaviour is near zero. It reverses for targets already better than the norm, and for targets shown a lower local norm or a lower prevalence than they believed. Information about the *prevalence* of rare costly acts lowers \(\hat r\), because people overestimate that prevalence. | \(\beta(\hat r_i)\), where the sign of \(\delta_i\) depends on what is estimated: \(\delta > 0\) for broad support, \(\delta < 0\) for the share performing rare costly acts. Moderated by the cost threshold \(\kappa_i\) and by the target's prior relative to \(r\). | (a) Support information no more effective than harm information on actual behaviour for cheap, socially sanctioned behaviours. (b) Equal effects for cheap and costly behaviours. (c) No reversal among above-norm targets or in low-support reference groups when no injunctive cue is given. | A preregistered factorial field experiment: information type (support / harm / both / control) × behaviour cost (cheap / costly) × the respondent's prior relative to the truth. At least two non-climate domains, using the designs of Hallsworth et al. 2016, Beshears et al. 2015 and Bursztyn et al. 2025. Outcome: *actual* behaviour. Pool with a meta-analysis that corrects for publication bias. | B.4; C.3 (C5); App. B F3 |
| P4 | **Elite exposure beats severity.** Reform clusters when harm enters the veto holders' radius (disasters in capitals, legislators' constituencies or families), not with severity per se. | \(V(H_{\text{elite}})\) | Elite-exposure events are no more reform-producing than equally severe non-elite events | Extend Nohrstedt et al. 2021 and CrisisDB with an elite-exposure coding | B.4.1; App. A §7; App. B F4 |
| P5 | **Larger polities lag longer.** Controlling for veto points, larger polities with similar committed minorities sit longer just below tipping. | N-scaling of \(T_{\text{tip}}\) (Xie et al.) | No size effect, or faster large polities | Cross-national adoption lags; confound: population covaries with federalism and veto points | B.4; App. B F5; App. A §6 (CrisisDB scale effect) |
| P6 | **Benefit/harm asymmetry predicts lurchiness.** Policy topics with diffuse harm and concentrated benefit show *higher* budget kurtosis than topics with concentrated harm. | \(L^R/H\) asymmetry → friction | No difference, or the reverse | Comparative Agendas Project budget series by topic | App. B F6 |
| P7 | **Deadline panel: action lands at the deadline.** Across hazards with a publicly known, dated deadline (trust-fund depletion, agreement expiry, statutory sunset, debt-limit X-date, treaty step), comprehensive action arrives near the deadline: the distribution of lead times (deadline minus date of comprehensive action) is skewed toward zero. The clustering strengthens with the number of veto points and with the size of the incumbents' \(L^R\) from the status quo. | \(V\) as a war of attrition with a known deadline. Generic "deadline effect" models predict clustering at any known end date, whoever holds the vetoes; the model predicts that clustering rises with veto count and with \(L^R\), and that interaction is what distinguishes it. A deadline also makes the date of harm public, which acts on \(\varphi\) (temporal distance becomes known) and on \(\hat r\) (the date is common knowledge). | Lead times that are uniform or skewed early, or lead time unrelated to the \(V\) and \(L^R\) scores (a generic deadline effect without the model's interaction) | Pre-registered panel, \(V\) and \(L^R\) scored before outcomes are known (blind to lead time for resolved members). Open: US OASI (Q4 2032), US Medicare HI (Q2 2033), Kigali non-Article 5 HFC steps (85% by 2036). Resolved: 1983 Social Security amendments, US debt-limit episodes 2011, 2013, 2023 and 2025, TCJA individual provisions (end-2025), Colorado River operations (from 1 October 2026), Korea's National Pension (2055 projection) | App. B F7, B6, case 13; App. B §7.1 (DL1–DL10) [abstain: unverifiable — proposed, not yet tested] |
| P8 | **Crisis polarity under identity sorting.** In partisan-sorted domains (guns, democracy, US climate), crises *increase* divergence in enacted policy rather than producing convergence. | \(\sigma\Pi\) in \(V\); partisan \(\varphi\) | Crises producing cross-partisan convergence in sorted domains | State-level enacted-law panels (Luca et al. design) | B.4.1; App. B F8 |
| P9 | **Institutional memory protects against shifting baselines.** Recurrent hazards with standing institutions are pre-empted more often than first-encounter hazards of similar severity. Institutional capacity (\(M\)) erodes as fiscal capacity falls. | \(M\) in \(\varphi\) | Recurrence and standing institutions show no advantage | CrisisDB and Seshat; disaster-history panels; Riris et al. 2024 design | App. A §7.2 |
| P10 | **Aligned radius means enduring commons.** Commons where users = beneficiaries = rule-makers outlast those with externally breached boundaries or outside rule-makers. They also decay when decision-making is captured by actors outside the exposed population. | Radius alignment of \(L^R\) and \(H\) | Boundary alignment does not predict durability | Ostrom / Cox et al. 2010 meta-analysis extended; van Bavel et al. water-board panel | App. A §6 |
| P11 | **Endogenous information suppression.** Where incumbents control the research on a hazard, the warning-to-action lag is longer than for comparable hazards studied independently. | \(\varphi\) endogenous to \(V\) | No lag difference | EEA *Late lessons* cases coded for funding source of early research | App. B B10 |
| P12 | **Pre-emption exports harm.** Pre-emptive successes within a radius show measurable displacement of harm onto out-radius populations. | Externality leakage | No displacement in matched cases | Paired historical and modern cases (Venice/mainland; offshoring of emissions) | App. A §7.2 |

**P7 in combination.** Paired with P9 (recurrent vs first-encounter hazards), P7 forms a 2×2 design, known vs novel hazard × deadline vs no deadline, which separates "waits for the deadline" from "cannot perceive the threat": the first predicts late action on known hazards with deadlines, the second predicts late action on novel hazards whatever the deadline. Within the panel, P20 predicts that members with more distinct beneficiary groups or statutes land closer to their deadlines.

Predictions P13–P21, on downstream harms and accreted wickedness, are in G.4 in the same format. Predictions P22–P24, on causal AI, attribution and the atrophy of tracing, are in H.5.

**Applied to the three systems in the research question (forward-looking, unverified).**
- *Credit:* P4 predicts reform when debt-service costs hit governing coalitions' fiscal base, not when household distress peaks. P7 predicts that where fiscal hazards carry dated deadlines (debt-limit X-dates, trust-fund depletion, tax sunsets), resolution lands close to them, and closer where the budget process has more veto points.
- *Climate:* P3, P4 and P9 predict faster action where misperceived support is publicly corrected (for cheap, socially sanctioned steps), where elites are directly exposed, and where adaptation institutions persist between disasters.
- *AI safety:* the Collingridge dilemma, P1 and P11 predict delay until harms are attributable and fall on veto holders. Incumbent-funded safety research would lengthen the lag.

[abstain: unverifiable — forward predictions]

---

## PART G — n-order harms and accreted wickedness (summary of Appendix C)

Parts B–F treat a harm as if it fell directly on the people who perceive it and the elites who veto action against it. Most harms do not. An unresolved root cause produces harms that travel down a causal chain into other domains: French deficits into social budgets and euro-area spreads, warming and fuel build-up into utility bankruptcy and insurance withdrawal, an unstudied product into adolescent health, a food environment into metabolic disease. Appendix C codes four current chains and three resolved historical ones (lead, tobacco, CFCs) and checks the literature on unintended consequences, policy feedback, layering, termination and wicked problems.

### G.1 Downstream harm changes the model

1. **Attribution decays along the chain.** Let a_j ∈ (0, 1] be the attributability of link j: how clearly the people who bear that link's harm trace it to its cause. The perception filter for the root's harm, seen from link k, is then roughly

$$
\varphi_k \;\approx\; \varphi_0 \prod_{j=1}^{k} a_j \;+\; M .
$$

   A single contested link drives the product toward zero. Social media → body image (r ≈ .16, causation contested) and lead → crime (publication bias, near-zero effects in the best studies) are examples. [admit: App. C SM10 (association); abstain: source-vs-prior conflict — causation, App. C SM9, H4]

2. **Downstream cost-bearers hold no veto in the originating domain.** Homeowners in fire zones have no vote on global emissions; adolescents have no say over platform design; future French taxpayers and euro-area partners have no seat in the coalitions that defend current commitments. In B.4 terms, H is large where V is absent, and V is large where H is small. [Synthesis, App. C §5]

3. **Responses settle at the nearest attributable, lowest-veto link.** Writing V_k for the veto against action at link k and θ for the attribution needed to act,

$$
k^{*} \;=\; \arg\min_{k}\,\big\{\, V_k \;:\; \varphi_k H_k \ge \theta \,\big\}, \qquad V_{k^{*}} \ll V_{\text{root}} .
$$

   In all four current chains most enacted policy sits downstream: utility liability funds (AB 1054, SB 254), insurer rules and the FAIR Plan in California; age limits, phone bans and design codes for social media; GLP-1 coverage beside narrow food rules for obesity; and in France, government collapses and market repricing rather than deficit correction. Root-tier action exists in each (cap-and-invest to 2045, the soft drinks levy, the EU deficit procedure) but is slower and smaller. Four non-random cases show a pattern, not a rate. [Synthesis; facts admitted in App. C §3]

4. **Symptomatic relief lowers root-cause pressure.** This is Senge's "shifting the burden" at policy scale: relief R_k at link k lowers the harm that reaches the root, so the felt root harm is H_root − R_k. The concern that GLP-1 drugs will weaken pressure for food regulation is asserted in commentary but not yet demonstrated. [abstain: non-authoritative source — Senge reached only through summaries, App. C L16; unverifiable — crowd-out effect, App. C OB13]

5. **Carriers bring the harm into the veto radius.** A carrier is an actor who moves a downstream cost onto the root veto holders, raising H_elite in V = V₀ − γH_elite + δL^R_elite + σΠ:
   - **creditors and bond markets**: France's rating cuts (2024–25) and spreads at their widest since 2012 hit the governing coalition's fiscal base [admit: AFT ratings record; abstain: non-authoritative source — spread data from market press, App. C FR6];
   - **insurers**: State Farm's and Allstate's withdrawal and the first FAIR Plan assessment since 1994 put fire risk on property owners and the state [admit: CDI orders];
   - **courts and state treasuries**: Medicaid cost-recovery suits turned smokers' disease into a state-budget claim, settled in the 1998 Master Settlement Agreement [admit: GAO-01-851; NEJM 2004];
   - **partner states and foreign regulators**: the EU deficit procedure for France; EU, UK and Australian platform rules reaching US firms [admit: OJ L 2024/2122; App. C SM1, SM5].

   In the three resolved historical chains, root action followed a carrier, not a peak in downstream harm. That is consistent with B.4.1's claim that reform follows harm entering the veto radius, and it is untested on unselected data (P16). [Synthesis, App. C §4]
**Precedent: traceability.** The closest precedent for points 1 and 3 is R. Douglas Arnold's *The Logic of Congressional Action* (1990). Arnold argued that the "nature of the causal chain that links a policy instrument with its policy effects" structures congressional action: citizens can hold a legislator to account for an effect only if they can trace it to a government action and from there to their representative [admit: Mildenberger & Sahn 2025, LSQ, quoting Arnold]. Early-order effects are more traceable than later-order ones, and coalition leaders break traceable links, for example by folding costly provisions into omnibus bills [abstain: non-authoritative source — course summaries; book not opened]. In this report's terms, Arnold's traceability is the product \(\prod a_j\), and his legislators, choosing instruments whose effects voters can or cannot trace, are the actors who settle at \(k^*\). The present model differs in two ways. Arnold's chain runs from one policy to its effects; the chains here run from an *unaddressed* root through several domains, so the product has more terms and the root is an omission, not an act. And the first direct test of Arnold's claim found that legislators respond to policy and problem traceability while prospective voters are indifferent to it [admit: Mildenberger & Sahn 2025, LSQ 50(4):e70036]. Attribution decay may therefore bind mainly through elite anticipation of blame, not through mass judgement. Experiments on moral judgement add two qualifications. Blame of an agent weakens as the chain between act and harm lengthens, through reduced foreseeability [admit: Engelmann & Waldmann 2022, Cognition 226:105167]. And the loss concentrates at intervening *agents*: people trace attribution through physical links back to a human cause, but a voluntary intervening actor absorbs it [admit: Hilton, McClure & Sutton 2010, EJSP 40(3):383–400]. So \(a_j\) is low at insurers, utilities and local officials, and high at physical links such as warming to fire weather. Because veto holders can add agentive links on purpose (Hood's blame avoidance through delegation; Arnold's link-breaking), part of the decay is produced by the veto holders themselves, which ties point 1 to V [admit: Hood 2011, Princeton UP; Synthesis].

### G.2 Accreted wickedness

The core claim, with the corrections from Appendix C built in:

> Unresolved root causes produce n-order harms that are hard to trace. Policy responds at the symptom. Each response creates its own beneficiaries (policy feedback; Pierson 1993), who join the veto. In aggregate, and inadvertently (each layer is deliberate, the aggregate is not; Kahn's tyranny of small decisions), the layers turn a tractable problem into a wicked one: wickedness that is made, not found. The result is extremely difficult to unwind. Resolution is mostly crisis-driven, linking back to B.4.1: the crisis must enter the radius of *many* dispersed veto groups at once. Otherwise it comes through elite displacement or exit. Bundled loss-sharing bargains (1986 tax reform) and ideas-led reform (airline deregulation) are rarer non-crisis routes, and their gains can erode.

In model terms, each symptomatic layer ℓ adds a beneficiary group b_ℓ to the veto against root reform:

$$
V_{\text{root}}(n) \;=\; V_0 \;+\; \sum_{\ell=1}^{n} \delta_\ell\, L^{R}_{b_\ell} \;-\; \gamma\, H_{\text{elite}} \;+\; \sigma\Pi .
$$

A bargain that compensates every group must clear n distinct vetoes, so the bargain space shrinks as n grows.

**What the evidence supports, and the corrections.**
- **Components are established.** Unintended aggregate consequences (Merton 1936; Kahn 1966), policy creating its own constituencies (Pierson 1993), layering (Streeck & Thelen 2005), layered mixes that are incoherent and hard to change (Howlett & Rayner 2009), policy accumulating faster than it is removed (Adam et al. 2019), policy responding to its own consequences (Wildavsky 1979), iatrogenic regulation (Wiener 2003) and maladaptation (Barnett & O'Neill 2010). The IPCC states that "some responses to climate change result in new impacts and risks". [admit: App. C L1–L3, L5–L8, L33, L35, L39–L41]
- **"Made, not found" opposes Rittel & Webber,** who treat social planning problems as inherently wicked. Head & Alford (2015) treat wickedness as a matter of degree. The constructedness precedent is Daviter (2019), for whom wickedness is an interpretive framing; Peters (2017) argues only that the label is over-applied. Accreted wickedness differs from both: the wickedness is produced causally by policy layers, not by framing. [admit: L12, L13, L15; refute: L14]
- **Novelty.** No source names "accreted", "iatrogenic" or "policy-induced" wickedness, and none combines root-cause neglect, symptomatic layering, a beneficiary veto and a tractable-to-wicked transition. [abstain: unverifiable — negative search]
- **"Extremely difficult to unwind."** Termination is rare for large units and comprehensive repeal is rarer still, but single units do die: about 10% of US domestic programmes within a decade, 62% of post-1946 agencies under a broad definition, 7% of Texas sunset reviews. Quiet dismantling by default also occurs (Bauer et al. 2012). The defensible form is "comprehensive unwinding is rare", not "nothing is ever removed". [admit: L18–L20, L24, L42; refute: L19 figure]
- **Base rate.** No study measures how often accumulated policy is unwound comprehensively without a crisis. "Mostly crisis-driven" is therefore a hypothesis consistent with the case record, not a measured rate. [abstain: unverifiable — no dataset located]
- **Non-crisis routes.** The 1986 Tax Reform Act was a revenue-neutral bundle: base broadening for a top-rate cut from 50% to 28%. Its erosion was partial: rates rose in 1990 and 1993, and tax expenditures fell from about 9% to 6% of GDP, then rose without returning to the 1985 level. Airline deregulation (1978) is explained by ideas and expert advocacy rather than a sector crisis; whether stagflation was the trigger is contested. [admit: L26–L29; abstain: L30]

**Two further points.**
- **Doubt-manufacturing is an accelerant, not the mechanism.** Tobacco and lead show incumbents depressing φ (App. B M15, B10), which lengthens chains and links to P11. But the chains in Section 3 of Appendix C accrete without any documented doubt campaign: attribution decay, veto mismatch and feedback suffice.
- **Complexity makes non-crisis unwinding rarer.** As veto groups multiply, the bargain space shrinks. Olson's (1982) sclerosis thesis, that distributional coalitions accumulate in stable societies and slow growth, is "generally, but certainly not universally, supported", although the coalition mechanism itself has only weak support. Tainter's declining returns to complexity points the same way. [refute: "tests are mixed" — Heckelman 2007; admit: Bischoff 2007; L10]

### G.3 The lateral-connection problem

- **Chains cross domains; institutions do not.** Mandates, budgets and data are siloed. The fiscal ministry does not own social-security outcomes, the energy regulator does not own insurance, the education ministry does not own platform design. The 9/11 Commission's finding that without integrated all-source analysis "it is not possible to 'connect the dots'" names the same problem in intelligence. Vaughan's structural secrecy and Tett's silos describe it in organisations. [admit: L38; abstain: tier-floor: unearned confidence — L36, L37 not opened]
- **Cross-domain institutions are fragile.** The US Office of Technology Assessment, created in 1972 to assess technology across committees, was defunded in 1995; its statute was never repealed. In model terms this is erosion of M, the institutional memory term, at exactly the point where chains cross mandates. [admit: L31]
- **Early catches are invisible.** An intercepted chain produces no downstream harm, no crisis and no case record, so the evidence base is selected toward failures (App. B §4.2). The defensible claim is "rarely caught early, and the successes go unseen", not "never caught early".

### G.4 Predictions

All predictions below are proposed and untested. [abstain: unverifiable — proposed, not yet tested]

| # | Prediction | Model term tested | What would falsify it | Data or design | Source |
|---|---|---|---|---|---|
| P13 | **Fixes land near the symptom.** The probability of a root-cause response falls with causal distance from the visible harm, and the response targets the nearest attributable, lowest-V link. | k* = argmin V_k s.t. φ_k H_k ≥ θ | Response locus uncorrelated with causal distance or with link-level veto | Code enacted measures in a policy-agenda dataset by their position on documented causal chains (e.g. EEA *Late lessons* cases) | G.1; App. C §5 |
| P14 | **Attribution decays at agentive links, and elites track it more than publics do.** Holding the harm constant, attribution to a policy root falls as the chain from root to harm lengthens. Most of the loss occurs at links where an intervening actor (an insurer, utility or local official) offers a nearer target. Links that are physical processes pass attribution back to a human or policy root with little loss. Legislators' attribution and choice of instrument respond to traceability more than mass attribution does. Partisan cues gate each link. | \(\varphi_k \approx \varphi_0 \prod_{j=1}^{k} a_j + M\), with \(a_j = a(\text{type}_j, \pi_i)\): low for agentive links, near 1 for physical links, and filtered by party alignment \(\pi_i\). Veto holders can lower \(a_j\) on purpose (Hood's blame avoidance; Arnold's link-breaking). | (a) Attribution flat across chain depth. (b) Equal decay at physical and agentive links. (c) Publics' attribution as sensitive to depth as elites'. (d) No partisan gating once role information is supplied. | A survey experiment presenting the same harm at depths 1–4, crossing link type (physical vs intervening agent), party cue and role information. Run in parallel on a public sample and on legislators or staff (the Mildenberger & Sahn 2025 design). Separately, media content coding of chains, with episodic or thematic frame as a covariate (Iyengar 1991). | G.1; Arnold 1990; Mildenberger & Sahn 2025; Engelmann & Waldmann 2022; Hilton et al. 2010 |
| P15 | **Symptomatic fixes crowd out the cure.** Root-cause policy momentum (bills, hearings, budget) falls after a downstream fix is adopted. | Shifting the burden: H_root − R_k | Root momentum unchanged or rising after downstream adoption | Event study around GLP-1 coverage decisions vs food-policy activity; insurance backstops vs climate bills | G.1; App. C OB13 |
| P16 | **Reform waits for a carrier.** Root-cause action tracks the emergence of a cost-bearer with leverage over the veto holders, not the severity of downstream harm. | Carrier raising H_elite in V | Root action predicted by harm severity, not carrier emergence | Historical chains coded for carrier dates (tobacco suits, rating actions, insurer exits) | G.1; App. C §4 |
| P17 | **Layers depress root reform.** Controlling for severity, the probability of root-cause reform falls with the number of symptomatic layers already enacted. | V_root(n) | No layer-count effect | Panel of policy domains with counts of downstream statutes (Adam et al. accumulation data) | G.2 |
| P18 | **Symptomatic programmes outlive their cause.** Programmes created to treat a downstream harm persist after the root cause is resolved. | Feedback beneficiaries in V | Programmes terminated promptly once the root is fixed | Programme-survival data (Berry et al. design) matched to root-resolution dates | G.2 |
| P19 | **Successful unwinds are packages.** Comprehensive unwinds are bundled loss-sharing packages adopted under root-reform conditions (a carrier, a crisis reaching many veto groups, or an ideas coalition), not piecemeal repeals. | Bargain space vs n | Successful unwinds are mostly piecemeal | Case set of comprehensive reforms (tax, deregulation, pensions) | G.2; App. C L26–L29 |
| P20 | **More groups, fewer unwinds.** The probability of a non-crisis unwind falls with the number of distinct beneficiary groups or statutes in the domain. | V_root(n) | No relationship, or the reverse | Sunset-review outcomes (Texas) by number of affected statutes and lobby registrations | G.2; App. C L24 |
| P21 | **Interception needs a spanning mandate.** Early interception happens mainly where one institution's mandate spans both the root domain and the harm domain. | M; lateral connection | Early interceptions as common where mandates are split | Paired cases with and without a spanning agency (e.g. OTA-era vs post-1995 technology assessments; integrated vs split health-and-food regulators) | G.3 |

**Applied to the three systems in the research question (forward-looking, unverified).**
- *Credit:* P16 predicts that French root-deficit action follows bond-market and EU pressure on the governing coalition, not household distress; P17 predicts that each new compensatory measure makes it harder.
- *Climate:* P13 and P15 predict continued investment in insurance backstops and suppression over emissions, with root action tracking carriers such as insurers and reinsurers.
- *AI safety:* P13 and P21 predict that AI harms will be handled where they surface (content moderation, fraud, employment law) unless a body with a mandate spanning AI development and its downstream harms exists.

[abstain: unverifiable — forward predictions]

---

## PART H — Can causal AI break the trap? (summary of Appendix D)

Part G ends on a data problem as much as a political one. Accreted wickedness grows where cause and effect are hard to link across large, heterogeneous, multi-polar networks: attribution decays link by link (P14), cross-domain institutions are fragile (P21), and institutional memory M erodes. A family of techniques now promises to link causes and effects at that scale. This Part asks what they could fix in the model's terms, which of their limits are real ceilings, and what their success would cost. Appendix D holds the verification; tags here re-cite it and are not counted again.

**A note on terms.** "Causal model", "causal discovery" and "causal AI" are used here as the names of a model class, as terms of art. They carry no ontological commitment to causes as things in the world. The position taken throughout is relational: a model embeds relations between actants, and actants affect one another. Whether a given event is "the cause" or "the effect" is moot. What matters for the argument is what the model class does with those relations, and H.4 shows that one of the things it does is give them a direction.

### H.1 Causal models as a candidate solution

**The model class.**
- **Structural causal models (SCMs).** Pearl's ladder of causation separates association ("seeing"), intervention ("doing") and counterfactuals ("imagining"). The causal hierarchy theorem shows the layers "almost never" collapse: for almost any SCM, data at one layer underdetermines the layers above it. [admit: App. D CM1]
- **Causal discovery.** PC and FCI (Spirtes, Glymour & Scheines) infer graph structure from conditional independences; FCI allows hidden common causes and returns a partial ancestral graph, an equivalence class rather than a single graph [admit: App. D CM2]. NOTEARS (Zheng et al. 2018) recasts structure learning as continuous optimisation, using an exact smooth characterisation of acyclicity, because the space of directed acyclic graphs grows superexponentially with the number of nodes [admit: App. D CM3].
- **Causal representation learning.** Schölkopf et al. (2021) relate causal inference to open problems in machine learning, including transfer and generalisation, and frame the task of learning causal variables from low-level data [admit: App. D CM4].
- **Digital twins and world models.** The EU's Destination Earth began implementation in January 2022 (ECMWF, ESA, EUMETSAT) and launched on 10 June 2024 with digital twins for weather extremes and climate adaptation, aiming at a "full" Earth-system twin by 2030 [admit: App. D CM9]. These are mechanistic simulations whose relational structure comes from physics rather than from discovery; they belong to the same family only in the broad sense of models built to answer interventional questions. **Synthesis.**
- **LLMs are not, by themselves, causal models.** Zečević et al. (2023) argue that LLMs are at best "causal parrots": they reproduce correlations between causal *statements* in their training text, not causal structure [admit: App. D CM5].

**What causal AI could fix, in the model's terms.** **Synthesis**, building on the admitted findings.
1. **Attribution decay (P14).** In φ_k ≈ φ₀∏a_j + M, a model that estimates each link's strength from pooled data raises low a_j toward their true values, to the extent that its assumptions hold (H.2). The product decays less, so harm several links downstream is more often attributed to its root.
2. **A substitute for spanning mandates (P21).** Interception currently needs one institution whose mandate spans root and harm. A shared model that spans the chain could do part of that work without a single spanning agency, because the lateral connection is made in the model rather than in the organisation chart.
3. **Resisting M-erosion.** A standing model is a form of institutional memory. It need not renormalise its baseline every 2–8 years the way perception does, unless it is retrained only on recent data, in which case it can inherit a shifting baseline of its own (H.2).
4. **Creating carriers.** Two precedents show attribution tools producing actors who move costs into the veto holders' radius:
   - *Extreme-event attribution.* World Weather Attribution, founded in 2014, has run more than 100 rapid studies under a published protocol [admit: App. D AT1]. In *Lliuya v RWE* (Hamm Higher Regional Court, 28 May 2025) the court dismissed the claim on the facts but held that a major emitter can in principle be liable, in proportion to its share of emissions, for climate risks to property abroad [admit: App. D AT4]. **Correction:** attribution has opened legal standing in principle; it has not yet carried a damages award, and in that case the court never reached the attribution evidence. A review of 73 lawsuits found that the evidence submitted "lags considerably behind" the state of the science (Stuart-Smith et al. 2021) [admit: App. D AT3; refute: App. D AT8]. That attribution has entered insurance pricing could not be confirmed; insurers price with catastrophe models, which are a different tool [abstain: App. D AT5].
   - *Pharmacovigilance.* Disproportionality methods (the proportional reporting ratio; the WHO Uppsala centre's Bayesian neural network, in routine use since 1998) detect drug-safety signals in millions of spontaneous reports [admit: App. D AT6].

### H.2 Limits, reclassified

Suppose causal models are run the way frontier labs run LLMs: retrained on fresh data and re-released, with the aim of updating close to continuously. **Correction:** current frontier practice is periodic retraining with versioned releases, not continuous updating of deployed weights; the training–deployment boundary is itself treated as an auditability boundary [abstain: App. D CM10]. The scenario below is the limiting case.

**What continuous updating addresses.** Non-stationarity and drift. A model retrained on recent data tracks a moving world, and policy actions, once logged with their timing and targets, can serve as interventions or natural experiments that move the model up Pearl's ladder from seeing to doing. **Synthesis.**

**Residual limits, which are ceilings.**
1. **Hidden confounders.** Without assumptions or interventions, observational data cannot settle interventional questions; that is what the causal hierarchy theorem says [admit: App. D CM1]. FCI tolerates hidden confounders only by returning an equivalence class in which some edge directions stay open [admit: App. D CM2]. Continuous updating adds data at the same layer of the ladder; it does not climb it.
2. **Performative prediction.** When predictions drive decisions, they change the distribution they predict. Perdomo et al. (2020) show that repeated retraining converges, under conditions, to a *performatively stable* point, and that "performatively stable classifiers need not be performatively optimal" [admit: App. D CM7]. A causal model that informs policy is retrained on a world its own outputs have shaped. It can settle on a fixed point that is self-consistent but not true to the world the policy would otherwise have produced. This is the ceiling continuous updating cannot remove, because updating is its mechanism.

**Limits that are risks or governance questions, not ceilings.** **Synthesis**, mapped to admitted findings in the main body and Appendices B and C.
- *Partisan filtering of outputs.* The model's attribution enters φ through the same partisan gate π as any other signal (Hazlett & Mildenberger 2020). A better a_j does not raise φ for those who discount the source.
- *Capture of the model.* If veto holders fund, train or license the model, φ becomes endogenous to V, as with doubt-manufacturing in tobacco and lead. P11 then applies to the model itself.
- *V still binds.* Where harm is delayed and L^R is large, detection is rarely the bottleneck. (Where harm is immediate and attributable, detection does decide the outcome: thalidomide was withdrawn within about ten days, App. B.) Rofecoxib's heart-attack signal appeared in the VIGOR trial in 2000, was attributed to naproxen's cardioprotection, and the drug was withdrawn only in September 2004, after more than 80 million patients had taken it; a cumulative meta-analysis concluded it should have gone years earlier [admit: App. D AT7]. Tobacco's harms were attributed in 1964; root action waited for the state Medicaid suits and the 1998 settlement (App. C H6–H7). Attribution raises φH; it does not by itself raise H_elite.
- *Institutional data silos.* A model that spans a chain needs data that span it. Mandates, budgets and data are siloed (G.3), so the lateral-connection problem moves from the organisation chart into data governance.

### H.3 Reification as the cost of success

Every limit in H.2 is worst when causal AI fails or is captured. One limit is different. It is intrinsic to the success scenario and worsens the more the system succeeds. Successful causal AI black-boxes the tracing of causal relations itself.

**(i) Inscrutable by scale, not by design.** An SCM's graph is explicit: every node and edge can in principle be inspected. That is the basis of advocacy claims that causal AI does not operate as a black box [admit: App. D N3]. But a graph with millions of nodes, re-estimated as data arrive, is beyond any human's tracing. Burrell (2016) separates opacity from secrecy, opacity from technical illiteracy, and opacity from "the characteristics of machine learning algorithms and the scale required to apply them usefully" [admit: App. D AU10]. An explicit graph removes the first two and leaves the third untouched. Rudin argues for inherently interpretable models in high-stakes decisions [admit: App. D AU14]. **Synthesis:** that remedy presumes a model a person can read, and transparency by design does not survive opacity by scale.

**(ii) Continuous updating destroys the stable referent tracing needs.** To trace a diagnosis back through a model, the model has to stay still long enough to be traced. Machine-learning engineering already recognises that in an entangled system "Changing Anything Changes Everything" (Sculley et al. 2015) [admit: App. D AU15], and that a continuously updating model is a moving target that cannot be versioned or certified once [abstain: App. D AU17]. **The trade-off, stated explicitly:** the fix for H.2's drift problem is the cause of H.3's traceability problem. The faster the model updates, the better it tracks the world and the less any past output can be reconstructed. A frozen model can be traced and drifts; an updating model tracks and cannot be traced. No setting of the update rate removes both costs. **Synthesis.**

**(iii) Atrophy.** The institutional muscle of tracing wastes away when it is not used.
- Bainbridge (1983) named the problem: skills "deteriorate when they are not used", so a formerly experienced operator who has been monitoring becomes an inexperienced one, exactly when the automation fails [admit: App. D AU1].
- Automation complacency and automation bias occur in experts, are not overcome by practice, and cannot be prevented by training or instructions (Parasuraman & Manzey 2010) [admit: App. D AU2].
- Air France 447 (2009): the BEA's final report (July 2012) cites the absence of high-altitude training in manual handling among the causes, and recommends mandatory regular exercises in manual handling of approach to stall and stall recovery [admit: App. D AU3]. Elish (2019) uses the same accident to show the "moral crumple zone": responsibility lands on the nearest human operator, who had limited control over the automated system [admit: App. D AU12].
- In four Polish endoscopy centres, the adenoma detection rate in colonoscopies performed *without* AI fell from 28.4% (226/795) to 22.4% (145/648) after the centres introduced AI-assisted detection (Budzyń et al. 2025; odds ratio for AI exposure 0.69) [admit: App. D AU7]. The design is an observational before-and-after comparison that the authors call hypothesis-generating, so the causal reading is not established [abstain: App. D AU8].
- The end state is epistemic dependence without a check. Hardwig (1985) shows that depending on experts is rational when one has good reason to think they have good reasons [admit: App. D AU9]. When the expert is a model that neither society nor its operators can trace, those reasons are no longer available to anyone. Nobody can say why a diagnostic, predictive or prescriptive output was produced, because every route to the answer runs through the model. Messeri & Crockett (2024) describe the scientific version: AI tools can produce "illusions of understanding" and scientific monocultures [admit: App. D AU13].

**The report's own model predicts the atrophy.** Maintaining an unused capacity is M, and B.4.1 predicts that M erodes under fiscal pressure: the late-Qing granaries decayed with fiscal distress (Will & Wong 1991), and the US Office of Technology Assessment was defunded in 1995 (App. C L31). Human tracing capacity kept in reserve beside a model that usually works is the same kind of standing buffer. It costs money every year and pays off only in the year the model fails, which makes it the first candidate for cuts. **Synthesis.**

**The causal model as the ultimate accreted layer.** Put (i)–(iii) together with G.2:
- it has **beneficiaries**: its operators, the firms and agencies whose decisions it licenses, and the downstream programmes calibrated to its outputs, who join the veto against changing it (Pierson's feedback, App. C L5);
- it **cannot be traced in practice**, so it cannot be unwound: removing a layer requires knowing what it holds up;
- its operators hold an **epistemic veto** over what counts as a cause, because contesting an attribution means contesting the model, and only they can open it.
This is accreted wickedness in its most complete form: a layer adopted to see through the layers beneath it. **Synthesis.**

**A risk, not a certainty, with mitigations the documented pressures work against.**
- *Frozen and versioned snapshots,* so any output can be re-run against the model that produced it. The EU AI Act requires high-risk systems to allow automatic logging of events (Art. 12) [admit: App. D AU16].
- *Provenance logs* for data and updates. The same Act requires that human overseers stay aware of the tendency toward "automation bias" and be able to override outputs (Art. 14(4)) [admit: App. D AU16].
- *Mandated human tracing kept in practice,* on the model of pilots' manual flying. **Correction:** manual flying is encouraged, not mandated. FAA SAFO 13002 (2013) "encourages operators to promote manual flight operations", and a 2016 Inspector General audit found the FAA had not determined whether carriers had increased manual flying as a result [admit: App. D AU5; refute: App. D AU6]. The aviation precedent is therefore evidence for the risk as well as a template for the mitigation: thirty years after Bainbridge, and with a fatal accident on record, the practice is advisory and unmeasured.
- Each mitigation is a standing cost with a deferred, uncertain benefit. Under B.4.1's fiscal erosion of M, they are the parts of the system most likely to be cut. **Synthesis.**

### H.4 The ANT lineage

H.3's argument is not new to actor-network theory. It is close to ANT's founding observations about how technical success disappears from view. This section traces each step to its source, maps it to the model, and states the report's ontological position that follows from it.

**1. Black-boxing (Latour 1987, 1999).** In *Science in Action* Latour borrows "black box" from cybernetics: a device too complex to describe is replaced by a box "about which they need to know nothing but its input and output" (pp. 2–3) [admit: App. D ANT1]. The *Pandora's Hope* glossary defines blackboxing as the way technical work is "made invisible by its own success", and adds that the more science and technology succeed, the more opaque they become (p. 304) [admit: App. D ANT2]. That is H.3's thesis in Latour's own words. The cost of success is not a malfunction of black-boxing but its definition. Callon & Latour (1981) had already tied black boxes to power: "An actor grows with the number of relations he or she can put... in black boxes", and a black box "contains that which no longer needs to be reconsidered" [admit: App. D ANT4]. *Model mapping:* each layer ℓ in V_root(n) is a black box that its beneficiaries no longer need to reconsider. The causal model is the black box that makes reconsidering any of the others depend on it.

**2. Punctualisation (Law 1992).** A network that acts as a single unit is *punctualised*; "the appearance of unity, and the disappearance of network, has to do with simplification". Widely performed networks are the ones most easily punctualised, and any actor is a punctualised network that can be unpacked again [admit: App. D ANT6]. Punctualisation holds until breakdown. *Model mapping:* a widely adopted causal model is a punctualisation of the whole chain it describes: data pipelines, estimation choices, update schedules, operators and the institutions that consume its outputs, all appearing as one source of attributions.

**3. The model's variables are punctualisations.** This is the report's ontological position, and it follows directly from Law. V, L^R, the trust radius R and M are not pre-given structural forces. They are punctualised summaries of networks of associations that are continually performed and maintained. Elites, the power they are afforded and a radius of trust cannot emerge out of nothing; each is assembled. Latour's "The powers of association" makes the point for power itself: power "must be treated as a consequence rather than as a cause of action" (1986, p. 264), and "power" is a convenient way to summarise the consequence of a collective action, not to explain what holds it in place [admit: App. D ANT5]. Callon & Latour (1981) make it for macro-actors: a macro-actor is a micro-actor seated on black boxes, and black boxes never remain fully closed [admit: App. D ANT4]. The formal model in B.4 and B.4.1 is therefore a black-boxed description of network effects. Three consequences follow.
   - **Carriers are de-punctualisers.** If V is performed, it can be reopened. The carriers of Part G are actants that reopen the black box of V: they re-associate a downstream harm with the veto holders' own network. State attorneys general and Medicaid cost-recovery suits re-associated smokers' disease with state budgets; the US skin-cancer valuation re-associated distant ozone loss with American citizens; attribution science re-associates a flood risk in the Andes with a German utility's emissions (App. C H6–H7, H10; App. D AT4).
   - **The H.3 risk is the inverse.** A widely adopted causal model is a new punctualisation, harder to reopen than V, because the associations it summarises are too many and change too fast to unpack (H.3 (i)–(ii)). Its operators become the obligatory passage point (point 4 below). Carriers depend on being able to open black boxes; the causal model is the black box through which every future carrier would have to pass.
   - **Method.** The variables' values must be traced in each case: who assembles the veto, through which associations, and with what materials. They cannot be assumed. This is Part F's requirement to code parameters before outcomes are known, made stronger: coding V ex ante means tracing its network ex ante, not reading it off a list of office-holders. **Synthesis**, from ANT4–ANT6.

**4. The sociology of translation and the obligatory passage point (Callon 1986).** In the St Brieuc Bay study, three researchers try to become indispensable to scallops, fishermen and scientific colleagues through four moments: *problematisation*, in which they define the others' problems and make their own research programme the "obligatory passage point"; *interessement*, which locks the others into proposed roles; *enrolment*, which defines and interrelates those roles; and *mobilisation*, which ensures that spokesmen actually represent their collectivities. Callon's method rests on agnosticism, generalised symmetry and free association [admit: App. D ANT7]. *Model mapping:* the operators of a widely adopted causal model problematise policy disputes as questions the model answers, and so make the model the OPP. Every attribution, and every carrier that depends on one, must pass through it. That is the epistemic veto of H.3 expressed in Callon's vocabulary. Callon's case also shows the counter-move. The translation came apart in *dissidence*: in later years the larvae did not anchor, and fishermen fished the protected stock one Christmas Eve, so the researchers' claim to represent both was "brought into question" [admit: App. D ANT7]. A model's OPP status is likewise held, not owned, and lasts only while the actants it speaks for do not betray their spokesmen.

**5. Irreversibility (Callon 1991).** Callon's paper on techno-economic networks asks how some links "achieve longevity and tend to shape future processes of translation" [admit: App. D ANT8]. Irreversibility is usually glossed in two parts: the network cannot return to a point where alternative translations were possible, and it shapes the translations that follow [abstain: App. D ANT9]. *Model mapping:* "extremely difficult to unwind" (G.2) is irreversibility. A causal model that has been used to calibrate programmes, liabilities and prices has shaped the later translations that would be needed to replace it.

**6. Centres of calculation and immutable mobiles (Latour 1987).** Networks make distant things mobile, stable and combinable so that they can be accumulated at a centre and acted on from there; the centre's "theory" is the crossroads where traces are combined and rewritten (*Science in Action*, ch. 6) [admit: App. D ANT3]. *Model mapping:* the causal model is a centre of calculation for chains that cross domains. Its outputs (an attribution fraction, a risk score, a recommended intervention) travel as immutable mobiles into courts, insurers' tables and budget documents, detached from the estimation that produced them. They keep their form while losing their history, which is what makes them useful as carriers and what makes them hard to contest.

**7. Delegation and scripts (Akrich 1992; Latour 1992).** Akrich's script analysis follows how designers inscribe a world into an object and how users de-scribe it in use [admit: App. D ANT11]. Latour's door-closer ("groom") replaces an unreliable human porter with a delegated non-human that prescribes back what kind of people may pass [admit: App. D ANT13]. Akrich adds that as objects become indispensable they have to efface themselves [abstain: App. D ANT12]. *Model mapping:* tracing competence is delegated to a non-human, and the delegation prescribes back. Once the model traces, institutions are reorganised around consuming its traces, and the human role it replaced is the one that atrophies (H.3 (iii)).

**8. Mediators, intermediaries and direction.** For Latour (2005), an intermediary transports meaning or force without transformation, "defining its inputs is enough to define its outputs"; mediators "transform, translate, distort, and modify" what they carry (p. 39) [admit: App. D ANT14]. A causal model is presented as an intermediary, a transparent conduit from data to causes. It is a mediator. The author's relational position and ANT agree here: a model only embeds relations, actants affect one another, and whether an event is a cause or an effect is moot. The sharper point concerns what the model class does to those relations.
   - **SCMs are directional.** Their edges are asymmetric, and the well-studied subclass is acyclic. Bongers et al. (2021) show that once cycles are allowed, "many of the convenient properties of acyclic SCMs do not hold in general": solutions may not exist, distributions may not be unique, Markov properties may fail and graphs may not match their causal semantics. Only a restricted class of "simple" cyclic SCMs recovers most of those properties [admit: App. D CM6]. NOTEARS makes acyclicity an explicit constraint of the optimisation [admit: App. D CM3].
   - **So the model inscribes direction onto mutual relations.** Feedback, the normal condition of the chains in Part G (debt and spreads, insurance withdrawal and development, platform design and use), is either cut into a DAG or handled by a narrower class of cyclic models. In Akrich's terms this is an inscription. It also resembles what Latour calls purification. **Attribution note:** in *We Have Never Been Modern*, purification is specifically the practice that "creates two entirely distinct ontological zones", humans and non-humans, while translation creates hybrids (pp. 10–11) [admit: App. D ANT16]. Applying it to the separation of cause from effect is an extension by analogy, not Latour's usage.
   - **And the outputs circulate as directional matters of fact.** Latour (2004) asks critique to move from "matters of fact" to "matters of concern": from settled objects to the assemblies needed to hold them in place [admit: App. D ANT17]. A model's attribution travels as a matter of fact ("X caused 30% of Y") with the direction already decided. This feeds H.3: the model black-boxes not only its reasoning but the imposition of direction itself. What could be reopened as a matter of concern (who is affected by whom, in which direction, through which associations) arrives closed.

**9. Infrastructure becomes visible on breakdown (Star 1999; Bowker & Star 1999).** Star lists, among infrastructure's properties, that it "becomes visible upon breakdown" (1999, p. 382, after Star & Ruhleder 1996) [admit: App. D ANT18]. Bowker & Star's *infrastructural inversion* is the method of forcing the invisible underpinning into view, as they do for the International Classification of Diseases, "an invisible underpinning to medical practice" [admit: App. D ANT19]. *Model mapping:* a working causal model is infrastructure. It becomes visible when it fails, and H.3 (iii) predicts that by then the people able to inspect it may have gone. Infrastructural inversion is the research programme a mitigation regime would need to institutionalise.

**10. Performativity (Callon 1998; MacKenzie 2006) and performative prediction.** Callon argues that economics "performs, shapes and formats the economy, rather than observing how it functions" (1998, p. 2) [admit: App. D ANT20]. MacKenzie distinguishes generic, effective and *Barnesian* performativity, in which use of a model makes the world more like its depiction, and counterperformativity, in which use makes the world less like it; options pricing after Black–Scholes–Merton is his strongest case [admit: App. D ANT21]. Perdomo et al.'s performatively stable point (H.2) is the machine-learning formalisation of the same family of effects, and the originators have drawn the link themselves, noting that for MacKenzie it is the practice of applying a theory, not the predictions as such, that is performative [admit: App. D CM8]. *Model mapping:* a causal model used for policy is Barnesian when its attributions shape the interventions that generate its next training data. Its convergence to a stable point is then evidence of its performative success, not of its truth.

**11. Reification and how ANT reworks it.** Lukács (1923) describes reification as the process by which "a relation between people takes on the character of a thing" and acquires a "phantom objectivity" [admit: App. D ANT22]. Berger & Luckmann (1966) generalise it: reification is "the apprehension of human phenomena as if they were things", in which people forget their own authorship of the human world [admit: App. D ANT23]. ANT keeps the observation and drops the diagnosis of false consciousness. Latour rejects "critical sociology" that replaces actors' accounts with hidden social forces and treats their objections as proof of the explanation; for ANT, actors are "much more than mere informants" [admit: App. D ANT15]. In ANT terms reification is punctualisation that has stopped being reopened, a practical achievement of the network, not an illusion in anyone's head. That is the sense in which the author's essay uses it: "the thoughts that form actor networks become increasingly embedded until their origins are forgotten." *Model mapping:* the risk in H.3 is not that people are deceived by the model but that the associations needed to reopen it lapse.

**12. Summary mapping.** **Synthesis.**

| ANT concept | Source | Model term | H.3 step |
|---|---|---|---|
| Black-boxing | Latour 1987, 1999; Callon & Latour 1981 | Each accreted layer in V_root(n); the causal model as the black box over the others | Cost of success |
| Punctualisation | Law 1992 | V, L^R, R and M as punctualised network effects; the model as punctualisation of the chain | (i) scale |
| Power as consequence | Latour 1986 | V as performed, hence re-openable by carriers | Carriers vs model |
| Translation, OPP | Callon 1986 | Operators as OPP; epistemic veto | Epistemic veto |
| Irreversibility | Callon 1991 | "Extremely difficult to unwind" (G.2) | Cannot be unwound |
| Centres of calculation, immutable mobiles | Latour 1987 | Model outputs as carriers detached from production | (ii) no stable referent |
| Delegation, script | Akrich 1992; Latour 1992 | Tracing delegated to a non-human; M atrophies | (iii) atrophy |
| Mediator vs intermediary; purification (by analogy) | Latour 2005, 1993 | Directional inscription on mutual relations; attribution a_j as a mediated output | Black-boxing of direction |
| Visible on breakdown; infrastructural inversion | Star 1999; Bowker & Star 1999 | M as reserve capacity, visible only when needed | (iii) atrophy |
| Performativity | Callon 1998; MacKenzie 2006 | Performatively stable φ; model shapes its own data | Ceiling in H.2 |
| Reification (reworked) | Lukács 1923; Berger & Luckmann 1966; Latour 2005 | Punctualisation no longer reopened | Whole argument |
| Matters of fact vs concern | Latour 2004 | Attribution as settled fact vs assembly to trace | Black-boxing of direction |

### H.5 Predictions

All predictions below are proposed and untested. [abstain: unverifiable — proposed, not yet tested] In ANT terms, P22 tests whether attribution tools de-punctualise V, P23 whether the model's own punctualisation erodes the capacity to reopen it, and P24 whether its operators become the obligatory passage point.

| # | Prediction | Model term tested | What would falsify it | Data or design | Source |
|---|---|---|---|---|---|
| P22 | **Attribution speeds carriers, not reform.** Where attribution tools become available for a harm, carriers emerge faster (litigation filed, insurance repriced, regulatory standing granted), but root reform still waits for V conditions: harm in the veto holders' radius, a crisis reaching many veto groups, or elite displacement. | Carrier emergence vs V(H_elite) | Root reform following attribution capability directly, without a carrier, or carriers no faster after attribution becomes available | Event study around the first attribution studies for a hazard class (WWA event types; pharmacovigilance signals) against carrier dates and root-reform dates; Sabin Center litigation database | H.1; G.1; App. D AT1–AT8 |
| P23 | **Delegated tracing impairs unassisted proficiency, most in novices and for cognitive tasks, and its maintenance is cut first.** Where diagnostic or causal tracing is delegated to models: (a) people trained with the model reach lower unassisted proficiency than people trained without it; (b) experienced practitioners' unassisted proficiency declines with time since their last unassisted practice, faster for cognitive monitoring and diagnostic judgement than for perceptual-motor execution; (c) active engagement (verifying outputs, asking for explanations, guardrails that withhold answers) weakens (a) and (b); (d) mandates to maintain unassisted proficiency erode first under fiscal pressure. Automation bias while assisted is a separate, immediate effect and does not count as evidence for (a) or (b). | M erosion: (a) failed formation, (b) atrophy through disuse (H.3 iii), (d) M under fiscal erosion (B.4.1) | (a) and (b): unassisted proficiency at 12 months or more no lower in exposed units than in unexposed units, or no gradient between novices and experts, or between cognitive and motor tasks. (c): no moderation by engagement. (d): maintenance mandates surviving fiscal consolidation at rates no lower than other functions. | A stepped-wedge cluster trial of model deployment with periodic unassisted probes, recording case mix and procedural covariates (extending and replicating Budzyń et al. 2025). Novice-cohort RCTs on the designs of Bastani et al. 2025 and Shen & Tamkin 2026. Budget lines for oversight and reserve capacity under consolidation. | H.3; B.4.1; App. D AU1–AU8; Casner et al. 2014; Arthur et al. 1998; Haslbeck & Hoermann 2016 |
| P24 | **Disputes move from causes to access.** Where one causal model becomes widely adopted in a policy domain, its operators become an obligatory passage point, and policy disputes shift from contesting causes to contesting access to, or control of, the model (data access, audit rights, licensing, who may retrain it). | OPP; epistemic veto | Disputes continuing to contest causal claims directly at similar rates after adoption, or access disputes not rising | Content coding of regulatory proceedings and litigation before and after adoption of a shared model; DSA researcher-access disputes as a near analogue (App. C SM5) | H.3; H.4 point 4 |

**Applied to the three systems in the research question (forward-looking, unverified).**
- *Credit:* P22 predicts that better attribution of French fiscal spill-overs speeds rating and market repricing (carriers) without itself producing deficit correction.
- *Climate:* P22 and P24 predict that attribution and digital twins speed liability claims and repricing, and that disputes shift toward who runs and audits the twins.
- *AI safety:* P23 predicts that as AI systems are used to audit other AI systems, human auditing capacity declines, and that its maintenance is the first oversight cost cut.

[abstain: unverifiable — forward predictions]

### H.6 Concluding synthesis

The author's essay argues that LLMs reify language at light speed: a translation that standardises rather than diversifies, producing simulacra, copies detached from any original. This report has traced a slower version of the same process in policy. Root causes go untraced, symptomatic layers accrete, and each layer is punctualised by the beneficiaries who come to depend on it, until a tractable problem is wicked and cannot be unwound. Causal AI is the obvious instrument for breaking that trap, because the trap is partly a failure to link causes and effects across networks too large to trace by hand. Part H's conclusion is that the instrument risks becoming the trap's most complete form. A causal model that succeeds is black-boxed by its own success, in exactly Latour's sense: it inscribes direction onto mutual relations, sends its outputs out as matters of fact, lets the human capacity to trace waste away as unused M, and turns its operators into the obligatory passage point for every future carrier. In the essay's terms it would be a simulacrum of tracing: the form of causal explanation, circulating without the work that once produced it. The mitigations are known (snapshots, provenance, practised human tracing). The report's own model predicts that they are the first things to go. Whether that prediction holds is P23. **Synthesis.**

---

## Annotated reading list (grouped by discipline)

Citation counts are given only where I verified them this session. "DOI (from memory)" means the DOI was not re-checked.

### Sociology
- **Granovetter, M. (1978).** Threshold models of collective behavior. *AJS* 83(6):1420–1443. https://gwern.net/doc/sociology/1978-granovetter.pdf (DOI from memory: 10.1086/226707). *The foundational cascade model. Read p. 1420 (threshold = net-benefit crossover), fn. 3 (proportions vs numbers) and p. 1437 (misperception).*
- **Uslaner, E. M. (2002).** *The Moral Foundations of Trust.* Cambridge UP. Ch. 2: http://gvptsites.umd.edu/uslaner/Trustch2.pdf. *Particularised vs generalised trust; the author's "circles".*
- **Delhey, J., Newton, K., & Welzel, C. (2011).** How general is trust in "most people"? Solving the radius of trust problem. *ASR* 76(5):786–807. doi:10.1177/0003122411420817. *Operationalises the trust radius for 51 countries; the empirical hook for testing the synthesis.*
- **Banfield, E. C. (1958).** *The Moral Basis of a Backward Society.* Free Press. *Amoral familism. Read with Miller (1974, American Ethnologist), who failed to replicate it.*
- **Oliver, P. E., & Marwell, G. (1988).** The paradox of group size in collective action: a theory of the critical mass II. *ASR* 53(1):1–8. doi:10.2307/2095728. Also Marwell & Oliver (1993), *The Critical Mass in Collective Action*, Cambridge UP. *The direct rebuttal to Olson on group size.*
- **Norgaard, K. M. (2011).** *Living in Denial.* MIT Press. *Socially organised denial (not re-checked).*
- **Beck, U. (1992 [1986]).** *Risk Society.* Sage. *Manufactured risk (not re-checked).*
- **Pauly, D. (1995).** Anecdotes and the shifting baseline syndrome of fisheries. *TREE* 10(10):430. doi:10.1016/S0169-5347(00)89171-5. About 1,560 WoS references (1998–2023, per Alleway et al. 2023).

### Economics
- **Alesina, A., & Drazen, A. (1991).** Why are stabilizations delayed? *AER* 81(5):1170–88. https://dash.harvard.edu/bitstream/handle/1/4553028/alesina_whystabilizations.pdf. *War-of-attrition model of delay.*
- **Drazen, A., & Grilli, V. (1993).** The benefit of crises for economic reforms. *AER* 83(3):598–607. JSTOR 2117535. 189 citations (EconPapers). *The closest formal statement of the author's crossover.*
- **Drazen, A., & Easterly, W. (2001).** Do crises induce reform? *Economics & Politics* 13(2):129–58. doi:10.1111/1468-0343.00087. *Only extreme crises do.*
- **Fernandez, R., & Rodrik, D. (1991).** Resistance to reform. *AER* 81(5):1146–55. JSTOR 2006910. About 1,160 citations (Semantic Scholar).
- **Olson, M. (1965).** *The Logic of Collective Action.* Harvard UP (quote p. 2). **Olson (1982)** *The Rise and Decline of Nations*, Yale UP.
- **Isaac, R. M., Walker, J., & Williams, A. (1994).** Group size and the voluntary provision of public goods. *J Public Econ* 54(1):1–36. doi:10.1016/0047-2727(94)90068-X.
- **Minsky, H. P. (1992).** The Financial Instability Hypothesis. Levy WP 74. https://www.levyinstitute.org/pubs/wp74.pdf.
- **Guttentag, J., & Herring, R. (1986).** *Disaster Myopia in International Banking.* Princeton Essays in Int'l Finance 164.
- **Krippner, G. (2005).** The financialization of the American economy. *Socio-Economic Review* 3(2):173–208. doi:10.1093/SER/mwi008.
- **Arcand, J.-L., Berkes, E., & Panizza, U. (2015).** Too much finance? *J Econ Growth* 20:105–148. doi:10.1007/s10887-015-9115-2. *Counterpoint: Cline (2015) PIIE PB15-9.*
- **Herndon, T., Ash, M., & Pollin, R. (2014).** Does high public debt consistently stifle economic growth? *Camb J Econ* 38(2):257–79. doi:10.1093/cje/bet075.
- **Andre, P., Boneva, T., Chopra, F., & Falk, A. (2024).** Globally representative evidence on the actual and perceived support for climate action. *Nat Clim Change* 14:253–59. doi:10.1038/s41558-024-01925-3.
- **Carney, M. (2015).** Breaking the tragedy of the horizon. Bank of England speech, 29 Sep 2015. https://www.bis.org/review/r151009a.pdf.
- **IMF (2025/2026).** Global Debt Database; *Fiscal Monitor* Apr 2026. https://www.imf.org/en/publications/fm/issues/2026/04/15/fiscal-monitor-april-2026.

### Political science and public policy
- **Kuran, T. (1991).** Now out of never. *World Politics* 44(1):7–48. **Kuran (1995)** *Private Truths, Public Lies*, Harvard UP. *The theory behind the "iceberg".*
- **Lohmann, S. (1994).** The dynamics of informational cascades. *World Politics* 47(1):42–101. doi:10.2307/2950679.
- **Chenoweth, E., & Stephan, M. (2011).** *Why Civil Resistance Works.* Columbia UP. **Chenoweth (2020)** "Questions, answers, and some cautionary updates regarding the 3.5% rule", Carr Center DP 2020-005, https://www.hks.harvard.edu/sites/default/files/2024-05/Erica%20Chenoweth_2020-005.pdf. **Chenoweth (2020)** "The future of nonviolent resistance", *J Democracy* 31(3):69–84, doi:10.1353/jod.2020.0046.
- **Levin, K., Cashore, B., Bernstein, S., & Auld, G. (2012).** Overcoming the tragedy of super wicked problems. *Policy Sciences* 45:123–152. doi:10.1007/s11077-012-9151-0.
- **Hazlett, C., & Mildenberger, M. (2020).** Wildfire exposure increases pro-environment voting within Democratic but not Republican areas. *APSR* 114(4):1359–65. doi:10.1017/S0003055420000441.
- **Ostrom, E. (2010).** Beyond markets and states. *AER* 100(3):641–72. doi:10.1257/aer.100.3.641. Also *Governing the Commons* (Cambridge UP, 1990).
- **Bazerman, M., & Watkins, M. (2004).** *Predictable Surprises.* HBS Press. HBR article 2003, 81(3):72–80.
- **Baumgartner & Jones (1993)** *Agendas and Instability* (Chicago); **Kingdon (1984)** *Agendas, Alternatives, and Public Policies*; **Hirschman (1970)** *Exit, Voice, and Loyalty* (Harvard). Not re-checked.
- **Noelle-Neumann, E. (1974).** The spiral of silence. *J Communication* 24(2). Meta-analyses: Glynn, Hayes & Shanahan 1997, *POQ* 61:452–63, doi:10.1086/297808; Matthes, Knoll & von Sikorski 2018, *Comm Research*, doi:10.1177/0093650217745429.
- **Lawrence, M., Homer-Dixon, T., et al. (2024).** Global polycrisis. *Global Sustainability* 7:e6. doi:10.1017/sus.2024.1.
- **Arnold, R. D. (1990).** *The Logic of Congressional Action.* Yale University Press. Some listings give 1992. *The origin of "traceability": legislators anticipate whether citizens can trace an effect along the causal chain to a government action and to their own vote. The closest precedent for G.1's attribution decay and for responses settling near the symptom.* First direct test: **Mildenberger, M. & Sahn, A. (2025).** The effect of policy traceability on legislative incentives. *Legislative Studies Quarterly* 50(4):e70036. doi:10.1111/lsq.70036. Elites respond to traceability; voters do not.

### Philosophy and ethics
- **Gardiner, S. M. (2006).** A perfect moral storm. *Environmental Values* 15(3):397–413 (DOIs differ across sources: 10.3197/096327106778226293 / …310). Book: OUP 2011.
- **Jamieson, D. (2014).** *Reason in a Dark Time.* OUP. Not re-checked.
- **Collingridge, D. (1980).** *The Social Control of Technology.* Frances Pinter. *The dilemma, applied to AI.*
- **Diamond, J. (2005).** *Collapse,* ch. 14. Viking. *Creeping normalcy, landscape amnesia, rational bad behaviour, elite insulation.*
- **Tainter, J. (1988).** *The Collapse of Complex Societies.* Cambridge UP (publisher from memory).

### Psychology and behavioural science
- **Weber, E. U. (2006).** Experience-based and description-based perceptions of long-term risk. *Climatic Change* 77:103–120. doi:10.1007/s10584-006-9060-3.
- **Moore, F. C., Obradovich, N., Lehner, F., & Baylis, P. (2019).** Rapidly declining remarkability of temperature anomalies… *PNAS* 116(11):4905–10. doi:10.1073/pnas.1816541116.
- **Sparkman, G., Geiger, N., & Weber, E. U. (2022).** Americans experience a false social reality… *Nat Commun* 13:4779. doi:10.1038/s41467-022-32412-y.
- **Tiede, K. E., Maur, K., Betsch, C., et al. (2026).** People systematically under- and overestimate public engagement in climate action. *Nat Clim Change.* doi:10.1038/s41558-026-02668-z.
- **Feygina, I., Jost, J. T., & Goldsmith, R. E. (2010).** System justification and denial of global warming. *PSPB* 36(3):326–38. doi:10.1177/0146167209351435. About 565 Scopus citations.
- **Howe, P., Marlon, J., Mildenberger, M., & Shield, B. (2019).** How will climate change shape climate opinion? *ERL* 14:113001. doi:10.1088/1748-9326/ab466a.
- **Diekmann, A. (1985).** Volunteer's dilemma. *J Conflict Resolution* 29(4):605–10. doi:10.1177/0022002785029004003.
- **Kahneman & Tversky (1979)** *Econometrica* 47(2):263–91; **Samuelson & Zeckhauser (1988)** *J Risk Uncertainty* 1:7–59; **Laibson (1997)** *QJE* 112(2):443–77; **Darley & Latané (1968)** *JPSP* 8(4):377–83. Not re-checked.

### Complexity, mathematics and physics of social systems
- **Watts, D. J. (2002).** A simple model of global cascades on random networks. *PNAS* 99(9):5766–71. doi:10.1073/pnas.082090499.
- **Xie, J., Sreenivasan, S., Korniss, G., Zhang, W., Lim, C., & Szymanski, B. (2011).** Social consensus through the influence of committed minorities. *PRE* 84:011130. doi:10.1103/PhysRevE.84.011130. arXiv:1102.3931.
- **Centola, D., Becker, J., Brackbill, D., & Baronchelli, A. (2018).** Experimental evidence for tipping points in social convention. *Science* 360:1116–19. doi:10.1126/science.aas8827.
- **Iacopini, I., Petri, G., Baronchelli, A., & Barrat, A. (2022).** Group interactions modulate critical mass dynamics in social convention. *Communications Physics* 5. doi:10.1038/s42005-022-00845-y. *Higher-order interactions change the critical mass (not read in full).*
- **Otto, I. M., Donges, J. F., et al. (2020).** Social tipping dynamics for stabilizing Earth's climate by 2050. *PNAS* 117(5):2354–65. doi:10.1073/pnas.1900577117. Critiques: Smith, Christie & Willis 2020 (PNAS letter); **Milkoreit, M. (2023)** *WIREs Clim Change* 14:e813, doi:10.1002/wcc.813.
- **Schelling, T. (1978).** *Micromotives and Macrobehavior.* Norton. Not re-checked.

### Climate science (Part A primary sources)
- IPCC AR6 WG1 Ch. 4 & Ch. 9; SPM. https://www.ipcc.ch/report/ar6/wg1/
- WMO *State of the Global Climate 2025* (Mar 2026); WMO El Niño/La Niña Update (3 Sep 2026): https://wmo.int/news/media-centre/el-nino-set-become-very-strong-raising-risks-of-extreme-weather-2027
- Cai et al. 2014 *NCC* doi:10.1038/nclimate2100 · Seager et al. 2019 *NCC* doi:10.1038/s41558-019-0505-x
- Ditlevsen & Ditlevsen 2023 *Nat Commun* doi:10.1038/s41467-023-39810-w · Terhaar et al. 2025 *Nat Commun* doi:10.1038/s41467-024-55297-5 · Baker et al. 2025 *Nature* doi:10.1038/s41586-024-08544-0 · Drijfhout et al. 2025 *ERL* doi:10.1088/1748-9326/adfa3b · van Westen et al. 2026 *NCC* doi:10.1038/s41558-026-02730-w

---

## Disposition ledger (counts)

| Section | admit | refute | abstain |
|---|---|---|---|
| A.1 Debt (A1–A8) | 4 (A1, A2, A5, A6) | 2 (A4, A8) | 2 (A3, A7) |
| A.2 Climate (A9–A21) | 9 (A9–A12, A14, A17–A19, A21) | 0 | 4 (A13, A15, A16, A20) |
| A.3 AI (A22–A34) | 10 (A22–A28, A31–A33) | 0 | 3 (A29, A30, A34) |
| B.2 mapping table (32 rows) | 26 | 0 | 6 (gray rhino; Diamond ch. 14; Hardin/Ostrom; behavioural classics; punctuated equilibrium/Kingdon/Overton; Beck–Norgaard–Jamieson–Hirschman group) |
| B.3 named term | 0 | 0 | 1 |
| C.1–C.2 maths | 18 (Granovetter; Cases 1–4; Centola; Oliver–Marwell; Isaac et al.; Diekmann; Chenoweth ×3; Otto; Milkoreit; verdict points 1–4) | 3 (Olson as general law; 3.5% as law; universal tipping fraction) | 2 (Centola group N; social tipping by 2050) |
| C.3 iceberg | 8 (C1–C8) | 0 | 1 (worked calibration) |
| **Total** | **75** | **5** | **19** |

Rows grouping several "not re-checked" classics count as one abstain per row.

**Combined ledger.**

| Source | admit | refute | abstain |
|---|---|---|---|
| Main body (Parts A–C) | 75 | 5 | 19 |
| Main body (G.1 traceability precedent) | 5 | 0 | 1 |
| Appendix A (deep history) | 57 | 5 | 26 |
| Appendix B (cross-system, incl. §7.1 deadline panel) | 105 | 4 | 25 |
| Appendix C (n-order harms) | 66 | 10 | 27 |
| Appendix D (causal AI and ANT lineage) | 48 | 2 | 11 |
| **Combined** | **356** | **26** | **109** |

The synthesis text in B.4.1 and Parts D–H re-cites appendix findings and is not counted again. Part G summarises Appendix C, and its tags are not double-counted, except the G.1 traceability precedent, which cites sources outside Appendix C and has its own row. Part H summarises Appendix D, and its tags are not double-counted either; its two prediction abstains (H.5) follow the G.4 convention and are not counted.

---

## Appendix A: Is the Montreal Protocol the exception or the rule?
### Pre-emptive collective action against slow, foreseeable threats, from the Bronze Age to 1990

**Prepared:** 10 October 2026
**Question:** Is the Montreal Protocol an exception rather than the rule, judged across earlier human history rather than modern politics alone?

**Method.** I looked for a primary or authoritative source for every substantive claim and tried to refute the claim against it before tagging it:
- `[admit: source]`: an authoritative source for this specific claim confirmed it this session, and the refutation attempt failed.
- `[refute: source]`: an authoritative source contradicts the claim as usually stated. The correction is given.
- `[abstain: reason]`: the claim could not be confirmed. The reason is one of `unverifiable` (no authoritative source reached this session), `source-vs-prior conflict` (credible sources disagree, or a live historiographical dispute), or `non-authoritative source` (only encyclopaedias, press, blogs or student work were reached).

Text marked **Synthesis** is my own inference from the tagged findings. It is not a sourced claim and is not counted in the ledger.

**A definition used throughout.** A response is **pre-emptive** if it is adopted before the threat has done major, visible damage to the population that decides. It is **crisis-triggered** if it follows a vivid shock. It is **last-moment** if it comes only when damage is already severe and ongoing. It **failed** if no adequate response came before the outcome. Many historical responses are a hybrid: **reactive-then-institutionalised**, where an institution created after a first disaster becomes a standing, anticipatory rule against later recurrences (quarantine, dike boards, granaries).

---

### 1. Summary verdict

1. **For novel, global, slow-onset threats, Montreal is an exception, and only a partial one.** It was pre-emptive in one sense: when it was signed, no statistically significant mid-latitude ozone loss had been measured, and the cause of the Antarctic ozone hole was not settled. But a vivid shock catalysed it (the ozone hole, plus NASA's satellite images). Its 1987 terms were weak: a 50% CFC cut. It was ratcheted up to a full phase-out only in 1990–92, after the science was confirmed. It succeeded because each of the model's variables was unusually favourable:
   - a small number of producers, so a small N among those with a veto;
   - a dominant producer (DuPont) that came to expect profit from substitutes, so the incumbent loss L^R flipped sign for the actor holding the veto;
   - unilateral benefits for the United States that exceeded its costs, so the harm H fell inside the veto-holder's own radius;
   - trade sanctions on non-parties, which raised every actor's expected share of others acting (r̂) and removed free-riding.
2. **In deep history, pre-emption is not rare in general. It is rare against first-encounter threats.** The historical record splits sharply.
   - **Recurrent, local, visible hazards on a bounded commons.** These include floods, plague arrivals, grazing pressure, irrigation water and harvest failure. Societies very often built standing anticipatory institutions, usually after a first disaster: Dutch and Flemish water boards, Ragusa's 1377 quarantine, the Törbel alp statutes, Japanese *iriai* forests, the Valencian huertas and the Qing ever-normal granaries. Many lasted for centuries.
   - **Novel, diffuse, slow threats whose costs fall on people outside the decision-makers' circle.** The usual pattern is that the response is reactive, late or blocked by elites. Examples are Gracchan land reform, England's 1349–51 labour laws, Mamluk Egypt, 15th-century Flemish flood defence and 17th-century Italian plague.
3. **Best-supported base-rate statement. Uncertainty is high.**
   - **No study estimates the base rate of pre-emptive action directly.** The closest data (CrisisDB, n = 168) samples societies that already entered crisis, so it is selected on the outcome.
   - **What CrisisDB does show.** Once in crisis, only about 31% of cases saw any welfare-enhancing reform. Reform was not correlated with how severe the crisis was. The authors describe successfully "flattening the curve" as rare. They study 4 such cases.
   - **My own count.** In this appendix's non-random set of about 25 pre-modern cases, roughly 3 qualify as pre-emptive before first major damage (about 10–15%). Roughly 10 are reactive-then-effective, roughly 9 are failed, late or elite-blocked, and about 4 are transformations or contested.
   - **My stated range.** For novel slow threats with concentrated incumbent benefits, a fair range is **about 5–25% pre-emptive**. That is a judgemental estimate, not a measured one.
4. **The deep-history evidence strongly supports the radius-bounded mechanism and refines it in four ways** (Section 7):
   - **Ostrom-type successes are cases where the trust radius matches the commons.** Users, beneficiaries and rule-makers are the same bounded population, so L^R and H are computed over the same people. Ostrom's own failure cases occur where that alignment breaks.
   - **When decision-makers' interests diverged from the exposed population, anticipatory institutions decayed.** This happened in the Flemish water boards once absentee landlords captured them.
   - **Crisis is not sufficient.** Reform is uncorrelated with crisis severity, so the "eventually pressure > V" assumption needs an alternative exit: displacement of elites or collapse.
   - **The model needs an institutional-memory term.** Repeated exposure builds resilience, and standing institutions keep the perceived harm H high across generations, against shifting baselines.

---

### 2. The Montreal Protocol: pre-emptive, crisis-triggered, or both?

#### 2.1 Timeline and the status of the evidence at signing

| Date | Event | Tag |
|---|---|---|
| 1978 | US bans most non-essential CFC aerosol uses. The ban cost US producers about 20% of the global market. | [abstain: non-authoritative source] (Maxwell & Briscoe 1997 as relayed in search results; not opened) |
| 1980 | DuPont helps organise the Alliance for Responsible CFC Policy to resist EPA controls, and leads industry opposition to 1986. | [admit: Smith 1998; Maxwell & Briscoe 1997, both scholarly business-ethics/strategy papers, via search extracts] |
| Mar 1985 | Vienna Convention: a framework treaty with no binding cuts. | [admit: US Senate Exec. Rpt 107-10; UNFCCC fact sheet] |
| May 1985 | Farman et al. publish the Antarctic springtime ozone "hole". | [admit: UKRI/NERC history; Harvard EPS281r course source] |
| 26 Sep 1986 | DuPont position statement: "If the necessary incentives were provided, we believe alternatives could be introduced in volume in a time-frame of roughly five years." | [admit: DuPont 1986, *Environmental Conservation* 13(4), doi:10.1017/S0376892900035475] |
| 16 Sep 1987 | Montreal Protocol signed. Developed countries were to freeze and then halve their consumption of five CFCs by about 1999 (a 50% cut), and to freeze halons. | [admit: EPA; Canada.ca; EU fact sheet] |
| Mar 1988 | Ozone Trends Panel reports measured depletion, six months after signing. On 24 March DuPont announces it will phase out CFCs. | [admit: Harvard EPS281r source; Smith 1998] |
| 1990 / 1992 | London and Copenhagen amendments turn the 50% cut into a full phase-out by 2000 (London), then accelerate it (Copenhagen). | [admit: US Senate Exec. Rpt 107-10; UNFCCC fact sheet] |

**F1.** When the Protocol was negotiated, no statistically significant mid-latitude ozone depletion had been measured. Models predicted no significant global depletion for about two decades. The Antarctic hole was widely treated as an anomaly of uncertain cause. Benedick called the treaty "preventive action on a global scale". [admit: Benedick, *Ozone Diplomacy* (HUP 1991/1998), and Benedick's 2005 Senate EPW testimony as relayed in search extracts. The PDF itself returned 403. Independently corroborated by Grevsmühl & Briday 2023, abstract: "despite the absence of a scientific consensus on the mechanisms of ozone depletion over Antarctica".]

**F2.** The claim that the ozone hole played *no* role in Montreal is wrong. Negotiators said they deliberately ignored the hole because no theory could yet explain it, but NASA's ozone-hole images "still loomed large for many of the actors involved". [refute: Grevsmühl & Briday 2023, *BJHS* 56(2):247–267]. **Correction:** Montreal is best classified as **pre-emptive with respect to measured damage, but catalysed by a vivid, causally unexplained shock**.

**F3.** The 1987 terms were modest: a 50% cut for five CFCs. Full phase-out came only with the 1990 London Amendment, after the Ozone Trends Panel (1988) and later assessments. [admit: US Senate Exec. Rpt 107-10; UNFCCC fact sheet]. That is, the *adequate* response was ratcheted up after confirmation, which is the crisis-reinforced part of the story.

#### 2.2 Why it succeeded, mapped to model variables

| Enabling condition | Evidence | Model variable | Tag |
|---|---|---|---|
| Few producers. DuPont alone had about a quarter of world output and about half of US output. | 18 companies made most world CFCs in the early 1980s. DuPont had >50% of US and about 25% of world capacity. US 1986 production was about 300,000 t. | Small N among veto players, so a small V and a short time to tip | [abstain: non-authoritative source] (Rapid Transition Alliance; GESDA; C&EN via search). The DuPont share is consistent across sources, but no peer-reviewed source was opened. |
| CFCs were a small line for the main incumbent | CFCs were about 3% of DuPont's sales | Small L^R for the veto-holder | [abstain: non-authoritative source] |
| Substitutes in view: "roughly five years" with incentives (1986) | DuPont 1986 statement | L^R for the producer turns positive under regulation, because it gains first-mover rents on substitutes | [admit: DuPont 1986, *Environ. Conserv.*] |
| US unilateral benefits ≫ costs | Sunstein: the US adopted Montreal readily because perceived domestic benefits far exceeded costs. Kyoto shows a "radically different picture". | H falls inside the radius of the veto-holding state | [admit: Sunstein 2007, 31 *Harv. Envtl. L. Rev.* 1 (abstract and ELR summary)]. The specific figures (US$21 bn costs vs US$3,575 bn benefits; Barrett's "65 times the costs") are [abstain: non-authoritative source] because they were reached only through citing papers and a magazine. |
| Trade sanctions on non-parties; Multilateral Fund (1990) for developing countries | Barrett: the treaty reversed free-riding incentives through trade restrictions plus side-payments | Raises everyone's perceived share of others acting (r̂) toward 1 and lowers the payoff from defecting | [admit: Barrett 2003, *Environment and Statecraft*, ch. 8 (OUP), via OUP description and secondary summaries. Corroborated by Barrett 2009 Policy Exchange paper.] |
| Vivid, image-able harm (the "hole"), skin-cancer framing | Grevsmühl & Briday 2023 | Raises perceived harm (φ·H) despite distance | [admit: Grevsmühl & Briday 2023] |

**Synthesis.** Montreal is not evidence that pre-emption is normal. It is a case in which **every term of the inequality was unusually favourable at once**:
- small N, so a fast tip;
- incumbent L^R small, and for the pivotal firm it turned positive;
- H fell inside the dominant state's own radius;
- r̂ was made accurate and high by an enforcement design;
- a vivid image raised φ.

Climate change differs on every one of these points. That matches Sunstein's and Barrett's Montreal-versus-Kyoto contrast.

---

### 3. Modern comparators

| Case | Threat foreseen since | Response | Lag | Classification | Model reading | Tag |
|---|---|---|---|---|---|---|
| **Montreal Protocol** (1987–92) | 1974 (Molina–Rowland) | Framework 1985, 50% cut 1987, phase-out 1990–92 | ~13 yr to treaty, ~16 to adequacy | **Hybrid: pre-emptive on measured damage, catalysed by a shock, ratcheted after confirmation** | Section 2 | see F1–F3 |
| **Acid rain → 1990 CAAA Title IV** | 1970s science; US debate through the 1980s | SO₂ cap-and-trade 1990 | ~15–20 yr | **Delayed / reactive.** It also "did the right thing for the wrong reason": most benefits came from cutting particulate-matter health harm, not from acidification. | High L^R (coal regions) and elite veto in the 1980s. Crossed once cheap low-sulphur coal (rail deregulation) cut costs. | [admit: Schmalensee & Stavins 2013, *JEP* 27(1):103–22]. The "1980s Reagan-era delay" detail is [abstain: unverifiable]: the full text was not opened. |
| **Leaded petrol** | Toxicity warnings from the 1920s | Japan eliminated it in 1972; UNEP campaign from 2002; Algeria last in July 2021 | ~100 yr | **Failed for decades, then last-moment and piecemeal** | Very high L^R (cheap octane, used-car trade). H diffuse and invisible, a textbook shifting baseline. | [admit: UNEP announcement 30 Aug 2021 as reported by NPR/Al Jazeera/E&T]. "Warnings from the 1920s" is [abstain: non-authoritative source]. |
| **Smallpox eradication** | Eradication proposed 1953 and 1958 (USSR) | Intensified programme 1967, last case 1977, certified 1980 | ~20 yr from proposal | **Proactive removal of an *ongoing* harm.** For already-free rich countries, pre-emptive self-interest. | A weakest-link good (Barrett 2007). US dividend about $150 m/yr against about $100 m total endgame cost, so H sat inside the radius of rich funders. | [admit: Barrett 2007 typology via OUP ToC and Barrett's PMC paper; Fenner et al. 1988 cost figures via CGD *Millions Saved*]. The "US recoups every 26 days" claim is [abstain: unverifiable]. |
| **Partial Test Ban Treaty 1963** | Castle Bravo / *Lucky Dragon* 1954; Sr-90 in baby teeth | PTBT signed 5 Aug 1963 | ~9 yr | **Crisis-triggered** (Cuban Missile Crisis, Oct 1962), on top of years of built-up pressure | Pressure built slowly; the shock lowered V (superpower leaders) | [admit: Britannica; Atomic Heritage Foundation; Bulletin of the Atomic Scientists 2023]. Historians weight the causes differently. |
| **Y2K** | Known decades ahead; fixed deadline | Massive remediation 1996–99 | none | **Pre-emptive.** Quiggin argues it was *over*-pre-emptive, with most spending wasted and "fix on failure" adequate. | A known deadline removes shifting baselines. Near-zero L^R (no incumbent gains from the bug). Organisations' r̂ was high, as a conformist cascade. | [admit: Quiggin 2005, *AJPA* 64(3):46–55] |
| **London Clean Air Act 1956** | Coal smoke known for centuries | Act only after the Dec 1952 smog (~12,000 deaths). Government stalled; Beaver Committee 1953–54; a private member's bill (Nabarro) forced the government's own bill. | Centuries (1952→1956) | **Crisis-triggered, last-moment** | Ministers played it down: H was outside φ until mass deaths, and even then the executive acted as a veto. | [admit: *History & Policy* paper on the 1956 Act; UoL Press *Law and Justice in the 1950s*] |
| **Great Stink 1858 → Bazalgette's sewers** | Sewage/cholera link argued from 1850s; Metropolitan Board of Works from 1855 | Act passed **18 days** after introduction (15 Jul → 2 Aug 1858) once the Thames stench reached Parliament | years | **Crisis-triggered, and the crisis was located inside the elite's own building** | **Synthesis:** the clearest modern case of V collapsing once H enters the veto-holders' own radius. Cholera deaths among the poor had not done it. | [admit: Portland State Young Historians paper citing Hansard; London Museum]. Pre-1858 obstruction and cholera dates are [abstain: unverifiable]. |

**Synthesis.** Of the 8 modern cases, only **Y2K** (zero incumbent L^R, fixed deadline) is cleanly pre-emptive. Montreal and smallpox are hybrids. Four are crisis-triggered or delayed. Leaded petrol was a near-century failure.

---

### 4. Deep history: cases of collective response to slow-building threats

Key to "Response": **PRE** pre-emptive; **R→I** reactive-then-institutionalised (standing anticipatory rule after a first disaster); **CT** crisis-triggered; **LATE** last-moment; **FAIL** failed or elite-blocked; **TRANS** transformation, migration or exit; **CONT** status contested.

| # | Case | Period | Slow threat | Foreseen? | Response | Mapped model variables | Historiographical status | Tag |
|---|---|---|---|---|---|---|---|---|
| D1 | **Mesopotamian soil salinisation** | ca. 2400–1700 BCE | Irrigation-driven salt build-up | Partly: the shift toward barley and fallowing practices imply awareness | **CONT.** Either slow failure (Jacobsen & Adams) or managed by fallow and leaching (Powell) | If Powell is right, local routine management (bounded radius); if Jacobsen–Adams is right, φ decays through slow yield decline | Live dispute. Powell 1985 critiques the yield texts; Artzy & Hillel 1988 defend the theory. | [abstain: source-vs-prior conflict] (Jacobsen & Adams 1958, *Science* 128:1251; Powell 1985, *ZA* 75:7–38; Artzy & Hillel 1988, *Geoarchaeology* 3(3)) |
| D2 | **Late Bronze Age collapse** (E. Mediterranean) | 13th–12th c. BCE | Drought, systemic fragility, raiding, political strife | Unclear | **FAIL / TRANS** (palace systems end) | Multi-causal. A rare extreme drought "can overwhelm contemporary risk-buffering practices". | No single explanation; climate overprecision criticised (Knapp & Manning). A severe drought ~1198–1196 BCE coincides with the Hittite collapse (Manning et al.). | [admit: Knapp & Manning 2016, *AJA* 120:99–149 (multi-causal, no final solution)]; [admit: Manning et al. 2023, *Nature* 614 (drought coincident)]. Drought as *sufficient* cause: [abstain: source-vs-prior conflict] |
| D3 | **Classic Maya** (southern lowlands) | drying 660–1000 CE; drought 1020–1100 | Multi-century drying trend | Plausibly, as a slow trend over generations | **FAIL** at the polity level (balkanisation, warfare, disintegration), after centuries of agricultural adaptation | Long, slow H; φ eroded by gradualness; elite (divine-king) competition | Kennett et al.: wet phase → expansion; drying → "balkanization… increased warfare… asynchronous disintegration". Douglas et al. 2015 stress agricultural adaptation and caveat the Yok Balum isotopes. | [admit: Kennett et al. 2012, *Science* 338:788–791]; adaptation-before-collapse: [admit: Douglas et al. 2015, *PNAS* 112:5607] |
| D4 | **Norse Greenland vs Inuit** | ca. 985–1450 CE | Little Ice Age cooling, market and ivory-trade shifts | Gradual | **R→ adaptation, then end.** Successful intensification of communal sealing (marine diet rose to as much as ~80%), but it created new vulnerabilities; the end came through "conjunctures". | Adaptation happened within the community radius. Arneborg: farming identity "held in place by an over-class that maintained power through agriculture and land ownership" is an elite L^R term. | Diamond's "inflexible, maladapted" picture is revised | [refute: Dugmore et al. 2012, *PNAS* 109:3658–63, and Arneborg/Nelson et al. 2012 isotope work] against the "refused to adapt" claim. The over-class quote is [abstain: non-authoritative source] (via ScienceDaily). |
| D5 | **Rapa Nui (Easter Island)** | ca. 1200–1722 CE | Deforestation and soil loss | Unclear | **No pre-contact collapse.** Adaptation (rock gardens, marine resources); ahu building continued to and beyond 1722. | Small island community; trust radius ≈ island; adaptive rather than ecocidal | **Highly contested.** Diamond's 2005 "ecocide" is challenged by DiNapoli et al. 2020 (*J. Archaeol. Sci.*), Davis et al. 2024 (*Sci. Adv.*, carrying capacity about 3,900 ± 800) and Moreno-Mayar et al. 2024 (*Nature*: genomes reject a severe 1600s bottleneck). Van Tilburg disputes the radiocarbon associations. Deforestation itself is not in dispute. | [refute: Moreno-Mayar et al. 2024, *Nature* 633:389–397; Davis et al. 2024, *Sci. Adv.* 10:eado1459] against "severe pre-contact demographic collapse". The residual dispute is [abstain: source-vs-prior conflict]. |
| D6 | **Tokugawa forestry** | 1570–1670 depletion; regeneration from late 1600s | Timber depletion, erosion | Yes, visible shortages | **CT / R→I:** a "negative regimen" of regulation, then silviculture and plantations ("regenerative forestry") | Top-down pre-emption once the elite's *own* timber supply (L^R) was threatened, plus village *iriai* rules | Totman 1989 is the standard account. Saito (J. Global Hist.) calls Totman's assessment "too optimistic"; Osako attributes the shift to coercion of peasants. | [admit: Totman 1989 (UC Press description and ToC)]; Saito's caveat: [abstain: source-vs-prior conflict] |
| D7 | **Tikopia** | ca. 1000–1900 CE | Island carrying capacity | Yes, culturally encoded | **R→I:** pigs eliminated (~1600, dated variously); population held near zero growth (celibacy, infanticide, voyaging, expulsion); orchard gardening | A ~1,200-person island where the trust radius equals the commons. Very high φ (small, bounded, visible). | Classic success case (Firth; Kirch & Yen; Diamond), but specific dates and figures reached only via secondary material | [abstain: non-authoritative source] (Kirch & Yen 1982 reached only through citing student and encyclopaedia material) |
| D8 | **Venetian lagoon river diversions** | 1501/1505 water magistracies; diversions 1507–1683 | Siltation closing the lagoon and inlets | **Yes**: an explicit slow-threat narrative ("keep the lagoon from becoming mainland") | **PRE** relative to loss of the lagoon: a two-century engineering programme on Brenta, Bacchiglione, Piave, Sile and others | Patrician elite's L^R (navigable lagoon, defence) aligned with acting; costs (flooding, marshes) displaced onto the mainland, *outside* the radius | Engineering history well documented; the externality claim reached only via encyclopaedic sources | [admit: Bondesan & Furlanetto 2012, *Géomorphologie* 4/2012:175–200 (purpose: inlets "menaced by progressive decreasing of water depth"; projects "only partially carried out")]. Mainland flood externality: [abstain: non-authoritative source] |
| D9 | **Low Countries water boards** (Holland, Flanders) | 12th–13th c. onward | Storm floods, peat subsidence | Yes, recurrent | **R→I:** boards, dike taxes and centralised maintenance from the late 13th c. Then, in 15th-c. Flanders, **FAIL under elite capture.** | Peasant voice declined; absentee landlords captured the boards and chose austerity, so flood losses rose. A direct case of decision-maker radius ≠ exposure radius. | Rijnland founding date 1248 vs 1255; "polder democracy" called a myth by van Tielhof's NWO project | [admit: van Bavel, Curtis & Soens 2018, *Ecology & Society* 23(4):30; Soens 2011 *Continuity & Change* 26:333–65; Soens 2013 *Environment & History* 19(2)]. Founding date: [abstain: source-vs-prior conflict] |
| D10 | **Törbel (Valais) alp commons** | Articles of 1483; wintering rule 1517 | Overgrazing | Yes | **PRE / R→I:** stinting by the rule that no one may send more cows to the alp than they can winter | User set = owner set = rule-makers; small N; monitoring | Netting 1981; Ostrom 1990 ch. 3. Whether degradation preceded the rules is unknown. | [admit: Ostrom 1990 ch. 3 (dates and rule)]. Pre-emptive timing: [abstain: unverifiable] |
| D11 | **Japanese *iriai* commons** | 17th c. onward | Forest and fodder depletion | Yes | **R→I** (emerged after the early-modern depletion) | Village-bounded rights; monitoring; graduated sanctions | McKean 1982/1986; Ostrom 1990 | [admit: Ostrom 1990 ch. 3; McKean 1982, *Environmental Review* 6(2)] |
| D12 | **Spanish huertas** (Valencia, Murcia, Orihuela) | medieval onward | Water scarcity, drought | Yes, recurrent | **R→I:** turn rules (*tanda/turno*); nested irrigators' institutions | Nested enterprises (Ostrom principle 8) | Ostrom 1990 ch. 3 | [admit: Ostrom 1990 ch. 3] |
| D13 | **Medieval NW European commons and guilds** | from ~1100 | Overuse of common land | Yes | **R→I:** a "silent revolution" of institutions for collective action | Bounded membership | De Moor 2015 (Flanders micro-study) | [admit: De Moor 2015, CUP, doi:10.1017/CBO9781139135450 (via review)] |
| D14 | **Black Death, Venice** | 1348; permanent magistracy 1490 | Plague recurrence | After 1348, yes | **CT** (three temporary *savi*, 30 Mar 1348), then **R→I** (*Magistrato alla Sanità* 1490) | Reactive learning converted into a standing anticipatory institution | Dates via encyclopaedic sources | [abstain: non-authoritative source] |
| D15 | **Ragusa (Dubrovnik) quarantine** | 27 Jul 1377 | Plague arrival by sea and land | Yes, after 1348 | **R→I:** a 30-day *trentino* (later 40 days). Outbreaks still occurred in 1391 and 1397. | Small merchant oligarchy whose trade interest (L^R) *aligned* with exclusion. One scholar argues the rule's main motive was protecting trade. | Classic case (Gensini et al. 2004; Cipolla) | [admit: Gensini, Yacoub & Conti 2004, *J. Infection*, PMC7133622, via search extract]. Trade-motive interpretation: [abstain: non-authoritative source] |
| D16 | **England after the Black Death** | Ordinance of Labourers 1349; Statute 1351 | Labour scarcity, social order | n/a | **FAIL (elite double-down):** a wage freeze at 1346 levels; coercion; "re-casting the labour shortage as a moral problem requiring a coercive solution"; largely ineffective | A pure elite-veto case: L^R defended against a population-wide shift | Bailey 2025 | [admit: Bailey 2025, *Economic History Review*, doi:10.1111/ehr.13355] |
| D17 | **Italian plague 1629–30 and 1656–57** | 17th c. | Plague recurrence | Yes: health boards existed | **Partial FAIL.** About one-third of northern Italy's population died in 1629–31, with lasting urban decline. | Standing institutions are not sufficient when the shock is pervasive | Alfani 2013; Alfani & Percoco 2019 | [admit: Alfani 2013, *EREH* 17(4):408–430; Alfani & Percoco 2019, *EcHR* 72(4)] |
| D18 | **Roman Republic agrarian crisis and the Gracchi** | 133–121 BCE | Smallholder landlessness, recruitment base | Long-discussed | **FAIL / LATE:** a tribune's veto (Octavius) backed by the senate; Tiberius killed in 133; Gaius in 121; then a century of civil wars | The canonical elite veto (V) on redistribution of *ager publicus* | The premise is contested. Rosenstein (2004) argues the crisis came from population *growth* and partible inheritance, not smallholder ruin by war. Brunt's "impoverishment" view is the traditional one. | Elite obstruction: [admit: Britannica (Gracchi entry); Flower 2010 via encyclopaedic citation]. Cause of the agrarian crisis: [abstain: source-vs-prior conflict] |
| D19 | **Qing ever-normal granaries** | 1650–1780s growth; decline 1781–1850 | Harvest failure, famine | **Yes**: a standing buffer | **PRE** (a standing anticipatory institution), then eroded by fiscal and organisational constraints and changed official evaluations | Pre-emption by a high-capacity state. Decay driven by fiscal distress (the structural-demographic mechanism, SDT). | Will & Wong 1991 | [admit: Will & Wong 1991 (Michigan; OA via OAPEN), Part I "Development and Decline"] |
| D20 | **Dutch Republic in the Little Ice Age** | 1560–1720 | Cooling, storms, ice | Partly | **Adaptive, even opportunistic:** commerce, war and culture exploited the cold. Degroot also notes who benefited unevenly. | High state and merchant capacity; recurrent hazard | Degroot 2018 (reviews caution on attributing prosperity to climate) | [admit: Degroot 2018, CUP (publisher abstract and H-Environment roundtable)] |
| D21 | **17th-century General Crisis** | 1618–1680s | LIA "fatal synergy" with war | Partly | Mostly **FAIL**; Tokugawa Japan the stand-out exception | Weak or overstretched states failed | Parker 2013 | [admit: Parker 2013, Yale (publisher description)]. Japan-as-exception: [abstain: non-authoritative source] (reader reviews only) |
| D22 | **Angkor** | decline from early 1300s | Hydraulic-network fragility; floods and drought | Unclear | **TRANS (elite exit):** land use in the core declined a century before the 1431 invasion. Infrastructure failed "because the urban elite had already left". | Exit rather than voice: the elite radius moved away and the commons was abandoned | The "catastrophic 15th-c. collapse" is revised | [refute: Penny et al. 2019, *PNAS* 116:4871–76] against catastrophic collapse. Climate contribution: [abstain: unverifiable] (Buckley et al. 2010 not opened) |
| D23 | **Ancestral Puebloans** (Mesa Verde etc.) | 500–1300 CE | Drought, niche contraction | Partly | **TRANS:** repeated reorganisations; the 13th-c. migration timed to niche size and stability | Critical slowing down (rising autocorrelation and variance) preceded transformations, not simply caused by climate | Kohler and Bocinsky programme | [admit: Scheffer et al. 2021, *PNAS* 118:e2024397118; Bocinsky & Kohler 2014, *Nat. Commun.* 5:5618] |
| D24 | **Mamluk Egypt, 14th c.** | 1340s onward | Inequality, floods, plague | Yes | **FAIL (double-down):** resources diverted to monuments rather than relief, then civil war | Elite veto plus elite L^R | Holder et al. (forthcoming), via Hoyer et al. 2026 | [admit: Hoyer et al. 2026, SUERF Policy Brief 1359]. The full study is not yet peer-reviewed, so treat this as preliminary. |
| D25 | **"Crises averted"**: early Republican Rome, Chartist England, Russian Reform era, US Progressive Era | various | Structural-demographic pressure | Yes | **LATE but effective:** adaptive reform under high pressure, before outright collapse | Elites ceded part of L^R while the state still had capacity | Hoyer et al. 2025, Cliodynamics | [admit: Hoyer et al. 2025, *Cliodynamics*, doi:10.21237/C7clio.38365 (via CSH/EurekAlert summary and SUERF brief)] |

#### 4.1 Notes on contested cases (collapse revisionism)

- **The revisionist programme** (McAnany & Yoffee 2010; Middleton 2017; Butzer 2012) argues that "collapse" usually means political transformation with demographic continuity, and that resilience is under-reported. Butzer: "Undue attention to stressors risks underestimating the intricate interplay of environmental, political, and sociocultural resilience". He adds that alarmist literature "fails to appreciate that resilience and readaptation depend on identified options, improved understanding, cultural solidarity, enlightened leadership, and opportunities for participation". [admit: Butzer 2012, *PNAS* 109:3632–39 (abstract)]; [admit: Middleton 2017 (CUP abstract; Anderson 2020 review in *Cliodynamics*)].
- **Degroot et al. 2021** argue that methodological problems lead researchers to *systematically over-represent disastrous responses* to past climate change. [admit: Degroot et al. 2021, *Nature* 591:539–550 (abstract)]. **Implication for this question:** the "failure" column of any case table drawn from the collapse literature is inflated. The pre-emption base rate in Section 5 should be read as a lower-bound-biased estimate *for the threats that got written about*.
- **Diamond (2005)** remains the reference account for Rapa Nui, the Norse and the Maya as self-inflicted failures, and for Tikopia, Tokugawa Japan and the New Guinea highlands as successes. His Rapa Nui and Norse narratives are substantially revised (D4, D5). His success cases are broadly supported, with Saito's caveat on Tokugawa. Diamond's "top-down vs bottom-up" typology of successes: [abstain: unverifiable] (not opened this session).

---

### 5. Quantitative and base-rate evidence

| Study | Sample | Key result relevant to pre-emption | Tag |
|---|---|---|---|
| **Hoyer et al. 2023**, *Phil. Trans. R. Soc. B* 378:20220402 | CrisisDB, >150 crises (fig. 1, n = 169) | Outcomes range from collapse to reform. "More often… power holders tend to 'double-down' on prevailing systems and entrenched privilege during crises… undermining attempts at adaptation and reform." "On rare occasions" crises enable welfare-raising reform. Three pressures undermine collective action: immiseration, elite overproduction and conflict, and state fiscal distress. | [admit: Hoyer et al. 2023, full text read this session] |
| **Hoyer et al. 2025**, *Social Science History* (preprint 2024, osf.io/rk4gd) | CrisisDB, 168 coded crises (from 250 candidates), Bronze Age to early 20th c. | **Only 31% of cases experienced one or more reforms.** Reform shows **no obvious correlation with crisis severity**. Median crisis duration 22 years. The sample deliberately includes "potential" (averted) crises. Scale and administrative complexity correlate *negatively* with reform; hierarchical complexity positively. | [admit: Hoyer et al. preprint full text read this session; published version doi:10.1017/ssh.2025.10113]. The "~5% end in collapse" figure is [abstain: non-authoritative source] (blog summary). |
| **Hoyer et al. 2026**, SUERF Policy Brief 1359 | Same >150 cases | "In the vast majority of cases the outcomes were massive loss of life, the failure of critical institutions, civil war or even complete societal collapse. In rare instances… societies… managed to 'flatten the curve'." "At the very point where reform is most needed, those with the greatest power to enact it are least inclined to do so." | [admit: SUERF brief full text read this session]. A policy brief, not peer-reviewed; it summarises peer-reviewed work. |
| **Hoyer et al. 2025**, *Cliodynamics* "Crises Averted" | 4 averted cases | Averted crises "rarely produced perfect or permanent solutions". Elites ceding privilege while state capacity remained was common to all four. | [admit: CSH publication page / EurekAlert release; SUERF brief] |
| **Scheffer et al. 2023**, *PNAS* 120:e2218834120 | 324 premodern states (MOROS) | The risk of a state ending rises over the first ~200 years, then levels off. This is the first quantitative support for declining state resilience over time. | [admit: PNAS abstract via search] |
| **Riris et al. 2024**, *Nature* 629:837–842 | 154 population-downturn periods, 16 regions, 30 kyr (radiocarbon SPDs) | "A single factor — the frequency of downturns — increases both the ability to withstand disturbances and to recover from them." Farming societies are more vulnerable but more resilient. | [admit: Riris et al. 2024, full text read via Europe PMC] |
| **Scheffer et al. 2021**, *PNAS* | 5 Pueblo transformations, 8 centuries | Critical slowing down preceded transformations. They were "not simply driven by climate downturns". | [admit: PNAS abstract via search] |
| **Cumming & Peterson 2017**, *TREE* 32(9):695–713 | 17 representative cases | 14 mechanisms of social-ecological collapse in 5 classes; system structure shapes the type of collapse | [admit: abstract via JCU/UWA repositories] |
| **Cox, Arnold & Villamayor-Tomás 2010**, *Ecol. & Soc.* 15(4):38 | 91 empirical studies of commons | Ostrom's design principles are "well supported empirically", to be read probabilistically. Scale transfer is uncertain. | [admit: Cox et al. 2010 abstract] |
| **van Bavel, Curtis & Soens 2018**, *Ecol. & Soc.* 23(4):30 | Comparative historical flood cases (Low Countries) | Institutional adaptation "may not inevitably occur in the aftermath of hazards, as a result of power asymmetries… a mismatch between the broader needs for societal resilience and the needs of a more select group with focused interests". | [admit: abstract] |
| **Kemp 2025**, *Goliath's Curse* | >440 societal lifespans | Average state lifespan is 326 years; the largest states average 155. Inequality and extraction hollow out "Goliaths" before external shocks. More democratic societies are more resilient. | [abstain: non-authoritative source] (trade book; figures via Kirkus and The Tyee reviews, not peer-reviewed) |
| **Turchin & Nefedov 2009** *Secular Cycles*; **Tainter 1988**; **Scheffer 2009** *Critical Transitions* | Theory and cases | SDT, diminishing returns to complexity, critical transitions: the theoretical backdrop for CrisisDB and Scheffer 2021/2023 | [abstain: unverifiable] (standard works; not opened this session) |

#### 5.1 What these numbers do and do not say about the base rate

1. **No dataset measures P(pre-emptive | foreseeable slow threat).** CrisisDB conditions on crisis, so it misses the societies that pre-empted successfully and never entered its sample. Its 31% reform rate is a rate of *reform during or after crisis*, not of pre-emption. **Synthesis:** the true pre-emption rate across all foreseeable threats is therefore *higher* than CrisisDB's numbers imply. The pre-emption rate among threats severe enough to become crises is probably *lower* than 31%, since most of those reforms came during or after turmoil.
2. **The reform/severity null result is the most important number for the model.** A large crisis does not reliably produce large reform. [admit: Hoyer et al. preprint, fig. 4]. This **refutes the Drazen–Grilli crisis hypothesis as a general historical regularity**. The hypothesis was formulated for modern fiscal stabilisations, so the refutation applies to its extrapolation, not its original domain. [refute: Hoyer et al. 2025 *SSH* / 2024 preprint]
3. **Recurrent exposure breeds resilience** (Riris 2024). This explains why the institutionalised pre-emption cases (water boards, quarantine, granaries, alp statutes) all concern *recurrent* hazards. The first encounter is almost always reactive.
4. **Literature bias runs toward disaster** (Degroot 2021), and **case selection runs toward success in the commons literature** (Ostrom chose "long-enduring" institutions and confined failures to ch. 5). These two biases point in opposite directions, so neither literature alone gives a base rate.
5. **My illustrative tally** from Section 4 (25 cases, non-random, judgemental):

| Category | Count | Cases |
|---|---|---|
| Pre-emptive before first major damage | ~3 | D8 Venice lagoon, D19 Qing granaries (as a standing buffer), D10 Törbel (if rules preceded degradation) |
| Reactive-then-institutionalised or reactive-effective | ~10 | D6, D7, D9 (early), D11, D12, D13, D14, D15, D20, D25 |
| Failed, late or elite-blocked | ~9 | D2, D3, D4 (end), D16, D17, D18, D21, D24, D9 (15th-c. Flanders) |
| Transformation, exit or contested | ~4 | D1, D5, D22, D23 |

**Best-supported statement:** truly pre-emptive collective action (before first major damage) against a *novel* slow threat is a **minority outcome, plausibly 5–25%**. Anticipatory *institutions* against *known, recurrent* hazards are **common, often durable for centuries, and typically born from a first disaster**. Confidence: LOW–MEDIUM on the number, MEDIUM–HIGH on the qualitative split.

---

### 6. What distinguishes pre-emptive successes (mapped to model variables)

| Distinguishing condition | Historical exemplars | Counter-exemplars | Model variable | Strength of evidence |
|---|---|---|---|---|
| **1. The trust radius coincides with the commons.** Users = beneficiaries = rule-makers; clearly bounded. | Törbel, *iriai*, huertas, Tikopia, early Flemish boards with peasant voice | Sri Lankan beach-seine fishery (politicians issued new permits, so the boundary was breached: 20 → 100 nets); Bodrum/Izmir (large, heterogeneous N; state failed to enforce the 3-mile zone); 15th-c. Flemish boards after landlord capture | L^R and H summed over the **same** population, so the sign of the net payoff is the same for decision-makers and exposed people | **Strong:** Ostrom 1990 chs 3 & 5 [admit: Ostrom 1990 ch. 5 sections as listed in the ToC; Sri Lanka and Turkey details via summaries]; Cox et al. 2010 [admit]; van Bavel et al. 2018 [admit] |
| **2. The harm falls inside the veto-holder's own radius**, or the veto-holder's L^R turns positive | Great Stink (Parliament on the Thames); Montreal (DuPont substitutes; US unilateral gain); Venice (the patriciate's lagoon); Tokugawa (the shogunate's timber); Ragusa (merchant oligarchy's trade) | London smog (ministers outside φ until mass deaths); leaded petrol; Gracchi; Mamluk Egypt; English labour statutes | V is *endogenous*: it falls, or reverses into a driver, when H enters the elite radius | **Medium–strong** (multiple cases). **Synthesis** across admitted findings. |
| **3. Small N of decision-makers / small polities** | Tikopia (~1,200), Törbel, Ragusa, Venetian Great Council; Montreal (few producers) | Large empires; CrisisDB: Scale and Gov correlate negatively with reform | Time-to-tip grows with N (Xie et al. 2011); fewer pivotal vetoes | **Medium:** CrisisDB negative Scale–reform association [admit: Hoyer et al. preprint]; Ostrom's Turkish cases |
| **4. Monitoring that makes compliance mutually visible** | Ostrom principle 4; guard rotations in the huertas; alp counting | Hidden overfishing; diffuse emissions | Corrects the **r̂ bias** (pluralistic ignorance) directly: each agent observes others' actions | **Medium:** Cox et al. 2010 support for monitoring principles [admit]. Mapping to r̂ is **Synthesis**. |
| **5. Recurrence plus institutional memory** (the hazard has struck before) | Water boards, quarantine after 1348, granaries, dike taxes | First-encounter threats (ozone to 1974, lead, CO₂) | Counteracts **φ decay** from shifting baselines: institutions store H across generations | **Medium–strong:** Riris et al. 2024 [admit] |
| **6. Cheap substitutes / low incumbent cost** | Montreal (HCFCs/HFCs); Y2K (no incumbent beneficiary); Tikopia fishing replacing pigs | Coal (acid rain until cheap low-S coal); leaded petrol | Small L^R | **Medium** (modern cases well documented; pre-modern inferred) |
| **7. State capacity and fiscal health** | Early Qing granaries; Crises Averted cases | Late-Qing granary decline; 17th-c. crisis states | Capacity to act once the threshold is crossed. Fiscal distress raises V and lowers response. | **Medium–strong:** Will & Wong 1991 [admit]; Hoyer et al. 2023 [admit] |
| **8. Visible, image-able harm** | Ozone-hole images; Great Stink; 1952 smog; Castle Bravo | Salinisation (D1); slow Maya drying (D3) | φ high | **Medium:** Grevsmühl & Briday 2023 [admit]; others **Synthesis** |

**The core finding.** Ostrom's long-enduring commons are cases where the radius of trust and decision **encompasses** the commons. Design principle 1 (clearly defined user and resource boundaries) and principle 3 (those affected by the rules can modify them) make the population counted in L^R identical to the population exposed to H. Principle 7 (minimal recognition of the right to organise) holds external elite veto near zero. Ostrom's ch. 5 failures occur exactly where the boundary is breached from outside (Sri Lanka), the decision unit is too large or heterogeneous (Turkey), or an outside authority imposes rules (Nova Scotia). Van Bavel, Curtis & Soens show the same mechanism over time *within one institution*. As Flemish water boards passed from inclusive peasant participation to absentee-landlord control, the decision-makers' payoff diverged from the exposed population's. The boards chose austerity, and flood losses grew.

**Synthesis.** This is strong confirmatory evidence for the radius-bounded mechanism, with two caveats:
- Ostrom selected successes, so the cases are survivorship-biased.
- "Trust radius" in the Uslaner/Delhey sense (generalised vs particularised trust) is not measured in these historical cases. What is documented is *membership, rights and decision boundaries*. Treating those as the operative radius is a reasonable proxy, not an identity.

---

### 7. Implications for the model

#### 7.1 Where deep history supports the model

1. **Radius-bounded L^R vs H.** Supported strongly by Ostrom's successes and failures, the Flemish elite capture of the water boards, Venetian externalisation onto the mainland, and the Great Stink. (Sections 4, 6)
2. **Elite veto V as the binding constraint.** Supported by CrisisDB's "double-down" finding, the SUERF brief ("those with the greatest power to enact it are least inclined to do so"), the English labour statutes, Mamluk Egypt and the Gracchi. The Gracchi premise is contested, but the obstruction is not.
3. **N-dependence of time to tip.** Consistent with small-polity successes and CrisisDB's negative Scale–reform association. This is not a direct test of Xie et al.
4. **φ decay through gradualness.** Consistent with slow-onset failures (Maya drying, salinisation if real, lead) and with vivid shocks catalysing action (Great Stink, 1952 smog, the ozone hole).
5. **r̂ bias.** Pre-modern small-community successes are exactly those where monitoring makes r̂ accurate. That is consistent with pluralistic ignorance being a *large-N* pathology that the model should weight by N.

#### 7.2 Where deep history refines the model

Refinements (all Synthesis; adopted in B.4.1):
1. **Make V endogenous to the elite radius.** Use V = V₀ − γ·H_elite + δ·L^R_elite. Pre-emptive *top-down* successes (Tokugawa, Venice, Qing, Montreal) occur when H enters the elite radius or L^R_elite turns positive. Then the elite becomes the initiator, not the veto.
2. **Add an institutional-memory term M** that keeps φ from decaying, for example φ_i = φ₀·e^{−λt} + M. M is built by past disasters (Riris 2024) and maintained by standing institutions. This explains why *recurrent* hazards are routinely pre-empted and *novel* ones are not. It also predicts erosion of M when fiscal capacity falls (Qing granaries).
3. **Crisis is not sufficient. Add an exit branch.** CrisisDB's null correlation between severity and reform means pressure can stay below V indefinitely. Historically, the alternative resolutions are **elite displacement, collapse or exit** (Angkor's elites leaving; Hoyer's "positive destruction"). The model should allow reform when cascade pressure > V *or* when V is removed exogenously.
4. **Externality leakage.** Radius-bounded success can *export* harm: Venice protected the lagoon at the mainland's expense. Pre-emption within a radius is not the same thing as welfare-improving pre-emption overall.

#### 7.3 Where deep history challenges the model

1. **The "waiting until the last moment" framing is too uniform.** Many pre-modern communities acted *early relative to the second, third or nth occurrence* of a hazard, once memory was institutionalised. Delay is concentrated in **first encounters** and in **cross-radius** threats. It is not a universal property of collective action.
2. **Collapse revisionism weakens the failure side.** Rapa Nui and the Norse are no longer clean "failure to act" cases; they show adaptation that ran into conjunctures or colonial shocks. The canonical "societies that chose to fail" set is smaller than the 2005 literature suggested (Degroot 2021).
3. **Some pre-emption was coercive, not cascade-driven.** Tokugawa forestry (Osako: coercion of peasants), Tikopia's population controls (infanticide, expulsion) and the Venetian magistracies were imposed, not tipped. The threshold-cascade model captures *bottom-up* coordination. Top-down pre-emption needs the endogenous-V amendment above, not a cascade.

**Bottom line.** Montreal is the exception for *novel, global* threats, but deep history says why. Pre-emption happens when the people who hold the veto are inside the radius of the harm, when the community that pays is the community that decides, and when memory of a previous disaster has been institutionalised. Climate change and AI risk currently satisfy none of the three. That is the radius-bounded mechanism's prediction, and the historical record broadly confirms it.

---

### 8. Annotated bibliography

#### Montreal Protocol and modern comparators
- **Barrett, S. (2003).** *Environment and Statecraft: The Strategy of Environmental Treaty-Making.* Oxford University Press. ISBN 9780199257331. Ch. 8 (Montreal): trade sanctions and side-payments made participation self-enforcing.
- **Barrett, S. (2007).** *Why Cooperate? The Incentive to Supply Global Public Goods.* OUP. doi:10.1093/acprof:oso/9780199211890.001.0001. Typology of single-best-effort, weakest-link and aggregate-effort goods. Smallpox as a weakest link.
- **Benedick, R. E. (1991; enlarged ed. 1998).** *Ozone Diplomacy: New Directions in Safeguarding the Planet.* Harvard University Press. The US chief negotiator's account: precaution under uncertainty. Also Benedick, testimony to US Senate EPW Committee, 28 Sep 2005 (epw.senate.gov; returned 403 to direct fetch).
- **DuPont (1986).** "DuPont position statement on the chlorofluorocarbon–ozone–greenhouse issues." *Environmental Conservation* 13(4). doi:10.1017/S0376892900035475. Primary source for "roughly five years" to substitutes, conditional on incentives.
- **Grevsmühl, S. V. & Briday, R. (2023).** "Satellite images as tools of visual diplomacy: NASA's ozone hole visualizations and the Montreal Protocol negotiations." *British Journal for the History of Science* 56(2):247–267. doi:10.1017/S000708742300002X. Negotiators formally excluded the hole, but the images shaped actors anyway.
- **Grundmann, R. (2001).** *Transnational Environmental Policy: Reconstructing Ozone.* Routledge. A US–Germany policy-network comparison; critic of Sunstein's history.
- **Maxwell, J. & Briscoe, F. (1997).** "There's money in the air: the CFC ban and DuPont's regulatory strategy." *Business Strategy and the Environment* 6:276–286 (details as relayed; not opened). Argues DuPont's 1986–88 shift was strategic.
- **Parson, E. A. (2003).** *Protecting the Ozone Layer: Science and Strategy.* OUP. Feedback between control revisions and industry strategy.
- **Quiggin, J. (2005).** "The Y2K scare: causes, costs and cures." *Australian Journal of Public Administration* 64(3):46–55. doi:10.1111/j.1467-8500.2005.00451.x. Y2K as over-pre-emption, a conformist cascade.
- **Schmalensee, R. & Stavins, R. N. (2013).** "The SO₂ allowance trading system: the ironic history of a grand policy experiment." *Journal of Economic Perspectives* 27(1):103–122. doi:10.1257/jep.27.1.103.
- **Sunstein, C. R. (2007).** "Of Montreal and Kyoto: a tale of two protocols." *Harvard Environmental Law Review* 31:1–65. Reprinted 38 *ELR* 10566 (2008). The domestic cost–benefit asymmetry explains the US embrace of Montreal and rejection of Kyoto.
- **Fenner, F. et al. (1988).** *Smallpox and Its Eradication.* WHO. Cost figures (via CGD *Millions Saved*, Case 1).

#### Deep-history cases
- **Alfani, G. (2013).** "Plague in seventeenth-century Europe and the decline of Italy: an epidemiological hypothesis." *European Review of Economic History* 17(4):408–430. doi:10.1093/ereh/het013. **Alfani, G. & Percoco, M. (2019).** *Economic History Review* 72(4):1175–1201. doi:10.1111/ehr.12652.
- **Arneborg, J. et al. (2012).** "Norse Greenland dietary economy ca. AD 980–ca. AD 1450: Introduction." *Journal of the North Atlantic* Special Vol. 3:1–39. doi:10.3721/037.004.s303. Marine share of diet rose toward ~80%.
- **Artzy, M. & Hillel, D. (1988).** "A defense of the theory of progressive soil salinization in ancient southern Mesopotamia." *Geoarchaeology* 3(3). doi:10.1002/gea.3340030306.
- **Bailey, M. (2025).** "The implementation of national labour legislation in England after the Black Death, 1349–1400." *Economic History Review*. doi:10.1111/ehr.13355.
- **Bocinsky, R. K. & Kohler, T. A. (2014).** "A 2,000-year reconstruction of the rain-fed maize agricultural niche in the US Southwest." *Nature Communications* 5:5618. doi:10.1038/ncomms6618.
- **Bondesan, A. & Furlanetto, P. (2012).** "Artificial fluvial diversions in the mainland of the Lagoon of Venice during the 16th and 17th centuries inferred by historical cartography analysis." *Géomorphologie* 4/2012:175–200. journals.openedition.org/geomorphologie/9815.
- **Davis, D. S. et al. (2024).** "Island-wide characterization of agricultural production challenges the demographic collapse hypothesis for Rapa Nui." *Science Advances* 10(25):eado1459. doi:10.1126/sciadv.ado1459.
- **De Moor, T. (2015).** *The Dilemma of the Commoners.* Cambridge University Press. doi:10.1017/CBO9781139135450. The "silent revolution" of medieval institutions for collective action.
- **Degroot, D. (2018).** *The Frigid Golden Age: Climate Change, the Little Ice Age, and the Dutch Republic, 1560–1720.* Cambridge University Press.
- **Diamond, J. (2005).** *Collapse: How Societies Choose to Fail or Succeed.* Viking. The reference narrative, now substantially revised for Rapa Nui and Norse Greenland.
- **DiNapoli, R. J., Rieth, T. M., Lipo, C. P. & Hunt, T. L. (2020).** "A model-based approach to the tempo of 'collapse': the case of Rapa Nui (Easter Island)." *Journal of Archaeological Science* (DOI not confirmed this session).
- **Douglas, P. M. J. et al. (2015).** "Drought, agricultural adaptation, and sociopolitical collapse in the Maya Lowlands." *PNAS* 112(18):5607–5612. doi:10.1073/pnas.1419133112.
- **Dugmore, A. J. et al. (2012).** "Cultural adaptation, compounding vulnerabilities and conjunctures in Norse Greenland." *PNAS* 109(10):3658–3663. doi:10.1073/pnas.1115292109.
- **Gensini, G. F., Yacoub, M. H. & Conti, A. A. (2004).** "The concept of quarantine in history: from plague to SARS." *Journal of Infection* 49(4):257–261. PMC7133622.
- **Hunt, T. & Lipo, C. (2011).** *The Statues That Walked.* Free Press.
- **Jacobsen, T. & Adams, R. McC. (1958).** "Salt and silt in ancient Mesopotamian agriculture." *Science* 128(3334):1251–1258.
- **Kennett, D. J. et al. (2012).** "Development and disintegration of Maya political systems in response to climate change." *Science* 338(6108):788–791. doi:10.1126/science.1226299.
- **Kirch, P. V. & Yen, D. E. (1982).** *Tikopia: The Prehistory and Ecology of a Polynesian Outlier.* Bishop Museum Bulletin 238.
- **Knapp, A. B. & Manning, S. W. (2016).** "Crisis in context: the end of the Late Bronze Age in the eastern Mediterranean." *American Journal of Archaeology* 120(1):99–149. doi:10.3764/aja.120.1.0099.
- **Manning, S. W. et al. (2023).** "Severe multi-year drought coincident with Hittite collapse around 1198–1196 BC." *Nature* 614. doi:10.1038/s41586-022-05693-y.
- **McKean, M. A. (1982).** "The Japanese experience with scarcity: management of traditional common lands." *Environmental Review* 6(2):63–88.
- **Moreno-Mayar, J. V. et al. (2024).** "Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas." *Nature* 633:389–397. doi:10.1038/s41586-024-07881-4.
- **Ostrom, E. (1990).** *Governing the Commons.* Cambridge University Press. Ch. 3 (Törbel; Hirano, Nagaike, Yamanoka; huertas; zanjeras; design principles); ch. 5 (failures: Turkey, California, Sri Lanka, Nova Scotia).
- **Parker, G. (2013).** *Global Crisis: War, Climate Change and Catastrophe in the Seventeenth Century.* Yale University Press.
- **Penny, D., Hall, T., Evans, D. & Polkinghorne, M. (2019).** "Geoarchaeological evidence from Angkor, Cambodia, reveals a gradual decline rather than a catastrophic 15th-century collapse." *PNAS* 116(11):4871–4876. doi:10.1073/pnas.1821460116.
- **Powell, M. A. (1985).** "Salt, seed, and yields in Sumerian agriculture: a critique of the theory of progressive salinization." *Zeitschrift für Assyriologie* 75:7–38. doi:10.1515/zava.1985.75.1.7.
- **Rosenstein, N. (2004).** *Rome at War: Farms, Families, and Death in the Middle Republic.* University of North Carolina Press. Challenges the smallholder-ruin account of the Gracchan crisis.
- **Saito, O. (c. 2009).** "Forest history and the Great Divergence: China, Japan, and the West compared." *Journal of Global History* (volume and DOI not confirmed). Calls Totman "too optimistic".
- **Soens, T. (2011).** "Floods and money: funding drainage and flood control in coastal Flanders (13th–16th centuries)." *Continuity and Change* 26:333–365. **Soens, T. (2013).** "Flood security in the medieval and early modern North Sea area: a question of entitlement?" *Environment and History* 19(2):209–232. **Soens, T. (2018).** "Resilient societies, vulnerable people." *Past & Present* 241:143–177.
- **Totman, C. (1989).** *The Green Archipelago: Forestry in Preindustrial Japan.* University of California Press.
- **van Bavel, B., Curtis, D. R. & Soens, T. (2018).** "Economic inequality and institutional adaptation in response to flood hazards: a historical analysis." *Ecology and Society* 23(4):30. doi:10.5751/ES-10491-230430. **Key evidence for radius mismatch causing institutional decay.**
- **Will, P.-E. & Wong, R. B. (1991).** *Nourish the People: The State Civilian Granary System in China, 1650–1850.* Ann Arbor: Center for Chinese Studies (OA via OAPEN 2020).

#### Comparative, quantitative and theoretical
- **Butzer, K. W. (2012).** "Collapse, environment, and society." *PNAS* 109(10):3632–3639. doi:10.1073/pnas.1114845109.
- **Cox, M., Arnold, G. & Villamayor-Tomás, S. (2010).** "A review of design principles for community-based natural resource management." *Ecology and Society* 15(4):38. doi:10.5751/ES-03704-150438.
- **Cumming, G. S. & Peterson, G. D. (2017).** "Unifying research on social–ecological resilience and collapse." *Trends in Ecology & Evolution* 32(9):695–713. doi:10.1016/j.tree.2017.06.014.
- **Degroot, D. et al. (2021).** "Towards a rigorous understanding of societal responses to climate change." *Nature* 591:539–550. doi:10.1038/s41586-021-03190-2. Literature over-represents disaster.
- **Hoyer, D. et al. (2023).** "Navigating polycrisis: long-run socio-cultural factors shape response to changing climate." *Phil. Trans. R. Soc. B* 378:20220402. doi:10.1098/rstb.2022.0402. Data: doi:10.5061/dryad.mkkwh715m.
- **Hoyer, D. et al. (2025).** "All crises are unhappy in their own way: the role of societal instability in shaping the past." *Social Science History* (FirstView). doi:10.1017/ssh.2025.10113. Preprint: doi:10.31235/osf.io/rk4gd. **The 31% reform figure, the median duration of 22 years, and the null correlation between reform and severity.**
- **Hoyer, D. et al. (2025).** "CRISES AVERTED: how a few past societies found adaptive reforms in the face of structural-demographic crises." *Cliodynamics* 16:1–50. doi:10.21237/C7clio.38365.
- **Hoyer, D., François, P., Reddish, J., Bennett, J. S. & Turchin, P. (2026).** "Flattening the curve on societal crisis: lessons from history." SUERF Policy Brief 1359.
- **Kemp, L. (2025).** *Goliath's Curse: The History and Future of Societal Collapse.* Knopf/Viking. A trade book; >440 lifespans; inequality and extraction as drivers.
- **McAnany, P. A. & Yoffee, N. (eds) (2010).** *Questioning Collapse.* Cambridge University Press.
- **Middleton, G. D. (2017).** *Understanding Collapse: Ancient History and Modern Myths.* Cambridge University Press. doi:10.1017/9781316584941.
- **Riris, P. et al. (2024).** "Frequent disturbances enhanced the resilience of past human populations." *Nature* 629:837–842. doi:10.1038/s41586-024-07354-8.
- **Scheffer, M. (2009).** *Critical Transitions in Nature and Society.* Princeton University Press.
- **Scheffer, M., van Nes, E. H., Bird, D., Bocinsky, R. K. & Kohler, T. A. (2021).** "Loss of resilience preceded transformations of pre-Hispanic Pueblo societies." *PNAS* 118:e2024397118. doi:10.1073/pnas.2024397118.
- **Scheffer, M. et al. (2023).** "The vulnerability of aging states: a survival analysis across premodern societies." *PNAS* 120(48):e2218834120. doi:10.1073/pnas.2218834120.
- **Tainter, J. A. (1988).** *The Collapse of Complex Societies.* Cambridge University Press.
- **Turchin, P. & Nefedov, S. A. (2009).** *Secular Cycles.* Princeton University Press.

---

### 9. Disposition ledger

Machine-counted (`grep`) over every bracketed tag in Sections 2–6. Synthesis passages are excluded. Where one cell carries two tags, for example a core fact admitted and a contested detail abstained, both are counted. Seven bare `[admit]` markers in Section 6 re-cite findings already tagged in Sections 4–5 and are **not** counted again.

| Disposition | Count |
|---|---|
| `admit` | 57 |
| `refute` | 5 |
| `abstain` | 26 |
| of which `non-authoritative source` | 13 |
| of which `unverifiable` | 7 |
| of which `source-vs-prior conflict` | 6 |
| **Total tagged findings** | **88** |

**The 5 refutations:**
1. "The ozone hole played no role in Montreal." Refuted by Grevsmühl & Briday 2023. The images mattered even though negotiators formally excluded the hole.
2. "The Norse Greenlanders refused or failed to adapt." Refuted by Dugmore et al. 2012 and Arneborg/Nelson et al. 2012: sealing intensified and marine diet rose toward ~80%.
3. "Rapa Nui suffered a severe pre-contact demographic collapse." Refuted by Moreno-Mayar et al. 2024 (*Nature*) and Davis et al. 2024 (*Sci. Adv.*). A residual dispute (Van Tilburg) is abstained separately.
4. "Angkor collapsed catastrophically in the 15th century." Refuted by Penny et al. 2019 (*PNAS*): a gradual decline from the early 1300s, with the elite leaving first.
5. "Crisis severity drives reform" (Drazen–Grilli extrapolated as a historical regularity). Refuted by Hoyer et al. 2024/2025 (CrisisDB): reform is uncorrelated with severity, and only 31% of crises saw any reform.

**Main abstentions to resolve before publication:**
- CFC producer concentration figures. These are consistent across sources, but none was peer-reviewed. Check Maxwell & Briscoe 1997 or Parson 2003.
- Barrett's "65×" and Sunstein's US$21 bn / US$3,575 bn figures. Check against the original texts.
- Tikopia dates (Kirch & Yen 1982).
- Venice's 1348 *savi* and the 1490 *Magistrato alla Sanità*. Check Cipolla 1976/1981.
- The Venetian mainland flood externality.
- CrisisDB's "~5% collapse" figure. It appears only in a blog; check the published *SSH* fig. 5.

---

## Appendix B: Does the micro-mechanism of collective delay generalise across civilisational systems?

**Researched:** 2026-10-10
**Model terms** (L^R, H, φ, r̂, κ, V, N-scaling) are as defined in B.4. Claims already admitted in the main body (Uslaner, Delhey et al., Moore et al., Hazlett & Mildenberger, Andre et al., Sparkman et al., Alesina–Drazen, Drazen–Grilli, Fernandez–Rodrik, Kuran, Xie et al., Herndon–Ash–Pollin) are cited here but not re-tagged or re-counted.
**Method:** For each claim I first tried to refute it against a primary or authoritative source, then tagged it:
- `[admit: source]`: confirmed this session in an authoritative source, and the refutation attempt failed.
- `[refute: source]`: an authoritative source contradicts the claim. The correction is given.
- `[abstain: reason]`: reason is one of *unverifiable*, *source-vs-prior conflict*, or *non-authoritative source*.

**Confidence:** MEDIUM overall. The case facts are mostly HIGH. Classifying the cases and judging how well the model fits each one is analytical judgement, not sourced fact (MEDIUM–LOW). Base-rate claims are LOW, because no source estimates a representative base rate.

---

### 1. Summary verdict

**Short answer: yes, with bounds.** The mechanism is a credible description of a **plurality, and probably a majority, of documented cases where harm is slow-onset, diffuse or delayed while benefits are concentrated**. That class covers chemical and occupational hazards, fisheries and land commons, financial booms, pension and demographic systems, infrastructure maintenance, antimicrobial resistance, and parts of democratic erosion. It does **not** describe a majority of *all* civilisational systems. Many systems run on routine, acute, attributable feedback, such as aviation safety, food-poisoning recalls, acute drug toxicity and wartime logistics. The record of those systems is mostly quiet success, and quiet success is invisible to the case literature.

Four findings matter most:

1. **The quantitative signature of "delay, then lurch" is near-universal in one domain where it has been measured systematically.** Every public-budget distribution studied by the Comparative Agendas Project is leptokurtic (Jones et al. 2009). The authors attribute this to "fundamental operations of human and organizational information processing". That is a domain-general *meso-level* mechanism, institutional friction, not the author's *micro* one.
2. **The crisis half of the model is weaker than the delay half.** Across 85 countries and 10,976 hazard events, disaster frequency and severity were *unassociated* with improved disaster-risk policy (Nohrstedt et al. 2021). Mass shootings raise the number of gun bills introduced by 15%, but in Republican-controlled US legislatures they *double* the laws that **loosen** restrictions (Luca et al. 2020). Crises are not a reliable tipping input. When φ is partisan-filtered, a crisis can **raise** V.
3. **The prompt-action cases share identifiable features.** These are the boundary conditions. Harm is immediate, concentrated, visible and attributable (thalidomide). Harm enters the veto players' own radius (the Great Stink in Parliament, dust over Washington, the Cuban Missile Crisis). Substitutes are cheap (CFCs, flue-gas desulfurisation). Decision-makers are few and monitor each other (Ostrom; the Sheridan-6 LEMA). A free local press and electoral accountability raise φ and lower V (Sen; Besley & Burgess 2002), but they are not sufficient (Malawi 2002, Niger 2005).
4. **The literature already offers domain-general mechanisms of delay, but not this exact composite.** The closest are Platt's (1973) *social traps* (micro, domain-general, time-delay traps), Kuran's (1995) *preference falsification* (micro, the r̂ term), Jones & Baumgartner's *institutional friction / disproportionate information processing* (meso), *lock-in* (Arthur, David, Pierson; Unruh; Seto et al. 2016), Geels's *regime resistance*, Collingridge's *dilemma of control*, Turner's *disaster incubation*, Bazerman & Watkins's *predictable surprises*, and Meyer & Kunreuther's six biases. Herding in that last list is the r̂ analogue.

**Does the polycrisis literature share a mechanism of delay?** Not in Lawrence et al. (2024). They give system-level causal pathways (common stresses, domino effects, inter-systemic feedbacks), not a micro-mechanism of delay. It does in the polycrisis literature as a whole. Søgaard Jørgensen et al. (2024), explicitly framed by the polycrisis, identify **shared trap mechanisms across 14 global systems**: shifting baselines, "masked interactions" that weaken signals across space (the analogue of φ decaying with distance), short-termism, and "powerful actors with entrenched interests" (the analogue of V). That is a shared *mechanism-level* account. It is not a formal micro-model with a cascade threshold, a biased r̂ or N-scaling.

**Catalogue tallies.** 33 cases in 10 domains. 7 prompt or pre-emptive (21%); 11 late, after cumulative harm or a crisis (33%); 10 where prevention failed and catastrophe came first (30%); 5 ongoing with no adequate action (15%). This is a **non-random convenience sample biased toward famous failures**. EEA itself says its cases were "chosen from a range of well-known hazards".

---

### 2. Meta-literature on ignored early warnings

#### 2.1 European Environment Agency, *Late lessons from early warnings*

| # | Finding | Tag |
|---|---|---|
| M1 | **Vol. I (Environmental issue report 22/2001, published Jan 2002; eds. Harremoës, Gee et al.)** has 14 case studies "arranged chronologically according to the first date of early warning". Authors were asked "to identify the dates of early warnings, to analyse how this information was used, or not used". | [admit: EEA 2001, *Summary points* §1] |
| M2 | **Vol. I case list:** fisheries (incl. the Canadian cod collapse), radiation, benzene, asbestos, PCBs, halocarbons/ozone, DES, antimicrobials as growth promoters, sulphur dioxide/acidification, MTBE, Great Lakes contamination, TBT antifoulants, hormones as growth promoters, BSE. | [admit: EEA 2001 ch. 16 text and *Summary points*; every case is named there] |
| M3 | **First warnings named in Vol. I:** radiation injuries 1896; asbestos 1898 ("first clear and credible early warning"); CFCs 1974; antibiotics in feed 1969 onward. | [admit: EEA 2001 *Summary points* §3, Table 2] |
| M4 | **Measured gap.** Vol. I does **not** publish an aggregate lag statistic. Its conclusion is qualitative: "the gap was long, certainly many years or decades, and in some cases over a century". Even after the precautionary principle was articulated in the 1970s–80s, "examples of unequivocal precautionary action were relatively scarce". Per-case date tables sit at the end of each chapter. *The common premise that EEA provides measured lag statistics is therefore only partly true: lags are per case, with no base rate.* | [refute: EEA 2001 ch. 16.1 (no aggregate lag statistic exists; per-chapter tables only)] |
| M5 | **Why warnings were ignored:** "adequate information about potential hazards was available well before decisive regulatory advice was taken, but... was either not brought to the attention of the appropriate decision-makers early enough, or was discounted". In some cases even "loud and late" warnings "were effectively ignored... because of short-term economic and political interactions" (asbestos, PCBs, Great Lakes, SO2). This maps directly to L^R and V. | [admit: EEA 2001 ch. 16.1] |
| M6 | **Misplaced certainty:** "Misplaced 'certainty' about the absence of harm played a key role in delaying preventive actions in most of the case studies." This is a φ-type filter operating on experts. | [admit: EEA 2001 *Summary points* §4] |
| M7 | **Asymmetric error preference:** science's bias toward avoiding false positives "inevitably involves generating false negatives". Underwood (1999) is quoted: the chance of a Type I error is "deliberately kept small" and the chance of a Type II error is not. | [admit: EEA 2001 ch. 16] |
| M8 | **Selection admission:** Vol. I cases were "chosen from a range of well-known hazards... where sufficient is now known about their impacts". This is an explicit selection on famous outcomes. | [admit: EEA 2001 *Summary points* §1] |
| M9 | **Asbestos lag:** 1898 (UK factory inspector Lucy Deane). UK decided to ban white asbestos in 1998, EU in 1999, "one hundred years later". | [admit: EEA 2001 ch. 1/5, Gee & Greenberg] |
| M10 | **Vol. II (EEA Report 1/2013).** Part A covers health hazards: false alarms, lead in petrol, PCE in mains water, Minamata, beryllium, tobacco, vinyl chloride, DBCP, bisphenol A, DDT. Part B covers ecosystems: booster biocides, ethinyl oestradiol, climate change, floods, seed-dressing insecticides and honeybees, ecosystem dynamics. Part C covers emerging issues: Chernobyl/Fukushima, GM crops, invasive species, mobile phones, nanotechnology. Part D covers costs, justice and innovation, including ch. 25 "Why did business not react with precaution". Part E covers governance. | [admit: EEA 2013 table of contents] |
| M11 | **False positives (Vol. II ch. 2, Hansen & Tickner):** of 88 alleged false positives, only 4 were genuine (US swine flu, saccharin, food irradiation, Southern leaf corn blight). Critics call the 88 "inevitably selective". | [admit: EEA 2013 ch. 2; EEA slides Apr 2013] |
| M12 | **Business non-precaution (ch. 25, Le Menestrel & Rode):** "In virtually all reviewed cases it was perceived to be profitable for industries to continue using potentially harmful products". This is the closest EEA comes to a cross-case statement of L^R. | [admit: EEA 2013 Part D summary] |
| M13 | **Vol. II lags:** lead in petrol, warnings at the 1925 "one day trial" and EU phase-out 1998–2005. Minamata, officially identified 1956, cause process stopped 1968, equitable compensation only by 2004 ("almost fifty years"). Climate, first credible warning 1897. | [admit: EEA 2013 ch. 3, 5, 14, 24 summaries] |
| M14 | **A counterexample inside EEA:** vinyl chloride features "a very prompt response from the global chemical industry to the publication of the liver cancer evidence". Industry cost estimates were "greatly exaggerated". | [admit: EEA 2013 ch. 8 summary] |

#### 2.2 Other meta-literature

| # | Finding | Tag |
|---|---|---|
| M15 | **Oreskes & Conway, *Merchants of Doubt* (Bloomsbury, 2010).** A small group of physicists (Seitz, Singer, Nierenberg, Jastrow) with think tanks and corporations ran the same doubt strategy across tobacco, acid rain, the ozone hole, secondhand smoke, DDT and global warming. This is a *cross-domain* mechanism by which V actively depresses φ. | [admit: publisher record; *American Scientist* review 2010, doi 10.1511/2010.86.424] |
| M16 | **Bazerman & Watkins, *Predictable Surprises* (Harvard Business School Press, 2004).** Prototypes are 9/11 and Enron. Roots are cognitive, organisational and political (special interests). The prescription is the "RPM" sequence: recognition, prioritisation, mobilisation. The political root is the analogue of V. | [admit: HBS Press record; HBR 81(3):72–80 (2003)] |
| M17 | **Wucker, *The Gray Rhino* (St. Martin's Press, 2016).** A "highly probable, high impact yet... neglected threat". It exists as described, but it is **trade press, not university press or peer-reviewed**, and should not be used as analytical evidence. | [abstain: non-authoritative source] |
| M18 | **Reinhart & Rogoff, *This Time Is Different* (Princeton UP, 2009).** 66 countries, eight centuries. "Serial default remains the norm". Waves of capital mobility have often been followed by banking crises, and crises cluster with "surprisingly consistent frequency, duration, and ferocity". The 90% debt-threshold refutation (Herndon et al.) concerns their separate 2010 paper; see A8 in Part A. | [admit: PUP record; NBER WP 13882] |
| M19 | **Predictability of financial crises:** rapid credit plus asset-price growth over three years carries a **40%** probability of crisis within three years, versus about **7%** in normal times. This "challenges the view that financial crises are unpredictable 'bolts from the sky'". | [admit: Greenwood, Hanson, Shleifer & Sørensen 2022, *J Finance* 77:863–921] |
| M20 | **Crisis frequency:** the IMF systemic banking crises database records **164 banking crises (incl. borderline) between 1970 and 2025**. I could not confirm the oft-quoted "151 in 1970–2017" figure for the 2020 version. | [admit: Laeven & Valencia, IMF WP/26/94 (2026)] |
| M21 | **Baumgartner & Jones, punctuated equilibrium; Jones et al. 2009, "A General Empirical Law of Public Budgets", *AJPS* 53(4):855–873.** "Frequency distributions of public budget changes are leptokurtic for all cases studied". Increases are more punctuated than decreases, and local governments less so. Cross-national differences in parameters "correspond to differences in formal institutional structures". The general form is "probably dictated by the fundamental operations of human and organizational information processing". Coverage is European and North American democracies. | [admit: Jones et al. 2009 abstract] |
| M22 | **Friction mechanism:** institutions impose costs on translating inputs into outputs. The result is "long periods of stasis interspersed with dramatic policy punctuations", with positive kurtosis in all distributions examined. | [admit: Jones, Sulkin & Larsen 2003, *APSR* 97(1):151–169] |
| M23 | **Kingdon's policy windows:** problem, policy and politics streams couple in a short-lived "window" exploited by policy entrepreneurs. | [admit: framework as described in secondary sources (wording); original 1984 Little, Brown edition not opened] |
| M24 | **Birkland's focusing events:** "sudden, attention-grabbing events" central to policy change (1998, p. 53). The fuller four-part definition is commonly cited: sudden and rare; harmful; harms concentrated in a place or community; known to public and elites simultaneously. It is not verified verbatim this session. | [admit: Birkland 1998, *J Public Policy* 18(1):53–74, p. 53 phrase]; [abstain: unverifiable (four-part wording)] |
| M25 | **Sabatier's advocacy coalition framework:** policy-core attributes are unlikely to change "in the absence of significant perturbations external to the subsystem", a necessary but not sufficient condition. The "decade or more" time horizon is a well-known ACF premise but was not verified this session. | [admit: hypothesis wording via Jenkins-Smith et al. 2018 as quoted in *Policy Sciences* 2026]; [abstain: unverifiable ("decade or more")] |
| M26 | **Fouquet 2010 (*Energy Policy* 38:6586–96):** across historical energy transitions, "the whole innovation chain took more than 100 years and the diffusion phase nearly 50 years". Niche protection may be needed "for decades". | [admit: Fouquet 2010 abstract] |
| M27 | **Against universal slowness:** Sovacool (2016, *ERSS* 13:202–215) documents ten national transitions taking 1–16 years. Grubler et al. (2016) argue that, compared properly, these took 6–32 years against 47–69 years for 20th-century Western European transitions. Whether transitions are necessarily slow is contested. | [abstain: source-vs-prior conflict] |
| M28 | **Geels (2014, *TCS* 31(5):21–40):** "resistance and resilience of coal, gas and nuclear production regimes currently negates the benefits from increasing renewables deployment". Regime resistance is the socio-technical analogue of L^R + V. | [admit: Geels 2014 abstract] |
| M29 | **Disaster incubation (Turner 1978; Turner & Pidgeon 1997):** disasters follow an "incubation period" of unnoticed events at odds with accepted beliefs. Vulnerability "remains concealed by social processes which attenuate evaluations of risk". This is a domain-general organisational φ-mechanism. | [admit: Pidgeon & O'Leary 2000, *Safety Science* 34:15–30] |
| M30 | **Collingridge dilemma (1980):** "When change is easy, the need for it cannot be foreseen; when the need for change is apparent, change has become expensive, difficult and time-consuming". Entrenchment is the second horn. | [admit: Collingridge 1980 p. 19 as quoted in Genus & Stirling 2018, *Research Policy*] |
| M31 | **Meyer & Kunreuther, *The Ostrich Paradox* (Wharton, 2017):** six domain-general biases explain under-preparation: myopia, amnesia, optimism, inertia, simplification, and herding ("base choices on the observed actions of others"). Herding is the r̂ analogue; amnesia is the shifting-baseline analogue. | [admit: book text and *Disaster Prevention & Management* review] |
| M32 | **Myopic voters:** US voters reward relief spending but not preparedness. "$1 spent on preparedness is worth about $15 in terms of the future damage it mitigates". Electoral incentives produce systematic under-investment. | [admit: Healy & Malhotra 2009, *APSR* 103(3):387–406] |
| M33 | **Disasters do not reliably trigger reform:** in 85 countries over eight years (10,976 events), "frequency and severity factors are generally unassociated with improved DRR policy". There is large unexplained variation between similarly hit countries. | [admit: Nohrstedt, Mazzoleni, Parker & Di Baldassarre 2021, *Nat Commun* 12:193] |
| M34 | **Diamond, *Collapse* (2005), ch. 14:** a four-stage taxonomy of failure: to anticipate, to perceive ("creeping normalcy", "landscape amnesia"), to try (including "rational bad behaviour" when elite interests clash with society's), and failed solutions. The content matches B.2 in the main body, but this session confirmed it only through summaries and a non-official text copy. | [abstain: non-authoritative source] |

---

### 3. Cross-domain case catalogue

**Legend.** Category: **P** = prompt or pre-emptive (action within about 4 yrs of the first credible warning, before large cumulative harm). **L** = late (action after decades of cumulative harm or a crisis). **F** = prevention failed (catastrophe struck first). **O** = ongoing (no adequate action). "Fit" is how well the full micro-mechanism explains the timing: **S** = strong (mass-level L^R, φ, r̂ and V all plausibly active); **Pa** = partial (mainly L^R + V among few decision-makers; r̂ marginal); **W** = weak (a different mechanism dominates, or the case is prompt). Fit and category are **my analytical judgements**, not sourced facts. Each case's Tag column covers its dated facts.

| # | Domain | Case | First credible warning | Action (date, type) | Lag (yrs) | Trigger | Private support before action? | L^R (beneficiaries) / V (veto) | Dominant terms | Cat. / Fit | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Public health | Asbestos | 1898, UK factory inspector L. Deane | UK ban 1998, EU 1999 (ban); US 2024 | ~100 (EU) | Accumulated mortality and litigation; no single event | Unknown | Industry, construction / industry influence on UK regulation | L^R, φ (decades of latency), V | L / Pa | [admit: EEA 2001 ch. 5] |
| 2 | Public health | Leaded petrol | 1925 "one day trial" expert warnings | Phase-outs from 1970s; EU 1998–2005; global end July 2021 (Algeria) | ~50–96 | Independent science in the 1960s–70s plus catalytic-converter compatibility | Unknown | Additive and oil industry; industry monopoly on research for decades / same | V suppressing φ (information monopoly), L^R | L / Pa | [admit: EEA 2013 ch. 3; UNEP 30 Aug 2021] |
| 3 | Public health | Tobacco | Doll & Hill, *BMJ* 30 Sep 1950 | US Surgeon General report 11 Jan 1964; WHO FCTC adopted 2003, in force 27 Feb 2005 | 14 (official recognition); ~55 (treaty) | Gradual accumulation | Unknown | Tobacco firms; smokers' own utility / industry doubt campaign | All four; V acts by depressing φ (Proctor; Oreskes & Conway) | L / S | [admit: Doll & Hill 1950; NLM; WHO FCTC; Proctor 2011 UC Press] |
| 4 | Public health | Thalidomide | Lenz, 11–16 Nov 1961 (McBride in Sydney acted June 1961) | Withdrawn 26/27 Nov 1961; Kefauver-Harris Amendments 10 Oct 1962 | ~0 (withdrawal); ~1 (law) | Visible, concentrated, attributable harm plus press | n/a | Grünenthal / weak | φ≈1 (immediate, visible); low L^R (substitutes) | P / W | [admit: Lenz 1992 account; *Mayo Clin Proc*; C&EN]; withdrawal date [abstain: source-vs-prior conflict (26 vs 27 Nov)] |
| 5 | Public health | Vinyl chloride | Liver cancer evidence (mid-1970s) | "Very prompt" industry and regulatory response | ~1 | Attributable rare cancer | n/a | Chemical industry / gave way | φ high (signature cancer), V low | P / W | [admit: EEA 2013 ch. 8]; exact dates [abstain: unverifiable] |
| 6 | Public health | Opioids | Misbranding as "less addictive" from 1996 (later admitted) | Purdue plea 10 May 2007; CDC guideline 18 Mar 2016; federal public health emergency 26 Oct 2017 | ~20 from launch; 9 from plea to guideline | Mounting overdose mortality | Unknown | Manufacturer, distributors, prescribers / same | L^R, V, φ (harm concentrated in specific regions and classes) | L / Pa | [admit: DOJ 2007 plea documents; *Federal Register* 23 Mar 2016; ASPR declaration 2017] |
| 7 | Public health | Antimicrobials in animal feed | UK Swann report 1969 | Sweden ban 1986; EU avoparcin 1997; full EU ban 1 Jan 2006; UN 2024 declaration (10% death cut by 2030) | 17 (Sweden); 37 (EU) | Gradual; resistance surveillance | Unknown | Livestock and feed sectors / meat-producing states | L^R, φ (harm distant in space and time), V | L / S | [admit: Castanon 2007 *Poultry Sci*; EEA 2001; UN PGA declaration 2024]; dropped 30% animal-use target "due to pressure from meat-producing nations" [abstain: non-authoritative source (Health Policy Watch)] |
| 8 | Public health | Pandemic preparedness | GPMB *A World at Risk*, 18 Sep 2019 (and many earlier warnings) | WHO Pandemic Agreement adopted 20 May 2025; PABS annex deferred to WHA May 2027; not yet open for signature | ~6+ and incomplete | COVID-19 | Unknown | States guarding sovereignty; pharma (PABS terms) / North–South bargaining | V (attrition over benefit-sharing), φ decays post-crisis | L / Pa | [admit: GPMB 2019; UN News May 2025; Swiss FOPH on 2027 deferral] |
| 9 | Public health | London cholera and sewerage | Snow 1854 (cholera via water) | Great Stink (June–July 1858): Act passed in 18 days, law 2 Aug 1858; Bazalgette's system finished 1875 | ~4 (from Snow); sewer plans debated longer | Smell reached Parliament itself | Unknown | Ratepayers; vestries / MBW deferral ("until the middle of October") | **Harm entered the veto players' own radius** → V collapsed | L / S (elite-exposure lurch) | [admit: *The London Gazette* history notice]; first-reading date [abstain: source-vs-prior conflict (15 June vs 15 July)] |
| 10 | Public health / env. | Minamata | Officially identified 1956 | Chisso stopped the process 1968; equitable compensation 2004 | 12 (source); ~48 (justice) | Litigation | Unknown | Chisso; state industrial-growth priority / same | V, L^R | L / Pa | [admit: EEA 2013 ch. 5, ch. 24] |
| 11 | Finance | 2008 global financial crisis | Rajan, Jackson Hole Aug 2005 (dismissed as "slightly Luddite") | Post-crisis re-regulation (Dodd-Frank, Basel III) | ~3–5 | Crisis | Unknown | Intermediaries' risk-taking pay / regulators confident "private sector knows how to take care of itself" | L^R, φ (expert consensus filter), V | L / Pa | [admit: Rajan 2005 Fed KC proceedings; IMF F&D 2015]; reform dates [abstain: unverifiable] |
| 12 | Finance | Recurrent banking crises | Predictable precursors (credit plus asset-price boom) | Rarely pre-empted; 164 crises 1970–2025 | Structural | Bust | Unknown | Boom-phase borrowers, lenders, asset holders / same | L^R (boom gains inside radius), V | F / S | [admit: Greenwood et al. 2022; Laeven & Valencia 2026; Reinhart & Rogoff 2009] |
| 13 | Demography / pensions | US Social Security | Trustees' long-standing warnings | None comprehensive. 2026 report: OASI depleted **Q4 2032** (78% payable); OASDI Q3 2034 (83%) | Ongoing | Depletion date as deadline (an open member of the F7 deadline panel, §7.1) | Unknown | Current retirees and near-retirees; taxpayers / divided government | L^R, φ (temporal distance), V (war of attrition) | O / S | [admit: SSA 2026 Trustees Report highlights]; the 2025 report's "OASI 2033" is superseded [refute: SSA 2026 Trustees Report (now Q4 2032)] |
| 14 | Resources | Northern cod | Stock "rarely sustainable" at observed rates since 1962 | Commercial extinction and moratorium 1992 | Decades | Collapse | Unknown | Fishers, processors, outport economies / DFO and politics | L^R, φ (shifting baselines; Pauly's original domain), V | F / S | [admit: Hutchings & Myers 1994, *CJFAS* 51:2126–46]; specific ignored-warning dates (e.g. 1989–90) [abstain: unverifiable] |
| 15 | Resources | Aral Sea | Soviet-era diversion for cotton from the 1960s | Kok-Aral dam 2005 (North Aral only); South Aral still shrinking | ~40, partial | Ecological collapse; post-Soviet funding | Unknown | Cotton economy; planners / central state | V (single authority), L^R | F / Pa | [admit: Micklin 2007 *Annu Rev Earth Planet Sci* 35:47–72; White & Micklin 2021]; whether planners foresaw the shrinkage [abstain: unverifiable] |
| 16 | Resources | Dust Bowl soil erosion | Bennett & Chapline 1928, "Soil Erosion: A National Menace" | Soil Conservation Act signed 27 Apr 1935 | 7 | Dust storms reached Washington (May 1934; March 1935) | Unknown | Plains farmers' short-run returns / weak | φ raised by elite exposure; crisis | L / S | [admit: NRCS history; USDA]; testimony-day timing [abstain: source-vs-prior conflict] |
| 17 | Resources | Ogallala, Sheridan-6 LEMA (Kansas) | Local aquifer decline | 2013 voluntary 20% cut by farmers (185 irrigation wells); met, with profits maintained or higher | Short | Local, visible depletion; enabling law 2012 | Yes (producer-initiated) | Same farmers / none (self-governed) | **Small N, mutual monitoring** (Ostrom) → r̂ accurate | P / W | [admit: K-State Research & Extension 2019; Kansas Geological Survey via K-State] |
| 18 | Ecology | Global biodiversity (Aichi 2011–2020) | Targets set 2010 | **0 of 20** targets fully met; 6 partly | Failure | None | Unknown | Land-use and extraction sectors / states | All four; diffuse H | O / S | [admit: CBD GBO-5 press release 15 Sep 2020] |
| 19 | Infrastructure | New Orleans levees (Katrina) | Hurricane Pam exercise, July 2004 ("prescient") | None adequate; follow-up 2005 exercise unfunded; flood Aug 2005 | ≥1 (exercise); decades (levee design) | Catastrophe | Unknown | Diffuse responsibility; budget / funding | V (diffuse responsibility), φ | F / Pa | [admit: House Select Committee, *A Failure of Initiative* (H. Rpt. 109-377), 2006] |
| 20 | Infrastructure | Grenfell cladding | Knowsley Heights fire 1991; Select Committee Dec 1999 | None before the 2017 fire. Inquiry: "decades of failure"; department "well aware" by 2016 "but failed to act" | 26 | Catastrophe | Unknown | Construction products industry; deregulatory department / same | V, L^R, φ (BRE reports narrowed) | F / Pa | [admit: Grenfell Tower Inquiry Phase 2 Overview, 4 Sep 2024, paras 2.4–2.5] |
| 21 | Tech / energy | Fukushima tsunami defence | Govt estimate 2002; TEPCO internal 15.7 m flood height 2008; Jōgan 869 research 2008–09 | None; accident 11 Mar 2011 | ~9 | Catastrophe | n/a | TEPCO; nuclear village / regulators "deliberately postponed decisions" | V (collusion), L^R | F / Pa | [admit: NAIIC 2012 executive summary ("profoundly manmade"); TEPCO interim report 2011]; WNA says TEPCO reassessed 5 times and acted twice [abstain: source-vs-prior conflict] |
| 22 | Security | Pearl Harbor | Signals present (MAGIC intercepts) | None; attack 7 Dec 1941 | Months | Attack | n/a | n/a | **Signal-to-noise**, not L^R or cascade | F / W | [admit: Wohlstetter 1962 Stanford UP; CIA review] |
| 23 | Security | 9/11 | Pre-attack warnings | None adequate | Years | Attack | n/a | Agency silos | Organisational φ ("failure of imagination") | F / W | [admit: 9/11 Commission phrase as quoted in H. Rpt. 109-377]; Bazerman & Watkins treat it as a prototype predictable surprise [admit: Bazerman & Watkins 2004] |
| 24 | Security | Nuclear crisis management | Cuban Missile Crisis Oct 1962 | Hotline 20 Jun 1963; LTBT signed 5 Aug 1963 | <1 | Near-miss focusing event | n/a | Two governments / few deciders, personally exposed | Small N; harm inside the deciders' radius | L / W | [admit: State Dept Office of the Historian; State Dept treaty text] |
| 25 | Tech governance | CFCs / ozone | Molina & Rowland, *Nature* June 1974 | US aerosol ban 1978; Montreal Protocol Sept 1987 after Farman et al. 1985; DuPont exit Mar 1988 | 4 (partial); 13 (treaty) | Ozone-hole discovery for the treaty | Unknown | DuPont, aerosol sector / weakened once substitutes existed | Low L^R (cheap substitutes; Montreal costs ~$21bn vs ~$3.6tn benefits per Sunstein) | P / W | [admit: *Nature* 249:810; *Nature* 315:207; Sunstein 2007 *Harv Envtl L Rev* 31:1]; cost figures [abstain: non-authoritative source (secondary quotation of Sunstein)] |
| 26 | Env. / tech | Waldsterben and acid rain (W. Germany) | Ulrich and Schütt warnings from 1979; *Der Spiegel* 16 Nov 1981 | Large Combustion Plants Ordinance 1983; FGD retrofits | ~2–4 | Press-driven salience | Unknown | Utilities / weakened by "massive public pressure" | **φ raised by mass press**; identity-salient harm; tractable technology | P / Pa | [abstain: non-authoritative source (Historisches Lexikon Bayerns; taz; BUND)] |
| 27 | Tech / infra | Y2K | Known well before 2000 | Massive pre-emptive remediation (US and UK governments plus industry) | Pre-deadline | Hard deadline | n/a | Firms bore the harm themselves | Harm inside the actors' own radius; fixed date; tractable fix | P / W | [admit: Quigley 2008, Palgrave, doi 10.1057/9780230241640 (characterisation "over-reacted to but... successfully headed-off")]; cost figures [abstain: unverifiable] |
| 28 | Tech governance | Social media and youth mental health | US Surgeon General advisory 23 May 2023 (earlier research contested) | Australia's under-16 minimum age in force 10 Dec 2025; little elsewhere | ≥2 and ongoing | Accumulating evidence | **Yes, latent.** Experiments show a negative surplus once non-user effects count; many users "would prefer the product not to exist" | Platforms; users' FOMO-driven utility / platform lobbying | **r̂ and coordination**: a "product market trap" (Bursztyn et al. 2025) | O / S | [admit: HHS advisory 2023; OAIC / Australian government; Bursztyn, Handel, Jiménez-Durán & Roth 2025, *AER* 115(12):4105–36] |
| 29 | Political institutions | Democratic backsliding | Long-standing scholarly warnings | V-Dem 2026: 74% of world population in autocracies; 44 countries autocratising; US loses liberal-democracy status | Ongoing | — | **Professed support high, revealed priority low**: "only a small fraction of Americans prioritize democratic principles in their electoral choices" | Co-partisan policy wins / incumbents | **Partisan φ** plus L^R (policy wins) | O / S | [admit: V-Dem Democracy Report 2026; Graham & Svolik 2020, *APSR* 114(2):392–409] |
| 30 | Political institutions | US gun policy after mass shootings | Recurrent mass shootings | +15% firearm bills; in Republican legislatures laws that **loosen** restrictions double; no effect on tightening | — | Focusing events | Unknown | Gun owners and industry / partisan legislatures | **Crisis raises V** under partisan φ | O / S | [admit: Luca, Malhotra & Poliquin 2020, *J Public Econ* 181:104083] |
| 31 | Food systems | Somalia famine 2011 | FEWS NET special report Aug 2010; 16 escalating warnings | Famine declared 20 Jul 2011; donor scale-up only after the declaration; ~258,000 excess deaths (Oct 2010–Apr 2012) | ~1 | Famine declaration | n/a | Armed groups restricting access; donor risk aversion / same | V (access, counter-terror constraints), φ (distance) | F / Pa | [admit: Checchi & Robinson 2013 for FSNAU/FEWS NET; Food Policy "Early warning, late response (again)"] |
| 32 | Food systems | India after 1947 (famine prevention) | Food-production shortfalls, floods | Relief responsive where newspaper circulation and electoral accountability are higher (1958–92) | Short | Press and elections | n/a | — | **φ raised by local-language press; V lowered by elections** | P / W (consistent negative case) | [admit: Besley & Burgess 2002, *QJE* 117(4):1415–51] |
| 33 | Food systems | Malawi 2002, Niger 2005 | Food crises | "Belated and inadequate" responses despite electoral democracy and a free press | ~1 | Famine | n/a | Fragile state; donor dependence / denial | V and capacity; **Sen's protection not sufficient** | F / Pa | [admit: Rubin 2008 *Nordic J Afr Stud* 17(1):47–65; Rubin 2009 *EJDR* 21(5)] |

**Excluded from the tallies:** climate change, the author's target domain. The first credible warning was 1897 (EEA 2013 ch. 14) [admit: EEA 2013]. Including it would be circular.

---

### 4. Generality assessment

#### 4.1 Counts (convenience sample, n = 33)

| Category | Count | Share | Cases |
|---|---|---|---|
| P: prompt / pre-emptive | 7 | 21% | 4, 5, 17, 25, 26, 27, 32 |
| L: late, after cumulative harm or crisis | 11 | 33% | 1, 2, 3, 6, 7, 8, 9, 10, 11, 16, 24 |
| F: prevention failed, catastrophe first | 10 | 30% | 12, 14, 15, 19, 20, 21, 22, 23, 31, 33 |
| O: ongoing, no adequate action | 5 | 15% | 13, 18, 28, 29, 30 |
| **Late, failed or ongoing (L+F+O)** | **26** | **79%** | |

| Fit of the full micro-mechanism | Count | Share |
|---|---|---|
| S: strong (mass-level L^R + φ + r̂ + V all plausibly active) | 11 | 33% |
| Pa: partial (L^R + V among few deciders; r̂ marginal) | 13 | 39% |
| W: weak or other mechanism dominant (signal detection, small-N bargaining, or prompt cases) | 9 | 27% |

Strong: 3, 7, 9, 12, 13, 14, 16, 18, 28, 29, 30. Partial: 1, 2, 6, 8, 10, 11, 15, 19, 20, 21, 26, 31, 33. Weak: 4, 5, 17, 22, 23, 24, 25, 27, 32. The S/Pa boundary is a judgement call; see the caveat below.

**Reading.** Delay is the modal outcome in this sample. But the *full* four-term micro-mechanism, with a mass-public cascade and a biased r̂, is clearly needed in only about one-third of cases. In a further two-fifths, the delay is better explained by **incumbent L^R plus an institutional V operating among few decision-makers**: regulatory capture, organisational incubation, collusion (asbestos, Fukushima, Grenfell, Minamata, opioids). There the r̂/cascade term is idle, because no mass threshold had to be crossed for regulators to act. The author's mechanism is *one* of the routes to delay, and it is the dominant route for **commons and mass-behaviour problems**.

#### 4.2 Selection-bias caveat (must accompany any use of these numbers)

- **The sample is selected on the dependent variable.** Famous failures are written up; quiet prevention leaves no record. EEA explicitly chose "well-known hazards" [admit: EEA 2001, M8]. The prompt cases here were found only because I searched for counterexamples.
- **The "lag" depends on how the first credible warning is defined.** It is often fixed in hindsight, which inflates lags.
- **The 4-of-88 false-positive result (M11) also rests on a selected set** of alleged false positives, and critics dispute it.
- **No representative base rate exists in the literature** for "share of credible hazard warnings acted on pre-emptively". I found none in EEA, CAP, the policy-process literature or the disaster literature. This is a genuine gap [abstain: unverifiable; negative search result, not proof of absence].

#### 4.3 The more rigorous evidence that does exist

| Evidence | What it shows for generality | Tag |
|---|---|---|
| CAP budget distributions (Jones et al. 2009; Jones, Sulkin & Larsen 2003) | Delay-then-lurch is **ubiquitous** in democratic budgeting and agenda change, and stronger where institutional friction is higher. This is a *population-level*, non-selected signature. It is consistent with the model's veto/friction term, but it does not isolate L^R or r̂. | [admit: M21, M22] |
| Financial crises (Reinhart & Rogoff; Laeven & Valencia; Greenwood et al.) | Crises recur on a large scale (164 since 1970) and are *predictable*: a 40% vs 7% probability. Predictable yet unprevented is the model's core claim, and here it holds at population scale. | [admit: M18–M20] |
| Disaster-policy panel (Nohrstedt et al. 2021) | **Against** the "crisis → lurch" half: severity does not predict reform globally. | [admit: M33] |
| Myopic voters (Healy & Malhotra 2009) | For the delay half: preparedness is under-supplied across US counties and elections. | [admit: M32] |
| Anthropocene traps (Søgaard Jørgensen et al. 2024) | Participatory expert assessment: 12 of 14 global traps (86%) "could be in an advanced phase of trapping with high risk of hard-to-reverse lock-ins". Traps interact reinforcingly in 45% of pairs and dampen in 3%. These are expert judgements, not measurement. | [admit: *Phil Trans R Soc B* 379:20220261] |
| Energy transitions (Fouquet 2010 vs Sovacool 2016) | Typically slow, but fast transitions exist under specific conditions (small markets, state direction). | [admit: M26]; [abstain: M27 conflict] |

---

### 5. Where the mechanism fails: boundary conditions mapped to model variables

| # | Boundary condition | Model variable(s) | Evidence | Tag |
|---|---|---|---|---|
| B1 | **Harm is immediate, concentrated, visible and attributable** (a signature injury, a short latency, a clear cause). Delay collapses to days or months. | φ → 1; time-since-baseline ≈ 0; H falls on identifiable victims | Thalidomide withdrawn within about 10 days of Lenz's warning; vinyl chloride's "very prompt" response. Birkland's focusing-event criteria (sudden, concentrated, simultaneously known) describe exactly when φ jumps. | [admit: Lenz 1992; EEA 2013 ch. 8; Birkland 1998] |
| B2 | **Harm enters the veto players' own radius.** V falls because the elites' own L^R turns negative. *This is a sharpening of the model: V should be written V(H_elite).* | V = f(H inside the elite radius) | Great Stink: an 18-day Act once the smell reached Parliament. Dust Bowl: dust over Washington, then the Act in 1935. Cuban Missile Crisis: the hotline within 8 months. Y2K: firms' own systems. | [admit: London Gazette; NRCS; State Dept Historian; Quigley 2008] |
| B3 | **Cheap substitutes exist**, so the incumbent's L^R is small or falls. | L^R ↓ | Montreal (DuPont exit in 1988; Sunstein's cost-benefit asymmetry vs Kyoto); FGD in Germany; the alcohol additive alternative to lead in 1925, which shows substitutes are *necessary but not sufficient* when V controls information. | [admit: Sunstein 2007; EEA 2013 ch. 3] |
| B4 | **Few decision-makers who monitor each other** (small N, bounded resource, local rules). | r̂ accurate (no pluralistic ignorance); the N-scaling of time-to-tip is irrelevant; κ is coordinated | Sheridan-6 LEMA (185 wells) cut use by 20% or more; Ostrom's design principles (boundaries, mutual monitoring, graduated sanctions). This is also why the Xie et al. N-scaling result predicts large polities lag *more* than small ones. | [admit: K-State 2019; Ostrom 1990 (via secondary descriptions of the principles)] |
| B5 | **Free local press plus electoral accountability** raise φ and lower V, but are **not sufficient**. | φ ↑ (information), V ↓ (accountability) | Indian states respond more to food shortfalls where newspaper circulation is higher. Famine occurred anyway in electoral democracies with a free press (Malawi 2002, Niger 2005). **Sen's thesis as an absolute law is refuted; as a tendency it is supported.** | [admit: Besley & Burgess 2002]; "no famine in a functioning democracy" as a universal claim [refute: Rubin 2008, 2009] |
| B6 | **Hard, known deadlines** produce *deadline lurches* rather than prevention, unless the fix is cheap and the harm falls on the actors themselves. | V (war of attrition) with a known terminal date | Y2K was pre-empted because firms bore the harm. US Social Security has a known depletion date (Q4 2032) with no comprehensive action. The model predicts a deadline lurch there and, across dated deadlines generally, lead times skewed toward zero (F7; §7.1). | [admit: SSA 2026; Quigley 2008] |
| B7 | **The bottleneck is signal detection inside a small expert organisation, not collective action.** | φ (organisational noise) only; L^R and r̂ idle | Pearl Harbor (signals vs noise); 9/11 ("failure of imagination"); disaster incubation. The author's mass-cascade mechanism is the wrong tool here. | [admit: Wohlstetter 1962; Pidgeon & O'Leary 2000] |
| B8 | **Partisan or identity-sorted φ: a crisis can raise V instead of tipping.** | φ gated by identity; V responsive to co-partisan elites | Mass shootings double loosening laws under Republican legislatures. Undemocratic candidates are punished only weakly, and less so as polarisation rises. | [admit: Luca et al. 2020; Graham & Svolik 2020] |
| B9 | **Single-authority systems:** delay is V-dominated and the mass cascade matters only for regime change. | V ≫; r̂ suppressed (Kuran) | Aral Sea and Minamata (state industrial priorities). In autocracies the r̂ term reappears as preference falsification, which explains *sudden* collapse (1989), not policy delay. | [admit: Micklin 2007; EEA 2013 ch. 5]; Kuran admitted in the main body (B.2) |
| B10 | **Information monopoly by incumbents**: V depresses φ directly. | φ is endogenous to V | Leaded petrol: decades with "virtually no independent research". Tobacco, beryllium, and the doubt merchants. | [admit: EEA 2013 ch. 3, 6, 7; Oreskes & Conway 2010] |

**Top three boundary conditions for the summary:** (B1) immediate, concentrated, attributable harm; (B2) harm reaching the veto players' own radius; and (B3/B4) cheap substitutes or small-N self-governance. B5 (press and democracy) is the main *institutional* lever, but it is demonstrably insufficient on its own.

---

### 6. Existing domain-general theories of delay, and how the author's mechanism relates

| Theory | Level | Overlap with the author's terms | What the author adds or differs on | Tag |
|---|---|---|---|---|
| **Social traps** (Platt 1973, *Am Psychol* 28(8):641–651; Messick & McClelland 1983 on temporal traps) | **Micro, domain-general** | Short-term individual reinforcement vs long-term or collective cost: L (near benefit) vs H (delayed harm); "time-delay traps" | Platt has no cascade threshold, no biased r̂, no trust radius on L, no elite veto, no N-scaling. **This is the most direct micro-level precedent and should be cited.** | [admit: Platt 1973 citation; trap typology via Messick & McClelland 1983] |
| **Preference falsification** (Kuran 1989, 1991, 1995) | Micro, domain-general (revolutions, ethnicity, caste, policy) | r̂ (hidden private support), thresholds, sudden cascades | Kuran explains *surprise and suddenness*, not the L^R radius or V. The author's composite adds both. | Kuran admitted in the main body (B.2); [admit: *World Politics* 44:7–48 citation] |
| **Punctuated equilibrium / institutional friction / disproportionate information processing** (Baumgartner & Jones 1993; Jones & Baumgartner 2005; Jones et al. 2003, 2009) | Meso, domain-general, **quantitatively validated** | V ≈ friction; φ ≈ attention; delay-then-lurch | No individual payoff structure (L^R, H). The author's micro-model could *generate* friction-like kurtosis, which is a testable bridge (F6 below). | [admit: M21, M22] |
| **Path dependence / increasing returns** (Arthur 1989; David 1985; Pierson 2000 *APSR* 94(2):251–267; *Politics in Time* 2004) | Macro or meso | L^R grows with adoption; reversal becomes "almost impossible" | Explains entrenchment, not a perception or cascade route to escape. | [admit: Pierson 2000]; Arthur, David and *Politics in Time* details [abstain: unverifiable] |
| **Carbon lock-in / techno-institutional complex** (Unruh 2000 *Energy Policy* 28:817–830; Seto et al. 2016 *Annu Rev Environ Resour* 41:425–452) | Meso | Infrastructural, institutional and behavioural lock-in. Actors who benefit "push for institutional rules that further their interests": the L^R → V feedback | Unruh (2002) argues escape requires *exogenous* forces, which agrees with the model's crisis term. The author adds micro-heterogeneity (radius, φ, r̂). | [admit: Unruh 2000; Seto et al. 2016] |
| **Regime resistance / MLP** (Geels 2002, 2014) | Meso, socio-technical | L^R (regime incumbents), V (resistance), landscape shocks ≈ crises | MLP has no individual threshold or cascade algebra. | [admit: Geels 2014] |
| **Collingridge dilemma** (1980) | Technology governance, general | Information problem (φ early) plus entrenchment (L^R and V late) | A two-horn timing dilemma, no cascade. It fits AI governance directly. | [admit: M30] |
| **Disaster incubation** (Turner 1978; Pidgeon & O'Leary 2000) | Organisational, general | φ attenuated by social processes | Organisational, not mass-public. | [admit: M29] |
| **Predictable surprises** (Bazerman & Watkins 2004) | Organisational and political, general | Cognitive (φ), organisational, political (V, special interests) | Prescriptive taxonomy, no formal model. | [admit: M16] |
| **Ostrich paradox** (Meyer & Kunreuther 2017) | Individual, general | Myopia, amnesia (baselines), herding (r̂), inertia | Disaster-preparedness focus; no V. | [admit: M31] |
| **Product-market collective traps** (Bursztyn et al. 2025) | Micro, market | Individually rational use, collectively negative welfare: a coordination trap | Empirical demonstration outside climate that majorities can be trapped. Directly supports r̂ and coordination. | [admit: *AER* 115(12)] |
| **Anthropocene evolutionary traps** (Søgaard Jørgensen et al. 2024) | Global, cultural-evolutionary | Shifting baselines (φ over time); masked interactions weaken signals across space (φ over distance); short-termism; entrenched powerful actors (V) | **Closest polycrisis-literature analogue.** It is a shared mechanism across 14 systems, but qualitative and participatory, with no r̂, threshold algebra or N-scaling. | [admit: *Phil Trans B* 379:20220261] |
| **Polycrisis causal mechanisms** (Lawrence et al. 2024, *Glob Sustain* 7:e6) | Systems | Slow stresses plus fast triggers push systems out of equilibrium; three pathways (common stresses, domino effects, inter-systemic feedbacks) | System-level entanglement, **no micro-mechanism of delay**, so the main body's characterisation of *this paper* stands. | [admit: Lawrence et al. 2024 abstract] |
| **Ideational root of the polycrisis** (Purdey 2025, *Glob Sustain* 8:e9) | Cultural | An exaggerated human exceptionalism legitimises "profligate behavior" | A shared *cause*, not a micro-mechanism. | [admit: Purdey 2025 abstract] |

**Does the polycrisis literature have a shared micro-mechanism of delay?** For Lawrence et al. 2024 itself: yes [admit: Lawrence et al. 2024]. For the polycrisis literature broadly: **no**. Søgaard Jørgensen et al. (2024) propose shared trap mechanisms that overlap substantially with φ (temporal and spatial decay) and V [refute: Søgaard Jørgensen et al. 2024]. Theirs is not a *formal micro* mechanism, so the narrower claim, that no paper offers a formal individual-level threshold model of delay with veto and N-scaling across domains, survives my search. Absence in a search is weak evidence [abstain: unverifiable].

**Unifying name.** No single canonical name exists for a domain-general *micro*-mechanism of delay. The best existing labels are: **"social trap / time-delay trap"** (micro; Platt 1973), **"lock-in"** (meso/macro; path dependence, carbon lock-in), **"regime resistance"** (socio-technical), **"institutional friction"** (policy process), and **"predictable surprise"** (management). The author's coinage in B.3, a *radius-bounded crisis threshold*, remains a fair label for the specific composite.

---

### 7. Falsification criteria

The model explains prompt cases by parameter values: high φ, low L^R, low V. That makes it **at risk of unfalsifiability unless the parameters are measured before outcomes are known.** These tests avoid that:

- **F1, ex-ante parameter coding.** Code φ (latency, visibility, attributability), L^R concentration (share of benefits to top-k actors), V (veto points and incumbent lobbying share) and r̂ bias (survey gap) for a *pre-registered* set of current hazards. Predict lag ranks. A rank correlation near zero falsifies the model.
- **F2, trust radius.** Countries with a wider trust radius (Delhey et al. scores) should act sooner after equivalent warnings, for example on adoption lags for the same EU directive or WHO guideline. No relationship falsifies the L^R-radius term.
- **F3, correcting r̂.** Correcting pluralistic ignorance should raise action *outside* climate: pensions, AMR stewardship, social-media coordination (testable on the Bursztyn et al. design). A null across domains falsifies the r̂ term's generality.
- **F4, elite exposure (B2).** Reform should cluster when harm falls inside the veto holders' radius, for example disasters in capitals or legislators' constituencies or families. If elite-exposure events are no more reform-producing than equally severe non-elite events, the V(H_elite) sharpening fails. Nohrstedt et al.'s null for disaster severity makes this a live test.
- **F5, N-scaling.** Controlling for veto points, larger polities should show longer lags on equivalent problems (Xie et al.). No size effect, or faster large polities, counts against the N-scaling claim. The confound is that population covaries with federalism and veto points.
- **F6, bridge to CAP.** Policy topics with high L^R/H asymmetry (diffuse harm, concentrated benefit) should show *higher* budget kurtosis than topics with concentrated harm. Testable with existing Comparative Agendas data.
- **F7, a deadline panel.** Across hazards with a publicly known, dated deadline, comprehensive action should land near the deadline, and more tightly where veto points are many and incumbents' L^R is large. Lead times that are uniform or skewed early, or unrelated to the V and L^R scores, falsify it. The panel is in §7.1. One open member is a forward prediction: no comprehensive US Social Security solvency law passes until within about 2 years of OASI depletion (Q4 2032). On its own that case would be a single but salient disconfirmation; in the panel it is one observation among several.
- **F8, crisis polarity.** Where φ is partisan-sorted (guns, democracy, climate in the US), the model predicts that crises *increase* polarisation in enacted policy (Luca et al.). Crises producing cross-partisan convergence in sorted domains would contradict B8.

#### 7.1 Deadline panel for P7

Members are hazards with a dated deadline set publicly by an official projection, statute, agreement or treaty. Lead time is the deadline minus the date of comprehensive action: an enactment, signature or final agency decision that resolves the deadline for at least several years. Resolved members give evidence now, but their outcomes are known, so their V and L^R scores should be coded blind to lead time. Open members are scored and registered before their deadlines. Aquifer and fishery depletion were considered and left out: no authoritative dated depletion projection was found.

| # | Member | Deadline | Comprehensive action | Lead time | Tag |
|---|---|---|---|---|---|
| DL1 | US OASI trust fund (open) | Depletion Q4 2032 (2026 Trustees Report) | None comprehensive | Open; the model predicts under about 2 years | Admitted at case 13; not re-counted |
| DL2 | US Medicare HI trust fund (open) | Depletion Q2 2033 (2026 Trustees Reports) | None | Open | [admit: SSA Trustees Report summary 2026] |
| DL3 | 1983 Social Security amendments (resolved) | 1982 Trustees Report: OASI unable to pay benefits on time from July 1983 without legislation | P.L. 98-21 signed 20 April 1983 | About 2.5 months | [admit: CRS R47040; Reagan Library signing remarks] |
| DL4 | Korea National Pension (resolved, parametric) | 2023 (5th) financial projection: fund depleted 2055 | National Pension Act amendment passed 20 March 2025: contributions 9% to 13% by 2033, replacement rate 43% | About 30 years (an early-skewed member) | [admit: NABO; *KDI J Econ Policy* 47(1)]; post-reform depletion year given as 2064, 2065 or 2071 depending on projection [abstain: source-vs-prior conflict (Ministry of Health and Welfare vs NABO)] |
| DL5 | Colorado River operating rules (resolved) | 2007 Interim Guidelines, 2019 Drought Contingency Plans and related agreements expire in 2026; new operations must begin 1 October 2026 | Interior Record of Decision (August 2026) adopts a 2027–2036 Decision Framework. The seven Basin States reached no consensus, and specific shortage volumes and distributions were not adopted | About 1–2 months, by federal fallback rather than negotiated settlement | [admit: Reclamation ROD, August 2026] |
| DL6 | US debt limit, 2011 (resolved) | Treasury X-date 2 August 2011 | Budget Control Act (P.L. 112-25) signed 2 August 2011 | 0 days | [admit: CRS R41633; CRS RL31967] |
| DL7 | US debt limit, 2013 (resolved) | Treasury: extraordinary measures exhausted no later than 17 October 2013 | P.L. 113-46 signed shortly after midnight on 17 October 2013 | 0 days | [admit: CRS R41633; CBO Nov 2013] |
| DL8 | US debt limit, 2023 (resolved) | X-date 5 June 2023 (Treasury letter of 26 May) | Fiscal Responsibility Act (P.L. 118-5) enacted 3 June 2023 | 2 days | [admit: CRS IN11829 (enactment)]; the 5 June date [abstain: non-authoritative source (press reports of the Treasury letter; CRS gives "early June")] |
| DL9 | US debt limit, 2025, and TCJA individual provisions (resolved) | Debt limit reinstated 2 January 2025, X-date projected mid-August to late September 2025; TCJA individual provisions due to expire after 31 December 2025 | P.L. 119-21 enacted 4 July 2025: debt limit raised by $5 trillion; most TCJA individual provisions made permanent | About 6–12 weeks (debt limit); about 6 months (TCJA). One law resolved both, so they count as one event | [admit: CRS IN12045; congress.gov H.R. 1 record]; X-date window and the permanence of individual provisions [abstain: non-authoritative source (secondary reports of CBO; Tax Foundation, PwC)] |
| DL10 | Kigali Amendment HFC phase-down (open) | Non-Article 5 parties cut HFC production and consumption 85% from baseline by 2036, in steps from 2019 | Domestic implementing measures before each step | Open | [admit: CRS IF11779]; intermediate steps (40% from 2024, 70% from 2029, 80% from 2034) [abstain: non-authoritative source (industry regulatory alert; treaty text not opened)] |

**Reading (analytical, not tagged).** Six of the seven resolved events landed within about three months of their deadlines, three within two days. Korea's reform landed about 30 years early, but it was parametric, so the coding rule for "comprehensive" has to be fixed before scoring. The debt-limit episodes share one institution and are not independent. Colorado shows a second route to the deadline: when the veto players do not agree, a federal fallback lands at it. These seven events are not yet scored on V or L^R, so they test only the skew, not the interaction that distinguishes the model.

---

### 8. Annotated bibliography

#### Meta-literature and case compendia
- **European Environment Agency (2001/2002).** *Late lessons from early warnings: the precautionary principle 1896–2000.* Environmental issue report 22. Copenhagen: EEA. https://www.eea.europa.eu/en/analysis/publications/environmental_issue_report_2001_22. 14 cases, twelve lessons, no aggregate lag statistic.
- **European Environment Agency (2013).** *Late lessons from early warnings: science, precaution, innovation.* EEA Report 1/2013. Includes false positives (ch. 2), lead (ch. 3), Minamata (ch. 5), tobacco (ch. 7), vinyl chloride (ch. 8), climate (ch. 14) and business non-precaution (ch. 25).
- **Oreskes, N. & Conway, E. M. (2010).** *Merchants of Doubt.* New York: Bloomsbury. ISBN 978-1-59691-610-4. Cross-domain doubt strategy (V lowering φ).
- **Bazerman, M. H. & Watkins, M. D. (2004).** *Predictable Surprises.* Boston: Harvard Business School Press. ISBN 1-59139-178-4. Cognitive, organisational and political roots; RPM.
- **Wucker, M. (2016).** *The Gray Rhino.* New York: St. Martin's Press. ISBN 978-1250053824. Trade book; use for vocabulary only.
- **Reinhart, C. M. & Rogoff, K. S. (2009).** *This Time Is Different: Eight Centuries of Financial Folly.* Princeton UP. https://www.jstor.org/stable/j.ctvcm4gqx
- **Greenwood, R., Hanson, S. G., Shleifer, A. & Sørensen, J. A. (2022).** Predictable financial crises. *J Finance* 77(2):863–921. doi:10.1111/jofi.13105
- **Laeven, L. & Valencia, F. (2020).** Systemic Banking Crises Database II. *IMF Econ Rev* 68:307–361. doi:10.1057/s41308-020-00107-3. Updated as IMF WP/26/94 (2026), 1970–2025.
- **Diamond, J. (2005).** *Collapse.* New York: Viking. Ch. 14 decision-failure taxonomy (confirmed only through summaries).

#### Policy process and institutions
- **Baumgartner, F. R. & Jones, B. D. (1993).** *Agendas and Instability in American Politics.* University of Chicago Press. (Bibliographic details not re-verified.)
- **Jones, B. D. et al. (2009).** A general empirical law of public budgets: a comparative analysis. *AJPS* 53(4):855–873. doi:10.1111/j.1540-5907.2009.00405.x
- **Jones, B. D., Sulkin, T. & Larsen, H. A. (2003).** Policy punctuations in American political institutions. *APSR* 97(1):151–169. doi:10.1017/S0003055403000583
- **Kingdon, J. W. (1984).** *Agendas, Alternatives, and Public Policies.* Boston: Little, Brown. (Publisher not re-verified.)
- **Birkland, T. A. (1998).** Focusing events, mobilization, and agenda setting. *J Public Policy* 18(1):53–74. doi:10.1017/S0143814X98000038
- **Sabatier, P. A. (1988).** An advocacy coalition framework of policy change. *Policy Sciences* 21:129–168. (Hypothesis wording via Jenkins-Smith et al. 2018.)
- **Nohrstedt, D., Mazzoleni, M., Parker, C. F. & Di Baldassarre, G. (2021).** Exposure to natural hazard events unassociated with policy change for improved disaster risk reduction. *Nat Commun* 12:193. doi:10.1038/s41467-020-20435-2. The key null for the crisis term.
- **Nohrstedt, D. (2022).** When do disasters spark transformative policy change and why? *Policy & Politics* 50(3):425–441. doi:10.1332/030557321X16508834302815
- **Healy, A. & Malhotra, N. (2009).** Myopic voters and natural disaster policy. *APSR* 103(3):387–406. doi:10.1017/S0003055409990104
- **Pierson, P. (2000).** Increasing returns, path dependence, and the study of politics. *APSR* 94(2):251–267. doi:10.2307/2586011. *Politics in Time* (Princeton UP, 2004) not re-verified.
- **Ostrom, E. (1990).** *Governing the Commons.* Cambridge UP. Eight design principles.

#### Socio-technical transitions and lock-in
- **Fouquet, R. (2010).** The slow search for solutions. *Energy Policy* 38(11):6586–6596. doi:10.1016/j.enpol.2010.06.029
- **Sovacool, B. K. (2016).** How long will it take? *ERSS* 13:202–215. doi:10.1016/j.erss.2015.12.020. Rebutted by Grubler, Wilson & Nemet (2016), *ERSS*.
- **Geels, F. W. (2014).** Regime resistance against low-carbon transitions. *Theory, Culture & Society* 31(5):21–40. doi:10.1177/0263276414531627
- **Unruh, G. C. (2000).** Understanding carbon lock-in. *Energy Policy* 28(12):817–830. doi:10.1016/S0301-4215(00)00070-7
- **Seto, K. C. et al. (2016).** Carbon lock-in: types, causes, and policy implications. *Annu Rev Environ Resour* 41:425–452.
- **Collingridge, D. (1980).** *The Social Control of Technology.* London: Frances Pinter. See also Genus & Stirling (2018), *Research Policy* 47(1):61–69.

#### Micro-mechanisms and behavioural accounts
- **Platt, J. (1973).** Social traps. *Am Psychol* 28(8):641–651. doi:10.1037/h0035723. The most direct micro precedent.
- **Messick, D. M. & McClelland, C. L. (1983).** Social traps and temporal traps. *PSPB* 9(1):105–110. doi:10.1177/0146167283091015
- **Kuran, T. (1991).** Now out of never. *World Politics* 44(1):7–48. *Private Truths, Public Lies* (Harvard UP, 1995).
- **Meyer, R. & Kunreuther, H. (2017).** *The Ostrich Paradox.* Philadelphia: Wharton Digital Press. ISBN 9781613630792.
- **Bursztyn, L., Handel, B., Jiménez-Durán, R. & Roth, C. (2025).** When product markets become collective traps: the case of social media. *AER* 115(12):4105–4136. doi:10.1257/aer.20231468
- **Centola, D., Becker, J., Brackbill, D. & Baronchelli, A. (2018).** Experimental evidence for tipping points in social convention. *Science* 360:1116–1119. doi:10.1126/science.aas8827. Threshold about 25%; see Part C.
- **Turner, B. A. (1978).** *Man-Made Disasters.* London: Wykeham. **Pidgeon, N. & O'Leary, M. (2000).** *Safety Science* 34:15–30. doi:10.1016/S0925-7535(00)00004-7
- **Wohlstetter, R. (1962).** *Pearl Harbor: Warning and Decision.* Stanford UP. Bancroft Prize 1963.
- **Graham, M. H. & Svolik, M. W. (2020).** Democracy in America? *APSR* 114(2):392–409. doi:10.1017/S0003055420000052
- **Luca, M., Malhotra, D. & Poliquin, C. (2020).** The impact of mass shootings on gun policy. *J Public Econ* 181:104083. doi:10.1016/j.jpubeco.2019.104083

#### Polycrisis
- **Lawrence, M., Homer-Dixon, T., Janzwood, S., Rockström, J., Renn, O. & Donges, J. F. (2024).** Global polycrisis: the causal mechanisms of crisis entanglement. *Glob Sustain* 7:e6. doi:10.1017/sus.2024.1
- **Søgaard Jørgensen, P. et al. (2024).** Evolution of the polycrisis: Anthropocene traps that challenge global sustainability. *Phil Trans R Soc B* 379:20220261. doi:10.1098/rstb.2022.0261
- **Purdey, S. J. (2025).** The social pathology of polycrisis. *Glob Sustain* 8:e9. doi:10.1017/sus.2025.11

#### Famine and democracy
- **Sen, A. (1981).** *Poverty and Famines.* Oxford: Clarendon. **Sen, A. (1999).** *Development as Freedom.* "Functioning multiparty democracy" formulation, p. 178 as quoted by Rubin.
- **Besley, T. & Burgess, R. (2002).** The political economy of government responsiveness. *QJE* 117(4):1415–1451.
- **Rubin, O. (2008).** The Malawi 2002 famine. *Nordic J African Studies* 17(1):47–65. **Rubin, O. (2009).** The merits of democracy in famine protection: fact or fallacy? *EJDR* 21(5).
- **Checchi, F. & Robinson, W. C. (2013).** *Mortality among populations of southern and central Somalia affected by severe food insecurity and famine during 2010–2012.* FAO/FSNAU and FEWS NET.

#### Case primary sources
- Doll & Hill (1950) *BMJ* 2:739–748. US Surgeon General (1964) *Smoking and Health*. WHO FCTC (2003/2005). Proctor (2011) *Golden Holocaust*, UC Press.
- UNEP (30 Aug 2021), "Era of leaded petrol over". Needleman & Gee, EEA 2013 ch. 3.
- Molina & Rowland (1974) *Nature* 249:810–812. Farman, Gardiner & Shanklin (1985) *Nature* 315:207–210. Sunstein (2007) *Harv Envtl L Rev* 31:1.
- Hutchings & Myers (1994) *CJFAS* 51:2126–2146. doi:10.1139/f94-214. Micklin (2007) *Annu Rev Earth Planet Sci* 35:47–72. doi:10.1146/annurev.earth.35.031306.140120
- Castanon (2007) *Poultry Science* 86:2466–2471 (AGP history). UN General Assembly AMR Political Declaration (Sept 2024).
- GPMB (2019) *A World at Risk*. ISBN 978-92-4-151701-0. WHO Pandemic Agreement (WHA78, 20 May 2025).
- US House (2006) *A Failure of Initiative*, H. Rpt. 109-377. Grenfell Tower Inquiry (2024) Phase 2 Report. NAIIC (2012) Official Report, executive summary.
- SSA (2026) *Annual Report of the Board of Trustees of the OASI and DI Trust Funds* (9 June 2026). CBD (2020) *Global Biodiversity Outlook 5*. V-Dem Institute (2026) *Democracy Report 2026*.
- HHS (2023) *Social Media and Youth Mental Health* (Surgeon General advisory). Online Safety Amendment (Social Media Minimum Age) Act 2024 (Cth).
- Quigley, K. (2008) *Responding to Crises in the Modern Infrastructure: Policy Lessons from Y2K.* Palgrave. doi:10.1057/9780230241640.
- Kuehn (2017) *JAMA* 318(24):2418 (opioid emergency). Dowell, Haegerich & Chou (2016) *JAMA* 315(15):1624–45.

---

### 9. Disposition ledger

Counted by bracketed tag occurrences in Sections 2–6 and the §7.1 deadline panel, excluding the three legend examples in the header. Where one table cell carries two tags, both are counted. Claims admitted in the main body are not re-counted.

| Disposition | Sections 2–6 | §7.1 deadline panel | Total |
|---|---|---|---|
| admit | 96 | 9 | 105 |
| refute | 4 | 0 | 4 |
| abstain | 21 | 4 | 25 |

**Refutations, with corrections:**
1. EEA provides "measured gaps" as a base rate. **False.** There is no aggregate lag statistic; lags are per case, and the general statement is "many years or decades, and in some cases over a century" (M4).
2. "OASI depletion 2033". **Superseded.** The 2026 Trustees Report gives Q4 2032 (case 13).
3. Sen's no-famine-in-democracy as a universal law. **Refuted as absolute** (Malawi 2002, Niger 2005). It is supported as a tendency by Besley & Burgess (B5).
4. "The polycrisis literature has no shared mechanism of delay". **Refuted in its broad form** by Søgaard Jørgensen et al. 2024. It stands for Lawrence et al. 2024 and for *formal micro* models (Section 6).

**Most consequential correction to the model (built from admitted sources, not a separate refute tag):** the model's implicit premise that crises reliably tip reform is contradicted globally by Nohrstedt et al. 2021 (M33) and, under partisan φ, by Luca et al. 2020 (B8). The crisis/V term therefore makes V depend on the elites' own harm and on identity sorting (B2, B8; see B.4.1).

**Open gaps:**
- No representative base rate of pre-emptive vs late action exists.
- The CAP kurtosis has not been broken down by L^R/H asymmetry (F6 is an open test).
- Kingdon, Baumgartner & Jones 1993, Arthur, David and *Politics in Time* bibliographic details were not re-opened this session.

---

## Appendix C: n-order harms, accreted wickedness and the lateral-connection problem

**Researched:** 2026-10-11
**Question.** When a root cause goes unresolved, its harms travel down a causal chain into other domains. Where along that chain does policy respond, who carries the harm back to the people who can fix the root, and does layering symptomatic responses on top of one another turn a tractable problem into a wicked one?
**Model terms** (φ, H, L^R, r̂, V, M, N-scaling) are as defined in B.4 and B.4.1. Findings already tagged in the main body or Appendices A and B are cited here but not re-tagged or re-counted.
**Method.** For each claim I first tried to refute it against a primary or authoritative source, then tagged it:
- `[admit: source]`: confirmed this session in an authoritative source, and the refutation attempt failed.
- `[refute: source]`: an authoritative source contradicts the claim. The correction is given.
- `[abstain: reason]`: reason is one of *unverifiable*, *source-vs-prior conflict*, *non-authoritative source*, or *tier-floor: unearned confidence*.

Text marked **Synthesis** is my own inference from tagged findings. It is not a sourced claim and is not counted in the ledger. The chain codings in Section 5 are Synthesis.

---

### 1. Summary verdict

1. **Responses settle near the symptom.** In all four current chains, most enacted policy sits at the downstream link nearest the visible harm: utility liability funds, insurer rules and the FAIR Plan in California; age limits, phone bans and platform codes for social media; GLP-1 drugs alongside narrow food rules for obesity; government collapses and market repricing, not deficit correction, in France. Root-tier action exists in each case (cap-and-invest to 2045, the soft drinks levy, the EU deficit procedure) but is slower and smaller. This is a pattern in four non-random cases, not a measured rate.
2. **Carriers decide when the root is reached.** In the three resolved historical chains, root-cause action followed the arrival of an actor that could move the cost into the veto holders' radius: state attorneys general and courts for tobacco (Medicaid cost-recovery suits from 1994, the 1998 Master Settlement), independent scientists and catalytic-converter compatibility for lead, and a skin-cancer cost–benefit case that made ozone loss a domestic US harm. In the current chains the carriers are bond markets and rating agencies (France), insurers and the FAIR Plan (California), and regulators of platform design (EU, UK, Australia).
3. **Accreted wickedness is not named in the literature, but its parts are.** No source uses "accreted", "iatrogenic" or "policy-induced" wickedness. The components exist separately: unintended aggregate consequences (Merton 1936; Kahn 1966), policy feedback creating constituencies (Pierson 1993), layering (Streeck & Thelen 2005; Howlett & Rayner 2009), policy accumulation without termination (Adam et al. 2019), policy reacting to its own consequences (Wildavsky 1979), iatrogenic regulation (Wiener 2003), and the IPCC's statement that "some responses to climate change result in new impacts and risks". The combination looks new. That is an absence-of-evidence judgement.
4. **No base rate exists for non-crisis comprehensive unwinding.** Unit-level termination is measured: about 10% of US domestic programmes eliminated within a decade (Berry, Burden & Howell), 7% of Texas sunset reviews ending in abolition, 15% of 1923 federal organisations gone by 1973 (Kaufman). No study measures how often an accumulated policy complex is unwound comprehensively, with or without a crisis.
5. **Corrections that change the Part G claim.** Olson's (1982) sclerosis thesis is "generally" supported, not mixed, though its coalition mechanism is weakly supported. Peters (2017) argues that "wicked" is over-applied, not that wickedness is constructed; the constructedness argument is Daviter (2019). The 1986 tax reform was eroded only partly. Airline deregulation is explained by ideas and expert advocacy (Derthick & Quirk), not by a sector crisis.

---

### 2. Coding scheme for causal chains

Each chain is a sequence root → link 1 → … → link k. Each link is coded on four dimensions (Section 5):
- **Attributability** a_j ∈ (0, 1]: how clearly link j's harm is traced to its cause by the people who bear it. High (H) for signature harms, medium (M) for statistically detectable harms, low (L) for contested or diffuse ones.
- **Who bears the harm** at that link.
- **Who holds the veto** over action at that link and at the root.
- **Carrier**: any actor who brings the link's cost into the root veto holders' own radius (creditors, insurers, courts, partner states, regulators in another jurisdiction).

---

### 3. Current chains

#### 3.1 Chain (a): French public debt → social spending → EU spill-over

| # | Finding | Tag |
|---|---|---|
| FR1 | General government debt was 119.0% of GDP (€3,595.5bn) at the end of Q2 2026, a record, up from 117.5% in Q1. End-2025 debt was 115.7% of GDP (first published as 115.6%). | [admit: INSEE Informations rapides n°239, 29 Sep 2026; INSEE IR n°78, 27 Mar 2026] |
| FR2 | The general government deficit was 5.8% of GDP in 2024 and 5.1% in 2025. | [admit: INSEE IR n°78, 27 Mar 2026; Insee Première n°2106, May 2026] |
| FR3 | The adopted 2026 budget targets a deficit of about 5.0% of GDP (the October 2025 draft said 4.7%). | [abstain: non-authoritative source — press reports of the budget law; the law itself was not opened] |
| FR4 | Budget fights brought down two governments in nine months. Barnier was censured on 4 Dec 2024 after forcing the social security budget through under article 49.3. Bayrou lost a confidence vote on 8 Sep 2025 (364–194). Lecornu was appointed on 9 Sep 2025, resigned on 6 Oct and was reappointed on 10 Oct. His government survived the January–February 2026 censure motions, the 2026 budget was adopted on 2 Feb 2026, and no government has fallen in 2026. | [abstain: non-authoritative source — dates consistent across press reports and encyclopaedic sources; Assemblée nationale records not reached] |
| FR5 | Rating cuts: Moody's Aa2 → Aa3 (Dec 2024; outlook negative 24 Oct 2025); Fitch AA- → A+ (12 Sep 2025); DBRS AA (high) → AA (19 Sep 2025); S&P AA- → A+ (17 Oct 2025). No major agency downgraded France in 2026 up to 10 Oct; DBRS moved its outlook to negative on 18 Sep 2026. | [admit: Agence France Trésor, "France's credit ratings", aft.gouv.fr; DBRS Morningstar rating actions] |
| FR6 | The 10-year OAT–Bund spread was about 40–50 bp from 2022 to June 2024. It passed 130 bp on 1 Oct 2026, the widest since 2012, and France's 10-year yield was above Italy's in early October 2026. | [abstain: non-authoritative source — market press (Bloomberg, Il Sole 24 Ore); no Banque de France or ECB series reached] |
| FR7 | France has been in the EU excessive deficit procedure since Council Decision (EU) 2024/2122 of 26 Jul 2024. A January 2025 Council recommendation sets 2029 for correction. | [admit: EUR-Lex, OJ L 2024/2122; European Commission EDP page for France] |
| FR8 | The IMF warns that delayed consolidation in high-debt euro-area countries, naming France and Italy, could force a disruptive correction with negative spillovers. | [admit: IMF, Euro Area Policies 2026 Article IV, press release 26/255, 22 Jul 2026] |
| FR9 | That a country under an EDP is ineligible for the ECB's Transmission Protection Instrument. | [abstain: non-authoritative source — press interpretation; no ECB statement found] |
| FR10 | The pressure reached social spending in the draft budgets, less in the enacted ones. The draft 2026 social security budget proposed a freeze of pensions and benefits ("année blanche") and capped health spending growth (ONDAM) at +1.6%. Parliament dropped the freeze, ONDAM ended at +3.1%, and the 2023 pension reform was suspended until January 2028 (law of 16 Dec 2025). | [abstain: non-authoritative source — secondary policy summaries (Touteleurope, Banque des Territoires); LFSS text not opened] |

**Correction.** "Debt pressure cut social security, health and education spending" holds for the *proposals* that brought governments down, not for the enacted 2026 budget, which raised ONDAM and suspended the pension reform. The chain's response so far has landed on governments (two fell) and on ratings and spreads, not on the root deficit.

#### 3.2 Chain (b): climate policy failure and forest management → California wildfire severity

| # | Finding | Tag |
|---|---|---|
| CA1 | Anthropogenic climate change caused a near doubling of western US forest-fire area over 1984–2015, plus about nine more high-fire-danger days a year. | [admit: Abatzoglou & Williams 2016, PNAS 113:11770–75] |
| CA2 | California's annual burned area rose about fivefold over 1972–2018, and summer forest-fire area more than eightfold, largely through warming-driven aridity. | [admit: Williams et al. 2019, Earth's Future 7:892–910] |
| CA3 | A century of fire exclusion left a "fire deficit" and fuel build-up in dry western forests. Climate and fuel both contribute; the evidence does not support either as the sole cause. | [admit: Hagmann et al. 2021, Ecol Appl 31:e02431; Hessburg et al. 2021, Ecol Appl] |
| CA4 | Federal forest-management law moved toward fuel reduction with the Healthy Forests Restoration Act (Pub. L. 108-148, 3 Dec 2003). | [admit: congress.gov] |
| CA5 | The 1935 US Forest Service "10 a.m. policy" and California SB 901 (2018) as the specific legislative roots. | [abstain: unverifiable — no primary text reached] |
| CA6 | PG&E filed for Chapter 11 on 29 Jan 2019, citing wildfire liabilities, and emerged on 1 Jul 2020. On 16 Jun 2020 it pleaded guilty to 84 counts of involuntary manslaughter (Camp Fire, 2018). | [admit: CPUC PG&E bankruptcy page; PG&E Form 8-K plea agreement, SEC] |
| CA7 | California's AB 1054 (12 Jul 2019) created a wildfire fund of up to $21bn to backstop utility liability. SB 254 (19 Sep 2025) added an $18bn continuation account. | [admit: bill texts as summarised by CalChamber; KQED] |
| CA8 | The ~$30bn PG&E liability estimate and the role of inverse condemnation. | [abstain: unverifiable — not reached] |
| CA9 | State Farm General stopped accepting new homeowner applications on 27 May 2023. Allstate had stopped writing new homeowner policies on 2 Nov 2022 (made public in June 2023). In March 2024 State Farm announced about 72,000 non-renewals (about 30,000 homeowner and 42,000 commercial apartment policies). An emergency 17% rate increase took effect on 1 Jun 2025. | [admit: California Department of Insurance, State Farm stipulation (6 Mar 2026) and Allstate settlement] |
| CA10 | Insured losses from the January 2025 Palisades and Eaton fires are estimated at $28–35bn. | [admit: Verisk PCS release, 22 Jan 2025] |
| CA11 | The FAIR Plan, the insurer of last resort, had 573,739 policies in March 2025, up 139% since September 2021. A $1bn assessment on member insurers was approved on 11 Feb 2025, the first since 1994. | [admit: Assembly Insurance Committee hearing, May 2025; CDI Order 2025-1] |
| CA12 | The Sustainable Insurance Strategy lets insurers price with catastrophe models and pass on reinsurance costs (rules finalised 13 and 30 Dec 2024), in exchange for writing at least 85% of their statewide market share in high-risk areas. | [admit: CDI release 065-2024] |
| CA13 | At the root, California extended cap-and-trade to 2045 as "cap-and-invest" (AB 1207, SB 840, signed 19 Sep 2025). | [admit: ICAP status report] |
| CA14 | Most legislative and regulatory effort since 2019 has gone to the symptom tier (utility liability funds, insurer rules, the FAIR Plan, suppression and thinning) rather than to the climate root. | [abstain: tier-floor: unearned confidence — an interpretive count, not a measured share of effort] |

**Correction.** "Forest-management legislation" did not cause the fuel load by itself. The fire deficit came from a century of suppression *practice*; the statutes reached here (HFRA 2003, AB 1054, SB 254) are responses.

#### 3.3 Chain (c): unstudied, unregulated social media → youth mental health, body image and behaviour

| # | Finding | Tag |
|---|---|---|
| SM1 | Australia's Online Safety Amendment (Social Media Minimum Age) Act 2024 passed on 29 Nov 2024. The under-16 account obligation applies from 10 Dec 2025, with penalties up to 150,000 penalty units (about A$49.5m). eSafety lists Facebook, Instagram, Threads, Snapchat, TikTok, X, YouTube, Reddit, Kick and Twitch as age-restricted. | [admit: Prime Minister's release on passage, 2024; eSafety Commissioner, "Which platforms are age-restricted", 21 Nov 2025] |
| SM2 | The US Surgeon General's advisory *Social Media and Youth Mental Health* (23 May 2023) says the evidence is insufficient to conclude social media is safe for adolescents. It does not assert that social media causes the mental-health trend. | [admit: HHS advisory and press release, 23 May 2023] |
| SM3 | The Surgeon General called for warning labels on social media in a newspaper op-ed of 17 Jun 2024. | [abstain: non-authoritative source — op-ed reached only through press reports] |
| SM4 | Phones in schools: England issued non-statutory guidance on 19 Feb 2024. In the US, 42 states plus DC and Puerto Rico had enacted school-phone laws by 15 Jul 2026. UNESCO's 2023 GEM report found that fewer than one in four countries banned phones in schools; by March 2026 its tracker counted 114 education systems (58%). | [admit: DfE guidance "Mobile phones in schools"; NCSL tracker; UNESCO GEM 2023 report and GEM tracker] |
| SM5 | EU: the Commission adopted non-binding guidelines on the protection of minors under DSA Article 28 on 14 Jul 2025. Proceedings against TikTok (opened Feb 2024) and Meta (opened May 2024) have produced preliminary findings on addictive design and minors in 2026, but no final decision or fine. UK: Ofcom's Protection of Children Codes under the Online Safety Act 2023 have applied since 25 Jul 2025. | [admit: European Commission digital-strategy and press releases; Ofcom statement "Protecting children from harms online"] |
| SM6 | Across three large datasets (n = 355,358), digital technology use explains at most 0.4% of the variance in adolescent well-being (specification-curve analysis, cross-sectional). | [admit: Orben & Przybylski 2019, Nat Hum Behav 3:173–182] |
| SM7 | Odgers' *Nature* review of Haidt's *The Anxious Generation* (2024) says the literature shows a mix of no, small and mixed associations, mostly correlational. It is a book review, not a systematic review. | [admit: Odgers 2024, Nature 628:29–30] |
| SM8 | Experimental evidence is mixed. A 2025 meta-analysis of 10 RCTs (N = 1,491, mostly adults) found reduced use lowered depression (g ≈ 0.28). Another 2025 meta-analysis of abstinence experiments found no effect on negative affect (g ≈ −0.01). | [admit: May et al. 2025, EJIHPE 15(11):222; Lemahieu et al. 2025, Sci Rep 15:7581] |
| SM9 | Social media *caused* the rise in adolescent depression and anxiety since about 2012. | [abstain: source-vs-prior conflict — Haidt 2024 vs Odgers 2024 and Orben & Przybylski 2019; experiments mixed (SM8)] |
| SM10 | Social media use correlates with body-image concern (63 samples, N = 36,552, r ≈ .16). | [admit: Saiphoo & Vahedi 2019, Comput Hum Behav 101:259–275] |
| SM11 | "Instagram makes 32% of teen girls feel worse about their bodies." Meta's internal March 2020 slide said this of teen girls *who already felt bad about their bodies*. It is an internal survey, not a population estimate. | [refute: internal slide as published in the WSJ "Facebook Files", 14 Sep 2021 — correction given] |
| SM12 | Social media causes clinical body dysmorphia. The studies measure body dissatisfaction, not body dysmorphic disorder. | [abstain: tier-floor: unearned confidence] |

**Reading.** Policy has gone to the link nearest the visible harm and the parents who bear it: age limits, phone bans, platform-design codes. The root, an unstudied product released at scale without independent research access, has been addressed only through the DSA's data-access and risk-assessment duties. Because the causal claim itself is contested (SM9), this chain is the weakest test of the model: a symptomatic response may also be the proportionate one.

#### 3.4 Chain (d): pharmaceutical and nutrition regulation gaps → obesity and metabolic disease → GLP-1 drugs vs food regulation

| # | Finding | Tag |
|---|---|---|
| OB1 | More than one billion people were living with obesity in 2022 (879m adults, 159m children and adolescents). | [admit: NCD-RisC 2024, Lancet 403:1027–50; WHO release 1 Mar 2024] |
| OB2 | US adult obesity prevalence was 40.3% in August 2021–August 2023; severe obesity 9.4%. | [admit: CDC NCHS Data Brief 508, Sep 2024] |
| OB3 | In an inpatient crossover trial (n = 20), an ultra-processed diet led to about 500 kcal/day more intake and about 0.9 kg weight gain in two weeks. The *Lancet* series on ultra-processed food (Nov 2025) argues for regulation; most of its evidence is observational and it is disputed. | [admit: Hall et al. 2019, Cell Metab 30:67–77; Monteiro et al. 2025, Lancet UPF series paper 1] |
| OB4 | US food-additive law lets firms self-affirm ingredients as "generally recognised as safe" (GRAS). An FDA proposed rule to end self-affirmation was published in August 2026. | [abstain: non-authoritative source — law-firm summaries; Federal Register notice not opened] |
| OB5 | The FDA approved semaglutide for weight management (Wegovy) on 4 Jun 2021 and tirzepatide (Zepbound) on 8 Nov 2023. In SELECT (n = 17,604), semaglutide cut major adverse cardiovascular events by 20% (HR 0.80). | [admit: Novo Nordisk and Lilly approval releases; Lincoff et al. 2023, NEJM 389:2221–32] |
| OB6 | A November 2025 agreement between the US administration and Novo Nordisk and Lilly set a Medicare/Medicaid price of about $245 a month and a $50 Medicare co-pay through a pilot. | [abstain: non-authoritative source — press reports; final pilot terms disputed in later reporting] |
| OB7 | The UK Soft Drinks Industry Levy took effect on 6 Apr 2018. The often-quoted reformulation figure of "35–46%" is outdated. Sugar per 100 ml in levy-liable drinks fell 47.4% over 2015–2024, and total sugar sold in them fell 39.8% while volume rose 13.5%. | [refute: OHID, "Sugar reduction in drinks 2015 to 2024" — use 47.4%] |
| OB8 | One year after the levy was implemented, obesity among Year 6 girls was 8% lower than the trend predicted (about 5,234 fewer cases a year). There was no effect for boys or reception-age children. The design is an observational interrupted time series. | [admit: Rogers et al. 2023, PLoS Med 20(1):e1004160] |
| OB9 | Mexico's 2014 soda tax was followed by a 6% average fall in taxed-beverage purchases in 2014 (12% by December), and larger falls in low-income households. | [admit: Colchero et al. 2016, BMJ 352:h6704] |
| OB10 | UK HFSS rules: restrictions on in-store placement took effect on 1 Oct 2022. A 9pm TV watershed and a ban on paid online advertising for less healthy food took legal effect on 5 Jan 2026, after voluntary compliance from 1 Oct 2025. | [admit: Advertising (Less Healthy Food Definitions and Exemptions) Regulations 2024; DHSC implementation guidance] |
| OB11 | The UK government said in July 2025 that it expects to repeal the volume-price (multibuy) restrictions. | [abstain: unverifiable — repeal status not confirmed] |
| OB12 | WHO recommends taxes that raise the retail price of sugary drinks by at least 20% (2016). Its "3 by 35" initiative (July 2025) calls for raising the real prices of tobacco, alcohol and sugary drinks by at least 50% by 2035. | [admit: WHO news release 11 Oct 2016; WHO "3 by 35" initiative page] |
| OB13 | GLP-1 drugs reduce political pressure for food regulation. Commentators raise the concern (e.g. *Lancet* regional journals, 2024–26), but no study shows the effect. | [abstain: unverifiable — concern asserted, effect not demonstrated] |

**Reading.** The pharmaceutical response is at the metabolic-disease link and is attributable, effective and profitable. The food-regulation response sits closer to the root, and where it has been tried it is modest but measurable (OB7–OB9). Whether the drug response crowds out the regulatory one is an open empirical question (P15).

---

### 4. Historical chains with resolved outcomes

| # | Finding | Tag |
|---|---|---|
| H1 | Children with higher dentine lead had lower IQ and worse classroom behaviour. | [admit: Needleman et al. 1979, NEJM 300:689–95] |
| H2 | Pooled analysis of seven cohorts (1,333 children) found IQ losses with no threshold, steepest at low blood-lead levels. | [admit: Lanphear et al. 2005, EHP 113:894–9] |
| H3 | Leaded petrol exposure cost Americans an estimated 824 million IQ points (as of 2015). This is a modelled estimate. | [admit: McFarland, Hauer & Reuben 2022, PNAS 119:e2118631119] |
| H4 | Lead removal caused a large share of the US crime decline. A meta-analysis (529 estimates, 24 studies) finds publication bias and near-zero effects in the best-identified studies. | [abstain: source-vs-prior conflict — Nevin 2000 and Reyes 2007 vs Higney, Hanley & Moro 2022, Reg Sci Urban Econ 97:103826] |
| H5 | EPA began phasing lead out of petrol in 1973 (0.1 g/gal from 1986) and banned it for on-road vehicles from 1 Jan 1996. Removal was at source, not at the harm link. | [admit: EPA archive release, "EPA Takes Final Step in Phaseout of Leaded Gasoline", 1996] |
| H6 | The Master Settlement Agreement (23 Nov 1998) settled the suits of 46 states and other jurisdictions with the four largest US cigarette makers, for about $206bn over the first 25 years, with payments continuing indefinitely. | [admit: GAO-01-851] |
| H7 | The state suits began with Mississippi's Medicaid cost-recovery suit (May 1994, Attorney General Mike Moore). Mississippi, Florida, Texas and Minnesota settled separately in 1997–98. | [admit: NEJM 2004, doi:10.1056/NEJMsr031421] |
| H8 | "States spend less than 3% of settlement money on tobacco control." The share depends on the year and on whether tobacco tax revenue is in the denominator: below 2% in FY2013, 3.4% of $21.7bn (settlement plus tax revenue) in FY2026. | [refute: Campaign for Tobacco-Free Kids, *Broken Promises to Our Children*, FY2013 and FY2026 — use "about 2–4%"] |
| H9 | "The Montreal Protocol prevents about 280 million US skin cancers." That is an older EPA figure. The 2020 EPA estimate is about 443 million skin cancers (11 million melanomas), 2.3 million deaths and 63 million cataracts for Americans born 1890–2100. | [refute: EPA, *Updating Ozone Calculations and Emissions Profiles for Use in the Atmospheric and Health Effects Framework Model*, 2020] |
| H10 | US policymakers framed ozone loss as a domestic skin-cancer harm. The Council of Economic Advisers' cost–benefit analysis found the skin-cancer benefits far outweighed compliance costs, and skin cancer was a highly salient harm that engaged officials and citizens. | [admit: Sunstein 2007, Harv Envtl L Rev 31:1] |

**Reading (Synthesis).** All three chains were resolved at the root, and in each a carrier changed who bore the cost. Tobacco's health costs became a state-budget cost that attorneys general could litigate. Ozone's distant harm became a quantified US skin-cancer toll. Lead's diffuse cognitive harm reached decision-makers through independent research and a technical forcing event (catalytic converters, App. B case 2). Doubt-manufacturing lengthened the tobacco and lead chains (App. B M15, B10) but did not create them.

---

### 5. Chain coding (Synthesis)

| Chain | Root | Downstream links (attributability) | Who bears the harm | Who holds the veto at the root | Carrier into the veto radius | Where response landed |
|---|---|---|---|---|---|---|
| (a) France | Structural deficit since 2008; pension and benefit commitments | Interest burden (H) → pressure on social budgets (M) → spreads, ratings and EU spill-over (M) | Future taxpayers, pensioners, euro-area partners | Pensioner and public-sector constituencies; a fragmented Assembly | Bond markets and rating agencies; EU deficit procedure; IMF | Governments (two fell); proposed social cuts withdrawn; root deficit largely unaddressed |
| (b) California | Emissions (global) and a century of suppression practice | Hotter, drier fire seasons (M) → fire severity (M) → utility liability (H) → insurance withdrawal (H) | Homeowners in high-risk areas; ratepayers; insurers | Global emitters; developers and local land-use authorities | Insurers and the FAIR Plan assessment; PG&E's creditors | Utility funds, insurer rules, FAIR Plan, suppression and thinning; cap-and-invest extended |
| (c) Social media | Product released at scale without independent study | Heavy adolescent use (H) → mental-health and body-image effects (L, contested) | Adolescents and parents | Platforms; their lobbying; free-speech constituencies | Foreign regulators (EU, UK, Australia); school systems | Age limits, phone bans, design codes |
| (d) Obesity | Food environment; permissive additive and marketing law | Diet (M) → obesity (M) → metabolic and cardiovascular disease (H) | Patients; health systems | Food and beverage industry; consumers' habits | Health budgets; drug makers (as a counter-lobby) | GLP-1 coverage at scale; narrow food rules (levies, HFSS) |
| Tobacco (resolved) | Cigarettes | Smoking (H) → disease (H, after 1964) → Medicaid costs (H) | Smokers; state budgets | Industry; tobacco-state legislators | State AGs and courts | MSA 1998 and later FCTC; marketing curbs at the root |
| Lead (resolved) | Leaded petrol | Exposure (L) → cognition (M after 1979) → crime (contested) | Children | Additive and oil industry | Independent research; converter compatibility | Removal at source, 1973–96 |
| CFCs (resolved) | CFC production | Ozone loss (M) → UV (M) → skin cancer (M) | Future populations, US citizens | Few producers | EPA/CEA skin-cancer valuation; ozone-hole images | Phase-out at the root, 1987–92 |

---

### 6. Literature

| # | Finding | Tag |
|---|---|---|
| L1 | Kahn (1966), "The tyranny of small decisions", *Kyklos* 19(1):23–47. A sequence of small, individually rational market choices can produce an outcome that consumers would have voted against. The example is the loss of Ithaca's passenger rail. | [admit: Wiley record and abstract, doi:10.1111/j.1467-6435.1966.tb02491.x] |
| L2 | Odum (1982), "Environmental degradation and the tyranny of small decisions", *BioScience* 32(9):728–729, applies Kahn's idea to incremental environmental loss. | [admit: text of the essay (hosted copy)] |
| L3 | Merton (1936), "The unanticipated consequences of purposive social action", *ASR* 1(6):894–904. Sources: ignorance, error, the "imperious immediacy of interest", basic values, and self-defeating predictions. | [admit: full text] |
| L4 | Schelling (1978), *Micromotives and Macrobehavior* (Norton): individual choices aggregate into macro patterns nobody chose. | [abstain: tier-floor: unearned confidence — not opened this session] |
| L5 | Pierson (1993), "When effect becomes cause: policy feedback and political change", *World Politics* 45(4):595–628. Policies feed back through resource/incentive effects and interpretive effects, on elites, groups and mass publics. | [admit: article text (hosted copies); IPPA conference paper giving page references] |
| L6 | Streeck & Thelen (eds.) (2005), *Beyond Continuity* (OUP): five modes of gradual change, including layering, defined as "active sponsorship of amendments, additions, or revisions" to existing institutions (p. 24). The term draws on Schickler (2001). | [admit: page-cited secondary reviews (van der Heijden; Maggetti 2014, IRAS 80(2))] |
| L7 | Teles (2013), "Kludgeocracy in America", *National Affairs* 17:97–114. Accumulated complexity raises compliance costs, sustains a "kludge industry" and hides what government costs. | [admit: nationalaffairs.com] |
| L8 | Wildavsky (1979), *Speaking Truth to Power*, ch. 3, "Policy as its own cause": as government grows, policy increasingly responds to the consequences of earlier policy. | [admit: Routledge contents; Taylor & Francis chapter record] |
| L9 | Illich, *Medical Nemesis* "(1976)": clinical, social and cultural iatrogenesis. The first edition is 1975 (Calder & Boyars); 1976 is the US edition and *Limits to Medicine*. | [refute: bibliographic record — date corrected to 1975] |
| L10 | Tainter (1988), *The Collapse of Complex Societies* (Cambridge UP): investment in complexity meets declining marginal returns. | [admit: excerpts of the text (Schumacher Center), as in B.2] |
| L11 | Perrow (1984), *Normal Accidents*: interactive complexity plus tight coupling makes accidents normal. | [abstain: tier-floor: unearned confidence — not opened] |
| L12 | Rittel & Webber (1973), "Dilemmas in a general theory of planning", *Policy Sciences* 4(2):155–169: ten properties of wicked problems. They treat social planning problems as *inherently* wicked. | [admit: text of the article] |
| L13 | Head & Alford (2015), *Administration & Society* 47(6):711–739: wickedness arises from complexity, diversity and uncertainty and is a matter of degree. | [admit: SAGE record, doi:10.1177/0095399713481601] |
| L14 | Peters (2017), *Policy and Society* 36(3):385–396, argues that wickedness is "constructed". **Correction:** Peters argues that the term is a fad and over-applied, and that most problems so labelled fail a strict test. He does not argue constructedness. | [refute: Peters 2017 abstract (OUP)] |
| L15 | Daviter (2019), *Public Policy and Administration* 34(1):62–83: problems "have come to be interpreted" as wicked. Wickedness here is an analytic framing, not something produced by policy. | [admit: SAGE full text] |
| L16 | Senge (1990), *The Fifth Discipline*: "shifting the burden". A symptomatic fix relieves the symptom, reliance on it grows, and capacity for the fundamental solution atrophies. | [abstain: non-authoritative source — reached through system-dynamics summaries quoting the book] |
| L17 | Olson (1982), *The Rise and Decline of Nations*: distributional coalitions accumulate in stable societies and slow growth. The claim that empirical tests are "mixed" is wrong. A review of more than 50 studies finds the thesis "generally, but certainly not universally, supported". A companion study finds only weak support for the coalition mechanism itself. | [refute: Heckelman 2007, Southern Econ J 74(1):18–33; Bischoff 2007, same issue] |
| L18 | Kaufman (1976), *Are Government Organizations Immortal?* (Brookings): about 85% of 175 federal organisations existing in 1923 still existed in 1973. | [admit: Brookings record and summaries] |
| L19 | Lewis (2002), *Journal of Politics* 64(1):89–107: "about 60%" of agencies created since 1946 were terminated. The figure is 62%, under a broad definition of termination; hazard rises with political turnover. | [refute: Lewis 2002 abstract — 62%] |
| L20 | Berry, Burden & Howell (2010), *AJPS* 54(1):1–17: of US domestic programmes 1971–2003, about 10% were eliminated within a decade; terminations follow partisan change. | [admit: AJPS record and authors' working paper (figures from the working paper)] |
| L21 | deLeon (1978), "Public policy termination: an end and a beginning", *Policy Analysis* 4(3):369–392: termination is rare and hard. Obstacles: psychological (intellectual) reluctance, institutional permanence, dynamic conservatism, anti-termination coalitions, legal obstacles, high start-up costs. | [admit: SFU thesis and 2026 *Policy & Society* review quoting the article] |
| L22 | Bardach (1976), "Policy termination as a political process", *Policy Sciences* 7(2):123–131. | [abstain: tier-floor: unearned confidence — not opened] |
| L23 | "Sunset laws had spread to 36 states by about 1980." The figure is 36 states by 1982; by 1990, 12 had stopped using them, citing cost, lobbying and unmet expectations of termination. Large agencies uniformly survived. | [refute: CRS RL34551 (2008), drawing on Kearney 1990, PAR 50(1):49–57 — date corrected] |
| L24 | Texas's Sunset Advisory Commission has reviewed 603 agencies and programmes since 1977, abolishing 42 (about 7%) and consolidating 54. | [admit: Sunset Advisory Commission, *Sunset in Texas*, 2025] |
| L25 | Baumgartner & Jones (1993), *Agendas and Instability in American Politics*: policy monopolies produce long stability broken by punctuations. | [abstain: tier-floor: unearned confidence — not re-opened; App. B M21–M22 admit the later empirical work] |
| L26 | The Tax Reform Act of 1986 (P.L. 99-514, signed 22 Oct 1986) was revenue-neutral, broadened the base and cut the top rate from 50% to 28%. | [admit: Tax Policy Center] |
| L27 | Its erosion was real but partial. The top rate rose to 31% (1990) and 39.6% (1993). Tax expenditures fell from about 9% of GDP (1985) to 6% (1988), then rose gradually but stayed below the 1985 level. | [admit: Tax Policy Center, *Trends in Tax Expenditures, 1985–2016*] |
| L28 | The Airline Deregulation Act was signed on 24 Oct 1978. The Civil Aeronautics Board was abolished with effect from 1 Jan 1985. | [admit: National Archives, Records of the CAB] |
| L29 | Derthick & Quirk (1985), *The Politics of Deregulation* (Brookings), attribute airline, trucking and telecoms deregulation chiefly to economists' ideas and expert advocacy, not to economic events or interest-group pressure. | [admit: Brookings description] |
| L30 | Late-1970s stagflation was the trigger for airline deregulation. | [abstain: source-vs-prior conflict — inflation politics gave consumer-price arguments salience, but Derthick & Quirk explain the reform by ideas; McDonnell 2015 disputes them] |
| L31 | The Office of Technology Assessment was created in 1972 (P.L. 92-484) and closed on 29 Sep 1995, when Congress cut its funding to closeout costs. Its authorising statute was never repealed. | [admit: CRS R46327] |
| L32 | IPCC AR6 WGII SPM B.5 says risks "will increasingly interact, creating compound and cascading risks that are more complex and difficult to manage". That wording is from the AR6 *Synthesis Report* headline statements, not WGII B.5. | [refute: IPCC WGII headline statements — wrong document] |
| L33 | WGII SPM B.5 says that multiple climatic and non-climatic risks will interact, producing compounding risk and risks cascading across sectors and regions, and that "some responses to climate change result in new impacts and risks" (*high confidence*). | [admit: IPCC AR6 WGII headline statements page] |
| L34 | WGII SPM C.4 reports increased evidence of maladaptation across sectors and regions since AR5. | [abstain: unverifiable — ipcc.ch returned an error; wording from memory] |
| L35 | Barnett & O'Neill (2010), "Maladaptation", *Global Environmental Change* 20(2):211–213: action taken to reduce vulnerability that increases the vulnerability of other systems, sectors or groups. Pathways include high opportunity costs and path dependence. | [admit: GEC editorial text] |
| L36 | Vaughan (1996), *The Challenger Launch Decision*: normalisation of deviance and "structural secrecy" across organisational units. | [abstain: tier-floor: unearned confidence — not opened] |
| L37 | Tett (2015), *The Silo Effect* (Simon & Schuster): organisational silos hide risks that cross units. | [abstain: tier-floor: unearned confidence — not opened] |
| L38 | The 9/11 Commission Report (2004) says that without integrated all-source analysis "it is not possible to 'connect the dots'" (ch. 13, p. 408), and recommends a National Counterterrorism Center. | [admit: House Science Committee letter citing the page; report chapter not opened directly] |
| L39 | Adam, Hurka, Knill & Steinebach (2019), *Policy Accumulation and the Democratic Responsiveness Trap* (CUP): democratic responsiveness adds policies faster than old ones are removed. Environmental policy stocks roughly quadrupled and social policy stocks doubled from the 1980s to the 2010s, overloading implementation. | [admit: CUP record and published introduction, doi:10.1017/9781108646888] |
| L40 | Howlett & Rayner (2009), *Policy and Society* 28(2): repeated layering yields incoherent, counter-productive policy mixes that are difficult to change. | [admit: article PDF] |
| L41 | Wiener (2003), "Managing the iatrogenic risks of risk management" (OMB report): regulations create countervailing risks. | [admit: OMB 2003 report text] |
| L42 | Bauer, Jordan, Green-Pedersen & Héritier (eds.) (2012), *Dismantling Public Policy* (OUP): dismantling, including dismantling "by default" through non-indexation, is more common than the immortality view suggests. | [admit: OUP record] |

---

### 7. Novelty check

| # | Finding | Tag |
|---|---|---|
| N1 | Searches for "iatrogenic wickedness", "accreted wickedness", "manufactured wickedness", "policy-induced wicked problems", "self-inflicted wicked problems", "policy iatrogenesis", "policy sediment" and "policy cumulation" found no established use. | [abstain: unverifiable — negative web search, not a full database crawl] |
| N2 | The nearest work, by component: accumulation without termination (Adam et al. 2019, L39); incoherent layering (Howlett & Rayner 2009, L40); constituencies created by policy (Pierson 1993, L5); policy reacting to its own consequences (Wildavsky 1979, L8); iatrogenic regulation (Wiener 2003, L41); maladaptation (Barnett & O'Neill 2010, L35); framed wickedness (Daviter 2019, L15). None combines root-cause neglect, symptomatic layering, beneficiaries joining the veto, and a transition from tractable to wicked. | **Synthesis** from L5, L8, L15, L35, L39–L41 |

---

### 8. Base rate: comprehensive unwinding without a crisis

| Study | Unit | Finding | Conditions on crisis? |
|---|---|---|---|
| Kaufman 1976 (L18) | 175 federal organisations, 1923–73 | 15% gone in 50 years | No |
| Lewis 2002 (L19) | Agencies created 1946–97 | 62% terminated (broad definition, includes reorganisations) | No; driven by political turnover |
| Berry, Burden & Howell 2010 (L20) | US domestic programmes 1971–2003 | About 10% eliminated within a decade | No; driven by partisan change |
| Texas Sunset 1977–2025 (L24) | 603 reviews | 7% abolished, 9% consolidated | No |
| State sunset laws (L23) | 36 states | 12 stopped using them by 1990; large agencies survived | No |
| Adam et al. 2019 (L39) | OECD policy stocks | Additions far exceed removals | No |

**Finding.** These studies measure the death of single units. None measures how often an accumulated policy complex is unwound *comprehensively*, and none conditions on crisis. The canonical non-crisis cases (1986 tax reform; late-1970s deregulation) are case studies, and the 1986 reform was partly re-eroded. The base rate of comprehensive non-crisis unwinding is therefore unknown. [abstain: unverifiable — no dataset located]

---

### 9. Implications for the model (Synthesis; adopted in Part G)

1. **Attribution decays multiplicatively along the chain.** If a_j is the attributability of link j, the perceived harm of the root at link k is roughly φ_k ≈ φ_0 · ∏_{j≤k} a_j. Contested links (social media → body image, lead → crime) push the product toward zero.
2. **Response lands at the lowest-veto attributable link.** Downstream cost-bearers hold no veto in the originating domain. Policy goes to the link where attributed harm clears a threshold and the veto is smallest.
3. **Symptomatic relief lowers root pressure.** This is Senge's "shifting the burden" at policy scale: relief at link k reduces the harm felt at the root.
4. **Carriers bring the harm into the veto radius.** Creditors, insurers, courts and partner states raise H_elite for the root veto holders. This is the mechanism by which B.4.1's V(H_elite) falls in chains.
5. **Each symptomatic layer creates beneficiaries who join the root veto.** This combines Pierson's feedback with Adam et al.'s accumulation. As layers and veto groups multiply, the space for a bundled loss-sharing bargain shrinks, which is consistent with Olson's sclerosis thesis (generally supported, L17) and Tainter's declining returns (L10).
6. **Cross-domain interception is institutionally fragile.** The OTA was defunded (L31). Silos and structural secrecy (L36–L38) hide chains that cross mandates. Early interceptions leave no record, so the claim is "rarely caught early, and successes go unseen", not "never".

---

### 10. References

- Abatzoglou, J. T. & Williams, A. P. (2016). Impact of anthropogenic climate change on wildfire across western US forests. *PNAS* 113(42):11770–75. doi:10.1073/pnas.1607171113
- Adam, C., Hurka, S., Knill, C. & Steinebach, Y. (2019). *Policy Accumulation and the Democratic Responsiveness Trap.* Cambridge UP. doi:10.1017/9781108646888
- Barnett, J. & O'Neill, S. (2010). Maladaptation. *Global Environmental Change* 20(2):211–213. doi:10.1016/j.gloenvcha.2009.11.004
- Berry, C. R., Burden, B. C. & Howell, W. G. (2010). After enactment: the lives and deaths of federal programs. *AJPS* 54(1):1–17. doi:10.1111/j.1540-5907.2009.00414.x
- Colchero, M. A. et al. (2016). Beverage purchases from stores in Mexico under the excise tax on sugar sweetened beverages. *BMJ* 352:h6704.
- Daviter, F. (2019). Policy analysis in the face of complexity: what kind of knowledge to tackle wicked problems? *Public Policy and Administration* 34(1):62–83. doi:10.1177/0952076717733325
- deLeon, P. (1978). Public policy termination: an end and a beginning. *Policy Analysis* 4(3):369–392.
- Derthick, M. & Quirk, P. J. (1985). *The Politics of Deregulation.* Brookings.
- Hagmann, R. K. et al. (2021). Evidence for widespread changes in the structure, composition, and fire regimes of western North American forests. *Ecological Applications* 31(8):e02431.
- Head, B. W. & Alford, J. (2015). Wicked problems: implications for public policy and management. *Administration & Society* 47(6):711–739.
- Heckelman, J. C. (2007). Explaining the rain: *The Rise and Decline of Nations* after 25 years. *Southern Economic Journal* 74(1):18–33.
- Higney, A., Hanley, N. & Moro, M. (2022). The lead–crime hypothesis: a meta-analysis. *Regional Science and Urban Economics* 97:103826.
- Howlett, M. & Rayner, J. (2009). Patching vs packaging in policy formulation. *Policy and Society* 28(2):99–109.
- Kahn, A. E. (1966). The tyranny of small decisions. *Kyklos* 19(1):23–47.
- Kaufman, H. (1976). *Are Government Organizations Immortal?* Brookings.
- Kearney, R. C. (1990). Sunset: a survey and analysis of the state experience. *PAR* 50(1):49–57.
- Lewis, D. E. (2002). The politics of agency termination. *Journal of Politics* 64(1):89–107.
- Lincoff, A. M. et al. (2023). Semaglutide and cardiovascular outcomes in obesity without diabetes. *NEJM* 389:2221–32. doi:10.1056/NEJMoa2307563
- McFarland, M. J., Hauer, M. E. & Reuben, A. (2022). Half of US population exposed to adverse lead levels in early childhood. *PNAS* 119(11):e2118631119.
- Merton, R. K. (1936). The unanticipated consequences of purposive social action. *ASR* 1(6):894–904.
- NCD Risk Factor Collaboration (2024). Worldwide trends in underweight and obesity. *Lancet* 403:1027–50. doi:10.1016/S0140-6736(23)02750-2
- Odgers, C. L. (2024). The great rewiring: is social media really behind an epidemic of teenage mental illness? *Nature* 628:29–30.
- Orben, A. & Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. *Nat Hum Behav* 3:173–182. doi:10.1038/s41562-018-0506-1
- Peters, B. G. (2017). What is so wicked about wicked problems? *Policy and Society* 36(3):385–396. doi:10.1080/14494035.2017.1361633
- Pierson, P. (1993). When effect becomes cause: policy feedback and political change. *World Politics* 45(4):595–628. doi:10.2307/2950710
- Rittel, H. W. J. & Webber, M. M. (1973). Dilemmas in a general theory of planning. *Policy Sciences* 4(2):155–169. doi:10.1007/BF01405730
- Rogers, N. T. et al. (2023). Associations between trajectories of obesity prevalence in English primary school children and the UK soft drinks industry levy. *PLoS Med* 20(1):e1004160.
- Streeck, W. & Thelen, K. (eds.) (2005). *Beyond Continuity.* Oxford UP.
- Teles, S. M. (2013). Kludgeocracy in America. *National Affairs* 17:97–114.
- Wiener, J. B. (2003). Managing the iatrogenic risks of risk management. In OMB, *Informing Regulatory Decisions: 2003 Report to Congress*.
- Wildavsky, A. (1979). *Speaking Truth to Power.* Little, Brown. Ch. 3, "Policy as its own cause".
- Williams, A. P. et al. (2019). Observed impacts of anthropogenic climate change on wildfire in California. *Earth's Future* 7:892–910.
- Primary records: INSEE (2026); Agence France Trésor ratings page; Council Decision (EU) 2024/2122; IMF Euro Area Article IV (2026); CPUC and California Department of Insurance orders; Online Safety Amendment (Social Media Minimum Age) Act 2024 (Cth); HHS (2023); Ofcom (2025); OHID (2025); GAO-01-851; EPA (1996, 2020); CRS RL34551 and R46327; Texas Sunset Advisory Commission (2025); IPCC AR6 WGII (2022).

---

### 11. Disposition ledger

Counted by bracketed tag occurrences in Sections 3–8, excluding the legend examples in the header. Synthesis passages (Sections 4 reading, 5, 7 N2, 9) are excluded. Findings re-cited from the main body or Appendices A and B are not counted again.

| Disposition | Count |
|---|---|
| `admit` | 66 |
| `refute` | 10 |
| `abstain` | 27 |
| of which `non-authoritative source` | 9 |
| of which `tier-floor: unearned confidence` | 8 |
| of which `unverifiable` | 7 |
| of which `source-vs-prior conflict` | 3 |
| **Total tagged findings** | **103** |

**Refutations, with corrections:**
1. "32% of teen girls" feel worse about their bodies because of Instagram. The figure applies to teen girls who already felt bad about their bodies (SM11).
2. Soft drinks levy reformulation of "35–46%". The latest figure is 47.4% (2015–2024) (OB7).
3. "Under 3% of tobacco settlement money goes to tobacco control." The share is about 2–4% depending on the year and denominator (H8).
4. "280 million US skin cancers avoided." EPA's 2020 estimate is about 443 million (H9).
5. Illich's *Medical Nemesis* "1976". First edition 1975 (L9).
6. Peters (2017) argues wickedness is "constructed". He argues the label is over-applied; the constructedness argument is Daviter (2019) (L14).
7. Olson (1982) "empirical tests are mixed". The thesis is "generally, but certainly not universally, supported"; the coalition mechanism itself has weak support (L17).
8. Lewis (2002) "about 60%". The figure is 62% (L19).
9. Sunset laws in 36 states "by about 1980". By 1982 (L23).
10. IPCC wording attributed to WGII SPM B.5. It is from the AR6 Synthesis Report; B.5 itself adds that some responses create new risks (L32–L33).

**Corrections carried by abstain-tagged findings (not counted as refutations):**
- The claim that budget pressure *cut* French social spending holds for the proposals that brought governments down, not for the enacted 2026 social security budget, which raised ONDAM by 3.1% and suspended the pension reform (FR10).
- Forest-management *statutes* did not create California's fuel load; a century of suppression practice did. The statutes reached here are responses (CA3–CA5).
- No study demonstrates that GLP-1 drugs have reduced pressure for food regulation; the concern is asserted only (OB13).

**Open gaps:**
- No dataset measures comprehensive policy unwinding, with or without a crisis (Section 8).
- The social-media causal question is unresolved (SM9).
- Schelling, Perrow, Bardach, Baumgartner & Jones 1993, Vaughan and Tett were not opened this session.

---

## Appendix D: Causal AI, automation and black-boxing: verification and ANT lineage

**Researched:** 2026-10-11
**Question.** Could causal models, causal discovery and digital twins break the trap of accreted wickedness described in Part G? Which of their limits are ceilings and which are governance risks? Does their success carry a cost of its own, and how does that cost read in the lineage of actor-network theory?
**Model terms** (φ, H, L^R, r̂, V, M, carriers, accreted layers) are as defined in B.4, B.4.1 and Part G. Findings already tagged in the main body or Appendices A–C are cited here but not re-tagged or re-counted.
**Terms of art.** "Causal model", "causal discovery" and "causal AI" name a model class. They carry no ontological commitment to causes as things; the position taken is relational (H.4 point 8).
**Method.** For each claim I first tried to refute it against a primary or authoritative source, then tagged it:
- `[admit: source]`: confirmed this session in an authoritative source, and the refutation attempt failed.
- `[refute: source]`: an authoritative source contradicts the claim. The correction is given.
- `[abstain: reason]`: reason is one of *unverifiable*, *source-vs-prior conflict*, *non-authoritative source*, or *tier-floor: unearned confidence*.

Text marked **Synthesis** is my own inference from tagged findings. It is not a sourced claim and is not counted in the ledger. The mapping table in Section 7 is Synthesis. Where a classic text was reached only through quotations in scholarly secondary sources that agree on wording and page, it is admitted and the route is named.

---

### 1. Summary verdict

1. **Causal AI addresses part of accreted wickedness.** It can slow attribution decay along chains, do some of the work of a spanning mandate, and act as standing institutional memory. Attribution tools already create carriers: extreme-event attribution has opened legal standing in principle (*Lliuya v RWE*, 2025), and pharmacovigilance detects drug-safety signals routinely. But no attribution has yet carried a climate damages award, and where harm is delayed and incumbent benefit large, detection is rarely the bottleneck: rofecoxib's signal preceded its withdrawal by four years.
2. **Two limits are ceilings.** Observational data cannot settle interventional questions without assumptions or interventions (the causal hierarchy theorem). Retraining on a world the model's outputs have shaped converges to performatively stable points that "need not be" optimal (Perdomo et al. 2020). The other limits (partisan filtering, capture, binding vetoes, data silos) are governance risks.
3. **Success has an intrinsic cost.** Explicit graphs become opaque by scale; updating to fix drift removes the stable referent that tracing needs; and the human capacity to trace atrophies (Bainbridge 1983; Parasuraman & Manzey 2010; AF447; Budzyń et al. 2025). The drift–traceability trade-off has precedents in machine-learning engineering (Sculley et al. 2015). The composite, in which the model becomes the most complete accreted layer and its operators the obligatory passage point, was not found in the literature. That is an absence-of-evidence judgement.
4. **The ANT lineage is direct.** Latour defines blackboxing as technical work "made invisible by its own success" (1999). Law's punctualisation, Callon's obligatory passage point and irreversibility, Latour's centres of calculation, delegation and mediators, Star's infrastructure, and Callon and MacKenzie's performativity each map onto a step of the argument. ANT also fixes the report's ontology: V, L^R, the trust radius and M are punctualised network effects, and carriers are the actants that reopen them.
5. **Corrections that change the argument.** Manual flying is encouraged, not mandated, and its uptake was never measured (FAA SAFO 13002; DOT OIG 2016). Attribution has not yet enabled successful climate litigation, only standing in principle. Frontier practice is periodic, versioned retraining, not continuous updating. The ML–ANT bridge between performative prediction and Barnesian performativity is already drawn by the ML authors themselves. Latourian purification refers to the separation of human and non-human zones; applying it to cause and effect is an analogy.

---

### 2. Causal modelling

| # | Finding | Tag |
|---|---|---|
| CM1 | Pearl's ladder (seeing, doing, imagining) formalised as the Pearl Causal Hierarchy. The causal hierarchy theorem: "The PCH almost never collapses"; for almost any SCM the layers remain distinct, so data at one layer virtually always underdetermines higher layers. Inference across layers needs causal assumptions. | [admit: Bareinboim, Correa, Ibeling & Icard 2022, in Geffner, Dechter & Halpern (eds.), *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books, pp. 507–556; technical report R-60] |
| CM2 | PC and FCI (Spirtes, Glymour & Scheines, *Causation, Prediction, and Search*). FCI allows hidden common causes and outputs a partial ancestral graph representing an equivalence class of models the data cannot distinguish; some edge marks leave direction or confounding open. | [admit: CCD (Pittsburgh) GFCI technical documentation; Mooij & Claassen 2020, arXiv:2005.00610] |
| CM3 | NOTEARS recasts DAG structure learning as continuous optimisation with a smooth, exact characterisation of acyclicity, because the DAG search space "scales superexponentially with the number of nodes". | [admit: Zheng, Aragam, Ravikumar & Xing 2018, NeurIPS; arXiv:1803.01422] |
| CM4 | Causal representation learning: Schölkopf et al. review causal inference and relate it to open problems in machine learning, including transfer and generalisation. *Proc. IEEE* 109(5):612–634. | [admit: Schölkopf, Locatello et al. 2021, doi:10.1109/JPROC.2021.3058954] |
| CM5 | LLMs may be "causal parrots": they sometimes answer causal questions correctly because they have seen correlations between causal facts in text; the authors find current LLMs are at best weak causal parrots. | [admit: Zečević, Willig, Dhami & Kersting 2023, TMLR (08/2023), openreview tv46tCzs83] |
| CM6 | Acyclic SCMs (recursive SEMs) are the well-studied subclass. "In the presence of cycles, many of the convenient properties of acyclic SCMs do not hold in general": no guaranteed solution, non-unique observational, interventional and counterfactual distributions, no guaranteed marginalisation or Markov property, and graphs not always consistent with causal semantics. A class of "simple SCMs" extends acyclic SCMs to cycles while preserving many of those properties. | [admit: Bongers, Forré, Peters & Mooij 2021, *Ann. Statist.* 49(5):2885–2915, abstract] |
| CM7 | Performative prediction: predictions that support decisions influence their target. Retraining converges, under conditions, to a performatively stable point of nearly minimal loss. "Performatively stable classifiers need not be performatively optimal." | [admit: Perdomo, Zrnic, Mendler-Dünner & Hardt 2020, ICML, PMLR 119:7599–7609, text] |
| CM8 | The originators link performative prediction to the sociology of performativity, noting that in MacKenzie's case "it is the practice of applying economic theory... and not the model's predictions per se that are performative". | [admit: Hardt & Mendler-Dünner 2023, "Performative prediction: past and future", arXiv:2310.16608] |
| CM9 | Destination Earth: Contribution Agreements signed 15 Dec 2021; implementation from Jan 2022 by ECMWF (digital twins), ESA (platform) and EUMETSAT (data lake); launched 10 Jun 2024 with the Extremes and Climate Adaptation twins; a "full" Earth-system twin targeted for 2030. | [admit: European Commission digital-strategy page; ECMWF DestinE news releases] |
| CM10 | "Frontier labs update model weights continuously." **Correction:** current practice is periodic retraining with versioned releases; continual learning in deployment is argued for but not standard, and the training–deployment separation is described as an auditability and governance boundary. | [abstain: non-authoritative source — a16z, "Why We Need Continual Learning" (2026); no lab documentation reached] |

**Synthesis.** Destination Earth is a mechanistic simulation, not a causal-discovery system. It belongs with causal AI only as a model built to answer interventional ("what if") questions.

---

### 3. Attribution and signal detection as carriers

| # | Finding | Tag |
|---|---|---|
| AT1 | World Weather Attribution was formed in 2014 by Friederike Otto and Geert Jan van Oldenborgh (with Climate Central); it has completed more than 100 rapid studies under an eight-step protocol published in 2020. | [admit: WWA FAQ; Imperial College WWA page; Philip et al. 2020, *ASCMO* 6:177] |
| AT2 | WWA's rapid studies are released before peer review; the methods are peer-reviewed. | [abstain: non-authoritative source — Science Media Centre view reached via an advocacy site] |
| AT3 | In 73 climate lawsuits across 14 jurisdictions, "the evidence submitted and referenced... lags considerably behind the state of the art in climate science, impeding causation claims". | [admit: Stuart-Smith, Otto et al. 2021, *Nat Clim Change* 11:651–655] |
| AT4 | *Lliuya v RWE*, OLG Hamm, 28 May 2025 (5 U 15/17): claim dismissed because the flood risk to the property was put at about 1% over 30 years; the court held that major emitters can in principle be liable under §1004 BGB in proportion to their share of emissions. The court did not assess attribution science, because the claim failed at the prior question of imminent interference. | [admit: court press release as analysed by C2LI/Lexxion and Loyens & Loeff; RWE release of 28 May 2025] |
| AT5 | "Attribution science is used in insurance pricing." **Correction:** insurers price with catastrophe models (App. C CA12); no source showed event-attribution results entering premiums. | [abstain: unverifiable — no insurer or regulator source reached] |
| AT6 | Pharmacovigilance signal detection: the proportional reporting ratio (Evans, Waller & Davis 2001, *Pharmacoepidemiol Drug Saf* 10:483–486; 481 signals for 15 new drugs, 1996–98) and the Bayesian confidence propagation neural network (Bate et al. 1998, *Eur J Clin Pharmacol* 54:315–321), in routine use on the WHO database at Uppsala since 1998. | [admit: Wiley record (Evans et al.); Bate et al. 1998; Bate 2007, *Drug Safety* 30(7)] |
| AT7 | Rofecoxib: VIGOR (2000) showed excess myocardial infarction, attributed to naproxen cardioprotection; labelling changed April 2002; Merck withdrew the drug on 30 Sep 2004 after APPROVe (3.5% vs 1.9% MI or stroke), after more than 80 million patients. A cumulative meta-analysis concluded it should have been withdrawn several years earlier. | [admit: Topol 2004, *NEJM* 351:1707–09; Jüni et al. 2004, *Lancet* 364:2021–29] |
| AT8 | "Extreme-event attribution has enabled climate litigation." **Correction:** it has supported recognition of liability in principle (AT4) but has not yet carried a damages award, and courts have largely not engaged with state-of-the-art attribution (AT3). | [refute: Stuart-Smith et al. 2021; OLG Hamm 2025 as in AT4] |

---

### 4. Automation, deskilling and opacity

| # | Finding | Tag |
|---|---|---|
| AU1 | Bainbridge, "Ironies of automation" (*Automatica* 19(6):775–779, 1983): physical skills "deteriorate when they are not used", so "a formerly experienced operator who has been monitoring an automated process may now be an inexperienced one" (p. 775); monitoring is a task with "no opportunity to acquire or maintain" the needed qualities (p. 776). | [admit: scan of the original; quoted with page in *AI & Society* 2021, doi:10.1007/s00146-021-01320-y] |
| AU2 | Automation complacency occurs under multiple-task load, in naive and expert participants, and cannot be overcome by simple practice; automation bias produces omission and commission errors and cannot be prevented by training or instructions. *Human Factors* 52(3):381–410. | [admit: Parasuraman & Manzey 2010, doi:10.1177/0018720810376055, abstract and full text (TU Berlin repository)] |
| AU3 | AF447 (1 Jun 2009): BEA final report of 5 Jul 2012. Causes include the absence of high-altitude training in manual airplane handling and in the unreliable-airspeed procedure; the BEA recommended that EASA make mandatory "specific and regular exercises dedicated to manual aircraft handling of approach to stall and stall recovery, including at high altitude". | [admit: BEA final report as quoted by NASA Safety Message (31 Jul 2012) and FlightGlobal] |
| AU4 | The BEA described the crew's state as a "total loss of cognitive control of the situation". | [abstain: unverifiable — phrase not located in the sources reached] |
| AU5 | FAA SAFO 13002, *Manual Flight Operations* (4 Jan 2013): "encourages operators to promote manual flight operations when appropriate", because continuous use of autoflight "could lead to degradation of the pilot's ability to quickly recover the aircraft from an undesired state". Updated by SAFO 17007 (2017). | [admit: FAA SAFO 13002 and SAFO 17007 texts] |
| AU6 | "Pilots are required to keep up manual flying hours." **Correction:** US guidance is advisory, and a DOT Inspector General audit (January 2016) found the FAA "has not determined whether air carriers have increased manual flying opportunities" as a result. | [refute: FAA SAFO 13002; DOT OIG, *Enhanced FAA Oversight Could Reduce Hazards Associated With Increased Use of Flight Deck Automation*, Jan 2016] |
| AU7 | Budzyń et al. 2025, *Lancet Gastroenterol Hepatol* 10(10):896–903 (ACCEPT trial centres, four in Poland): adenoma detection rate in standard non-AI colonoscopy fell from 28.4% (226/795) in the three months before AI introduction to 22.4% (145/648) in the three months after (absolute −6.0 points, p = 0.0089); ADR with AI was 25.3% (186/734); AI exposure OR 0.69 (95% CI 0.53–0.89). An erratum was published (10(11):e12); its content was not reached, and the figures are as in the indexed abstract. | [admit: PubMed 40816301 abstract; doi:10.1016/S2468-1253(25)00133-5] |
| AU8 | AI exposure *caused* endoscopist deskilling. The authors call the study non-confirmatory and hypothesis-generating; the design is an observational before-and-after comparison, and correspondence disputing it was published in Dec 2025. | [abstain: tier-floor: unearned confidence] |
| AU9 | Hardwig, "Epistemic dependence" (*J Philos* 82(7):335–349, 1985): one can rationally believe a proposition on good reasons to believe that experts have good reasons; experts also depend on one another; the paper ends with a worry about autonomy and democracy. | [admit: JSTOR 2026523; PhilPapers record] |
| AU10 | Burrell (2016), *Big Data & Society* 3(1): three forms of opacity, "intentional corporate or state secrecy", "technical illiteracy", and opacity arising from "the characteristics of machine learning algorithms and the scale required to apply them usefully". | [admit: Burrell 2016 abstract, doi:10.1177/2053951715622512] |
| AU11 | Pasquale (2015), *The Black Box Society* (Harvard UP): opaque algorithms in search, finance and reputation; the contemporary world "more closely resembles a one-way mirror". | [admit: Harvard UP edition; text excerpt of ch. 1] |
| AU12 | Elish (2019), "Moral crumple zones", *Engaging Science, Technology, and Society* 5:40–60: responsibility is misattributed to a human operator with limited control over an automated system; cases include Three Mile Island and AF447. | [admit: ESTS article, doi:10.17351/ests2019.260] |
| AU13 | Messeri & Crockett (2024), *Nature* 627:49–58: AI tools can produce "illusions of understanding" and scientific monocultures; science may "produce more but understand less". | [admit: Nature Perspective, doi:10.1038/s41586-024-07146-0] |
| AU14 | Rudin (2019), *Nat Mach Intell* 1:206–215: for high-stakes decisions, use inherently interpretable models rather than explaining black boxes. | [admit: doi:10.1038/s42256-019-0048-x] |
| AU15 | Sculley et al. (2015), "Hidden technical debt in machine learning systems", NeurIPS 28:2503–2511: entanglement means "Changing Anything Changes Everything" (CACE); hidden feedback loops and undeclared consumers create "visibility debt". | [admit: NeurIPS paper text] |
| AU16 | EU AI Act (Regulation (EU) 2024/1689): high-risk systems "shall technically allow for the automatic recording of events ('logs')" (Art. 12); overseers must remain aware of "automation bias" and be able to disregard, override or reverse outputs (Art. 14(4)). | [admit: regulation text as reproduced on artificial-intelligence-act.com; "'Human oversight' in the EU AI Act: what, when and by whom?", *Law, Innovation and Technology* (2023), doi:10.1080/17579961.2023.2245683] |
| AU17 | A continuously updating model "is a moving target that can't be versioned, regression-tested, or certified once". | [abstain: non-authoritative source — a16z essay] |

---

### 5. ANT lineage

| # | Finding | Tag |
|---|---|---|
| ANT1 | Latour, *Science in Action* (Harvard UP, 1987), Introduction: "black box" is a cyberneticians' term for a device too complex to describe, replaced by a box "about which they need to know nothing but its input and output" (pp. 2–3). | [admit: text excerpt; page-cited in *J Sustainable Development* (CCSE) and an ELTE course glossary] |
| ANT2 | Latour, *Pandora's Hope* (Harvard UP, 1999), glossary, p. 304: blackboxing is "the way scientific and technical work is made invisible by its own success"; "the more science and technology succeed, the more opaque and obscure they become". | [admit: glossary as quoted consistently, with page, in several scholarly sources; page not checked against the book] |
| ANT3 | *Science in Action* ch. 6, "Centres of calculation": networks make distant entities mobile, stable and combinable (immutable mobiles, p. 223); "theory" is the crossroads that lets centres "mobilise, manipulate, combine, rewrite and tie together" traces (pp. 241–242). | [admit: Bennett, *Society and Space* essay (p. 223); ELTE course glossary (pp. 241–242)] |
| ANT4 | Callon & Latour (1981), "Unscrewing the big Leviathan", in Knorr Cetina & Cicourel (eds.), *Advances in Social Theory and Methodology*, pp. 277–303: "An actor grows with the number of relations he or she can put... in black boxes"; "A black box contains that which no longer needs to be reconsidered" (pp. 284–285); black boxes never remain fully closed; macro-actors are not larger in kind than micro-actors. | [admit: text (bruno-latour.fr PDF) as quoted with pages] |
| ANT5 | Latour, "The powers of association", in Law (ed.), *Power, Action and Belief*, pp. 264–280: power "is not something one can possess"; it "must be treated as a consequence rather than as a cause of action" (p. 264); "power" summarises the consequence of collective action but cannot explain what holds it in place (p. 265). | [admit: Sociological Review Monograph text; Aston University paper quoting pp. 265–266] |
| ANT6 | Law (1992), "Notes on the theory of the actor-network", *Systems Practice* 5(4):379–393: "the appearance of unity, and the disappearance of network, has to do with simplification"; widely performed networks are those that can be punctualised; punctualised resources let actors draw on networks without dealing with their complexity (p. 385). | [admit: Law's text (heterogeneities.net); Springer record] |
| ANT7 | Callon (1986), "Some elements of a sociology of translation", in Law (ed.), *Power, Action and Belief*, pp. 196–233: four moments (problematisation, with the researchers' programme as "obligatory passage point"; interessement; enrolment; mobilisation); three principles (agnosticism, generalised symmetry, free association); dissidence, as larvae fail to anchor and fishermen fish the stock, puts "representivity" in question (p. 225). | [admit: Wiley record and abstract; text (Charles University course copy)] |
| ANT8 | Callon, "Techno-economic networks and irreversibility", in Law (ed.), *A Sociology of Monsters*, pp. 132–161: how heterogeneous networks converge and how some links "achieve longevity and tend to shape future processes of translation". | [admit: Wiley abstract, doi:10.1111/j.1467-954X.1990.tb03351.x] |
| ANT9 | Callon's irreversibility has two aspects: the network cannot return to a point where other translations were possible, and it shapes subsequent translations. | [abstain: non-authoritative source — reading summary only; the relevant pages were not reached] |
| ANT10 | Dates of the Sociological Review Monographs: Wiley dates *Power, Action and Belief* (Callon; Latour) to May 1984, while the Routledge book is cited as 1986; *A Sociology of Monsters* is dated 1990 by Wiley and 1991 as the Routledge book. The report cites the conventional book years. | [abstain: source-vs-prior conflict — Wiley records vs Routledge editions] |
| ANT11 | Akrich (1992), "The de-scription of technical objects", in Bijker & Law (eds.), *Shaping Technology/Building Society* (MIT Press), pp. 205–224: designers inscribe a world into an object; analysis moves between the world inscribed and the world described by its displacement. | [admit: MIT Press table of contents; Springer and Elgar reference works] |
| ANT12 | Akrich: as objects become indispensable, they "have to efface themselves". | [abstain: non-authoritative source — reading notes only] |
| ANT13 | Latour (1992), "Where are the missing masses?", same volume, pp. 225–258: delegation of the door's work to a non-human "groom", which "prescrib[es] back" what sort of people may pass. Earlier version published as Jim Johnson (1988), "Mixing humans and nonhumans together: the sociology of a door-closer", *Social Problems* 35(3). | [admit: text (bruno-latour.fr; Open University PDF); doi:10.2307/800624] |
| ANT14 | Latour (2005), *Reassembling the Social* (OUP), p. 39: an intermediary "transports meaning or force without transformation"; "Mediators transform, translate, distort, and modify the meaning or the elements they are supposed to carry". | [admit: text as quoted with page in *J Cultural Economy* 2024, doi:10.1080/17530350.2024.2360919] |
| ANT15 | Latour (2005) rejects "critical sociology" that replaces actors' accounts with social explanations and treats their objections as proof; actors are "much more than mere informants"; no "social force" is available to explain residual features. | [admit: text of *Reassembling the Social*; Aston University paper on Latour and critique] |
| ANT16 | Latour, *We Have Never Been Modern* (Harvard UP, 1993), pp. 10–11: "modern" names two sets of practices, translation, which creates hybrids of nature and culture, and purification, which "creates two entirely distinct ontological zones", human and non-human. | [admit: text (Harvard UP edition, Monoskop copy)] |
| ANT17 | Latour (2004), "Why has critique run out of steam? From matters of fact to matters of concern", *Critical Inquiry* 30(2):225–248. | [admit: University of Chicago Press record, doi:10.1086/421123; text] |
| ANT18 | Star (1999), "The ethnography of infrastructure", *American Behavioral Scientist* 43(3):377–391: infrastructure "becomes visible upon breakdown" (p. 382), one of the properties from Star & Ruhleder (1996). | [admit: doi:10.1177/00027649921955326; text as quoted with page] |
| ANT19 | Bowker & Star (1999), *Sorting Things Out* (MIT Press): infrastructural inversion as "a struggle against the tendency of infrastructure to disappear"; the ICD as "an invisible underpinning to medical practice". | [admit: MIT Press record, doi:10.7551/mitpress/6352.001.0001; reviews quoting the text] |
| ANT20 | Callon (1998), Introduction to *The Laws of the Markets* (Blackwell), p. 2: economics "performs, shapes and formats the economy, rather than observing how it functions". | [admit: quoted with page in MacKenzie, Muniesa & Siu (eds.) 2007, Princeton UP, ch. 1] |
| ANT21 | MacKenzie (2006), *An Engine, Not a Camera* (MIT Press): generic, effective and Barnesian performativity (use of a model makes processes more like their depiction) and counterperformativity; Black–Scholes–Merton as the main case. | [admit: book text] |
| ANT22 | Lukács (1923), "Reification and the consciousness of the proletariat", *History and Class Consciousness*: "a relation between people takes on the character of a thing and thus acquires a 'phantom objectivity'" (1971 trans., p. 83). | [admit: text as quoted with page by Fuchs (Westminster); SEP entry on Lukács] |
| ANT23 | Berger & Luckmann (1966), *The Social Construction of Reality*: "Reification is the apprehension of human phenomena as if they were things"; it implies that people can forget their own authorship of the human world. | [admit: text as compiled by the Library of Social Science (page varies by edition)] |
| ANT24 | Latour argues in *Pandora's Hope* ch. 5 that causality follows events rather than preceding them. | [abstain: unverifiable — passage not located; the verified analogue is ANT5 on power] |

---

### 6. Novelty check

| # | Finding | Tag |
|---|---|---|
| N1 | Searches combining "causal AI" with black-boxing, obligatory passage point, deskilling, reification and attribution found no work that treats a successful causal model as an accreted layer whose operators become an OPP, or that links continuous updating, tracing atrophy and M-erosion. | [abstain: unverifiable — negative web search, not a database crawl] |
| N2 | Nearest work by component: drift and entanglement (Sculley et al. 2015, AU15); automation deskilling (Bainbridge 1983, AU1; Parasuraman & Manzey 2010, AU2); blackboxing by success (Latour 1999, ANT2); illusions of understanding (Messeri & Crockett 2024, AU13); performative prediction and its sociological lineage (CM7, CM8). | **Synthesis** |
| N3 | Causal-AI advocacy claims that causal AI "doesn't operate within a black box", allowing researchers to check the model's reasoning. This is the position H.3 (i) opposes. | [admit: *Stanford Social Innovation Review*, "The Case for Causal AI" — confirms the claim is made, not that it holds] |

---

### 7. Mapping to the model (Synthesis; adopted in Part H)

| Finding | Model term | Reading |
|---|---|---|
| CM1, CM2 | φ ceiling | More observational data cannot raise a_j above what assumptions or interventions license |
| CM7, ANT20, ANT21 | φ performative | The model's attributions shape the data it retrains on; stability ≠ truth |
| AT1–AT8 | Carriers | Attribution creates carriers faster than it creates root reform (P22) |
| AT7 | V binding | Detection precedes action by years when L^R is large |
| AU1–AU8, AU5–AU6 | M erosion | Reserve tracing capacity atrophies; its maintenance is advisory and unmeasured (P23) |
| AU10, AU15, AU17 | Opacity by scale and update | No stable referent; explicit graph ≠ traceable graph |
| ANT2, ANT4, ANT6 | Accreted layers | Each layer a black box; the model a punctualisation of the chain |
| ANT5, ANT4, ANT6 | V, L^R, R, M | Punctualised network effects; carriers reopen them |
| ANT7 | Epistemic veto | Operators as OPP (P24); dissidence as the route to reopening |
| CM6, ANT14, ANT16 | Direction | SCMs inscribe direction on mutual relations; purification by analogy |

---

### 8. References

- Akrich, M. (1992). The de-scription of technical objects. In W. E. Bijker & J. Law (eds.), *Shaping Technology/Building Society*, 205–224. MIT Press.
- Bainbridge, L. (1983). Ironies of automation. *Automatica* 19(6):775–779.
- Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022). On Pearl's hierarchy and the foundations of causal inference. In H. Geffner, R. Dechter & J. Y. Halpern (eds.), *Probabilistic and Causal Inference: The Works of Judea Pearl*, 507–556. ACM Books.
- Bate, A. et al. (1998). A Bayesian neural network method for adverse drug reaction signal generation. *Eur J Clin Pharmacol* 54(4):315–321.
- Berger, P. L. & Luckmann, T. (1966). *The Social Construction of Reality.* Doubleday.
- Bongers, S., Forré, P., Peters, J. & Mooij, J. M. (2021). Foundations of structural causal models with cycles and latent variables. *Annals of Statistics* 49(5):2885–2915. doi:10.1214/21-AOS2064
- Bowker, G. C. & Star, S. L. (1999). *Sorting Things Out: Classification and Its Consequences.* MIT Press.
- Budzyń, K., Romańczyk, M., Kitala, D. et al. (2025). Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study. *Lancet Gastroenterol Hepatol* 10(10):896–903. doi:10.1016/S2468-1253(25)00133-5. Correction: 10(11):e12.
- Burrell, J. (2016). How the machine "thinks": understanding opacity in machine learning algorithms. *Big Data & Society* 3(1). doi:10.1177/2053951715622512
- Callon, M. (1986). Some elements of a sociology of translation: domestication of the scallops and the fishermen of St Brieuc Bay. In J. Law (ed.), *Power, Action and Belief*, 196–233. Routledge & Kegan Paul. (Sociological Review Monograph 32; Wiley dates it 1984.)
- Callon, M. (1991). Techno-economic networks and irreversibility. In J. Law (ed.), *A Sociology of Monsters*, 132–161. Routledge. (Sociological Review Monograph 38, 1990.)
- Callon, M. (1998). Introduction: the embeddedness of economic markets in economics. In M. Callon (ed.), *The Laws of the Markets*, 1–57. Blackwell.
- Callon, M. & Latour, B. (1981). Unscrewing the big Leviathan. In K. Knorr Cetina & A. V. Cicourel (eds.), *Advances in Social Theory and Methodology*, 277–303. Routledge & Kegan Paul.
- Elish, M. C. (2019). Moral crumple zones: cautionary tales in human-robot interaction. *Engaging Science, Technology, and Society* 5:40–60. doi:10.17351/ests2019.260
- Evans, S. J. W., Waller, P. C. & Davis, S. (2001). Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf* 10:483–486.
- Hardt, M. & Mendler-Dünner, C. (2023). Performative prediction: past and future. arXiv:2310.16608.
- Hardwig, J. (1985). Epistemic dependence. *Journal of Philosophy* 82(7):335–349.
- Jüni, P. et al. (2004). Risk of cardiovascular events and rofecoxib: cumulative meta-analysis. *Lancet* 364:2021–2029.
- Latour, B. (1986). The powers of association. In J. Law (ed.), *Power, Action and Belief*, 264–280. Routledge & Kegan Paul.
- Latour, B. (1987). *Science in Action.* Harvard UP.
- Latour, B. (1992). Where are the missing masses? The sociology of a few mundane artifacts. In Bijker & Law (eds.), *Shaping Technology/Building Society*, 225–258. MIT Press. (Earlier version: Johnson, J. (1988), *Social Problems* 35(3).)
- Latour, B. (1993). *We Have Never Been Modern.* Harvard UP.
- Latour, B. (1999). *Pandora's Hope.* Harvard UP.
- Latour, B. (2004). Why has critique run out of steam? From matters of fact to matters of concern. *Critical Inquiry* 30(2):225–248.
- Latour, B. (2005). *Reassembling the Social.* Oxford UP.
- Law, J. (1992). Notes on the theory of the actor-network: ordering, strategy, and heterogeneity. *Systems Practice* 5(4):379–393.
- Lukács, G. (1971 [1923]). *History and Class Consciousness.* Trans. R. Livingstone. Merlin Press / MIT Press.
- MacKenzie, D. (2006). *An Engine, Not a Camera: How Financial Models Shape Markets.* MIT Press.
- Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. *Nature* 627:49–58.
- Parasuraman, R. & Manzey, D. H. (2010). Complacency and bias in human use of automation: an attentional integration. *Human Factors* 52(3):381–410.
- Pasquale, F. (2015). *The Black Box Society.* Harvard UP.
- Perdomo, J. C., Zrnic, T., Mendler-Dünner, C. & Hardt, M. (2020). Performative prediction. *ICML*, PMLR 119:7599–7609.
- Philip, S. et al. (2020). A protocol for probabilistic extreme event attribution analyses. *ASCMO* 6:177.
- Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nat Mach Intell* 1:206–215.
- Schölkopf, B., Locatello, F. et al. (2021). Toward causal representation learning. *Proc. IEEE* 109(5):612–634.
- Sculley, D. et al. (2015). Hidden technical debt in machine learning systems. *NeurIPS* 28:2503–2511.
- Spirtes, P., Glymour, C. & Scheines, R. (2000). *Causation, Prediction, and Search*, 2nd ed. MIT Press.
- Star, S. L. (1999). The ethnography of infrastructure. *American Behavioral Scientist* 43(3):377–391.
- Star, S. L. & Ruhleder, K. (1996). Steps toward an ecology of infrastructure. *Information Systems Research* 7(1):111–134.
- Stuart-Smith, R. F., Otto, F. E. L. et al. (2021). Filling the evidentiary gap in climate litigation. *Nat Clim Change* 11:651–655.
- Topol, E. J. (2004). Failing the public health: rofecoxib, Merck, and the FDA. *NEJM* 351:1707–1709.
- Zečević, M., Willig, M., Dhami, D. S. & Kersting, K. (2023). Causal parrots: large language models may talk causality but are not causal. *TMLR*.
- Zheng, X., Aragam, B., Ravikumar, P. & Xing, E. P. (2018). DAGs with NO TEARS: continuous optimization for structure learning. *NeurIPS* 31.
- Primary records: BEA, final report on AF447 (Jul 2012); FAA SAFO 13002 (2013) and 17007 (2017); DOT Office of Inspector General audit on flight deck automation (Jan 2016); Regulation (EU) 2024/1689 (AI Act), Arts. 12 and 14; OLG Hamm, 5 U 15/17, judgment of 28 May 2025 (press release); European Commission, Destination Earth.

---

### 9. Disposition ledger

Counted by bracketed tag occurrences in Sections 2–6, excluding the legend examples in the header. Synthesis passages (Section 2 note, Section 6 N2, Section 7) are excluded. Findings re-cited from the main body or Appendices A–C are not counted again. Part H re-cites these findings and is not counted again.

| Disposition | Count |
|---|---|
| `admit` | 48 |
| `refute` | 2 |
| `abstain` | 11 |
| of which `non-authoritative source` | 5 |
| of which `unverifiable` | 4 |
| of which `tier-floor: unearned confidence` | 1 |
| of which `source-vs-prior conflict` | 1 |
| **Total tagged findings** | **61** |

**Refutations, with corrections:**
1. Extreme-event attribution "has enabled climate litigation". It has supported liability in principle (*Lliuya v RWE*) but has not yet carried a damages award, and submitted evidence lags the science (AT8).
2. Pilots "are required" to keep up manual flying. FAA guidance encourages it; the DOT Inspector General found uptake was never measured (AU6).

**Corrections carried by abstain-tagged findings (not counted as refutations):**
- Frontier labs retrain periodically and release versioned models; they do not update deployed weights continuously (CM10).
- Event attribution has not been shown to enter insurance pricing; insurers use catastrophe models (AT5).
- The deskilling effect in Budzyń et al. is an observational association that the authors call hypothesis-generating (AU8).
- Callon 1986, Latour 1986 and Callon 1991 carry earlier Wiley dates (1984; 1990) (ANT10).

**ANT attributions checked and held:** blackboxing by success (Latour 1999, p. 304); black box from cybernetics (Latour 1987); punctualisation (Law 1992); OPP and the four moments (Callon 1986); irreversibility as longevity shaping later translations (Callon 1991); power as consequence (Latour 1986); centres of calculation and immutable mobiles (Latour 1987); script and de-scription (Akrich 1992); delegation (Latour 1992); mediators and intermediaries (Latour 2005, p. 39); infrastructure visible on breakdown (Star 1999); infrastructural inversion (Bowker & Star 1999); performativity (Callon 1998, p. 2; MacKenzie 2006); reification (Lukács; Berger & Luckmann). **One attribution narrowed:** Latourian purification is the separation of human and non-human ontological zones (1993, pp. 10–11); its use for cause and effect in H.4 is an analogy.

**Open gaps:**
- The content of the Budzyń et al. erratum was not reached.
- The BEA final report, *Pandora's Hope* p. 304 and Callon's irreversibility pages were reached only through quotations.
- No source located for Latour's view that causality follows events (ANT24).

---

## Appendix E: The source essay in brief

This report follows up "The Cycle of Order and Disorder & the Challenge of LLMs" (26 March 2025). Its argument, summarised so that the report can be read on its own:

1. **Society oscillates between order and disorder.** Examples run from the post-Roman centuries to the Enlightenment, from the Warring States to the Qin, and from the Ming–Qing transition to the 1960s counterculture giving way to the modern radical right. Each ordered network forms partly in reaction to the one before, and acts as the catalyst for the next.
2. **Actor-Network Theory explains the transitions.** Social structures emerge through *translation* (Callon and Latour): ideas are transported with deformation through networks of human and non-human actants. Callon's four moments are problematisation, interessement, enrolment and mobilisation. *Tracing* is the laborious following of those associations as networks form, compete and become durable.
3. **LLM pre-training is a translation.** Next-token prediction is problematised as the obligatory passage point. Data sources are interested, and architectures, data schemas and compute are enrolled. The deployed model is mobilised as the spokesperson for all the linguistic patterns it has absorbed, and over time it becomes a black box.
4. **Reification.** As associations solidify, their origins are forgotten. Reification takes hours for small assemblages, and years or centuries for diffuse ones such as nation states and social norms. Democracy spread without the struggles that shaped it, becoming a *simulacrum*, a copy without an original. That obscuring may help explain its decline.
5. **Brittleness.** Brian Klaas's sandpile (self-organised criticality) describes over-reified structures: near a critical state, a single grain can trigger an avalanche. The essay's example is just-in-time supply chains and the 2021 Suez Canal blockage.
6. **LLMs reify at light speed.** LLMs decouple a network's size and diffusion from its assemblage density. They act as static averages of opinion: expertise without prudence, in Aristotle's terms. Translation through them standardises rather than diversifies. Copies of copies circulate, natural variation is lost, and networks converge on fewer, denser polarities.
7. **Necessary disorder.** Resilience requires preserving variability and the capacity to form countering networks: "allow some crazy". Newness emerges from the tension between order and disorder.

The report connects to this argument at three points:
- The sandpile is the physical analogue of the threshold-cascade models (Part C).
- The radius-bounded model reads its variables as punctualised network effects (B.4, H.4).
- Part H argues that a causal model built to escape accreted wickedness risks the essay's reification in a new form.

