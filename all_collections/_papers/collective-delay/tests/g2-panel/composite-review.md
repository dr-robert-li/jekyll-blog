# G2 panel — Review of P1's composite C (EXPLORATORY)

Written 2026-10-11, **after** the P1 result was known. Nothing here changes `preregistration.md`, `codings/` or the primary results in `results.md`. P1 on this panel stays **not supported** (ρ = −0.30 [−0.59, 0.05]).

**This is not a confirmatory test.** Any composite proposed here was chosen by someone who had seen how the 31 cases scored and how long their lags were. The same 31 cases cannot confirm it. Their numbers below only describe how the specification behaves. Only the forward cases (`forward-registration.md`) or a fresh case set, coded blind, can test a revised composite.

Code: `composite_review.py` (run with `../g1-data/.venv/bin/python -I composite_review.py`). Lag is ranked with censored cases tied at the top, as in `analysis.py`.

## 1. Do the coded directions match the model's signs?

| Component | Codebook: higher score = | Model term | Predicted sign for lag | In C as | Verdict |
|---|---|---|---|---|---|
| φ | more perceptible harm | φ·H in act_i | − | 6 − φ (+ for lag) | Direction correct |
| L^R | more concentrated benefit | −L^R in act_i; +δL^R_elite in V | + | +L^R | Direction correct, but counted twice (also inside V) |
| V | stronger veto | t* needs P > V | + | +V | **Direction correct, not inverted.** The anchors (§2.3: 1 = no opponent, 5 = captured regulator) match the model's V. So the ρ = −0.45 is not a coding-direction error. |
| r̂ | more hidden concern (larger δ) | +β(r − δ) | + | +r̂ | Direction correct |
| M | stronger standing institutions | φ = φ0·e^{−λ(t−t_base)} + M | − | **missing** | M is part of φ in the model, yet C leaves it out |
| dist | more causal links | G.1: φ_k ≈ φ0·∏a_j + M | + | missing | Partly double-counted with φ-att |
| carrier | active carrier | raises H_elite, so lowers V (G.1.5) | − | missing | The V that coders scored is V0 + δL^R_elite with no −γH_elite term |

No component is coded backwards. C fails for other reasons.

**Specification problems (from the model, before looking at the data):**

1. **M is left out.** In B.4.1, M adds to φ. C uses the φ score alone, so the institutional-memory route to quick action is missing.
2. **The γH_elite term is left out.** V as coded counts blocking capacity only. The model's V falls when harm reaches the elite, and the carrier variable is the codebook's proxy for that. C has no term for it.
3. **L^R is double-counted.** It enters directly and again through V (δL^R_elite). Spearman ρ(L^R, V) = 0.62.
4. **The functional form is wrong.** act_i is a threshold on φ·H − L^R + β·r̂. If filtered harm grows over time, the crossing time scales as barrier ÷ (φ·growth). Under that form, a low φ makes the barrier matter more. An additive sum has no such interaction. H, the size and growth of the harm, is not coded at all.
5. **r̂ is outside the model's scope here.** B.4 scope: "where few decision-makers decide … the r̂ cascade term is idle." Most EEA cases were decided by a regulator, not by a mass cascade.

**Design problems (not about the formula):**

6. **Scores are taken after the outcome.** Every variable is scored at t0 + 5. In 9 of 31 cases action came at lag ≤ 5, so V, M and carrier describe the fight that had already happened. A high V there can mean "there was a visible fight, which ended in regulation".
7. **Era confound.** t0 runs from 1896 to 1999. Lag is capped mechanically at 2026 − t0, and later hazards met an existing regulatory state. t0 correlates with lag at ρ = −0.50, and with V (+0.29), M (+0.38) and carrier (+0.41). Early hazards (X-rays, benzene, climate, DES) score low on V and M because no lobby or agency yet existed, and they have long lags because no regulator existed either.

## 2. Intercorrelations and the cases that drive the reversal

Spearman ρ (n = 31; carrier n = 27):

|  | φ | L^R | V | r̂ | M | dist | carrier | t0 | lag |
|---|---|---|---|---|---|---|---|---|---|
| φ | 1 | .15 | .16 | .35 | .16 | −.22 | .11 | −.39 | .12 |
| L^R |  | 1 | .62 | .60 | .24 | .06 | .30 | .09 | −.13 |
| V |  |  | 1 | .73 | .50 | .42 | .56 | .29 | −.45 |
| r̂ |  |  |  | 1 | .46 | .04 | .35 | .11 | −.10 |
| M |  |  |  |  | 1 | .08 | .46 | .38 | −.51 |
| dist |  |  |  |  |  | 1 | .43 | .35 | −.38 |
| carrier |  |  |  |  |  |  | 1 | .41 | −.59 |

- L^R, V and r̂ form one cluster (ρ = .60 to .73). Three of the four terms in C largely measure the same thing: an organised, secretive incumbent.
- V travels with M (.50) and carrier (.56). Both of those predict a *shorter* lag. High-V cases in this panel are also the ones with institutions and carriers already active.

**Partial ρ with lag, controlling for t0:** C −0.17, V −0.37, M −0.40, dist −0.25, φ −0.09. The era confound explains part of the reversal, not all of it. V stays negative.

**Cases with the largest gap between C rank and lag rank:**

