# G3 proposed revisions: P3, P14, P23, G.1 and the claims-status subsection

These are proposals only. Nothing here is merged into `q2-collective-delay-research.md`. The evidence and tags behind each change are in `evidence-review.md` (row numbers 3.x, 14.x, 23.x). Tags here re-cite that file and are counted again below only where this file states a claim of its own.

---

## 1. Replacement prediction rows

The column format follows Part F: Prediction | Model term tested | What would falsify it | Data or design | Source.

| # | Prediction | Model term tested | What would falsify it | Data or design | Source |
|---|---|---|---|---|---|
| P3 | **Correcting misperceived support works where the barrier is social, the step is cheap, and the target is below the true norm.** Publicising true private *support* (who thinks the behaviour should happen) raises actual behaviour more than equally vivid harm information when three conditions hold: the behaviour is low-cost or a first step; others' disapproval is what holds it back; and the target underestimates support. This applies in climate and outside it (AMR prescribing, pension enrolment, platform-use coordination). For costly or rare behaviours the effect on *actual* behaviour is near zero. It reverses for targets already better than the norm, and for targets shown a lower local norm or a lower prevalence than they believed. Information about the *prevalence* of rare costly acts lowers \(\hat r\), because people overestimate that prevalence. | \(\beta(\hat r_i)\), where the sign of \(\delta_i\) depends on what is estimated: \(\delta > 0\) for broad support, \(\delta < 0\) for the share performing rare costly acts. Moderated by the cost threshold \(\kappa_i\) and by the target's prior relative to \(r\). | (a) Support information no more effective than harm information on actual behaviour for cheap, socially sanctioned behaviours. (b) Equal effects for cheap and costly behaviours. (c) No reversal among above-norm targets or in low-support reference groups when no injunctive cue is given. | A preregistered factorial field experiment: information type (support / harm / both / control) × behaviour cost (cheap / costly) × the respondent's prior relative to the truth. At least two non-climate domains, using the designs of Hallsworth et al. 2016, Beshears et al. 2015 and Bursztyn et al. 2025. Outcome: *actual* behaviour. Pool with a meta-analysis that corrects for publication bias. | B.4; C.3 (C5); App. B F3; G3 review 3.1–3.24 |
| P14 | **Attribution decays at agentive links, and elites track it more than publics do.** Holding the harm constant, attribution to a policy root falls as the chain from root to harm lengthens. Most of the loss occurs at links where an intervening actor (an insurer, utility or local official) offers a nearer target. Links that are physical processes pass attribution back to a human or policy root with little loss. Legislators' attribution and choice of instrument respond to traceability more than mass attribution does. Partisan cues gate each link. | \(\varphi_k \approx \varphi_0 \prod_{j=1}^{k} a_j + M\), with \(a_j = a(\text{type}_j, \pi_i)\): low for agentive links, near 1 for physical links, and filtered by party alignment \(\pi_i\). Veto holders can lower \(a_j\) on purpose (Hood's blame avoidance; Arnold's link-breaking). | (a) Attribution flat across chain depth. (b) Equal decay at physical and agentive links. (c) Publics' attribution as sensitive to depth as elites'. (d) No partisan gating once role information is supplied. | A survey experiment presenting the same harm at depths 1–4, crossing link type (physical vs intervening agent), party cue and role information. Run in parallel on a public sample and on legislators or staff (the Mildenberger & Sahn 2025 design). Separately, media content coding of chains, with episodic or thematic frame as a covariate (Iyengar 1991). | G.1; Arnold 1990; Mildenberger & Sahn 2025; Engelmann & Waldmann 2022; Hilton et al. 2010; G3 review 14.1–14.20 |
| P23 | **Delegated tracing impairs unassisted proficiency, most in novices and for cognitive tasks, and its maintenance is cut first.** Where diagnostic or causal tracing is delegated to models: (a) people trained with the model reach lower unassisted proficiency than people trained without it; (b) experienced practitioners' unassisted proficiency declines with time since their last unassisted practice, faster for cognitive monitoring and diagnostic judgement than for perceptual-motor execution; (c) active engagement (verifying outputs, asking for explanations, guardrails that withhold answers) weakens (a) and (b); (d) mandates to maintain unassisted proficiency erode first under fiscal pressure. Automation bias while assisted is a separate, immediate effect and does not count as evidence for (a) or (b). | M erosion: (a) failed formation, (b) atrophy through disuse (H.3 iii), (d) M under fiscal erosion (B.4.1) | (a) and (b): unassisted proficiency at 12 months or more no lower in exposed units than in unexposed units, or no gradient between novices and experts, or between cognitive and motor tasks. (c): no moderation by engagement. (d): maintenance mandates surviving fiscal consolidation at rates no lower than other functions. | A stepped-wedge cluster trial of model deployment with periodic unassisted probes, recording case mix and procedural covariates (extending and replicating Budzyń et al. 2025). Novice-cohort RCTs on the designs of Bastani et al. 2025 and Shen & Tamkin 2026. Budget lines for oversight and reserve capacity under consolidation. | H.3; B.4.1; App. D AU1–AU8; Casner et al. 2014; Arthur et al. 1998; Haslbeck & Hoermann 2016; G3 review 23.1–23.16 |

