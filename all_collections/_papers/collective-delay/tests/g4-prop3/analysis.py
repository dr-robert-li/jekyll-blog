"""G4 panel analysis, as pre-registered in preregistration.md (H1-H4, S1-S3).

Usage: python -I analysis.py  (run from this folder). Writes panel-aggregated.csv and prints results.
"""
import sys
from collections import Counter
from pathlib import Path

import pandas as pd
from scipy import stats

HERE = Path(__file__).resolve().parent
CODERS = ["haiku", "sonnet", "opus", "fable"]
VARS = ["challenger", "supported", "target", "success", "content_reopen", "ground", "scope"]
MISSING = {"unclear", "NA", "", "nan"}
ALPHA = 0.05


def load():
    frames = []
    for c in CODERS:
        p = HERE / "codings" / f"{c}.csv"
        if not p.exists():
            print(f"missing coder file: {p.name}", file=sys.stderr)
            continue
        d = pd.read_csv(p, dtype=str).fillna("NA")
        d.columns = [x.strip() for x in d.columns]
        d = d.apply(lambda s: s.str.strip())
        d["coder"] = c
        frames.append(d)
    return pd.concat(frames, ignore_index=True)


def ep_key(df):
    return df["case"] + "-" + df["episode"]


def modal(values):
    vals = [v for v in values if v not in MISSING]
    if not vals:
        return "unclear"
    top = Counter(vals).most_common()
    if len(top) > 1 and top[0][1] == top[1][1]:
        return "unclear"  # tie, per prereg §5
    return top[0][0]


def aggregate(cod, recode_supported=False):
    rows = []
    for (case, ep), g in cod.groupby(["case", "episode"], sort=False):
        r = {"case": case, "episode": ep}
        for v in VARS:
            r[v] = modal(g[v].tolist())
        if recode_supported and r["supported"] == "1":
            r["challenger"] = "lone"  # S2
        rows.append(r)
    agg = pd.DataFrame(rows)
    agg["epn"] = agg["episode"].str.extract(r"(\d+)").astype(int)
    return agg.sort_values(["case", "epn"]).reset_index(drop=True)


def kripp_alpha_nominal(cod, var):
    """Krippendorff's alpha (nominal) over episodes; missing values excluded."""
    units = []
    for _, g in cod.groupby(["case", "episode"]):
        vals = [v for v in g[var] if v not in MISSING]
        if len(vals) >= 2:
            units.append(vals)
    if not units:
        return float("nan"), 0
    n_c = Counter()
    o = Counter()
    for vals in units:
        m = len(vals)
        cnt = Counter(vals)
        for a in cnt:
            for b in cnt:
                pairs = cnt[a] * (cnt[b] - (1 if a == b else 0))
                o[(a, b)] += pairs / (m - 1)
        n_c.update(vals)
    n = sum(n_c.values())
    d_o = sum(v for (a, b), v in o.items() if a != b) / n
    d_e = sum(n_c[a] * n_c[b] for a in n_c for b in n_c if a != b) / (n * (n - 1))
    if d_e == 0:
        return 1.0, len(units)
    return 1 - d_o / d_e, len(units)


def binom_greater(k, n):
    return stats.binomtest(k, n, 0.5, alternative="greater").pvalue if n else float("nan")


