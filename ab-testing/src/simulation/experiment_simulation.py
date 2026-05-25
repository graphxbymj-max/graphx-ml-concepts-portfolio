"""Simulation helpers for explaining randomness in A/B testing."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def simulate_repeated_experiments(n_experiments: int = 1000, n_per_group: int = 2000, p_control: float = 0.10, p_treatment: float = 0.112, seed: int = 7) -> pd.DataFrame:
    """Simulate many A/B tests to show how observed lift moves around."""
    rng = np.random.default_rng(seed)
    control = rng.binomial(n_per_group, p_control, size=n_experiments)
    treatment = rng.binomial(n_per_group, p_treatment, size=n_experiments)
    control_rate = control / n_per_group
    treatment_rate = treatment / n_per_group
    lift = treatment_rate - control_rate
    pooled = (control + treatment) / (2 * n_per_group)
    se = np.sqrt(pooled * (1 - pooled) * (2 / n_per_group))
    z_stat = np.divide(lift, se, out=np.zeros_like(lift), where=se > 0)
    p_value = 2 * (1 - stats.norm.cdf(np.abs(z_stat)))
    return pd.DataFrame({
        'experiment': np.arange(1, n_experiments + 1),
        'control_rate': control_rate,
        'treatment_rate': treatment_rate,
        'observed_lift': lift,
        'p_value': p_value,
        'significant_05': p_value < 0.05,
    })


def sample_size_sensitivity(sample_sizes=(200, 500, 1000, 2500, 5000, 10000), p_control: float = 0.10, p_treatment: float = 0.112, n_experiments: int = 600, seed: int = 11) -> pd.DataFrame:
    """Estimate how often experiments become significant as sample size grows."""
    rows = []
    for i, n in enumerate(sample_sizes):
        sims = simulate_repeated_experiments(n_experiments=n_experiments, n_per_group=n, p_control=p_control, p_treatment=p_treatment, seed=seed + i)
        rows.append({
            'n_per_group': n,
            'mean_lift': sims['observed_lift'].mean(),
            'lift_std': sims['observed_lift'].std(),
            'share_significant': sims['significant_05'].mean(),
        })
    return pd.DataFrame(rows)
