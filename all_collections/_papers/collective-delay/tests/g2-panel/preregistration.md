# G2 coded panel — Pre-registration

**Timestamp:** 2026-10-11T08:14:21+10:00 (2026-10-10T22:14:18Z)

**This plan was registered before any coding.** No coder has scored any packet. The outcome file (`outcomes.md`) is compiled by a separate process and is not shown to coders.

Status: exploratory. n = 31 cases (see `case-list.md`), so power is low; a null result here is weak evidence against the model and a positive result is not confirmation. Model reference: `q2-collective-delay-research.md` B.4, B.4.1, Part F (P1, P11), Part G (P13, P16), Appendix C §2.

## 1. Design

- **Case universe:** every hazard case chapter of EEA *Late lessons from early warnings* Vol. I (2001) and Vol. II (2013). Chosen before any search, so the search cannot drive selection. Exclusions and their reasons are listed in `case-list.md`. Selection caveat: EEA chose cases "where sufficient is now known about their impacts" (Vol. I), so the universe over-represents famous, harmful, delayed cases.
- **Predictors:** coded per `codebook.md` at t0 + 5 from evidence packets that contain only evidence dated at or before t0 + 5.
- **Coders:** at least three independent coders, each run on a different AI model, blind to outcomes and to each other.
- **Outcomes:** coded separately (definitions in §3), from EEA chapter tables and authoritative primary sources.

## 2. Aggregation and reliability

- Per case and variable, the panel score is the **median** of the non-IE coder scores. If fewer than two coders give a non-IE score, the variable is IE for that case.
- Carrier: majority of non-IE coders (tie → IE). Funding: modal category (tie → `mixed`).
- Inter-rater reliability: Krippendorff's α (ordinal for 1–5 scales, nominal for carrier and funding), reported per variable. A variable with α < 0.40 is reported but its test is flagged "unreliable" and not interpreted.
- Coders who say they recognised a case: all tests are repeated excluding scores from recognised cases (sensitivity analysis S1).

## 3. Outcome definitions (fixed now)

- **First meaningful regulatory action:** the first binding governmental measure (statute, regulation, ban, binding exposure, emission or catch limit, or binding international agreement, dated by adoption) in any national or supranational jurisdiction that targets the hazard. Excludes voluntary industry measures, non-binding guidance or advisory limits, research programmes, and sub-national measures.
- **Lag (years):** year of first meaningful action minus t0 (t0 as given in `case-list.md`).
- **Censoring:** if no qualifying action by 2026-10-11, lag is right-censored at 2026 − t0.
- **Locus of first action:** *root* = removes or reduces the agent or activity at its source (ban, phase-out, substitution mandate, production, emission or catch cap); *downstream* = controls exposure or harm while the source continues (workplace exposure limits, PPE, labelling or warnings, monitoring, compensation, clean-up, treatment, dispersal).

## 4. Hypotheses and tests

Family-wise α = 0.05, Holm–Bonferroni across the four primary tests. All tests one-sided in the stated direction. Uncorrected p-values are also reported.

| # | Hypothesis | Variables | Test | Direction (H1) | Falsified / not supported if |
|---|---|---|---|---|---|
| P1 | The composite of φ, L^R, V and r̂ predicts the rank of the lag | Composite C = (6 − φ) + L^R + V + r̂ (range 4–20); lag | Spearman ρ between C and lag. Censored cases enter with lag = censoring time and are ranked as tied at the top; sensitivity S2 excludes them | ρ > 0 (higher C, longer lag) | ρ ≤ 0, or one-sided Holm-adjusted p ≥ .05. ρ near zero (|ρ| < 0.15) is read as evidence against P1 |
| P11 | Industry-funded early research is associated with a longer lag | Funding (industry vs independent); lag | Mann–Whitney U, industry vs independent (mixed excluded). Secondary: Spearman with independent = 0, mixed = 1, industry = 2 | Industry lag > independent lag | No difference or the reverse |
| P13 | Greater causal distance is associated with a downstream first action | Causal distance; locus (downstream = 1, root = 0) | Mann–Whitney U on causal distance, downstream vs root groups. Censored cases (no action) excluded | Distance higher in downstream group | No difference or the reverse |
| P16 | Carrier presence is associated with shorter lag | Carrier (0/1); lag | Mann–Whitney U on lag, carrier = 1 vs carrier = 0. Censored cases as in P1 | Lag shorter when carrier = 1 | No difference or the reverse |

Effect sizes reported: ρ with bootstrap 95% CI (10,000 resamples); rank-biserial r for each U test.

**Exploratory, not tested for significance:** each component of C separately against lag; M against lag (prediction: higher M, shorter lag); a Cox model with C as covariate to handle censoring properly.

## 5. Missing data

- A case with IE on any component of C is excluded from P1 only. A case with IE on funding, distance or carrier is excluded from the test using that variable only.
- If more than one-third of cases are excluded from any test, that test is reported as "not evaluable".

## 6. Deviations

Any change to this plan after coding begins will be recorded below with a date and reason. Results will be reported for the plan as registered, whatever changes are made.

| Date | Change | Reason |
|---|---|---|
| — | — | — |
