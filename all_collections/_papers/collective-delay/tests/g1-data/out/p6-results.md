# P6 results: benefit/harm asymmetry vs budget kurtosis (exploratory)

## Pre-specified hypothesis
Pre-registered in `out/p6-coding.md`, which was written before the budget file was downloaded. H1: across CAP major topics, asymmetry A = (a) harm diffuseness × (b) benefit concentration is positively rank-correlated with the excess (Fisher) kurtosis of annual % changes in real US budget authority. The test is a one-sided Spearman at α = 0.05. The coding is **single-coder judgement**.

## Data provenance
- **Policy Agendas Project, "Budget Authority (Adjusted)".** Jones, B. D. & Koski, C. (2017), codebook "Updated 2018". The file is `Budget_Authority_Adjusted_2018_for_PAP_1.csv`, downloaded 2026-10-11 from https://minio.la.utexas.edu/compagendas/datasetfiles/Budget_Authority_Adjusted_2018_for_PAP_1.csv. It is linked from https://www.comparativeagendas.net/project/us/datasets.
  - Server last-modified: 10 Sep 2024. Size: 914,625 B. SHA-256: 5c09294f…0717c. 8,165 rows, FY1947–2017.
  - Values are real budget authority in millions, using the OMB 2009 deflator, by OMB function and subfunction. [admit: PAP codebook `Budget_Codebook_Abridged_pre_2018.pdf`, saved in data-raw]
- **Topic mapping.** The PAP "Budget Authority-Policy Crosswalk" (`US-Budget-policy_crosswalk_19.2.csv`, same page) maps each topic to its major OMB codes. Each OMB subfunction was assigned to exactly one CAP major topic. The mapping is in `scripts/p6_kurtosis.py` (`SUB2TOPIC`). Some topics cannot be measured:
  - Macroeconomics (1), Civil rights (2) and Immigration (9) have no budget series, according to the crosswalk.
  - Foreign trade (18) has no subfunction of its own; it shares 150/376.
  - Culture (23) is not present.
  - That leaves **N = 16 topics**.
- **Deviations from p6-coding.md.** These were decided after the data structure was seen but before any kurtosis was computed.
  1. The primary series uses only *programmatic* subfunctions. This excludes the financial subfunctions (e.g. 373 deposit insurance and 371 mortgage credit), whose budget authority goes negative. The PAP codebook (note 7) warns about these. All subfunctions are run as a robustness check.
  2. % changes whose base year is ≤ 0 are dropped.
  3. The budget data are coded by OMB subfunction, not CAP subtopic. So the "subtopic" check uses subfunctions, each scored with its parent topic's score.
  4. Topic-periods with fewer than 15 changes are dropped.

## Method
1. Sum real budget authority by topic and year.
2. Take the annual % change.
3. Compute excess kurtosis (`scipy.stats.kurtosis`, `bias=False`) and sample L-kurtosis τ4, using Hosking PWMs. For a Normal distribution, τ4 = 0.123.
4. Compute Spearman ρ between A and kurtosis.

Script: `scripts/p6_kurtosis.py <csv> <out_dir>`. It includes a self-check of the L-kurtosis and %-change code. Raw output is in `out/p6-results-raw.txt`.

