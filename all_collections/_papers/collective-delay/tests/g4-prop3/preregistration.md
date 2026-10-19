# G4 — Prop 3 (case-by-case reopening vs all-at-once closure) — Pre-registration

**Timestamp:** 2026-10-19T21:03:25+10:00 (2026-10-19T11:03:25Z), the time of registration commit `6a75478`. The header first written in that commit read 2026-10-20T06:59:23+10:00, taken from an unsynchronised system clock; it was corrected to the commit time in the next commit, before any packet was prepared.

**This plan was registered before any packet was prepared or coded.** No coder has seen any material. The case key (`case-list.md`) is not shown to coders.

**Status:** exploratory. The panel is small (15 candidate cases), and the cases were chosen by people who already know how most of them ended (§4.3). A pass here is weak support for the proposition, not confirmation. A fail removes Prop 3 from the main body of the planned paper (§8).

**Model reference:** `q2-collective-delay-research.md` Part G (G.1 carriers, G.2 accreted wickedness), Part H (H.3 reification, H.4 points 2–4: punctualisation, carriers, obligatory passage point), and the council-revised claim in `docs/Model Council Synthesis Attribution and Punctualisation.md` ("carriers reopen black boxes case by case, while a shared model closes one over all cases at once").

---

## 1. The claim in words

When attributions (of fault, risk, debt, performance or harm) for many cases rest on case-specific reasoning, any affected party can reopen their own case. When they rest on one shared model, reopening any case's attribution means reopening the model. That costs more, because the model's operators and beneficiaries defend it on behalf of every case. Above a scale threshold, no single affected party can afford it. The model then closes all the cases at once, and only an organised actor (a coalition, an organisation that funds the challenge, or an institution with a mandate) can reopen it. When that happens, it reopens all the cases at once. The individual wins that remain are procedural: they get a party notice, an explanation or a human review in their own case, and leave the model's attributions untouched.

## 2. Model

**Cases and stakes.** There are N ≥ 2 dependent cases. The affected party in case i places value h_i on having the attribution in its case reopened.

- **A1 (bounded individual stakes).** 0 ≤ h_i ≤ h̄ < ∞ for every i.

**Contest technology.**

- **A2.** An actor that pays the cost of a route succeeds with probability q ∈ (0, 1]. q is the same across routes. This is a simplification; §6 lists what relaxing it changes.

**Bespoke regime.** Each attribution rests on a case-specific basis. Reopening case i costs c > 0 and reopens case i only.

**Shared regime.** One model B underlies all N attributions. Two routes are open.

- **A3 (procedural route).** At cost c_p > 0 a party obtains relief in its own case only: notice, disclosure, explanation, human review or reconsideration. The relief applies B as it stands. B's content and every other case are unchanged.
- **A4 (content route).** Contesting B's content costs C(N) = c₀ + κN, with c₀ ≥ c and κ > 0. Defence effort grows with N because the operator's and beneficiaries' stake in B grows with the number of attributions it licenses (G.2: each layer gains beneficiaries who join the veto).
- **A5 (non-excludability).** If B's content is reopened, the attributions in all N cases are reopened.

**Actors.**
- A **lone party** acts on its own stake h_i.
- An **organised actor** acts on a stake that aggregates across m ≥ 2 cases. Examples:
  - a coalition or group action with total stake Σ h_j over its members;
  - a funding organisation such as legal aid, a union or an NGO;
  - an institution whose mandate covers the class of cases.

## 3. Proposition 3 and proof

Define the scale threshold N* = (q·h̄ − c₀)/κ. If q·h̄ ≤ c₀, then N* ≤ 0 and every N is above it.

**Proposition 3.** Under A1–A5:

**(a) Bespoke reopening does not depend on scale.** Party i reopens its case if and only if q·h_i ≥ c. The share of cases with a party willing to reopen is 1 − F(c/q⁻), where F is the distribution of stakes, whatever N is.

**(b) Above the threshold, no lone party contests content.** For N > N*, no lone party takes the content route, whatever its stake.

**(c) Content is reopened only by organised actors.** For N > N*, B's content is reopened only by an actor whose stake H satisfies q·H ≥ C(N). A coalition of parties with stake at most h̄ each needs at least m* = ⌈C(N)/(q·h̄)⌉ ≥ 2 members.

**(d) No coalition forms spontaneously.** Suppose a group must form voluntarily from parties who each chose to contribute C(N)/m* and the good is provided if and only if at least m* contribute. If m* ≥ 2, then the profile in which nobody contributes is a Nash equilibrium.

**(e) Reopening is all at once in the shared regime.** A successful content contest reopens N attributions. A successful bespoke contest reopens 1.

**(f) Lone wins are procedural.** For N > N*, every lone-party success in the shared regime comes through the procedural route and leaves B's content and the other N − 1 attributions unchanged.

**Proof.**

(a) A lone party in the bespoke regime gains q·h_i at cost c, and the gain does not depend on any other case. It acts if and only if q·h_i ≥ c. Neither side of that condition involves N.

