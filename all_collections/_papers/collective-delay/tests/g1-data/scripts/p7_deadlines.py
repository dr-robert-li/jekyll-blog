"""P7: deadline-panel lead-time analysis (exploratory).

Usage: python3 -I p7_deadlines.py <panel.csv> <out_dir>
panel.csv columns: id,member,cluster,deadline,action,V,LR  (dates ISO YYYY-MM-DD)
lead_days = deadline - action (negative = after the deadline).
"""
import sys, pathlib
import numpy as np, pandas as pd
from scipy import stats

WINDOWS = (365, 730)
B = 10000


def u_pos(lead, W):
    """Position in a W-day pre-deadline window, 0 = at/after deadline, 1 = at/before window start."""
    return np.clip(lead / W, 0, 1)


def cluster_boot_spearman(df, x, y, rng):
    cl = df.cluster.unique(); rs = []
    groups = {c: df[df.cluster == c] for c in cl}
    for _ in range(B):
        s = pd.concat([groups[c] for c in rng.choice(cl, len(cl))])
        if s[x].nunique() < 2 or s[y].nunique() < 2: continue
        rs.append(stats.spearmanr(s[x], s[y]).statistic)
    return np.nanpercentile(rs, [2.5, 97.5])


def main(path, out):
    rng = np.random.default_rng(7); lines = []
    def emit(s=''): lines.append(s); print(s)
    df = pd.read_csv(path, parse_dates=['deadline', 'action'])
    df['lead'] = (df.deadline - df.action).dt.days
    emit('## Panel'); emit(df[['id', 'member', 'cluster', 'deadline', 'action', 'lead', 'V', 'LR']]
                           .to_markdown(index=False)); emit()
    n, k = len(df), df.cluster.nunique()
    emit(f'N members = {n}, clusters = {k}')
    emit(f'Median lead = {df.lead.median():.0f} days; share within 30 d = {(df.lead <= 30).mean():.2f}; '
         f'within 90 d = {(df.lead <= 90).mean():.2f}; after deadline = {(df.lead < 0).mean():.2f}')
    cm = df.groupby('cluster').lead.median()
    emit(f'Cluster-median leads: median of cluster medians = {cm.median():.0f} d; '
         f'clusters with median <= 30 d: {(cm <= 30).sum()}/{k}; <= 90 d: {(cm <= 90).sum()}/{k}')
    emit()
    emit('### Skew toward zero vs uniform null on a W-day pre-deadline window')
    emit('(u = lead/W clipped to [0,1]; leads beyond W count as u=1, i.e. against the hypothesis)')
    for W in WINDOWS:
        u = u_pos(df.lead.values, W)
        ks = stats.kstest(u, 'uniform', alternative='greater')  # H1: empirical CDF above uniform -> mass near 0
        q = (u <= 0.25).sum()
        bt = stats.binomtest(q, n, 0.25, alternative='greater')
        uc = df.assign(u=u).groupby('cluster').u.median().values
        ksc = stats.kstest(uc, 'uniform', alternative='greater')
        qc = (uc <= 0.25).sum(); btc = stats.binomtest(qc, k, 0.25, alternative='greater')
        emit(f'- W={W} d, members: KS D+={ks.statistic:.2f}, p={ks.pvalue:.4f}; '
             f'{q}/{n} in first quarter (u<=0.25), binomial p={bt.pvalue:.2g}')
        emit(f'- W={W} d, cluster medians: KS D+={ksc.statistic:.2f}, p={ksc.pvalue:.4f}; '
             f'{qc}/{k} in first quarter, binomial p={btc.pvalue:.2g}')
    emit()
    emit('### Lead time vs V and L^R (prediction: negative rho; more vetoes / stake -> later action)')
    df['loglead'] = np.sign(df.lead) * np.log1p(np.abs(df.lead))
    for x in ('V', 'LR'):
        r = stats.spearmanr(df[x], df.lead)
        p1 = stats.spearmanr(df[x], df.lead, alternative='less').pvalue
        lo, hi = cluster_boot_spearman(df, x, 'lead', rng)
        emit(f'- {x} vs lead: rho={r.statistic:.3f}, one-sided p(rho<0)={p1:.3f}, '
             f'cluster-bootstrap 95% CI [{lo:.2f}, {hi:.2f}], N={n}')
        nd = df.groupby('cluster').agg({x: 'mean', 'lead': 'median'})
        r2 = stats.spearmanr(nd[x], nd.lead)
        emit(f'  cluster level ({k} clusters, mean score vs median lead): rho={r2.statistic:.3f}, two-sided p={r2.pvalue:.3f}')
    ex = df[df.cluster != 'US debt limit']
    for x in ('V', 'LR'):
        r = stats.spearmanr(ex[x], ex.lead)
        emit(f'- excluding debt-limit cluster, {x} vs lead: rho={r.statistic:.3f}, p={r.pvalue:.3f}, N={len(ex)}')
    df['VxLR'] = df.V * df.LR
    r = stats.spearmanr(df.VxLR, df.lead); lo, hi = cluster_boot_spearman(df, 'VxLR', 'lead', rng)
    emit(f'- V*LR vs lead: rho={r.statistic:.3f}, p={r.pvalue:.3f}, CI [{lo:.2f}, {hi:.2f}]')
    pathlib.Path(out, 'p7-results-raw.txt').write_text('\n'.join(lines) + '\n')


def _check():
    assert list(u_pos(np.array([-5, 0, 365, 1000]), 365)) == [0, 0, 1, 1]


if __name__ == '__main__':
    _check()
    main(sys.argv[1], sys.argv[2])
