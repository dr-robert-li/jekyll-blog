# P7.1 — deadline panel: lead-time analysis (EXPLORATORY)

**Prediction (P7).** For hazards with a public, dated deadline, comprehensive action lands near the deadline. Lead times are skewed toward zero, and the clustering strengthens with veto points (V) and with incumbents' stake in the status quo (L^R).

Script: `scripts/p7_deadlines.py`. Panels: `panel/p7-panel-{primary,expanded,durable}.csv`. Raw output: `out/p7-{primary,expanded,durable}/p7-results-raw.txt`.

## Panels

- **Primary (N = 7, 4 clusters).** The resolved members of report §7.1: DL3–DL9.
- **Expanded (N = 16, 6 clusters).** The primary panel plus:
  - six more US debt-limit episodes (2014, 2015, 2017, 2019, Oct 2021, Dec 2021);
  - two US tax sunsets (2010, the 2012 fiscal cliff);
  - the 2014 Highway Trust Fund shortfall.
- **Durable (N = 11, 5 clusters).** Expanded, minus actions that pushed the deadline back by less than about a year (Oct 2013, 2017, Oct 2021, 2010, HTF 2014). This applies §7.1's rule that the action must resolve the deadline "for at least several years". Because the rule is loose, I used a one-year cut-off.

Each date's source is in the `date_source` column.
- **Read on disk:** Treasury X-date letters (2013, 2014, 2015, 2017, 2019, Sep 2021); public laws 111-312, 112-240, 112-25, 113-159, 114-74; the USBR record of decision (21 Aug 2026); H. Rept 113-520.
- **Verified in a follow-up pass (2026-10-11), previously from model knowledge:** the signing dates of P.L. 113-83 (15 Feb 2014), 115-56 (8 Sep 2017), 116-37 (2 Aug 2019), 117-50 (14 Oct 2021), 117-73 (16 Dec 2021) and 119-21 (4 Jul 2025), each from the "Approved" line of the govinfo public-law HTML (`data-raw/govinfo-<law>/`). The 15 Dec 2021 X-date comes from Yellen's 16 Nov 2021 letter, Treasury press release jy0488 (`data-raw/treasury-jy0488/`). Every date matched the earlier value, so the results below are unchanged.
- **DL9's X-date** (15 Aug 2025) is the start of CBO's window, "between mid-August and the end of September 2025". Source: CBO Monthly Budget Review, May 2025, pub. 61302. cbo.gov blocked scripted access, so the copy on disk (`data-raw/cbo-61302/`) is a mirror of the same PDF. Using the window's earliest date gives a conservative lead. Treasury's 9 May 2025 letter said "in August", which would shorten the lead by about two weeks.

## Scoring (not blind; the scorer knew the outcomes)

- **V** counts partisan veto players (Tsebelis): distinct-party control of the House, Senate and presidency, plus one for a Senate filibuster pivot when the bill is not reconciliation.
  - Korea: 2 (divided government, unicameral).
  - Colorado: 8 (seven states plus the federal government).
- **L^R** is ordinal:
  - 3: resolution imposed concentrated losses on organised beneficiaries (benefit cuts, contribution rises, water cuts).
  - 2: resolution bundled contested spending or tax concessions.
  - 1: clean extension or transfer.
- **The L^R rule reads the content of the action.** That content is closely tied to the outcome. This is the main validity threat to the interaction test.

## Results

| | Primary | Expanded | Durable |
|---|---|---|---|
| Median lead (days) | 41 | 8 | 12 |
| Share within 90 days | 0.86 | 0.94 | 0.91 |
| Share after the deadline | 0.00 | 0.19 | 0.18 |
| Members in the first quarter of a 365-day window (binomial p vs 0.25) | 6/7 (p = .001) | 15/16 (p < .001) | 10/11 (p < .001) |
| Cluster medians, KS D+ vs uniform (W = 730 days) | 0.65, p = .018 | 0.73, p < .001 | 0.70, p = .003 |
| V vs lead, ρ (predicted < 0) | −0.44 (p = .16) | −0.24 (p = .19), CI [−0.90, 0.31] | −0.15 (p = .33) |
| L^R vs lead, ρ (predicted < 0) | **+0.78** | **+0.53**, CI [0.11, 0.89] | **+0.66** |
| V×L^R vs lead, ρ | +0.22 | +0.19 | +0.28 |

## Verdict

- **Skew toward the deadline: supported.** This holds in all three panels, at both the member and the cluster level. Within a two-year window, only Korea (about 30 years early) lies outside the first quarter.
  - About a fifth of expanded members land just after the deadline: the 2012 fiscal cliff (−2 days), Dec 2021 (−1 day) and the Highway Trust Fund (−7 days).
  - The debt limit supplies 9 of the 16 members. They share one institution, so cluster-level tests are the honest ones, and they are significant only in the expanded and durable panels.
- **The interaction that distinguishes the model: not supported.**
  - V has the predicted sign but is weak and not significant.
  - L^R has the **opposite** sign: members with concentrated losses (1983 Social Security, Korea, Colorado) acted *earlier*. Two readings fit equally well:
    - members with high L^R are the long-horizon pension and water cases, so horizon length is confounded with L^R;
    - the L^R coding reads the content of the action (see Scoring).
  - So P7's distinctive claim gets no support here. What is supported is the generic deadline effect, which rival models also predict.
- **Recommendation.**
  - Keep the P7 skew prediction.
  - Re-test the interaction only with V and L^R scored blind by independent coders, using the g2 coder protocol, and with horizon length (time from first projection to the deadline) as a covariate.
  - Use the open members DL1, DL2 and DL10 as the forward test.