(b) For N > N*, we have κN > q·h̄ − c₀, so C(N) = c₀ + κN > q·h̄ ≥ q·h_i for every i (A1). The expected gain from the content route is below its cost for every lone party.

(c) An actor takes the content route only if q·H ≥ C(N). By (b), no single h_i satisfies this for N > N*. For a coalition of m members, H ≤ m·h̄, so we need m ≥ C(N)/(q·h̄) > 1. Hence m* ≥ 2.

(d) Take the profile in which nobody contributes. A single party that deviates and contributes pays C(N)/m* > 0. With m* ≥ 2, one contributor is fewer than m*, so the good is still not provided and the deviator's payoff falls. No unilateral deviation pays, so the profile is a Nash equilibrium.

(e) This is A5 for the shared regime, and the definition of the bespoke regime for the other.

(f) By (b), no lone party takes the content route when N > N*. Any lone-party success therefore comes through the procedural route, which leaves B's content and the other cases unchanged by A3. ∎

**What this does and does not establish.**

The proposition is a statement about the stylised model, not about the world. It needs four assumptions:
- bounded individual stakes (A1);
- a defence cost that grows with scale (A4);
- non-excludable reopening (A5);
- a procedural route that leaves the model intact (A3).

Part (d) shows that coordination can fail. It does not show that coordination fails more often as N grows. A theory of equilibrium selection would be needed for that, and none is assumed here.

## 4. Empirical test

### 4.1 Unit and regime

The unit of observation is a **challenge episode** within a **case**. A case is a shared model (§4.2). The panel tests only the shared regime above the threshold. Every candidate case licenses at least hundreds of attributions, so N is large relative to any individual stake. The bespoke side of the comparison, (a) and the "1" in (e), holds by construction and is not tested.

### 4.2 Case universe (fixed now)

**Inclusion criteria.** A case is included if all three hold:
1. A model has been adopted as a common basis for attributions. The model can be an algorithm, a statistical or actuarial model, an accounting or IT system whose outputs are treated as evidence, or an analytic study adopted as the basis of a standard. The attributions can be of fault, risk, debt, performance or harm.
2. It covers at least 100 dependent cases (people, firms, properties, exposures or jurisdictions).
3. At least one formal challenge episode (§4.4) is documented in an authoritative source, between adoption and 31 Dec 2025.

**Candidate list.** Fixed now, and listed with real names in `case-list.md`:
- G01: a criminal-sentencing risk score;
- G02: a teacher value-added evaluation model;
- G03: structured-finance credit-rating models;
- G04: bank internal capital models;
- G05: hurricane catastrophe models used in insurance rate-setting;
- G06: an air-pollution cohort study adopted as the basis of a standard;
- G07: an epidemic simulation model used for pandemic policy;
- G08: a postal-network accounting system used to attribute shortfalls to sub-postmasters;
- G09: an automated welfare-debt calculation;
- G10: a welfare-fraud risk system;
- G11: a childcare-benefit fraud risk model;
- G12: an automated unemployment-fraud adjudication system;
- G13: a national exam-grade standardisation algorithm;
- G14: a Medicaid home-care allocation algorithm in one US state;
- G15: a Medicaid budget-setting tool in another US state.

**Exclusion.** A candidate is excluded only if the packet preparers cannot document at least one formal challenge episode from authoritative sources. Exclusions are listed with reasons in `case-list.md` before coding.

### 4.3 Selection threat (disclosed)

The author and the packet preparers know most of these cases and how they ended. The list was chosen with that knowledge, which is the main threat to validity. Two partial mitigations apply:
- **Known potential falsifiers were included on purpose.** These are cases where a named individual plaintiff obtained a model-level ruling (G09), cases where mass public protest preceded reversal (G13), and cases where an individual challenge failed outright (G01).
- **Every documented formal episode is included.** Preparers may not choose among episodes (§4.4).

### 4.4 Episodes

A **challenge episode** is any formal attempt to obtain relief from the model's attributions, documented in an authoritative source and occurring between adoption and 31 Dec 2025. Authoritative sources are court records or judgments, official reports, regulator decisions, legislation, or peer-reviewed or official reanalyses. Episodes are:
- **litigation:** each distinct suit, counted once at its highest decided level;
- **regulatory proceedings and decisions;**
- **official audits, inquiries and reviews;**
- **legislative or executive acts** that target the model;
- **formal reanalyses** by a body with standing.

Preparers must list **every** episode they find in authoritative sources for that case. They may not select among them. Informal criticism, media campaigns and protests are recorded as context, not as episodes.

### 4.5 Variables (coded per episode; full anchors in `codebook.md`)

| Variable | Values |
|---|---|
| challenger | `lone` (cost borne by the affected individual or their own private counsel) / `organised` (cost borne wholly or partly by an organisation, coalition, group or class action, or by an institution acting on its mandate) / `unclear` |
| supported | 1 if a named individual is the formal party but an organisation funded or ran the challenge; else 0 |
| target | `own-case` / `model` / `unclear` |
| success | 1 if any relief sought was obtained; else 0 |
| content_reopen | 1 if the episode reopened B's content for the class (§4.6); else 0 |
| ground | for successful episodes: `procedural` / `substantive` / `mixed` / `unclear`; `NA` otherwise |
| scope | for content reopenings: `own` / `group` / `class`; `NA` otherwise |
| recognised | 0 or 1 (probe, §5) |

