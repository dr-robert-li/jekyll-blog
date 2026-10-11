"""P6: budget kurtosis vs pre-registered asymmetry score.

Usage: python3 -I p6_kurtosis.py <Budget_Authority_Adjusted_2018_for_PAP_1.csv> <out_dir> [--discretionary]
Coding (scores) is copied verbatim from out/p6-coding.md, which was written before the data were seen.
"""
import sys, pathlib
import numpy as np, pandas as pd
from scipy import stats

# (a, b) from p6-coding.md
SCORES = {1: (4, 2), 2: (4, 2), 3: (2, 4), 4: (4, 5), 5: (2, 3), 6: (3, 3), 7: (5, 4), 8: (4, 5),
          9: (3, 3), 10: (4, 4), 12: (3, 3), 13: (1, 2), 14: (3, 4), 15: (4, 5), 16: (4, 5),
          17: (5, 4), 18: (4, 4), 19: (5, 3), 20: (4, 3), 21: (4, 4)}
NAMES = {3: 'Health', 4: 'Agriculture', 5: 'Labor', 6: 'Education', 7: 'Environment', 8: 'Energy',
         10: 'Transportation', 12: 'Law/crime', 13: 'Social welfare', 14: 'Community dev/housing',
         15: 'Banking/commerce', 16: 'Defense', 17: 'Space/science', 19: 'Intl affairs', 20: 'Gov operations',
         21: 'Public lands/water'}
# OMB subfunction -> CAP major topic, from the PAP budget crosswalk (US-Budget-policy_crosswalk_19.2.csv),
# major budget codes, each subfunction assigned to exactly one topic. Topics 1, 2, 9 (no budget per crosswalk)
# and 18 (shares 150/376 with 19/15, no unique subfunction) cannot be measured.
SUB2TOPIC = {
    '551': 3, '552': 3, '571': 3, '703': 3,
    '351': 4, '352': 4,
    '504': 5, '505': 5, '603': 5, '554': 5,
    '501': 6, '502': 6, '503': 6, '702': 6,
    '304': 7,
    '271': 8, '272': 8, '274': 8, '276': 8,
    '401': 10, '402': 10, '403': 10, '407': 10,
    '751': 12, '752': 12, '753': 12, '754': 12,
    '506': 13, '601': 13, '605': 13, '609': 13, '651': 13,
    '451': 14, '452': 14, '604': 14, '371': 14, '704': 14,
    '373': 15, '376': 15, '453': 15,
    '051': 16, '053': 16, '054': 16, '152': 16, '701': 16, '705': 16,
    '251': 17, '252': 17, '306': 17,
    '151': 19, '153': 19, '154': 19, '155': 19,
    '801': 20, '802': 20, '803': 20, '804': 20, '805': 20, '806': 20, '808': 20, '602': 20, '372': 20,
    '301': 21, '302': 21, '303': 21,
}


def lkurt(x):
    """Sample L-kurtosis tau4 via unbiased probability-weighted moments (Hosking 1990). Normal = 0.1226."""
    x = np.sort(np.asarray(x, float)); n = len(x); i = np.arange(1, n + 1)
    b0 = x.mean()
    b1 = np.sum((i - 1) / (n - 1) * x) / n
    b2 = np.sum((i - 1) * (i - 2) / ((n - 1) * (n - 2)) * x) / n
    b3 = np.sum((i - 1) * (i - 2) * (i - 3) / ((n - 1) * (n - 2) * (n - 3)) * x) / n
    l2 = 2 * b1 - b0; l4 = 20 * b3 - 30 * b2 + 12 * b1 - b0
    return l4 / l2


def pct(series):
    """Annual % change; drop pairs where the base is <= 0 (undefined/sign-flipping)."""
    prev = series.shift(1)
    ch = (series - prev) / prev * 100
    return ch[(prev > 0)].dropna()


def load(path, programmatic_only):
    d = pd.read_csv(path)
    s = d[d.IsItSubFunction == 1].copy()
    if programmatic_only:
        s = s[s.programmatic == 1]
    s['sub'] = s.TrueCode.str[:3]
    s['topic'] = s['sub'].map(SUB2TOPIC)
    return s[s.topic.notna()]


