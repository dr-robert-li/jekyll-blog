# Packet preparer brief (G4)

You prepare de-identified evidence packets for an exploratory coding study. Other people (the coders) will later classify the challenge episodes in your packets. You do **not** need to know the study's hypotheses. Do not open `preregistration.md`.

## Your job, per case

1. **Research the case** with web search and fetch. Use authoritative sources only:
   - judgments and court records;
   - official reports: audits, inquiries, regulator decisions;
   - legislation and official releases;
   - peer-reviewed or officially commissioned reanalyses.

   Reputable reporting (major newspapers, law-firm or academic case notes) may be used to locate those sources, or to describe who funded or ran a challenge when official sources are silent.

2. **List every formal challenge episode** from the model's adoption to 31 Dec 2025. Search systematically for all five kinds below. **Do not select:** if you find it in an authoritative source and it fits the definition, it goes in.
   - **Litigation.** Each distinct lawsuit or prosecution appeal that challenged the model's outputs or use, counted once at its highest decided level. Note any settlements.
   - **Regulatory proceedings or decisions** about the model.
   - **Official audits, inquiries and reviews** of the model.
   - **Legislative or executive acts** targeting the model.
   - **Formal reanalyses** of the model or study by a body with standing.

   Protests, media campaigns, open letters and informal academic criticism are **context**, not episodes.

3. **Write the packet** to `packets/<ID>.md` in the template below, de-identified.

4. **Write your private notes** to `prep/<ID>-notes.md`. These hold the real names, the token key (token → real name) and full source citations with URLs, keyed to the packet's source ids (S1, S2, …). Coders never see this file.

## De-identification

- Replace these with stable tokens: the model's name, the operator or vendor, firms, people, places, countries, states, courts, agencies, statutes and case names.
  - Tokens: [MODEL], [OPERATOR], [VENDOR], [COURT-1], [COURT-2 (appellate)], [AGENCY-1], [COUNTRY-A], [STATE-A], [STATUTE-1], [PLAINTIFF-1], [ORG-1], and so on.
  - Keep tokens consistent within a packet.
- Convert dates to years relative to adoption: A+0 is the adoption year, so A+3, A+7.5 and so on. Never give calendar years.
- Paraphrase any distinctive quotation that would identify the case.
- Keep the generic domain words a coder needs: "criminal sentencing", "teacher evaluation", "welfare debt", "insurance rate filing", "bank capital".
- Give the number of dependent cases only as an order of magnitude: "hundreds", "thousands", "tens of thousands" and so on.
- Keep the factual detail needed to classify each episode:
  - who formally brought it;
  - who funded or ran it, if reported;
  - what was sought;
  - the forum type;
  - the outcome;
  - the stated reasons;
  - whom the relief applied to.

## Neutral language (important)

Describe each episode in plain factual terms, using the source's own reasoning, paraphrased. **Do not use** these words or phrases anywhere in the packet:
- lone, organised / organized;
- procedural, substantive;
- content, reopen / reopening;
- "class" except inside the legal term "class action".

Instead, say what the court or body actually found. For example:
- "the court held that the teachers could not check their scores because the formula and data were withheld, and that this denied them a fair chance to contest dismissal";
- "the inquiry found the calculations were wrong in a large share of cases".

Do not editorialise or summarise patterns across episodes.

## Packet template

```
# Evidence packet <ID>

- **Domain:** <generic domain>
- **What the model does:** <what it calculates or attributes, and for whom; generic>
- **Scale:** <order of magnitude of people/firms/properties whose judgements rest on it>
- **Adoption:** A+0 = <short description of the adoption event, no calendar year>
- **De-identification:** <one line: what was tokenised; "not fully feasible" if the case is unmistakable>

## Context (not episodes)
- <dated A+x bullets: protests, media, informal criticism, relevant background>

## Episodes

E1. **[A+x] <forum type, tokenised>.**
- Brought by: <formal party>. Funded or run by: <as reported, or "not reported">.
- Sought: <what relief>.
- Outcome: <what happened, incl. settlement or appeal result>.
- Stated reasons: <paraphrase>.
- Relief applied to: <whom>.
- Sources: S1, S3.

E2. ...
```

## Quality bar

- Every fact must be traceable to a source id that is listed in your notes file.
- If you cannot verify something, say "not reported" rather than guess.
- Order episodes by date.
- Aim for completeness over polish. A case typically has 3–10 episodes.
- If you cannot document even one formal episode from authoritative sources, write a packet that says so and explain why in your notes. The case will then be excluded.