def tests(agg, label):
    out = {"label": label}
    # H1: lone vs organised content reopening
    h1 = agg[agg.challenger.isin(["lone", "organised"]) & agg.content_reopen.isin(["0", "1"])]
    t = pd.crosstab(h1.challenger, h1.content_reopen).reindex(index=["lone", "organised"], columns=["1", "0"], fill_value=0)
    lone_r, lone_n = int(t.loc["lone", "1"]), int(t.loc["lone"].sum())
    org_r, org_n = int(t.loc["organised", "1"]), int(t.loc["organised"].sum())
    p_h1 = stats.fisher_exact(t.values, alternative="less").pvalue if lone_n and org_n else float("nan")
    out["H1"] = dict(lone=f"{lone_r}/{lone_n}", organised=f"{org_r}/{org_n}", p=p_h1,
                     falsified=(lone_n and org_n and lone_r / lone_n >= org_r / org_n))
    # H1 case-level sign test
    better = worse = 0
    for _, g in h1.groupby("case"):
        lo = g[g.challenger == "lone"].content_reopen.astype(int)
        og = g[g.challenger == "organised"].content_reopen.astype(int)
        if len(lo) and len(og):
            if lo.mean() < og.mean():
                better += 1
            elif lo.mean() > og.mean():
                worse += 1
    out["H1_case_sign"] = dict(lone_lower=better, lone_higher=worse,
                               p=binom_greater(better, better + worse))
    # H2: successful lone episodes won on procedural grounds
    h2 = agg[(agg.challenger == "lone") & (agg.success == "1") & agg.ground.isin(["procedural", "substantive", "mixed"])]
    k2, n2 = int((h2.ground == "procedural").sum()), len(h2)
    out["H2"] = dict(procedural=f"{k2}/{n2}", p=binom_greater(k2, n2), descriptive_only=n2 < 5,
                     falsified=(n2 >= 5 and k2 / n2 <= 0.5))
    # H3: first content reopening per case is organised
    firsts = []
    for case, g in agg.groupby("case"):
        cr = g[g.content_reopen == "1"]
        if len(cr):
            firsts.append((case, cr.iloc[0].episode, cr.iloc[0].challenger))
    known = [f for f in firsts if f[2] in ("lone", "organised")]
    k3 = sum(f[2] == "organised" for f in known)
    out["H3"] = dict(organised_first=f"{k3}/{len(known)}", p=binom_greater(k3, len(known)),
                     falsified=(len(known) > 0 and k3 / len(known) <= 0.5), firsts=firsts)
    # H4: scope of content reopenings
    h4 = agg[(agg.content_reopen == "1") & agg.scope.isin(["own", "group", "class"])]
    k4, n4 = int((h4.scope == "class").sum()), len(h4)
    out["H4"] = dict(class_scope=f"{k4}/{n4}", p=binom_greater(k4, n4), falsified=(n4 > 0 and k4 / n4 <= 0.5))
    # S3: case-weighted means
    cw = []
    for case, g in h1.groupby("case"):
        lo = g[g.challenger == "lone"].content_reopen.astype(int)
        og = g[g.challenger == "organised"].content_reopen.astype(int)
        cw.append((case, lo.mean() if len(lo) else None, og.mean() if len(og) else None))
    lo_m = pd.Series([x[1] for x in cw if x[1] is not None]).mean()
    og_m = pd.Series([x[2] for x in cw if x[2] is not None]).mean()
    out["S3_case_weighted_reopen_rate"] = dict(lone=round(lo_m, 3), organised=round(og_m, 3))
    return out


def show(res):
    print(f"\n=== {res['label']} ===")
    for k, v in res.items():
        if k != "label":
            print(f"{k}: {v}")


def main():
    cod = load()
    print("coders:", sorted(cod.coder.unique()), "| episodes:", cod.groupby(['case', 'episode']).ngroups)
    print("\nKrippendorff alpha (nominal):")
    for v in VARS:
        a, n = kripp_alpha_nominal(cod, v)
        flag = "  UNRELIABLE (<0.40)" if a == a and a < 0.40 else ""
        print(f"  {v:15s} alpha={a:.3f} (units={n}){flag}")
    rec = cod.groupby("case").recognised.apply(lambda s: (s == "1").mean())
    print("\nshare of coder-episode rows recognised, by case:\n" + rec.round(2).to_string())

    agg = aggregate(cod)
    agg.to_csv(HERE / "panel-aggregated.csv", index=False)
    show(tests(agg, "Primary (all pairs)"))
    # S1: drop recognised coder-case pairs
    show(tests(aggregate(cod[cod.recognised != "1"]), "S1 (recognised pairs excluded)"))
    # S2: supported individuals re-coded as lone
    show(tests(aggregate(cod, recode_supported=True), "S2 (supported -> lone)"))


if __name__ == "__main__":
    main()
