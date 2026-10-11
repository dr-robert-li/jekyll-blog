# G2 coded panel — results (EXPLORATORY)

Coders: fable, haiku, opus, sonnet (each a different AI model). Cases: 31. Analysis follows preregistration.md; deviations are listed at the end.

## Inter-rater reliability (Krippendorff's α)

| Variable | Level | α | Flag |
|---|---|---|---|
| phi | ordinal | 0.84 |  |
| LR | ordinal | 0.86 |  |
| V | ordinal | 0.84 |  |
| rhat | ordinal | 0.88 |  |
| M | ordinal | 0.69 |  |
| dist | ordinal | 0.87 |  |
| carrier | nominal | 0.76 |  |
| funding | nominal | 0.75 |  |

**Cases recognised, by coder:** fable 31/31, haiku 30/31, opus 31/31, sonnet 31/31

Outcomes parsed: lag available for 31 cases (2 censored); locus root/downstream for 28.

## Pre-registered tests

### Primary (all cases)

| Test | n | Effect | p (one-sided) | Holm p | Evaluable |
|---|---|---|---|---|---|
| P1 | 31 | ρ = -0.30 [-0.59, 0.05] | 0.951 | 0.951 | yes |
| P11 | 23 | U = 48, r_rb = 0.26 (industry n=4, independent n=19) | 0.220 | 0.661 | yes |
| P13 | 28 | U = 76, r_rb = 0.03 (downstream n=7, root n=21) | 0.457 | 0.914 | yes |
| P16 | 27 | U = 28, r_rb = -0.69 (carrier n=16, none n=11) | 0.002 | 0.006 | yes |

### S1: scores from recognised cases excluded

| Test | n | Effect | p (one-sided) | Holm p | Evaluable |
|---|---|---|---|---|---|
| P1 | 0 | too few cases | – | – | no (> 1/3 excluded) |
| P11 | 0 | too few (industry n=0, independent n=0) | – | – | no (> 1/3 excluded) |
| P13 | 0 | too few (downstream n=0, root n=0) | – | – | no (> 1/3 excluded) |
| P16 | 1 | too few (carrier n=0, none n=1) | – | – | no (> 1/3 excluded) |

### S2: censored cases excluded

| Test | n | Effect | p (one-sided) | Holm p | Evaluable |
|---|---|---|---|---|---|
| P1 | 29 | ρ = -0.33 [-0.65, 0.06] | 0.958 | 0.958 | yes |
| P11 | 21 | U = 48, r_rb = 0.41 (industry n=4, independent n=17) | 0.113 | 0.339 | yes |
| P13 | 28 | U = 76, r_rb = 0.03 (downstream n=7, root n=21) | 0.457 | 0.914 | yes |
| P16 | 25 | U = 17, r_rb = -0.77 (carrier n=15, none n=10) | 0.001 | 0.003 | yes |

## Exploratory (no significance claims)

| Variable | Spearman ρ with lag (censored ranked top) | n |
|---|---|---|
| phi | 0.12 | 31 |
| LR | -0.13 | 31 |
| V | -0.45 | 31 |
| rhat | -0.10 | 31 |
| M | -0.51 | 31 |
| dist | -0.38 | 31 |

The Cox model listed as exploratory in the pre-registration was not run (lifelines is not installed). This is a deviation.

## Deviations and analysis decisions (recorded after coding, before interpretation)

| Date | Change | Reason |
|---|---|---|
| 2026-10-11 | Outcomes use the headline lag in each `outcomes.md` entry. The alternative lags the file lists (e.g. different t0 or jurisdiction) are ignored. | Pre-registration §3 fixes the definitions but not the choice between listed alternatives. The headline is the outcome compiler's application of §3. |
| 2026-10-11 | Locus: the first of "root" or "downstream" named in the entry. Entries beginning "unresolved" or "n/a" are coded missing (K01, K03, K26). | Mixed entries (K24, K25, K28) name a primary locus first. |
| 2026-10-11 | The Cox model (exploratory) was not run. | lifelines is not installed. Censoring affects only 2 of 31 cases. |
| 2026-10-11 | S1 (excluding recognised cases) is not evaluable. | Every coder recognised 30–31 of the 31 cases. |

## Reading

1. **Reliability is high (α 0.69–0.88).** But all four coders are language models that recognised almost every case. Their agreement may reflect shared background knowledge rather than independent reading of the packets. High α is not evidence of a valid measurement here.
2. **P16 (carrier → shorter lag) is supported and survives Holm:** r_rb = −0.69, Holm p = 0.006; without censored cases, −0.77. The contamination risk is greatest for this variable. A coder who knows a court, insurer or other state forced action can "see" a carrier in the packet. Treat this as consistent, not confirmatory.
3. **P1 (the composite predicts lag) is not supported, and the sign is reversed:** ρ = −0.30 [−0.59, 0.05]. The exploratory components show why. V (ρ = −0.45) and causal distance (ρ = −0.38) run *against* the model: higher-veto and longer-chain cases were regulated sooner in this sample. Two possible explanations, neither tested:
   - EEA selected high-profile industrial hazards, where strong opposition coexisted with strong warnings.
   - Coders may score V as high where they know a visible regulatory fight happened.
   Either way, the model's central V term is not supported in this panel.
4. **M (institutional memory) runs as predicted:** ρ = −0.51, so more memory goes with a shorter lag. This is exploratory.
5. **P11 (industry funding → longer lag) points the predicted way but is not significant:** r_rb = 0.26, with industry n = 4.
6. **P13 (distance → downstream first action) is null:** r_rb = 0.03, with downstream n = 7.
7. **Status:** exploratory, n = 31, coders not blind, and the case universe selected by EEA for known harm. These results should change priorities: re-examine how V is defined and coded before any confirmatory test, and test P16 with human coders blind to case identity. They do not settle the model.
