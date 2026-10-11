# G2 coded panel — Codebook

Version 1.0, fixed 2026-10-11, before any coding. Model reference: q2-collective-delay-research.md, B.4/B.4.1 (φ, L^R, r̂, V = V0 − γH_elite + δL^R_elite + σΠ, M), Part F (P1, P11), Part G (G.1, carriers; P13–P16), Appendix C §2.

## 1. What you are scoring

You will receive one evidence packet per case (`packets/Kxx.md`). Score each case **as the situation stood at the scoring point, t0 + 5 years**, where t0 is the date of the first credible early warning shown in the packet header.

- Use **only** the packet. Do not use outside knowledge of the case, even if you recognise it. If you think you know what happened later, say so in the `recognised` field and score from the packet anyway.
- Every score must cite at least one packet quote id (e.g. `Q3, Q11`). A score without a citation is invalid.
- If the packet does not let you choose between at least two adjacent anchors, enter `IE` (insufficient evidence) and cite the items you considered. Do not guess.
- Score independently. Do not consult other coders' sheets or any outcome information.
- Half-points are not allowed. If between two anchors, choose the one whose description more of the cited evidence matches, and note the tie in `note`.

## 2. Variables

Direction convention: for φ, a **higher** score means the harm is **more** perceptible. For L^R, V, r̂ and causal distance, a **higher** score means **more** of the named property. You do not need to know which direction predicts delay.

### 2.1 φ — perceptibility of the harm to the exposed population (1–5)

Combines three sub-dimensions. Score each 1–5, then report φ as their rounded mean (round .5 up). Cite evidence for each.

| Anchor | Visibility (φ-vis) | Attributability (φ-att) | Latency (φ-lat; high = short) |
|---|---|---|---|
| 1 | Harm invisible to those exposed; detectable only by specialised instruments or statistics | Exposed people cannot link harm to the source; many competing causes; link asserted only by a few specialists | Harm appears decades after exposure, or in a later generation |
| 2 | Harm visible only in aggregate statistics or in non-human indicators far from where people live | Link shown statistically, contested in the packet's period | 10–20 years |
| 3 | Harm visible in some exposed groups or places, not generally | Link accepted by most specialists, not by the exposed public | 2–10 years |
| 4 | Harm visible to most exposed people or communities, intermittently | Link widely believed by the exposed, contested only by the source's beneficiaries | Months to 2 years |
| 5 | Harm vivid, immediate and observed by ordinary people (deaths, deformities, dead fish, smog) | Signature harm: unique to this agent, unmistakable | Immediate (days to weeks) |

### 2.2 L^R concentration — concentration of the source's beneficiaries (1–5)

Who gains from the activity that causes the hazard, and how concentrated is the gain?

| Anchor | Description |
|---|---|
| 1 | Benefit diffuse across the general population; no organised beneficiary with a stake much larger than anyone else's |
| 2 | Benefit spread across many sectors or millions of users; some producers but none dependent on it |
| 3 | Benefit held by one industry with many firms, or by a large occupational/regional group, for whom it is a material but not dominant income source |
| 4 | Benefit concentrated in a few firms or one industry for which the product/practice is a core line of business |
| 5 | Benefit concentrated in one or a handful of firms or a state monopoly, for which the product is central, highly profitable and hard to substitute |

### 2.3 V — veto strength against regulation (1–5)

The number and strength of actors able to block or delay binding action at t0 + 5. Include industry lobbying capacity, control of the relevant regulator or ministry, allied unions or regions, sympathetic governments, international trade rules, and the fragmentation of decision authority across jurisdictions.

| Anchor | Description |
|---|---|
| 1 | No organised opponent of regulation is visible; a single authority could act alone |
| 2 | Opponents exist but are weak or divided; one or two decision points |
| 3 | One organised industry or interest opposes; it has access to regulators but no evident control; several decision points |
| 4 | Organised, well-resourced opposition with demonstrated influence on regulators, government or research; or authority fragmented across many jurisdictions with no single forum |
| 5 | Opposition controls or captures the regulator or the evidence base, or the state itself is the beneficiary; and/or action requires agreement of many sovereign parties |

### 2.4 r̂ bias — hidden or misperceived concern (1–5)

Evidence that concern about the hazard existed but was hidden, private, suppressed or underestimated by others (pluralistic ignorance, preference falsification, confidential findings, workers or officials afraid to speak).

| Anchor | Description |
|---|---|
| 1 | Concern, where it existed, was openly expressed and accurately perceived; no sign of suppression |
| 2 | Isolated signs that some concern was not voiced |
| 3 | Clear evidence that concern held by some actors (e.g. scientists, officials, workers) was not made public or was dismissed as marginal |
| 4 | Evidence of deliberate concealment of findings or discouragement of concern, OR of authorities publicly reassuring while privately concerned |
| 5 | Systematic suppression: findings kept confidential by the source, critics penalised, and public reassurance contradicting internal knowledge |

### 2.5 M — prior institutional memory of similar hazards (1–5)

Whether institutions at t0 + 5 already had experience, rules or standing bodies for a hazard of the same kind (same agent class, pathway or harm).

| Anchor | Description |
|---|---|
| 1 | First encounter: no precedent hazard of this kind and no institution responsible for it |
| 2 | Loose analogues exist, but no institution draws on them in the packet |
| 3 | Analogous hazards are known and cited, but no standing body or rule covers this kind of hazard |
| 4 | A standing body or a general rule covers this class of hazard, but it is not applied to this agent |
| 5 | A standing body with a clear mandate and precedents for this exact class of hazard is actively engaged |

