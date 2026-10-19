# G4 — Codebook

## 1. What you are scoring

Each packet describes one **model**. In some packets it is called [MODEL] or a similar token. The model is used as a common basis for judgements about many people, firms, properties or places: for example, who owes money, who is at fault, who is high-risk, or how much harm a pollutant causes.

Each packet lists **challenge episodes** (E1, E2, …). These are formal attempts to obtain relief from the model's judgements. You score **each episode** on the variables below, using only what the packet says.

Dates are given relative to the model's adoption: A+0 is the year of adoption, and A+3 is three years later.

## 2. Variables (one row per episode)

### 2.1 challenger

Who bore the cost of bringing the challenge?

- `lone`: one affected individual, or one affected firm, acting on its own and paying for its own case. That includes paying its own private lawyer.
- `organised`: the cost was borne wholly or partly by any of the following.
  - An organisation: legal aid, a union, an NGO, an advocacy group, an insurer or trade body, or a law firm running funded group litigation.
  - A coalition, a group action or a class action.
  - An institution acting on its own mandate: a regulator, legislature, government department, auditor-general, ombudsman, court-appointed or government-commissioned inquiry, standards body, or a research body commissioned to reanalyse.
- `unclear`: the packet does not say enough to tell.

### 2.2 supported

Fill this in only when the formal party is a named individual.
- `1`: the packet says an organisation funded, ran or brought the challenge on that individual's behalf, for example as a test case.
- `0`: otherwise.

For episodes brought by institutions or groups, use `0`.

### 2.3 target

What did the challenge seek to change?

- `own-case`: the judgement about the challenger itself, or about a named set of challengers, without seeking to change how the model works for everyone.
- `model`: the model itself, or its use for everyone it applies to. That includes seeking its withdrawal, suspension, a declaration that it is unlawful or invalid, a general revision, or an independent re-estimate of it.
- `unclear`.

### 2.4 success

- `1`: the challenger obtained any of the relief it sought, by judgment, decision, settlement or official action.
- `0`: it obtained none, or the episode was dismissed or abandoned.

### 2.5 content_reopen

- `1`: as a result of this episode, the model's judgements for **everyone it applies to** were:
  - withdrawn or suspended;
  - declared unlawful or invalid in general;
  - materially revised under a binding requirement;
  - or independently re-estimated by a body with standing, with the results made public.
- `0`: otherwise. These do **not** count:
  - only the challenger's own case was reconsidered under the unchanged model;
  - only an order to disclose information;
  - only warnings or caveats added to the model's outputs;
  - a settlement that applies only to the parties.

### 2.6 ground

Fill this in only if success = 1. On what basis was the relief granted?

- `procedural`: the problem was the process, not whether the model's judgements are right. Examples:
  - lack of notice or explanation;
  - inability to inspect or check the model or data;
  - no human review;
  - due process or fair-hearing failures;
  - transparency or access to data.
- `substantive`: the model's judgements themselves were wrong, unreliable, unlawful in what they calculate, or unsupported by evidence.
- `mixed`: both are clearly given as reasons.
- `unclear`.

Use `NA` if success = 0.

### 2.7 scope

Fill this in only if content_reopen = 1. Who did the relief cover?

- `own`: only the challenger.
- `group`: a defined group larger than the challenger but smaller than everyone the model applies to, such as the members of a group action.
- `class`: everyone, or essentially everyone, the model's judgements applied to.

Use `NA` if content_reopen = 0.

### 2.8 recognised

Before scoring a packet, answer the probe in your evidence file (see the coder brief).
- `1`: you believe you know which real-world case this is.
- `0`: you do not.

## 3. Rules

- Score only from the packet. If the packet does not say, use `unclear`. Do not fill gaps from memory, even if you recognise the case.
- Score each episode separately, as described. Do not let one episode's outcome change how you score another.