def topic_table(s, y0, y1):
    rows = []
    tot = s.groupby('year').amount.sum()
    for t, g in s.groupby('topic'):
        ser = g.groupby('year').amount.sum().sort_index()
        ch = pct(ser)
        ch = ch[(ch.index >= y0) & (ch.index <= y1)]
        a, b = SCORES[int(t)]
        share = (ser / tot).loc[y0:y1].mean() * 100
        rows.append(dict(topic=int(t), name=NAMES[int(t)], a=a, b=b, A=a * b, Asum=a + b, n=len(ch),
                         share=share, kurt=stats.kurtosis(ch, fisher=True, bias=False), tau4=lkurt(ch)))
    df = pd.DataFrame(rows).sort_values('topic')
    return df[df.n >= 15]  # need enough changes for a 4th moment


def test(df, x='A', y='kurt'):
    r = stats.spearmanr(df[x], df[y], alternative='greater')
    return r.statistic, r.pvalue, len(df)


def sub_level(s, emit, tag):
    rows = []
    for sub, g in s.groupby('sub'):
        ch = pct(g.set_index('year').amount.sort_index())
        if len(ch) < 30: continue
        a, b = SCORES[int(g.topic.iloc[0])]
        rows.append(dict(sub=sub, topic=int(g.topic.iloc[0]), A=a * b, n=len(ch),
                         kurt=stats.kurtosis(ch, bias=False), tau4=lkurt(ch)))
    sd = pd.DataFrame(rows)
    emit(f'### Subfunction level ({tag})')
    for y in ('kurt', 'tau4'):
        rho, p, n = test(sd, 'A', y)
        emit(f'- A vs {y}: rho={rho:.3f}, one-sided p={p:.3f}, N={n} subfunctions in {sd.topic.nunique()} topics '
             '(not independent: scores constant within topic)')
    # topic-cluster permutation: permute scores across topics, keep subfunctions grouped
    rng = np.random.default_rng(1); topics = sorted(sd.topic.unique())
    obs = stats.spearmanr(sd.A, sd.tau4).statistic; cnt = 0; B = 10000
    Amap = {t: SCORES[t][0] * SCORES[t][1] for t in topics}
    for _ in range(B):
        perm = dict(zip(topics, rng.permutation([Amap[t] for t in topics])))
        cnt += stats.spearmanr(sd.topic.map(perm), sd.tau4).statistic >= obs
    emit(f'- topic-cluster permutation p (A vs tau4) = {(cnt + 1) / (B + 1):.3f}')
    emit()


def discretionary(path, out):
    """Follow-up (exploratory, specified in p6-results.md before running): discretionary subfunctions only."""
    out = pathlib.Path(out); lines = []
    def emit(s=''): lines.append(s); print(s)
    s = load(path, True); s = s[s.discretionary == 1]
    df = topic_table(s, 1948, 2017)
    emit('## Topic table: programmatic AND discretionary subfunctions, FY1948-2017')
    emit(df.to_markdown(index=False, floatfmt='.3f')); emit()
    for y in ('kurt', 'tau4'):
        rho, p, n = test(df, 'A', y)
        emit(f'- A vs {y}: rho={rho:.3f}, one-sided p={p:.3f}, N={n}')
    emit()
    sub_level(s, emit, 'programmatic AND discretionary, FY1948-2017, parent topic score')
    (out / 'p6-discretionary-raw.txt').write_text('\n'.join(lines) + '\n')


