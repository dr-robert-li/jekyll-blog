"""G2 panel analysis, as pre-registered in preregistration.md.

Usage: python -I analysis.py <g2-panel dir>
Writes results.md into that directory.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

D = Path(sys.argv[1])
SCALES = ["phi", "LR", "V", "rhat", "M", "dist"]
rng = np.random.default_rng(20261011)


# ---------- inputs ----------
def load_codings():
    frames = []
    for f in sorted((D / "codings").glob("*.csv")):
        df = pd.read_csv(f, na_values=["NA", "IE"])
        df["coder"] = f.stem
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def load_outcomes():
    """Parses the three formats used in outcomes.md (## / ### headings; '- Lag (years):',
    '- Lag:' and '- **Lag:**'). Locus = first of root/downstream named; 'unresolved' or 'n/a' -> NA.
    Headline lag only; the alternatives listed in the file are ignored."""
    rows = []
    for block in re.split(r"^#{2,3} (?=K\d\d)", (D / "outcomes.md").read_text(), flags=re.M)[1:]:
        case = block.split()[0]
        lag_line = re.search(r"^- (?:\*\*)?Lag[^:\n]*:(?:\*\*)?(.*)$", block, re.M)
        loc_line = re.search(r"^- (?:\*\*)?Locus[^:\n]*:(?:\*\*)?(.*)$", block, re.M)
        lag, cens = np.nan, False
        if lag_line:
            txt = lag_line.group(1)
            m = re.search(r"censored(?: at|, ≥| ≥)\s*(\d+)", txt)
            if m and "not censored" not in txt:
                lag, cens = float(m.group(1)), True
            else:
                m = re.search(r"\d+", txt)
                if m:
                    lag = float(m.group(0))
        locus = np.nan
        if loc_line:
            txt = loc_line.group(1).strip().lower()
            if not txt.startswith(("unresolved", "n/a")):
                hits = [(txt.find(w), w) for w in ("root", "downstream") if w in txt]
                if hits:
                    locus = 0 if min(hits)[1] == "root" else 1
        rows.append(dict(case=case, lag=lag, censored=cens, locus=locus))
    return pd.DataFrame(rows)


# ---------- Krippendorff's alpha ----------
def kripp_alpha(units, level):
    """units: list of lists of values (one list per case, NaN dropped)."""
    units = [[v for v in u if pd.notna(v)] for u in units]
    units = [u for u in units if len(u) >= 2]
    if not units:
        return np.nan
    vals = sorted({v for u in units for v in u})
    idx = {v: i for i, v in enumerate(vals)}
    k = len(vals)
    o = np.zeros((k, k))
    for u in units:
        m = len(u)
        for a in range(m):
            for b in range(m):
                if a != b:
                    o[idx[u[a]], idx[u[b]]] += 1 / (m - 1)
    n_c = o.sum(axis=1)
    n = n_c.sum()
    if level == "nominal":
        d = 1 - np.eye(k)
    else:  # ordinal
        d = np.zeros((k, k))
        for c in range(k):
            for e in range(k):
                lo, hi = min(c, e), max(c, e)
                d[c, e] = (n_c[lo : hi + 1].sum() - (n_c[c] + n_c[e]) / 2) ** 2
    do = (o * d).sum()
    de = (np.outer(n_c, n_c) * d).sum() / (n - 1)
    return 1 - do / de if de > 0 else np.nan


# ---------- aggregation (prereg §2) ----------
def merge_outcomes(agg, outc):
    m = agg.merge(outc, on="case", how="left")
    m["censored"] = m["censored"].fillna(False).astype(bool)
    return m


def aggregate(cod):
    out = []
    for case, g in cod.groupby("case"):
        row = {"case": case}
        for v in SCALES:
            x = g[v].dropna()
            row[v] = x.median() if len(x) >= 2 else np.nan
        c = g["carrier"].dropna()
        cnt = c.value_counts()
        row["carrier"] = (
            np.nan if len(c) == 0 or (len(cnt) > 1 and cnt.iloc[0] == cnt.iloc[1]) else cnt.index[0]
        )
        f = g["funding"].dropna()
        fc = f.value_counts()
        row["funding"] = (
            np.nan if len(f) == 0 else ("mixed" if len(fc) > 1 and fc.iloc[0] == fc.iloc[1] else fc.index[0])
        )
        out.append(row)
    return pd.DataFrame(out)


# ---------- tests ----------
def boot_rho(x, y, n=10000):
    x, y = np.asarray(x), np.asarray(y)
    rs = []
    for _ in range(n):
        i = rng.integers(0, len(x), len(x))
        r = stats.spearmanr(x[i], y[i]).statistic
        if np.isfinite(r):
            rs.append(r)
    return np.percentile(rs, [2.5, 97.5])


def mwu(a, b, alt):
    """returns U, one-sided p, rank-biserial r (positive = a larger)."""
    res = stats.mannwhitneyu(a, b, alternative=alt)
    u_a = stats.mannwhitneyu(a, b, alternative="two-sided").statistic
    r = 2 * u_a / (len(a) * len(b)) - 1
    return res.statistic, res.pvalue, r


def run_tests(df, label, n_total):
    res = []
    # P1
    d = df.dropna(subset=["phi", "LR", "V", "rhat", "lag"]).copy()
    d["C"] = (6 - d["phi"]) + d["LR"] + d["V"] + d["rhat"]
    # censored ranked tied at top
    d["lag_r"] = np.where(d["censored"], d["lag"].max() + 1, d["lag"])
    if len(d) >= 4:
        t = stats.spearmanr(d["C"], d["lag_r"], alternative="greater")
        ci = boot_rho(d["C"], d["lag_r"])
        res.append(("P1", len(d), f"ρ = {t.statistic:.2f} [{ci[0]:.2f}, {ci[1]:.2f}]", t.pvalue))
    else:
        res.append(("P1", len(d), "too few cases", np.nan))
    # P11
    d = df.dropna(subset=["funding", "lag"])
    lag_r = lambda s: np.where(s["censored"], df["lag"].max() + 1, s["lag"])
    a, b = d[d.funding == "industry"], d[d.funding == "independent"]
    if len(a) >= 2 and len(b) >= 2:
        u, p, r = mwu(lag_r(a), lag_r(b), "greater")
        res.append(("P11", len(a) + len(b), f"U = {u:.0f}, r_rb = {r:.2f} (industry n={len(a)}, independent n={len(b)})", p))
    else:
        res.append(("P11", len(a) + len(b), f"too few (industry n={len(a)}, independent n={len(b)})", np.nan))
    # P13
    d = df.dropna(subset=["dist", "locus"])
    d = d[~d["censored"]]
    a, b = d[d.locus == 1]["dist"], d[d.locus == 0]["dist"]
    if len(a) >= 2 and len(b) >= 2:
        u, p, r = mwu(a, b, "greater")
        res.append(("P13", len(a) + len(b), f"U = {u:.0f}, r_rb = {r:.2f} (downstream n={len(a)}, root n={len(b)})", p))
    else:
        res.append(("P13", len(a) + len(b), f"too few (downstream n={len(a)}, root n={len(b)})", np.nan))
    # P16
    d = df.dropna(subset=["carrier", "lag"])
    a, b = d[d.carrier == 1], d[d.carrier == 0]
    if len(a) >= 2 and len(b) >= 2:
        u, p, r = mwu(lag_r(a), lag_r(b), "less")
        res.append(("P16", len(a) + len(b), f"U = {u:.0f}, r_rb = {r:.2f} (carrier n={len(a)}, none n={len(b)})", p))
    else:
        res.append(("P16", len(a) + len(b), f"too few (carrier n={len(a)}, none n={len(b)})", np.nan))
    # Holm
    ps = [(i, r[3]) for i, r in enumerate(res) if pd.notna(r[3])]
    ps.sort(key=lambda t: t[1])
    m = len(ps)
    adj, running = {}, 0
    for rank, (i, p) in enumerate(ps):
        running = max(running, min(1, (m - rank) * p))
        adj[i] = running
    lines = [f"\n### {label}\n", "| Test | n | Effect | p (one-sided) | Holm p | Evaluable |", "|---|---|---|---|---|---|"]
    for i, (name, n, eff, p) in enumerate(res):
        ev = "no (> 1/3 excluded)" if n < (2 / 3) * n_total else "yes"
        pa = adj.get(i, np.nan)
        lines.append(f"| {name} | {n} | {eff} | {p:.3f} | {pa:.3f} | {ev} |" if pd.notna(p) else f"| {name} | {n} | {eff} | – | – | {ev} |")
    return "\n".join(lines)


def main():
    cod = load_codings()
    outc = load_outcomes()
    coders = sorted(cod.coder.unique())
    n_total = cod.case.nunique()
    md = ["# G2 coded panel — results (EXPLORATORY)\n",
          f"Coders: {', '.join(coders)} (each a different AI model). Cases: {n_total}. "
          "Analysis follows preregistration.md; deviations are listed at the end.\n"]

    # reliability
    md.append("## Inter-rater reliability (Krippendorff's α)\n")
    md.append("| Variable | Level | α | Flag |\n|---|---|---|---|")
    alpha = {}
    for v in SCALES + ["carrier", "funding"]:
        lvl = "ordinal" if v in SCALES else "nominal"
        units = [g[v].tolist() for _, g in cod.groupby("case")]
        a = kripp_alpha(units, lvl)
        alpha[v] = a
        md.append(f"| {v} | {lvl} | {a:.2f} | {'unreliable (< 0.40)' if a < 0.40 else ''} |")

    rec = cod.groupby("coder")["recognised"].sum()
    md.append("\n**Cases recognised, by coder:** " + ", ".join(f"{c} {int(n)}/{n_total}" for c, n in rec.items()))

    agg = merge_outcomes(aggregate(cod), outc)
    agg.to_csv(D / "panel-aggregated.csv", index=False)
    md.append(f"\nOutcomes parsed: lag available for {agg['lag'].notna().sum()} cases "
              f"({int(agg['censored'].sum())} censored); locus root/downstream for {agg['locus'].notna().sum()}.")

    md.append("\n## Pre-registered tests")
    md.append(run_tests(agg, "Primary (all cases)", n_total))

    # flag unreliable
    flags = {"P1": ["phi", "LR", "V", "rhat"], "P11": ["funding"], "P13": ["dist"], "P16": ["carrier"]}
    unrel = [t for t, vs in flags.items() if any(alpha[v] < 0.40 for v in vs)]
    if unrel:
        md.append(f"\nFlagged unreliable (a component variable has α < 0.40), not interpreted: {', '.join(unrel)}.")

    # S1: exclude scores from recognised cases
    cod_s1 = cod[cod.recognised == 0]
    if cod_s1.case.nunique() > 0:
        agg1 = merge_outcomes(aggregate(cod_s1), outc)
        md.append(run_tests(agg1, "S1: scores from recognised cases excluded", n_total))
    else:
        md.append("\n### S1: scores from recognised cases excluded\n\nNot evaluable: every coder recognised every case.")

    # S2: censored excluded
    md.append(run_tests(agg[~agg.censored], "S2: censored cases excluded", n_total))

    # exploratory components
    md.append("\n## Exploratory (no significance claims)\n")
    md.append("| Variable | Spearman ρ with lag (censored ranked top) | n |\n|---|---|---|")
    d = agg.dropna(subset=["lag"]).copy()
    d["lag_r"] = np.where(d["censored"], d["lag"].max() + 1, d["lag"])
    for v in SCALES:
        e = d.dropna(subset=[v])
        if len(e) >= 4:
            md.append(f"| {v} | {stats.spearmanr(e[v], e['lag_r']).statistic:.2f} | {len(e)} |")
    md.append("\nThe Cox model listed as exploratory in the pre-registration was not run (lifelines is not installed). This is a deviation.")
    (D / "results.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
