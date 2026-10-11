# G2 forward registration — dated predictions on open cases

**Timestamp:** 2026-10-11T08:14+10:00. Registered before any of the events below is known.

**Deposit:** this file should be deposited on OSF (osf.io, "Registrations", open-ended template, or as a frozen file in an OSF project) by the user to obtain a public, immutable timestamp. The assistant cannot do this. Until it is deposited, the git commit hash of this file is the only timestamp.

Model reference: `q2-collective-delay-research.md` B.4/B.4.1, Part F (P7, P13–P16, P22, P24), Part G, Appendix B §7.1 (DL1, DL2, DL10), Appendix C §3, §5. Facts used as baselines carry the tags given in the research file; none were re-verified in this session.

Scoring rule for every item: each prediction is scored **hit**, **miss** or **void** (the triggering condition did not occur, or the observable was not published) at its resolution date, using the named source. A void is not a hit.

---

## 1. P7 open members (deadline panel)

The model predicts that comprehensive action lands close to the deadline, and closer when veto points and incumbent L^R are high.

| ID | Member | Deadline (baseline) | Prediction | Resolves | Falsified if | Source to check |
|---|---|---|---|---|---|---|
| F7.1 | US OASI trust fund | Depletion Q4 2032 (2026 Trustees Report; App. B DL1) | No comprehensive Social Security solvency law is enacted before **1 Oct 2030**. "Comprehensive" = a law that the SSA Chief Actuary scores as extending OASI (or combined OASDI) reserve depletion by ≥ 10 years. If one is enacted, it is enacted between 1 Oct 2030 and the depletion date. | 31 Dec 2032 (or depletion, if later) | A comprehensive law is enacted before 1 Oct 2030 | congress.gov; SSA OCACT letters on legislation |
| F7.2 | US Medicare HI trust fund | Depletion Q2 2033 (2026 Trustees Reports; DL2) | No law scored by the CMS Chief Actuary as extending HI depletion by ≥ 10 years is enacted before **1 Apr 2031**. | 30 Jun 2033 | Such a law is enacted before 1 Apr 2031 | congress.gov; CMS OACT memoranda |
| F7.3 | F7.1 and F7.2 together | — | Whichever of OASI/HI is resolved first, its law lands within 24 months of its own depletion date; the two are not resolved by one law more than 24 months before the earlier depletion date. | 30 Jun 2033 | A joint law > 24 months early | as above |
| F7.4 | Kigali Amendment, non-Article 5 HFC steps (85% cut by 2036; DL10) | Each step year Y (intermediate step years to be confirmed from the treaty text before scoring; App. B DL10 abstains on them) | For the EU and the US, the binding measure that sets HFC allowances or quotas for step year Y is adopted **within 24 months before 1 Jan Y**, not earlier. | 1 Jan of each step year through 2036 | For two or more steps, the governing measure is adopted ≥ 24 months before the step | EUR-Lex (F-gas Regulation and implementing acts); Federal Register (EPA AIM Act allocation rules) |
| F7.5 | Interaction (the model's distinctive claim) | — | Across the open and resolved P7 members, once V and L^R are scored blind to lead time, lead time is negatively rank-correlated with V + L^R (Spearman ρ < 0). | When the panel has ≥ 10 resolved members | ρ ≥ 0 | App. B §7.1 panel, scored per `codebook.md` §2.2–2.3 |

## 2. P22 — attribution tools speed carriers, not root reform

Prediction form: in each domain the first **carrier event** comes before the first **root reform**, and attribution-tool availability shortens time to carrier but not time to root reform.

| ID | Domain | Attribution tool | Carrier event (observable, date) | Root reform (observable) | Prediction | Resolves | Falsified if |
|---|---|---|---|---|---|---|---|
| F22.1 | Climate liability | Extreme-event attribution (WWA-type rapid studies; source attribution to emitters) | A national court judgment (not a settlement) that holds a private fossil-fuel or cement company liable in principle or in damages for a climate harm, relying on attribution evidence (Sabin Center climate litigation database) | A G20 member enacts a binding statutory end date for domestic fossil-fuel **production** | At least one carrier judgment occurs by 31 Dec 2030, and no G20 member enacts a production end date before the first such judgment | 31 Dec 2030 | A G20 production end date is enacted before any such judgment; or no such judgment by 2030 while attribution studies keep growing (carrier not sped) |
| F22.2 | Wildfire and property insurance (California chain) | Forward-looking catastrophe models now permitted in rate-setting (CDI Sustainable Insurance Strategy, Dec 2024; App. C CA12) | Either a second FAIR Plan member assessment, or an admitted insurer's filed non-renewal programme of ≥ 10,000 California homeowner policies | Any California or federal measure that reduces emissions beyond the existing cap-and-invest path to 2045 (CA13) | At least one carrier event occurs by 31 Dec 2028, and the next new California wildfire statute or regulation after it is at the insurance, utility or land-use tier, not the emissions tier | 31 Dec 2028 | The next new measure after the carrier event is at the emissions tier |
| F22.3 | Social media and adolescents | Platform internal-data disclosure and DSA Art. 34–35 risk assessments plus Art. 40 researcher data access | First final DSA non-compliance decision with a fine against a very large platform on minors' protection or addictive design (App. C SM5: only preliminary findings in 2026) | A US federal statute imposing a design duty of care or independent pre-release research duty on platforms | The EU fine comes before any such US statute | 31 Dec 2028 | A US federal design-duty statute is enacted before any DSA minors' fine |

## 3. P24 — obligatory passage point

| ID | Indicator | Prediction | Resolves | Falsified if |
|---|---|---|---|---|
| F24.1 | Under the EU DSA, the share of formal disputes (court actions before the CJEU/General Court, Digital Services Coordinator decisions under Art. 40, and Commission proceedings) that concern **access to, or audit of, platform data and models** (vetted-researcher access, auditor access, algorithmic transparency), as a share of all formal disputes that concern either access or the **causal claim** that platform design harms minors | The access share rises above 50% in calendar year 2029, from a lower share in 2025–2026 | 31 Mar 2030 (count from Commission DSA enforcement pages, DSC annual reports and CJEU case search) | Access share ≤ 50% in 2029, or not higher than the 2025–26 share |

Coding note: count each proceeding once, by its principal subject, coded blind to this prediction by a second coder.

## 4. P13–P16 forward predictions for the four current chains (Appendix C §3)

| ID | Chain | Test | Prediction (event, by when) | Resolves | Falsified if |
|---|---|---|---|---|---|
| F13.a | (a) French debt | P13 | Through 31 Dec 2028, no law raises the legal pension age above 64 or durably de-indexes pensions (≥ 2 consecutive years below inflation); consolidation measures adopted are one-off or downstream (temporary surtaxes, spending freezes, ONDAM caps). | 31 Dec 2028 | Either root measure is enacted by then |
| F16.a | (a) French debt | P16 | The general government deficit is not ≤ 3.0% of GDP in any year to 2029 unless, in the preceding 24 months, a carrier event occurred: a downgrade by Moody's, S&P or Fitch to A or below, a Council decision under TFEU Art. 126(8) or (9), or a 10-yr OAT–Bund spread above 150 bp for ≥ 20 trading days. | INSEE first estimate for 2029 (March 2030) | Deficit ≤ 3.0% with no carrier event in the prior 24 months |
| F13.b | (b) California wildfire | P13 | Of California wildfire-related statutes chaptered in the 2027 and 2028 sessions, more than 75% target the utility, insurance, suppression or land-use tier; fewer than 25% target emissions. | 31 Dec 2028 (leginfo.legislature.ca.gov) | ≥ 25% at the emissions tier |
| F16.b | (b) California wildfire | P16 | See F22.2. | 31 Dec 2028 | as F22.2 |
| F13.c | (c) Social media | P13 | Any US federal youth social-media statute enacted by 31 Dec 2028 is at the downstream tier (age limits, age verification, parental controls, school phones), not a product-level design or research-access duty. | 31 Dec 2028 | A federal design or research-access duty is the first such statute |
| F16.c | (c) Social media | P16 | Within 12 months of the first DSA final fine on minors' protection (F22.3), the fined platform announces EU product changes for minors; no comparable US-wide change by that platform precedes the fine. | 12 months after the fine | No EU change within 12 months, or a US-wide change before the fine |
| F15.d | (d) Obesity / GLP-1 | P15 | If CMS makes Medicare coverage of GLP-1 drugs for obesity permanent (beyond a pilot), then the number of US federal bills on food-tier measures (sugar-drink taxes, mandatory front-of-pack labelling, ultra-processed food marketing limits) introduced per Congress falls in the Congress after coverage relative to the mean of the 117th–119th Congresses. | End of the first full Congress after coverage | Bill count unchanged or higher (void if coverage is not made permanent by 2030) |
| F13.d | (d) Obesity / GLP-1 | P13 | By 31 Dec 2028, US federal action on obesity has expanded drug coverage or pricing (downstream) and has **not** finalised a mandatory front-of-pack nutrition labelling rule or ended GRAS self-affirmation (root tier). | 31 Dec 2028 (Federal Register) | Either root rule is finalised by then |

## 5. What would count against the model overall

- F7.1, F7.2 and F7.4 all miss (action lands early): the deadline-clustering claim fails for open members.
- In P22 domains, root reform precedes carriers in two or more of F22.1–F22.3.
- Three or more of the chain predictions F13.a–F13.d are falsified.

Misses are reported with the same prominence as hits.

---

## 6. Amendment 1 — P1 specification (2026-10-11T11:40+10:00)

Added after the exploratory panel and before any forward case resolves. Sections 1–5 are unchanged. Rationale: `composite-review.md`. Coding rules: `codebook.md` §5.

**Applies to:** every forward case and any fresh retrospective case set coded after this date. It does not apply to the 31-case exploratory panel (K01–K31), whose results stand as reported.

### 6.1 Composites (weights fixed here, never fitted)

Every 1–5 scale is rescaled with s(x) = (x − 1)/4. Harm magnitude is rescaled with h = H/5.

- φ_eff = s(φ) + s(M)
- V_net = s(V) − 0.5·carrier
- Barrier = s(L^R) + V_net + s(r̂)

| Role | Name | Formula |
|---|---|---|
| **Primary** | **B** (threshold crossing) | B = (Barrier + 0.25) / (φ_eff·h + 0.25) |
| Secondary | A (net drive) | A = Barrier − φ_eff·h |
| Reported alongside, for continuity | C (original) | C = (6 − φ) + L^R + V + r̂ |

- V enters with a positive sign and is not dropped.
- If A and B disagree in sign, P1 is reported as **indeterminate**.

### 6.2 Test

- **Outcome:** time from t0 to the first meaningful regulatory action, as defined in the outcome coding for the panel. Cases with no action are censored at the analysis date.
- **Model:** a Cox proportional-hazards model of action, with B and t0 (calendar year) as covariates.
- **Prediction:** the hazard ratio for B is below 1, meaning a higher B gives later action. One-sided test, α = 0.05.
- **Also reported:**
  - Spearman ρ of B with lag, with censored cases ranked at the top;
  - the same analysis for A and for C;
  - a check of the proportional-hazards assumption (Schoenfeld residuals).
- **Minimum sample:** 15 resolved cases. Below that, the result is descriptive only.

### 6.3 Conditions for a valid test

All of these come from `codebook.md` §5.

- **Scoring point:** set by the §5.1 rule.
- **De-identified packets:** prepared under the §5.2 protocol.
- **Recognition and leakage probes:** run under §5.3, with case–coder pairs excluded as specified there.
- **Harm magnitude H:** coded on the §5.4 scale.

If the panel-level leakage check fails, the P1 result is reported as **contaminated** and does not count for or against the model.