## Results
### Topic table (programmatic, FY1948–2017)
| Topic | a | b | A | mean share % | mandatory share | excess kurt | τ4 |
|---|---|---|---|---|---|---|---|
| 3 Health | 2 | 4 | 8 | 13.3 | 0.89 | 18.7 | 0.479 |
| 4 Agriculture | 4 | 5 | 20 | 2.1 | 0.86 | 8.5 | 0.346 |
| 5 Labor | 2 | 3 | 6 | 3.3 | 0.75 | 5.5 | 0.266 |
| 6 Education | 3 | 3 | 9 | 2.7 | 0.48 | 2.6 | 0.253 |
| 7 Environment | 5 | 4 | 20 | 0.39 | 0 | 11.0 | 0.535 |
| 8 Energy | 4 | 5 | 20 | 0.11 | 0 | 38.6 | 0.939 |
| 10 Transportation | 4 | 4 | 16 | 3.2 | 0 | 39.8 | 0.523 |
| 12 Law/crime | 3 | 3 | 9 | 0.92 | 0 | 4.1 | 0.270 |
| 13 Social welfare | 1 | 2 | 2 | 25.9 | 0.98 | 1.4 | 0.176 |
| 14 Community dev/housing | 3 | 4 | 12 | 2.2 | 0 | 10.7 | 0.460 |
| 15 Banking/commerce | 4 | 5 | 20 | 0.60 | 0 | 11.2 | 0.314 |
| 16 Defense | 4 | 5 | 20 | 35.9 | 0.07 | 26.3 | 0.423 |
| 17 Space/science | 5 | 4 | 20 | 1.4 | 0 | 41.9 | 0.593 |
| 19 Intl affairs | 5 | 3 | 15 | 1.6 | 0 | 3.3 | 0.274 |
| 20 Gov operations | 4 | 3 | 12 | 5.0 | 0.76 | 10.0 | 0.426 |
| 21 Public lands/water | 4 | 4 | 16 | 1.4 | 0 | 1.2 | 0.224 |

### Pre-specified test
**A vs excess kurtosis: ρ = 0.554, one-sided p = 0.013, N = 16.**

### Robustness (one-sided p)
| Check | ρ | p | N |
|---|---|---|---|
| A' = a+b vs kurt | 0.569 | 0.011 | 16 |
| A vs τ4 | 0.555 | 0.013 | 16 |
| Excl. topics < 0.5% share (drops Environment, Energy), kurt | 0.484 | 0.040 | 14 |
| Excl. tiny, τ4 | 0.426 | 0.064 | 14 |
| FY1948–76, kurt | 0.560 | 0.019 | 14 |
| FY1948–76, τ4 | 0.321 | 0.131 | 14 |
| FY1977–2017, kurt | 0.463 | 0.035 | 16 |
| FY1977–2017, τ4 | 0.530 | 0.017 | 16 |
| All subfunctions incl. financial, kurt | 0.327 | 0.108 | 16 |
| All subfunctions incl. financial, τ4 | 0.413 | 0.056 | 16 |
| Partial Spearman, controlling for mandatory share and size, kurt | 0.565 | 0.018 | df 12 |
| Partial Spearman, same controls, τ4 | 0.474 | 0.043 | df 12 |
| **Subfunction level** (parent score), kurt | −0.022 | 0.567 | 59 |
| **Subfunction level**, τ4 | 0.083 | 0.265 | 59 (topic-cluster permutation p = 0.292) |

### CAP baseline (Jones et al. 2009)
- Pooled annual % changes across all programmatic subfunctions: N = 3,881, excess kurtosis ≈ 3,875, L-kurtosis 0.957.
- 16 of 16 topics have excess kurtosis > 0 and τ4 above the Normal value.
- This replicates the general leptokurtosis finding. [admit: Jones, Baumgartner, Breunig et al. 2009, *AJPS* 53(4):855–873. Preprint seen; it reports leptokurtic budget changes in all cases and uses L-kurtosis.]
- P6 asks a different question: whether the *degree* of leptokurtosis varies with asymmetry.

## Verdict
**Consistent on the pre-specified test (ρ = 0.55, p = 0.013, N = 16), but the result is fragile.**
- It survives these checks: the sum score, L-kurtosis, both sub-periods for raw kurtosis, and controls for mandatory share and size.
- It weakens to p ≈ 0.06–0.13 in three cases: when tiny topics are dropped (τ4), when financial subfunctions are kept, and for FY1948–76 τ4.
- It **vanishes at the subfunction level** (ρ ≈ 0). This is the most important caveat. Within-topic subfunctions are no more lurchy in high-A topics. So the topic-level association may come from aggregation: how many lumpy programmes each topic adds or reorganises over time, such as Energy after 1973 or Space in the 1960s. A trait of the topic's payoff structure is not the only possible explanation.

