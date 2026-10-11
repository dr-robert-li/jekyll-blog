# P6 pre-specified coding (written before any budget outcome was viewed)

Written 2026-10-11, before the CAP budget file was downloaded. **Single-coder judgement** (the analysing agent). Not blind to the general literature (Jones et al. 2009 found leptokurtosis everywhere), but blind to topic-level kurtosis in this dataset.

## Hypothesis (committed)

H1 (one-sided): across CAP major topics, the asymmetry score A = (a) × (b) is positively rank-correlated with the excess (Fisher) kurtosis of annual percentage changes in real US budget authority.
Test: Spearman ρ, one-sided (ρ > 0), α = 0.05. Primary N = all major topics with a usable budget series.
Secondary (not confirmatory): A' = (a) + (b); L-kurtosis (τ4) in place of excess kurtosis.
Verdict rule: ρ > 0 and p < 0.05 → consistent; ρ ≤ 0 with p(ρ<0) < 0.05 → inconsistent; otherwise inconclusive.

## Rubric

(a) Harm diffuseness, 1–5: how spread out and delayed the costs of under- or over-provision are.
1 = cost lands immediately on an identifiable, organised group (e.g. a programme's own recipients stop being paid);
3 = mixed: some immediate identifiable losers, plus broad diffuse effects;
5 = costs are spread across the whole public and/or arrive years later (e.g. degraded environment, under-maintained infrastructure, lost research).

(b) Benefit concentration, 1–5: how concentrated the beneficiaries of the status quo allocation are.
1 = beneficiaries are the broad population with no organised stake;
3 = several organised constituencies of moderate size;
5 = a few well-organised producers/agencies/contractors/localities capture the benefit.

## Coding (CAP major topics; topic 23 Culture is not a budget topic in most US budget files and is coded in case it appears)

| Code | Topic | (a) | (b) | A=a×b | A'=a+b | One-line justification |
|---|---|---|---|---|---|---|
| 1 | Macroeconomics | 4 | 2 | 8 | 6 | Fiscal-management costs diffuse and delayed; beneficiaries broad (interest recipients diffuse). |
| 2 | Civil rights, minority issues, civil liberties | 4 | 2 | 8 | 6 | Under-enforcement harm is diffuse; small budget beneficiaries are advocacy groups. |
| 3 | Health | 2 | 4 | 8 | 6 | Cuts hit identifiable patients/providers fast; providers, insurers, pharma concentrated. |
| 4 | Agriculture | 4 | 5 | 20 | 9 | Costs borne by taxpayers/consumers diffusely; benefits concentrated on farm producers (classic case). |
| 5 | Labor and employment | 2 | 3 | 6 | 5 | Unemployment/pension cuts hit identifiable workers quickly; unions moderately organised. |
| 6 | Education | 3 | 3 | 9 | 6 | Harm to students delayed; teachers' unions and institutions organised. |
| 7 | Environment | 5 | 4 | 20 | 9 | Harm diffuse and delayed; under-provision benefits concentrated polluting industries. |
| 8 | Energy | 4 | 5 | 20 | 9 | Diffuse and delayed costs (prices, security); producers and utilities concentrated. |
| 9 | Immigration | 3 | 3 | 9 | 6 | Mixed; employer groups and border localities moderately concentrated. |
| 10 | Transportation | 4 | 4 | 16 | 8 | Infrastructure decay diffuse and delayed; contractors and localities concentrated (earmarks). |
| 12 | Law, crime, family | 3 | 3 | 9 | 6 | Crime harm partly local; law-enforcement and corrections constituencies moderate. |
| 13 | Social welfare | 1 | 2 | 2 | 3 | Cuts hit identifiable recipients immediately; beneficiaries broad and weakly organised. |
| 14 | Community development and housing | 3 | 4 | 12 | 7 | Housing harm moderately diffuse; builders, lenders, localities concentrated. |
| 15 | Banking, finance, domestic commerce | 4 | 5 | 20 | 9 | Regulatory/systemic risk diffuse and delayed; financial industry concentrated. |
| 16 | Defense | 4 | 5 | 20 | 9 | Security costs diffuse and delayed; contractors and base districts concentrated. |
| 17 | Space, science, technology, communications | 5 | 4 | 20 | 9 | Lost research is diffuse and very delayed; contractors/labs/universities concentrated. |
| 18 | Foreign trade | 4 | 4 | 16 | 8 | Trade costs diffuse on consumers; protected/exporting industries concentrated. |
| 19 | International affairs and foreign aid | 5 | 3 | 15 | 8 | Harm abroad and delayed; NGOs/contractors and foreign lobbies moderately concentrated. |
| 20 | Government operations | 4 | 3 | 12 | 7 | Administrative under-provision diffuse; federal employees moderately organised. |
| 21 | Public lands and water management | 4 | 4 | 16 | 8 | Resource degradation diffuse/delayed; western ranching, water and timber interests concentrated. |
| 23 | Culture (if present) | 4 | 3 | 12 | 7 | Cultural loss diffuse; arts institutions moderately organised. |

## Pre-specified robustness checks
1. Exclude tiny topics: drop topics whose mean real budget authority share is below 0.5% of the total.
2. Subtopics: if subtopic series are available, assign each subtopic its parent's score (no new coding) and rerun; report as weak check since the scores do not vary within major topic.
3. Periods: FY1947–1976 vs FY1977–end (pre/post Budget Act 1974 implementation), and full period.
4. A' (sum) and L-kurtosis.

## Confounds to report
Mandatory vs discretionary composition (Social welfare, Health, Labor dominated by mandatory entitlements and smooth); topic size (small series are noisier, more kurtotic); reorganisations/recoding (e.g. Energy dept 1977, Homeland Security 2003, budget function recodes).
