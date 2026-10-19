# G4 — Results

**Run:** analysis.py on four coder files (haiku, sonnet, opus, fable). Packets were frozen in commit `1f86041` before coding; the registration is commit `6a75478`, with the timestamp corrected in `acf6b05`.

**Panel:** 15 cases, 174 episodes, no exclusions.

**Decision under preregistration §8: MIXED.**
- H3 passes.
- H1 does not reject the null.
- H2 and H4 are not falsified.

Prop 3 therefore goes in a footnote and an appendix of the planned paper, not in its main body.

## 1. Reliability (Krippendorff's α, nominal)

| Variable | α | Units |
|---|---|---|
| challenger | 0.801 | 163 |
| supported | 0.653 | 174 |
| target | 0.948 | 161 |
| success | 0.604 | 174 |
| content_reopen | 0.806 | 174 |
| ground | 0.700 | 105 |
| scope | 0.881 | 42 |

All values are at or above the 0.40 threshold, so no test is flagged unreliable.

**Recognition.**
- Sonnet, Opus and Fable recognised all 15 cases.
- Haiku recognised 14 of 15 and did not recognise G15.

## 2. Hypotheses (primary analysis: all coder–case pairs)

| | Prediction | Result | One-sided p | Verdict |
|---|---|---|---|---|
| **H1** | Lone challengers reopen the model's content less often than organised ones | Lone 0/4; organised 38/156 (24%) | .33 (Fisher) | **Not rejected.** Direction as predicted, too few lone episodes to test. Case-level sign test: 2 cases lower, 0 higher, p = .25 |
| **H2** | Lone wins are mostly procedural | 0/1 | — | Descriptive only (fewer than 5 lone successes) |
| **H3** | The first content reopening in each case is by an organised challenger | 12/12 cases | .0002 | **Supported** |
| **H4** | Content reopenings cover the whole class | 21/37 episodes (57%) | .26 | Not falsified, not significant |

**First content reopening per case.** All were by organised challengers:
- G02 E1: a union suit;
- G04 E2: a supervisory review;
- G05 E12: a commission review;
- G06 E2: a commissioned reanalysis;
- G08 E17: legislation;
- G09 E8: a government decision;
- G10 E1: an NGO coalition suit;
- G11 E6: a government audit;
- G12 E2: federal regulator action;
- G13 E3: a funded pre-action letter;
- G14 E3: a legal-aid suit;
- G15 E2: a civil-liberties class action.

Three cases had no content reopening by the panel's modal coding: G01, G03 and G07.

## 3. Sensitivity analyses (reported, not decisive)

| | H1 | H2 | H3 | H4 |
|---|---|---|---|---|
| **S1:** recognised pairs excluded | 0/1 vs 1/1 | — | 1/1 | 1/1 |
| **S2:** supported individuals recoded as lone | 1/9 vs 37/151, p = .32 | 2/5 procedural: **falsified** | 11/12, p = .003 | 21/37 |
| **S3:** each case weighted equally | lone 0.00 vs organised 0.35 | — | — | case-mean class share 0.79; 9 of 11 cases above 0.5 |

**S1** leaves almost no data, because recognition was near-universal. The registered primary analysis includes recognised pairs for that reason.

**S2.** When named individuals backed by legal aid or another organisation are counted as lone, they win on the merits as often as on process. Examples are the welfare-debt test cases (G09 E4, E7) and the home-care injunction (G14 E2). That is consistent with the model, which treats the backing organisation's resources as an organised stake. It shows that the H2 prediction only holds if those cases are excluded.

**S3.** H4 is held down at the episode level by G04, where 14 of 15 reopenings are national measures scoped to a *group* (one jurisdiction's banks). Weighting each case equally, reopenings covered everyone in most cases.

## 4. Reading

- **What the panel shows.**
  - In every case where a shared model's attributions were reopened for everyone, an organised actor did it first (H3).
  - Reopenings mostly covered everyone (H4 case-weighted).
  - The four lone challenges in the panel reopened nothing (H1, in the predicted direction).
- **What the panel cannot show.** The comparison H1 needs, between lone and organised challengers, is close to empty: 4 lone episodes against 156 organised.
  - This is itself what Prop 3(b) predicts: lone parties do not take on shared models at all.
  - But it is also what the design predicts. The registration's §6 warned that unreported individual challenges would be under-counted.
  - Preparers listed formal episodes documented in authoritative sources. Individual tribunal appeals and complaints appear mostly as aggregated episodes, which coders classed as organised or unclear.
  - Three coders also coded named individuals with unreported funding as `unclear` rather than `lone`. The codebook left this open.
  - The test cannot separate "lone parties don't challenge" from "lone challenges aren't recorded".
- **What would settle it.** A panel built from individual-level records, for example a random sample of tribunal or administrative appeal decisions against a shared model, coded for outcome and ground. Neither this panel nor its sources can supply that.

## 5. Deviations from the plan

1. **S3 for H4 was computed outside `analysis.py`.** The script implemented S3 only for H1. The registration specifies S3 for "case-level mean of episode outcomes" generally, so the H4 version was computed afterwards, from `panel-aggregated.csv`, with the case-level mean of the class share. It does not affect the decision rule.
2. **The registration timestamp was corrected (commit `acf6b05`) before packet preparation.** See `preregistration.md`.
3. **One cross-reference in packet G14 E4 was corrected** after the second-preparer review and before coding ("E2 injunction" → "E3 injunction"; logged in `prep/review-log.md`).

No hypothesis, test or threshold was changed.

## 6. Limits specific to this run

- **Coders recognised the cases.** Near-universal recognition means classifications could reflect what coders knew, despite the instruction to code only from the packet.
- **Some sources were not fetched.** Several G03, G04 and G06 sources were cited from the preparers' memory and not fetched. Those are flagged in `prep/*-notes.md`.
- **The cases were selected with outcomes known.** See preregistration §4.3.
