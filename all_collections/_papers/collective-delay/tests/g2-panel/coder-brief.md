# Coder brief

You are an independent coder in an exploratory study.

**Read only:**
- `codebook.md`;
- the 31 files in `packets/` (K01–K31).

**Do NOT open** `outcomes.md`, `preregistration.md`, `case-list.md`, `forward-registration.md`, or any other file in `codings/` except your own.

**Rules:**
- Do not use web search.
- Score each case only from its packet's evidence, as at the scoring point stated in the packet.
- Do not use outside knowledge of what happened later. If you recognise the case, set `recognised=1` anyway and still score only from the packet.

**Output 1: `codings/<CODER>.csv`.** Header line, exactly:

`case,phi,LR,V,rhat,M,dist,carrier,funding,recognised`

- phi, LR, V, rhat, M, dist: integers 1–5 on the codebook anchors, or `NA` if there is insufficient evidence.
- carrier: 0 or 1.
- funding: `industry`, `independent`, `mixed` or `NA`.
- recognised: 0 or 1.

**Output 2: `codings/<CODER>-evidence.md`.** For each case and each variable, give one line with the cited quote ids (e.g. "K01 V: Q3, Q7 — two producers lobbied …").