**What changed and why.**

**P3.**
- "Across domains" is now conditional on cost, sanction and the target's prior. The reason: pensions backfired (Beshears et al. 2015), actual climate donations did not move (Tiede et al. 2026), and the health meta-analyses are null after correcting for publication bias.
- The prediction now names *support* rather than *prevalence*, because injunctive information outperformed descriptive information in Andre et al. 2024 and because Tiede et al. found that the prevalence of rare acts is overestimated.
- The \(\delta\)-sign problem is exposed in the model column.

**P14.**
- The uniform per-link product is replaced by decay that depends on link type (Hilton et al. 2010; Fincham & Shultz 1981).
- The elite–public pairing is split, following Mildenberger & Sahn 2025.
- The shark-attack evidence is dropped (Fowler & Hall 2018).

**P23.**
- Three mechanisms are separated.
- "Cognitive faster than motor" replaces any claim that only cognitive skills decay (Arthur et al. 1998; Haslbeck & Hoermann 2016).
- Engagement is added as a moderator.
- Automation bias (Dratsch et al. 2023) is excluded as evidence for atrophy.

---

## 2. Proposed addition to Part G, G.1

Insert after point 1, which sets out the attribution decay equation, or as a closing paragraph of G.1:

> **Precedent: traceability.** The closest precedent for points 1 and 3 is R. Douglas Arnold's *The Logic of Congressional Action* (1990). Arnold argued that the "nature of the causal chain that links a policy instrument with its policy effects" structures congressional action: citizens can hold a legislator to account for an effect only if they can trace it to a government action and from there to their representative [admit: Mildenberger & Sahn 2025, LSQ, quoting Arnold]. Early-order effects are more traceable than later-order ones, and coalition leaders break traceable links, for example by folding costly provisions into omnibus bills [abstain: non-authoritative source — course summaries; book not opened]. In this report's terms, Arnold's traceability is the product \(\prod a_j\), and his legislators, choosing instruments whose effects voters can or cannot trace, are the actors who settle at \(k^*\). The present model differs in two ways. Arnold's chain runs from one policy to its effects; the chains here run from an *unaddressed* root through several domains, so the product has more terms and the root is an omission, not an act. And the first direct test of Arnold's claim found that legislators respond to policy and problem traceability while prospective voters are indifferent to it [admit: Mildenberger & Sahn 2025, LSQ 50(4):e70036]. Attribution decay may therefore bind mainly through elite anticipation of blame, not through mass judgement. Experiments on moral judgement add two qualifications. Blame of an agent weakens as the chain between act and harm lengthens, through reduced foreseeability [admit: Engelmann & Waldmann 2022, Cognition 226:105167]. And the loss concentrates at intervening *agents*: people trace attribution through physical links back to a human cause, but a voluntary intervening actor absorbs it [admit: Hilton, McClure & Sutton 2010, EJSP 40(3):383–400]. So \(a_j\) is low at insurers, utilities and local officials, and high at physical links such as warming to fire weather. Because veto holders can add agentive links on purpose (Hood's blame avoidance through delegation; Arnold's link-breaking), part of the decay is produced by the veto holders themselves, which ties point 1 to V [admit: Hood 2011, Princeton UP; Synthesis].

