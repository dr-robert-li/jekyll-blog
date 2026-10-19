# Test programme: review summary

Date: 2026-10-11. Scope: the three-part goal (group 3 evidence review, group 2 exploratory panel, group 1 data analysis on P6 and P7.1). Only the accepted group 3 revisions have been merged into `q2-collective-delay-research.md` (see Group 3); everything else stays here for review.

## At a glance

| Group | Prediction | Result | Strength |
|---|---|---|---|
| 3 (existing evidence) | P3: lowering the private cost L^R of early action speeds it | Mixed by domain; fails for costly and health behaviours (Beshears pension-default backfire; Foxcroft Cochrane null) | Partly falsified; the sign of δ is not fixed, which is a specification issue |
| 3 | P14: attribution decays with distance along the chain | Mixed; decay depends on link type (intervening agents); traceability matters for elites, not voters (Mildenberger & Sahn 2025); shark-attack evidence not robust (Fowler & Hall) | Narrow it |
| 3 | P23: AI causal models atrophy tracing | Mixed; separate three mechanisms (automation bias, atrophy, non-formation); strongest for novices (Bastani 2025), plus Casner 2014 and Rinta-Kahila 2023; Sparrow Exp. 1 did not replicate | Narrow it |
| 2 (coded panel, 31 EEA cases) | P1: composite C predicts warning-to-action lag | ρ = −0.30 [−0.59, 0.05]; sign reversed | Not supported |
| 2 | P11: industry-funded doubt lengthens lag | r_rb = 0.26, Holm p = .66 (industry n = 4) | Underpowered null |
| 2 | P13: distant harms are addressed downstream | r_rb = 0.03 | Null |
| 2 | P16: a carrier shortens lag | r_rb = −0.69, Holm p = .006 (S2: −0.77, p = .003) | Supported, but every coder recognised every case |
| 1 (data) | P6: benefit/harm asymmetry predicts budget kurtosis | ρ = 0.55, p = .013, N = 16 topics; discretionary-only follow-up ρ = 0.03, p = .46 | Not supported: the result disappears with discretionary spending only and at subfunction level (ρ ≈ 0), so it is likely a mandatory-spending artefact |
| 1 | P7.1: deadline skew | 6/7 (primary), 15/16 (expanded) in the first quarter of a one-year window; cluster-level KS significant | Supported (generic deadline effect) |
| 1 | P7.1: V × L^R interaction | V ρ −0.15 to −0.44 (n.s.); L^R ρ +0.53 to +0.78 (wrong sign) | Not supported; the model's distinctive part fails |
| 4 (coded panel, 15 shared-model cases, 174 episodes) | Prop 3: shared models are reopened only by organised actors, and all at once | H3 12/12 first reopenings organised (p = .0002); H1 0/4 lone vs 38/156 organised (p = .33, too few lone episodes); H4 21/37 class scope (9/11 cases case-weighted) | Mixed under the registered rule; kept out of the paper's main body. See `g4-prop3/results.md` |

**Overall.** The parts of the model that rival accounts also predict hold up: deadline clustering and carriers. The parts that would set it apart do not: the composite C in P1 (still negative after the post-hoc repairs), the V and L^R interaction in P7, and the P6 link between asymmetry and budget punctuation, which disappears once mandatory spending is removed. These tests have small samples, and the scoring was not blind, so the distinctive parts are not refuted either. The next tests have to be blind and run forward.

## Group 3: review of existing evidence (`g3-review/`)

- `evidence-review.md`: 187 lines; tags admit 49 · refute 3 · abstain 20.
- `proposed-revisions.md`: replacement rows for P3, P14 and P23; an Arnold (1990) paragraph for G.1 (traceability as the closest precedent, with the Mildenberger & Sahn 2025 test); a reading-list entry; and the knock-on changes to the claims-status subsection.
- **Accepted and merged on 2026-10-11:** the revisions (P3, P14, P23 rows; G.1 Arnold paragraph and reading-list entry; claims-status changes) are in the report. Pre-merge backup: `/tmp/claude-1000/-home-rli-Desktop-projects-jekyll-blog/ee2143d7-0c17-46d2-9627-4ef28714dbda/scratchpad/q2-backup-pre-g3-merge.md`.

## Group 2: exploratory panel (`g2-panel/`)

- **Design.**
  - Cases: 31 Late Lessons cases, K01–K31, fixed in `case-list.md` before coding.
  - Documents: dated before each outcome only, in `packets/`.
  - Coders: four models (Opus, Sonnet, Haiku, Fable).
  - Pre-registration: `preregistration.md`, timestamped 08:14.
  - Analysis: `analysis.py`, results in `results.md`.
- **Reliability is good:** Krippendorff's α is 0.69 to 0.88 on every variable, so no variable was flagged.
- **Main caveat: contamination.** Each coder recognised 30 or 31 of the 31 cases. So the scores may encode remembered outcomes, and sensitivity S1, which drops recognised cases, could not be run. Treat P16 as suggestive only.
- **Exploratory components.** V (−0.45), distance (−0.38) and M (−0.51) correlate with lag in the opposite direction to the composite. That suggests the composite's construction is the problem, not every component.
- **Deviation from the pre-registration:** the Cox model was not run, because lifelines is not installed.
- **Forward registration.** `forward-registration.md` holds dated predictions:
  - F7.1–F7.5: OASI, Medicare HI, Kigali steps, and the interaction test;
  - P22 domains;
  - others.