## Limitations and confounds
- **Single coder, not blind to the literature.** For example, it is "known" that defence and science budgets are lumpy. The scores were set before topic kurtosis was seen, but priors could have leaked in. A second, independent coder is needed.
- **Mandatory vs discretionary.** Mandatory share correlates with A (ρ = −0.51). Low-A topics such as Social welfare, Health and Labor are mostly entitlements, which are mechanically smooth. The partial correlation survives, but with N = 16 and two controls it has little power. A cleaner test would use only discretionary subfunctions.
- **Size.** Small series are noisier, and size correlates with A (ρ = −0.54). The size-exclusion check weakens the result.
- **Reorganisation and re-coding.** Some subfunctions start from near zero, e.g. 272 energy conservation, 304 pollution control and 571 Medicare in 1966. Programmatic flags also change. These create spikes driven by creation or reclassification events, which is exactly what inflates topic kurtosis. True's consistent re-coding reduces this but does not remove it.
- **Crosswalk.** The crosswalk fit codes range from 1 to 5. Several topics (12, 14, 15, 17, 19, 20, 21) have fit 3, a mediocre correspondence.
- **Small N and moment estimates.** N = 16 topics. Kurtosis from about 70 annual changes is unstable, though τ4 is more robust and agrees.
- **Data vintage.** FY1947–2017 only. The 2018 file is the latest official PAP budget-authority release found.

## Follow-up: discretionary-only (specified before running) — EXPLORATORY
This test was written down on 2026-10-11, before any discretionary-only statistic was computed. It addresses the mandatory/discretionary confound described above.
- **Data.** The same file and the same programmatic-subfunction filter, further restricted to subfunctions with the PAP flag `discretionary == 1`. The flag is fixed for each subfunction. Subfunctions flagged mandatory, or flagged neither, are excluded.
- **Topic level.** The same pipeline as the primary test: sum by topic and year, take the % change, use FY1948–2017, and require at least 15 changes. Topics with no discretionary subfunction drop out.
- **Tests.** Spearman of A vs excess kurtosis, and of A vs τ4, both one-sided (ρ > 0) at α = 0.05.
- **Subfunction level.** Discretionary programmatic subfunctions with at least 30 changes, each scored with its parent topic's A. The same two Spearman tests, plus a topic-cluster permutation p for A vs τ4 (10,000 permutations, seed 1).
- **Reading.** If ρ > 0 with p < 0.05 at topic level, the topic-level association does not rest only on entitlement smoothness. If the subfunction level stays near zero, the aggregation caveat stands.

### Follow-up results (discretionary-only)
Command: `scripts/p6_kurtosis.py <csv> out --discretionary`. Raw output is in `out/p6-discretionary-raw.txt`. The refactor that added this option leaves `p6-results-raw.txt` byte-identical.

| Test | ρ | one-sided p | N |
|---|---|---|---|
| Topic level, A vs excess kurt | 0.026 | 0.462 | 16 |
| Topic level, A vs τ4 | 0.079 | 0.386 | 16 |
| Subfunction level, A vs excess kurt | −0.095 | 0.736 | 47 (16 topics) |
| Subfunction level, A vs τ4 | 0.025 | 0.433 | 47 (topic-cluster permutation p = 0.445) |

All 16 topics keep at least one discretionary subfunction. The low-A topics change most once their entitlements are removed:
- Social welfare's excess kurtosis goes from 1.4 to 34.5.
- Labor's goes from 5.5 to 41.0.
- Health's goes from 18.7 to 11.0.

### Verdict update
**The pre-specified topic-level result does not survive the discretionary-only restriction (ρ ≈ 0.03, p = 0.46).**
- This is the most plausible reading of the earlier ρ = 0.55: low-A topics are dominated by mandatory entitlements, and entitlements are mechanically smooth.
- The partial correlation controlling for mandatory share did not pick this up. That control had little power at N = 16.
- With the subfunction-level null already found, P6 now has **no support** in the CAP budget data. Treat the earlier result as confounded, not as a weak positive.