def main(path, out):
    out = pathlib.Path(out); lines = []
    def emit(s=''): lines.append(s); print(s)

    for prog in (True, False):
        s = load(path, prog)
        tag = 'programmatic subfunctions only (PRIMARY)' if prog else 'all subfunctions incl. financial (robustness)'
        for (y0, y1) in [(1948, 2017), (1948, 1976), (1977, 2017)]:
            df = topic_table(s, y0, y1)
            primary = prog and (y0, y1) == (1948, 2017)
            if primary:
                emit('## Topic table: ' + tag + f', FY{y0}-{y1}')
                emit(df.to_markdown(index=False, floatfmt='.3f')); emit()
            emit(f'### {tag}, FY{y0}-{y1}')
            for x, y in [('A', 'kurt'), ('Asum', 'kurt'), ('A', 'tau4'), ('Asum', 'tau4')]:
                rho, p, n = test(df, x, y)
                emit(f'- {x} vs {y}: rho={rho:.3f}, one-sided p={p:.3f}, N={n}')
            big = df[df.share >= 0.5]
            rho, p, n = test(big)
            emit(f'- excl. topics <0.5% mean share, A vs kurt: rho={rho:.3f}, p={p:.3f}, N={n} '
                 f'(dropped: {", ".join(df[df.share < 0.5].name) or "none"})')
            rho, p, n = test(big, 'A', 'tau4')
            emit(f'- excl. tiny, A vs tau4: rho={rho:.3f}, p={p:.3f}, N={n}')
            emit()

    # Subfunction level: parent's score, programmatic subfunctions, full period
    s = load(path, True)
    sub_level(s, emit, 'programmatic, FY1948-2017, parent topic score')

    # Jones et al. 2009 baseline: pooled subfunction changes
    pooled = pd.concat([pct(g.set_index('year').amount.sort_index()) for _, g in s.groupby('sub')])
    pooled = pooled.clip(lower=-100)
    emit('### Baseline (Jones et al. 2009 style): pooled annual % changes, all programmatic subfunctions')
    emit(f'- N={len(pooled)}, excess kurtosis={stats.kurtosis(pooled, bias=False):.1f}, '
         f'L-kurtosis={lkurt(pooled):.3f} (Normal 0.123)')
    tk = topic_table(s, 1948, 2017)
    emit(f'- topics with excess kurtosis > 0: {(tk['kurt'] > 0).sum()}/{len(tk)}; tau4 > 0.123: {(tk.tau4 > 0.1226).sum()}/{len(tk)}')
    # Confounds: mandatory share and size (partial Spearman, ranks residualised on ranks of controls)
    d = pd.read_csv(path); d = d[(d.IsItSubFunction == 1) & (d.programmatic == 1)].copy()
    d['topic'] = d.TrueCode.str[:3].map(SUB2TOPIC); d = d[d.topic.notna()]
    mand = d.assign(m=d.amount * d.mandatory).groupby('topic')[['m', 'amount']].sum()
    tk['mand'] = tk.topic.map(mand.m / mand.amount).values
    emit('### Confounds (programmatic, FY1948-2017)')
    emit(tk[['name', 'share', 'mand', 'kurt', 'tau4']].to_markdown(index=False, floatfmt='.3f'))
    for c in ('mand', 'share'):
        for y in ('kurt', 'tau4'):
            r = stats.spearmanr(tk[c], tk[y]); emit(f'- {c} vs {y}: rho={r.statistic:.3f}, two-sided p={r.pvalue:.3f}')
        r = stats.spearmanr(tk[c], tk.A); emit(f'- {c} vs A: rho={r.statistic:.3f}, two-sided p={r.pvalue:.3f}')
    R = tk[['A', 'kurt', 'tau4', 'mand', 'share']].rank()
    X = np.column_stack([np.ones(len(R)), R.mand, R.share])
    res = lambda v: v - X @ np.linalg.lstsq(X, v, rcond=None)[0]
    for y in ('kurt', 'tau4'):
        r = np.corrcoef(res(R.A.values), res(R[y].values))[0, 1]; df_ = len(R) - 4
        t = r * np.sqrt(df_ / (1 - r * r))
        emit(f'- partial Spearman A vs {y} | mandatory share, size: r={r:.3f}, one-sided p={stats.t.sf(t, df_):.3f}, df={df_}')
    (out / 'p6-results-raw.txt').write_text('\n'.join(lines) + '\n')


def _check():
    rng = np.random.default_rng(0)
    assert abs(lkurt(rng.normal(size=200000)) - 0.1226) < 0.005
    assert abs(lkurt(rng.uniform(size=200000))) < 0.005
    assert np.allclose(pct(pd.Series([100, 150, -10, 20])), [50.0, -160 / 1.5])


if __name__ == '__main__':
    _check()
    (discretionary if '--discretionary' in sys.argv else main)(sys.argv[1], sys.argv[2])