- **Timestamp:** `forward-registration.md` and `codebook.md` are fixed by a commit pushed to the public GitHub repo. This is enough for a blog; it is not a formal pre-registration.

## Group 1: data analysis (`g1-data/`)

### P6 (`out/p6-results.md`)
- **Data:** Policy Agendas Project, real US budget authority, FY1947–2017, with SHA-256 recorded.
- **Coding:** the hypothesis and coding were fixed before download. Coding was by a single coder.
- **Holds under:** the sum score, L-kurtosis, both sub-periods, and partial controls for mandatory share and size.
- **Fragility:**
  - The result vanishes within topics: at the subfunction level, ρ = −0.02 (N = 59).
  - It is confounded by mandatory share (ρ −0.51 with A) and by size (ρ −0.54).
  - The likely explanation is aggregation: lumpy programme creation and recoding inside a topic. The payoff structure may not be the driver.
- **Discretionary-only follow-up (specified before running, exploratory).**
  - Topic level: A vs kurtosis ρ = 0.03 (p = .46); A vs τ4 ρ = 0.08 (p = .39); N = 16.
  - Subfunction level: ρ ≈ 0 (N = 47; permutation p = .45).
  - Once their entitlements are removed, the low-A topics are as lurchy as the rest. The original ρ = 0.55 is best read as mandatory-spending smoothness.
  - **Verdict: P6 is not supported by the CAP data.**

### P7.1 (`out/p7-results.md`)
- **Panels** (dates in `panel/*.csv`):
  - Primary: the §7.1 resolved members, N = 7.
  - Expanded: N = 16, adding six more debt-limit episodes, two tax sunsets and the Highway Trust Fund.
  - Durable: N = 11, keeping only actions that resolved the deadline for at least a year.
- **Date sources:**
  - Most dates were read from the Treasury letters, public laws and the USBR record of decision on disk.
  - The five signing dates and one X-date that had come from model knowledge are now verified, all unchanged. The signing dates (and P.L. 119-21) come from the govinfo "Approved" lines. The 15 Dec 2021 X-date comes from Treasury press release jy0488. DL9's mid-August window start comes from CBO's Monthly Budget Review for May 2025. The results did not change.
- **Skew: supported.** Median lead is 8 days in the expanded panel; 15 of 16 members acted within a quarter of a year. About a fifth landed 1–7 days *after* the deadline.
- **Interaction: not supported.** L^R has the opposite sign. The high-L^R members (1983 Social Security, Korea, Colorado) are also the long-horizon ones, and the L^R rule reads the content of the action. So the result is confounded and not blind. It neither confirms nor cleanly refutes the claim.
- **Housekeeping.** The background agent ran out of context before writing up P7, and its X-date sub-agent stalled for about 85 minutes on GAO 403 errors and was stopped. The panel, scoring and write-up above were completed directly afterwards.

## Limitations across the programme

1. **Contamination.** Every model coder knows these historical cases. Retrospective blind coding is not achievable with these coders.
2. **Single-coder judgement.** One coder scored P6's a and b, and one scored P7's V and L^R.
3. **Small, clustered samples.** P7 is dominated by one institution, the US debt limit. P11 has only 4 industry-funded cases.
4. **Some dates are unverified.** They are flagged in the panel CSVs.

## Recommended next steps

1. ~~Decide on `g3-review/proposed-revisions.md`.~~ Done: accepted and merged on 2026-10-11.
2. Timestamp `g2-panel/forward-registration.md` and `codebook.md` with a commit pushed to the public GitHub repo (no OSF deposit; this is for the blog, not a journal). The forward cases are the only uncontaminated test of the distinctive claims.
3. Re-score P7's V and L^R using the g2 codebook (§2.2–2.3), with coders who see only pre-deadline documents, and add horizon length as a covariate. Then decide whether P7's interaction clause stays.
4. ~~Revisit how P1's composite C is built before any further test.~~ Done (exploratory): no component is coded backwards. C leaves out M and the carrier (H_elite) term, counts L^R twice, and is scored after the outcome in 9 cases, with an era confound. The threshold form B is recommended for pre-registration on the forward cases. See `g2-panel/composite-review.md`. **Accepted 2026-10-11:** B is now pre-registered as the primary P1 composite (amendment §6 of `g2-panel/forward-registration.md`). The scoring-point rule, de-identification, recognition and leakage probes, and an H scale are added in `g2-panel/codebook.md` §5.
5. ~~For P6, test discretionary subfunctions only.~~ Done (exploratory): ρ = 0.03, p = .46. The P6 result disappears, so it is now not supported.
6. ~~Optionally, recover the five knowledge-sourced P7 dates from congress.gov to make the panel fully sourced.~~ Done: all six dates were verified (govinfo, Treasury jy0488, CBO), with no changes and the same P7 results.