**Proposed reading-list entry** (under *Political science and public policy*):

- **Arnold, R. D. (1990).** *The Logic of Congressional Action.* Yale University Press. Some listings give 1992. *The origin of "traceability": legislators anticipate whether citizens can trace an effect along the causal chain to a government action and to their own vote. The closest precedent for G.1's attribution decay and for responses settling near the symptom.* First direct test: **Mildenberger, M. & Sahn, A. (2025).** The effect of policy traceability on legislative incentives. *Legislative Studies Quarterly* 50(4):e70036. doi:10.1111/lsq.70036. Elites respond to traceability; voters do not.

---

## 3. Proposed changes to the executive summary's claims-status subsection

**Group 2 (extends existing research).** Replace the attribution bullet:

- *Current:* "*Attribution decays multiplicatively along causal chains, and responses settle at the lowest-veto attributable link*. Builds on Senge's shifting the burden and Kahn 1966. (G.1)"
- *Proposed:* "*Attribution decays multiplicatively along multi-link, cross-domain chains with an unaddressed policy root, mainly at intervening agents, and responses settle at the lowest-veto attributable link*. Builds on Arnold 1990 (traceability), Engelmann & Waldmann 2022 (chain length lowers blame) and Hilton et al. 2010 (attribution passes through physical links), with Senge and Kahn for the response side. (G.1; P14)"

**Group 3 (aligns with research).** Add two bullets and qualify one:

- *Add:* "Attribution weakens as a causal chain lengthens, and legislators anticipate traceability. (G.1; Arnold 1990; Mildenberger & Sahn 2025; Engelmann & Waldmann 2022)"
- *Add:* "Practising with an AI model impairs the formation of unassisted skill, and cognitive skills decay with disuse faster than physical ones. (H.3; Bastani et al. 2025; Arthur et al. 1998; Casner et al. 2014)"
- *Qualify the existing bullet* "Majorities underestimate support for climate action (pluralistic ignorance)" by adding: "This holds for broad support. For rare, costly behaviours (donating, political engagement) the share acting is *over*estimated (Tiede et al. 2026)."

**Group 4 (opposes existing research, subject to testing).** Add one bullet:

- "*Against social-norms correction as a general lever*: correcting misperceived support raises action only where the barrier is social, the step is cheap and the target is below the norm. Evidence: null or backfire in pensions (Beshears et al. 2015), actual climate donations (Tiede et al. 2026), college drinking (Foxcroft et al. 2015 Cochrane) and health messaging after bias correction (Papakonstantinou et al. 2025). The report's own B.4 and executive point 3 lean on correction of \(\hat r\) as a lever, so this qualifies the report as well as the advocacy literature. Test: revised P3. (B.4; C.3)"

**Executive summary point 3 (optional).** After "the binding constraint is often *coordination and perception*", add: "Correcting the perception raises cheap and intention-level action, but has not moved costly actual behaviour in the best tests (Tiede et al. 2026; Beshears et al. 2015)."

**Related change outside the claims subsection (flag for B.4).** The decision rule uses \(\beta(r(t) - \delta_i)\), with \(r\) the share *acting*, but \(\delta\) is calibrated on the 26-pp *support* gap. Tiede et al. show \(\delta < 0\) for the share performing rare costly acts. Either define \(\hat r\) as perceived *support*, or allow \(\delta_i\) to change sign by behaviour [Synthesis; admit: Tiede et al. 2026 abstract].

**Do not add Sparrow et al. 2011** when extending the automation bullet. The report does not currently cite it, and its Experiment 1 failed to replicate (G3 review 23.9).

---

## Disposition count (this file)

Only the tags in section 2's proposed G.1 paragraph and the B.4 flag are new claims. Everything else re-cites `evidence-review.md`.

- **admit:** 6
- **refute:** 0
- **abstain:** 1