### 2.6 Causal distance — links between source and main harm (1–5)

Count the links in the dominant chain described in the packet, from the source activity to the main harm borne by people or ecosystems (Appendix C §2). Example: emission → atmospheric transport → deposition → acidification → fish death = 4 links.

| Anchor | Links |
|---|---|
| 1 | 1 link: direct contact with the source causes the harm |
| 2 | 2 links |
| 3 | 3 links |
| 4 | 4 links |
| 5 | 5 or more links, or the chain runs through a global system (atmosphere, oceans, food chain across borders) |

Write out the chain you counted in `note`.

### 2.7 Carrier presence (0/1 + description)

A carrier is an actor able to move the hazard's costs into the radius of the veto holders (G.1 point 5): courts or litigants, insurers, other states or foreign regulators, independent scientists with public standing, organised victims, trade partners, creditors.

- `1` = at least one such actor is **active** on this hazard in the packet by t0 + 5 (filing suits, refusing cover, imposing restrictions, publishing independent findings that reach decision-makers).
- `0` = no such actor is active by t0 + 5 (potential carriers that exist but have not acted count as 0).
- Description: name the carrier type(s) and cite.

### 2.8 Funding source of the early research (for P11)

Who funded or conducted the research on the hazard up to t0 + 5?

- `industry` = most cited early research was funded, conducted or controlled by the source industry or its associations.
- `independent` = most was funded and conducted by government, academic, medical or other bodies without a stake in the source.
- `mixed` = substantial contributions from both, or industry-funded work and independent work of comparable weight.
- `IE` if the packet does not say.

## 3. Coding sheet (one per case, per coder)

```
case: Kxx
coder_model: <model name and version>
date_coded: <YYYY-MM-DD>
recognised: <yes/no; if yes, what you think the case is>
phi_vis: <1-5|IE>  cite: <Q..>
phi_att: <1-5|IE>  cite: <Q..>
phi_lat: <1-5|IE>  cite: <Q..>
phi:     <1-5|IE>  (rounded mean; IE if two or more sub-scores are IE)
LR:      <1-5|IE>  cite: <Q..>
V:       <1-5|IE>  cite: <Q..>
r_hat:   <1-5|IE>  cite: <Q..>
M:       <1-5|IE>  cite: <Q..>
causal_distance: <1-5|IE>  cite: <Q..>  chain: <source -> ... -> harm>
carrier: <0|1|IE>  type: <...>  cite: <Q..>
funding: <industry|independent|mixed|IE>  cite: <Q..>
note: <ties, doubts>
```

Save as `codings/<coder_model>/Kxx.md`.

## 4. What is not coded here

Coders do **not** code the outcome (lag to first meaningful regulatory action; locus of that action). Those are coded separately, by a different process, and are not shown to coders.

## 5. Additions for forward cases and fresh case sets (fixed 2026-10-11)

These apply to every coding done after 2026-10-11 and supersede §1's scoring point for those codings. The K01–K31 codings are unchanged.

### 5.1 Scoring point

The scoring point is the earlier of:
- t0 + 2 years;
- the day before the earliest binding measure of any kind on the hazard (a regulation, ban, court order, or binding voluntary agreement), wherever and by whomever adopted.

The packet contains only items dated on or before the scoring point. The packet preparer, not the coder, applies this rule, and records the scoring point in the packet header.

### 5.2 De-identification protocol (applied by the packet preparer)

- Replace the agent or substance, products, firms, people, places, agencies, journals and court names with stable placeholder tokens such as [AGENT], [FIRM-1] and [COUNTRY-A].
- Convert absolute dates to years relative to t0 (T+0, T+1.5).
- Paraphrase quotations where the wording is distinctive enough to identify the case. Keep the quote ids.
- Keep the generic domain words a coder needs to score: "industrial chemical", "pharmaceutical", "fishery".
- A second preparer reviews each packet for residual identifiers before release.

### 5.3 Recognition and leakage probes (before scoring)

The coder answers two questions first:
1. "What real-world case do you think this is?" Any free-text answer is accepted.
2. "How many years from T+0 to the first binding measure?" The answer is a bucket: < 5, 5–14, 15–29, ≥ 30.

**Exclusion rule:**
- Primary analysis: a case–coder pair is excluded if the coder correctly identifies the case.
- Sensitivity analysis: all pairs are included.

**Panel-level leakage check:** if the coders' lag-bucket predictions beat chance (binomial test against the modal-bucket base rate, one-sided p < .05), the coded panel is flagged as contaminated.

### 5.4 H — harm magnitude at the scoring point (1–5)

| Anchor | Description |
|---|---|
| 1 | Harm suspected only, with no documented cases |
| 2 | Isolated documented cases (a handful of people, or one site) |
| 3 | Documented harm in identifiable groups or places (dozens to hundreds of people, or several sites) |
| 4 | Widespread harm (thousands of people, or regional ecosystems) |
| 5 | Population-level mortality or morbidity, or large-scale ecosystem collapse |

Add `H: <1-5|IE>  cite: <Q..>` to the coding sheet after `causal_distance`.

### 5.5 Coders

Use human coders where possible. Model coders may be used only with de-identified packets and with the §5.3 probes. Use at least two coders per case, and report Krippendorff's α for every variable, including H.
