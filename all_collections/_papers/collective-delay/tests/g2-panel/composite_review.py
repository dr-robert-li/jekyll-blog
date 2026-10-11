"""Post-hoc composite review (EXPLORATORY, non-confirmatory). See composite-review.md.
Run: ../g1-data/.venv/bin/python -I composite_review.py"""
import re
import numpy as np, pandas as pd
from scipy import stats

d = pd.read_csv("panel-aggregated.csv")
t0 = dict(re.findall(r"^\| (K\d\d) \|[^|]*\|[^|]*\| (\d{4}) \|", open("case-list.md").read(), re.M))
d["t0"] = d.case.map(t0).astype(int)
d["lag_r"] = np.where(d.censored, d.lag.max() + 1, d.lag)  # censored tied at top, as in analysis.py
rho = lambda x, y: stats.spearmanr(x, y, nan_policy="omit").statistic
s = lambda v: (d[v] - 1) / 4  # 1-5 -> 0-1

# Pre-registered C, for reference
d["C"] = (6 - d.phi) + d.LR + d.V + d.rhat
# A: net-drive form of act_i. Drive = phi_eff = phi + M (B.4.1: phi = phi0 e^-lt + M);
#    barrier = L^R + V_net + rhat bias; V_net = V - 0.5*carrier (G.1.5: carrier raises H_elite).
#    0.5 (half the V range) is a prior choice, not fitted.
car = d.carrier  # NaN for K10, K28, K30, K31 -> composites with carrier are NaN there
d["Vnet"] = s("V") - 0.5 * car
d["A"] = (s("LR") + d.Vnet + s("rhat")) - (s("phi") + s("M"))
# B: threshold-crossing time. If filtered harm grows ~linearly, phi_eff*h*t > barrier
#    gives t* ~ barrier / phi_eff. 0.25 floor keeps phi_eff=0 finite.
d["B"] = (s("LR") + d.Vnet + s("rhat") + 0.25) / (s("phi") + s("M") + 0.25)

if __name__ == "__main__":
    vs = ["phi", "LR", "V", "rhat", "M", "dist", "carrier", "t0"]
    print("Spearman matrix (+lag_r):")
    print(d[vs + ["lag_r"]].corr("spearman").round(2).to_string())
    lag5 = d.lag > 5  # action after the t0+5 scoring point: scores are pre-outcome
    print(f"\ncases with lag<=5 (scored after action): {(~lag5).sum()}")
    for c in ["C", "A", "B", "V", "M"]:
        print(f"{c}: all rho={rho(d[c], d.lag_r):.2f} (n={d[c].notna().sum()}); "
              f"lag>5 rho={rho(d[c][lag5], d.lag_r[lag5]):.2f} (n={d[c][lag5].notna().sum()})")
    for w in (0, 0.25, 1.0):  # sensitivity to the carrier weight
        a = (s("LR") + s("V") - w * car + s("rhat")) - (s("phi") + s("M"))
        print(f"A with carrier weight {w}: rho={rho(a, d.lag_r):.2f}")
    print("\nRanks driving the reversal (C rank vs lag rank):")
    d["dr"] = d.C.rank() - d.lag_r.rank()
    print(d.reindex(d.dr.abs().sort_values(ascending=False).index)
          [["case", "t0", "phi", "LR", "V", "rhat", "M", "carrier", "C", "lag", "dr"]].head(8).to_string(index=False))
    assert abs(rho(d.C, d.lag_r) - (-0.30)) < 0.01  # matches results.md primary P1
    # Era: lag is capped at 2026 - t0, and later t0 also means a regulatory state existed.
    def prho(x, y=d.lag_r, z=d.t0):  # partial Spearman given t0 (rank residuals)
        m = x.notna()
        r = lambda v: stats.rankdata(v[m])
        res = lambda a: a - np.polyval(np.polyfit(r(z), a, 1), r(z))
        return stats.pearsonr(res(r(x)), res(r(y))).statistic
    print("\npartial rho | t0: " + ", ".join(f"{c}={prho(d[c]):.2f}" for c in ["C", "A", "B", "V", "M", "dist", "phi"]))
