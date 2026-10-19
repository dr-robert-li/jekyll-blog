# Coder brief

You are an independent coder in an exploratory study.

## What to read

**Read only:**
- `codebook.md`;
- the files in `packets/` (G01.md, G02.md, …).

**Do not open:**
- `preregistration.md`;
- `case-list.md`;
- `analysis.py` or `results.md`;
- any file in `codings/` except your own;
- any file outside this folder.

## Rules

- Do not use web search.
- Score each episode only from its packet.
- If you recognise the case, record that in the probe. Then still score only from what the packet says.

## Output 1: `codings/<CODER>.csv`

The header line must be exactly:

`case,episode,challenger,supported,target,success,content_reopen,ground,scope,recognised`

Write one row per episode, using the case id (e.g. `G01`) and the episode id (e.g. `E2`). Allowed values:

| Column | Values |
|---|---|
| challenger | `lone`, `organised`, `unclear` |
| supported | `0`, `1` |
| target | `own-case`, `model`, `unclear` |
| success | `0`, `1` |
| content_reopen | `0`, `1` |
| ground | `procedural`, `substantive`, `mixed`, `unclear`, `NA` |
| scope | `own`, `group`, `class`, `NA` |
| recognised | `0`, `1` (the same value for every episode of a case) |

## Output 2: `codings/<CODER>-evidence.md`

**For each case:**
1. First give the probe: "Probe G01: I think this is … / I don't recognise it." Write this **before** you score that case.
2. Then give one line per episode, citing the packet sentences you relied on. For example: "G01 E2 challenger: the packet says the suit was brought by [UNION-1] on behalf of members …"