| Case | t0 | φ | L^R | V | r̂ | M | carrier | C | lag | Reading |
|---|---|---|---|---|---|---|---|---|---|---|
| K11 Nuclear accidents | 1986 | 2.5 | 5 | 5 | 4 | 5 | 1 | 17.5 | 0 | Action is immediate and scored after the fact; M = 5 (a standing body) |
| K21 BSE | 1986 | 2.5 | 3 | 5 | 5 | 4 | 1 | 16.5 | 2 | High V and high r̂, but the harm reached the elite (beef market, carrier) |
| K07 Tobacco | 1981 | 1.5 | 5 | 5 | 5 | 4.5 | 1 | 19.5 | 6 | t0 = 1981 (manipulation chapter). Action dated from a late warning |
| K18 X-rays | 1896 | 4.5 | 2 | 1.5 | 2.5 | 1 | 1 | 7.5 | 65 | No regulator in the era; M = 1 |
| K13 Benzene | 1897 | 3 | 2.5 | 1.5 | 1.5 | 4 | 0 | 8.5 | 66 | Same era effect |
| K02 Climate | 1897 | 1 | 2 | 2.5 | 1 | 1 | 0 | 10.5 | 93 | Low φ and M are right, but the low V score looks implausible |
| K26 Ethinyl oestradiol | 1978 | 2 | 2 | 2 | 3 | 3 | 0 | 11.0 | 48 (censored) | Low veto, no carrier, no action |
| K19 DES | 1938 | 1 | 2 | 1.5 | 1 | 3 | 0 | 9.5 | 33 | Era, and a low φ that C underweights |

Two patterns drive the reversal:

- **Early-era cases with low V and long lags:** K18, K13, K02, K19.
- **Modern high-V cases with an active carrier or memory, where action came within the scoring window:** K11, K21, K07.

## 3. Revised composites, derived from the model (post-hoc, non-confirmatory)

All scales are rescaled to 0–1 as s(x) = (x − 1)/4. The weights below were fixed from the equations, not fitted. The 0.5 carrier weight is a prior choice: an active carrier is assumed to cancel half the V range.

- φ_eff = s(φ) + s(M). From φ = φ0·e^{−λ(t−t_base)} + M.
- V_net = s(V) − 0.5·carrier. From V = V0 − γH_elite + δL^R_elite.
- Barrier = s(L^R) + V_net + s(r̂).

**Composite A (net drive, additive):** A = Barrier − φ_eff. This is the sign structure of act_i with M and the carrier added.

**Composite B (threshold crossing):** B = (Barrier + 0.25) / (φ_eff + 0.25). If filtered harm φ_eff·H grows roughly linearly, the crossing time t* ∝ barrier / φ_eff. The 0.25 floors keep the ratio finite.

Behaviour on these 31 cases (descriptive only; n = 27 where carrier is not missing):

| Spec | ρ with lag | ρ, lag > 5 only | Partial ρ given t0 |
|---|---|---|---|
| C (pre-registered) | −0.30 | −0.34 (n = 22) | −0.17 |
| A | −0.09 | −0.28 (n = 19) | −0.08 |
| B | −0.03 | −0.22 (n = 19) | −0.05 |

Reading:

- The revised forms remove most of the reversal but do **not** produce the predicted positive ρ.
- The gain comes almost entirely from the carrier term. The carrier was already the supported P16 variable, and it is the one most open to contamination by coders who know the outcome.
- Raising the carrier weight to 1.0 turns A positive (ρ = +0.11). Weight 0.25 gives −0.18; weight 0 gives −0.28. That is exactly the forking path a post-hoc search would exploit. Do not tune it on these data.
- Restricted to cases where the scores came before the action (lag > 5), all specifications stay negative. That means the model's veto logic has no support in this panel even after the obvious repairs. This holds subject to the caveats below.

## 4. Recommendation

Pre-register **Composite B** (threshold form) as the primary P1 composite for the forward cases and any fresh case set. Report C alongside it, so the change of specification is visible. Reasons:

- B is the form the act_i/t* equations imply.
- B includes M and the H_elite (carrier) term, which C leaves out.
- B gives a falsifiable interaction: the barrier matters more when φ_eff is low.

Fix these before any coding:

1. **Weights.** Carrier = 0.5 and floor = 0.25 as above, or values justified from the theory and set before coding. Never fitted.
2. **Scoring point at t0 + 2, or the date of the earliest packet item, and always before the earliest action.** Coders should see no packet item dated after the scoring point. This removes the post-outcome scoring problem.
3. **Era stratum or covariate.** Report a partial ρ controlling for t0, or restrict the sample to t0 within one regulatory era (for example post-1960). Use a Cox model with C/B as the covariate, so censoring and the lag cap are handled properly. Install lifelines first.
4. **Blind coders.** Use human coders, or models given fully de-identified packets, with a check that they do not recognise the case. S1 was not evaluable here.
5. **A coded H term,** the magnitude of harm at the scoring point. Without it, φ·H can only be approximated by φ.
6. **Hold-out rule.** Treat A as a secondary specification. If A and B disagree in sign, report P1 as indeterminate.

Not recommended: dropping V, or entering V with a negative sign. Either would fit this sample and turn P1 into an unfalsifiable accommodation of the reversal.
