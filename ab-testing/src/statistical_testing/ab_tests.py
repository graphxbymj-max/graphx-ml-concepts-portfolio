"""Statistical testing helpers for conversion experiments."""
from __future__ import annotations

import math
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


def _group_counts(df: pd.DataFrame, group_col: str = 'group', outcome_col: str = 'converted'):
    grouped = df.groupby(group_col)[outcome_col].agg(['sum', 'count']).sort_index()
    if len(grouped) != 2:
        raise ValueError('A/B test helpers expect exactly two groups.')
    return grouped


def two_proportion_ztest(df: pd.DataFrame, group_col: str = 'group', outcome_col: str = 'converted') -> dict[str, float]:
    """Run a two-sided two-proportion z-test for A/B conversion rates."""
    grouped = _group_counts(df, group_col, outcome_col)
    counts = grouped['sum'].to_numpy()
    nobs = grouped['count'].to_numpy()
    stat, p_value = proportions_ztest(count=counts, nobs=nobs, alternative='two-sided')
    rates = counts / nobs
    return {
        'control_rate': float(rates[0]),
        'treatment_rate': float(rates[1]),
        'z_statistic': float(stat),
        'p_value': float(p_value),
        'absolute_lift': float(rates[1] - rates[0]),
        'relative_lift': float((rates[1] - rates[0]) / rates[0]),
    }


def proportion_ci(successes: int, n: int, confidence: float = 0.95) -> tuple[float, float]:
    """Wilson confidence interval for one conversion rate."""
    if n == 0:
        return (np.nan, np.nan)
    z = stats.norm.ppf(1 - (1 - confidence) / 2)
    phat = successes / n
    denom = 1 + z**2 / n
    center = (phat + z**2 / (2 * n)) / denom
    half = z * math.sqrt((phat * (1 - phat) / n) + (z**2 / (4 * n**2))) / denom
    return float(center - half), float(center + half)


def conversion_confidence_intervals(df: pd.DataFrame, group_col: str = 'group', outcome_col: str = 'converted', confidence: float = 0.95) -> pd.DataFrame:
    """Return Wilson intervals for each experiment group."""
    grouped = _group_counts(df, group_col, outcome_col)
    rows = []
    for group, row in grouped.iterrows():
        low, high = proportion_ci(int(row['sum']), int(row['count']), confidence)
        rows.append({
            group_col: group,
            'users': int(row['count']),
            'conversions': int(row['sum']),
            'conversion_rate': row['sum'] / row['count'],
            'ci_low': low,
            'ci_high': high,
        })
    return pd.DataFrame(rows)


def difference_confidence_interval(df: pd.DataFrame, group_col: str = 'group', outcome_col: str = 'converted', confidence: float = 0.95) -> dict[str, float]:
    """Normal approximation interval for treatment-control conversion difference."""
    grouped = _group_counts(df, group_col, outcome_col)
    counts = grouped['sum'].to_numpy(dtype=float)
    nobs = grouped['count'].to_numpy(dtype=float)
    rates = counts / nobs
    diff = rates[1] - rates[0]
    se = math.sqrt(rates[0] * (1 - rates[0]) / nobs[0] + rates[1] * (1 - rates[1]) / nobs[1])
    z = stats.norm.ppf(1 - (1 - confidence) / 2)
    return {
        'difference': float(diff),
        'standard_error': float(se),
        'ci_low': float(diff - z * se),
        'ci_high': float(diff + z * se),
    }