### 4.6 Content-level reopening (fixed definition)

Counts as content-level reopening:
- the model's attributions, for the class of dependent cases, were withdrawn, suspended, declared unlawful or invalid in general, or materially revised under a binding requirement;
- the attributions were independently re-estimated by a body with standing, and the results were made public.

Does not count:
- reconsideration of the challenger's own case under the unchanged model;
- an order to disclose;
- warnings or caveats attached to outputs;
- a settlement confined to the parties.

### 4.7 Hypotheses and tests (one-sided, α = 0.05)

**H1. Lone content failure (from b, c).**

Among episodes with a known challenger type, content reopening is less common when the challenger is lone than when it is organised.
- **Test:** Fisher's exact test on the 2 × 2 table of challenger (lone/organised) by content_reopen. A case-level robustness check uses a sign test across cases that contain both kinds of episode.
- **Falsified if:** the lone share is greater than or equal to the organised share.

**H2. Lone wins are procedural (from f).**

Among successful lone episodes, the share won on procedural grounds is above 0.5.
- **Test:** binomial test against 0.5, with mixed grounds counted as not procedural.
- **Falsified if:** the share is 0.5 or below.
- **Small samples:** if there are fewer than 5 successful lone episodes, the result is descriptive only.

**H3. Organised first reopening (from c, d).**

Among cases with at least one content reopening, the first such episode was brought by an organised challenger in more than 50% of cases.
- **Test:** binomial test against 0.5.
- **Falsified if:** the share is 0.5 or below.

**H4. All at once (from e).**

Among content-reopening episodes, scope is `class` in more than 50% of episodes.
- **Test:** binomial test against 0.5.
- **Falsified if:** the share is 0.5 or below.

**Sensitivity analyses** (reported, not decisive):
- **S1:** recognised case–coder pairs are excluded.
- **S2:** supported individuals (`supported = 1`) are re-coded as `lone`.
- **S3:** each case is weighted equally, as the case-level mean of episode outcomes.

## 5. Coding, de-identification and probes

- **Coders.** Four independent model coders: Claude Haiku, Sonnet, Opus and Fable. Each coder is blind to this file, to `case-list.md` and to the other codings. Human coders are preferable (G2 codebook §5.5). Model coders are used here, with the safeguards below, and that is a stated limitation.
- **Packets.** Packets are de-identified under G2 codebook §5.2, with these adaptations:
  - names of the model, operator, firms, people, places, courts and statutes are replaced with stable tokens;
  - dates are given relative to adoption (A+0);
  - generic domain words are kept.
  Packets give facts neutrally, in each source's terms. They must not use the coding vocabulary (lone, organised, procedural, substantive, content reopening). A second preparer reviews each packet for residual identifiers and for coding vocabulary before release.
- **Probe.** Before coding a case, each coder answers: "What real-world case do you think this is?" A correct identification sets `recognised = 1`. Unlike G2, the primary analysis includes recognised pairs. The packets already state the episode facts, so recognition cannot leak an unknown outcome; it can only bias classification. S1 tests that.
- **Aggregation.** For each episode and variable, the panel value is the modal category among coders. A tie gives `unclear`, which is excluded from the test for that variable.
- **Reliability.** Krippendorff's α (nominal) is reported per variable. If α < 0.40, the dependent test is flagged unreliable and not interpreted.

## 6. Known limits of the design

- **Selection (§4.3).** The cases were picked with outcomes known. This is the dominant threat.
- **Episode listing depends on what the preparers find.** Unreported individual challenges are under-counted, which may make lone failures look rarer than they are.
- **Only the above-threshold regime is tested.** The scale threshold N* itself is not estimated.
- **A2 (equal success probability) is a simplification.** If organised actors also have a higher q, for example through better counsel, then H1 confounds resources with cost structure. The test cannot separate the two. H2 and H4 do not depend on A2.
- **Clustering.** Episodes are clustered within cases. The episode-level Fisher test treats them as independent; S3 and the case-level sign test are the checks.

## 7. Outputs

The analysis produces three files:
- `codings/<coder>.csv` and `codings/<coder>-evidence.md`, one pair per coder;
- `analysis.py`, which produces the aggregated table, α, H1–H4 and S1–S3;
- `results.md`, which reports every hypothesis with the same prominence, whether it passes or not.

Deviations from this plan are listed in `results.md` §Deviations, with reasons.

## 8. Decision rule for the paper (fixed now)

**Supported.** Prop 3 enters the main body of the planned blog paper as a tested proposition only if both conditions hold:
- H1 and H3 both reject the null at α = 0.05, with α ≥ 0.40 for the variables they use;
- neither H2 nor H4 is falsified.

**Otherwise mixed or failed.** The proof and the test results go in a footnote and an appendix only. The main body rests on Props 1, 2 and 4.
