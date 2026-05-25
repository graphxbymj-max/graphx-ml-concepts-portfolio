"""Data generation and preparation helpers for the A/B testing project."""
from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


def simulate_ab_test_data(n_users: int = 50000, seed: int = 42) -> pd.DataFrame:
    """Create a realistic ecommerce checkout A/B test dataset.

    The simulation keeps assignment randomized, then adds realistic context effects
    from device, traffic source, country, weekday, and a new checkout CTA.
    """
    rng = np.random.default_rng(seed)
    user_id = np.arange(1, n_users + 1)
    group = rng.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])
    variant = np.where(group == 'A', 'old_checkout_cta', 'new_secure_checkout_cta')

    start = np.datetime64('2026-03-01')
    timestamps = start + rng.integers(0, 28 * 24 * 60, size=n_users).astype('timedelta64[m]')

    device = rng.choice(['desktop', 'mobile', 'tablet'], size=n_users, p=[0.46, 0.44, 0.10])
    country = rng.choice(['US', 'IN', 'UK', 'CA', 'AU'], size=n_users, p=[0.44, 0.22, 0.14, 0.12, 0.08])
    traffic_source = rng.choice(['search', 'paid_ads', 'social', 'email', 'direct'], size=n_users, p=[0.30, 0.26, 0.18, 0.14, 0.12])

    base_logit = -2.16  # about 10.3% before context effects
    device_effect = {'desktop': 0.18, 'mobile': -0.13, 'tablet': -0.04}
    source_effect = {'email': 0.34, 'direct': 0.21, 'search': 0.08, 'paid_ads': -0.06, 'social': -0.18}
    country_effect = {'US': 0.08, 'IN': -0.04, 'UK': 0.03, 'CA': 0.02, 'AU': -0.02}
    weekday = pd.to_datetime(timestamps).dayofweek.to_numpy()
    weekend_effect = np.where(weekday >= 5, -0.07, 0.03)
    treatment_effect = np.where(group == 'B', 0.125, 0.0)  # roughly 1.1-1.3 absolute points

    logits = (
        base_logit
        + np.vectorize(device_effect.get)(device)
        + np.vectorize(source_effect.get)(traffic_source)
        + np.vectorize(country_effect.get)(country)
        + weekend_effect
        + treatment_effect
        + rng.normal(0, 0.08, size=n_users)
    )
    probability = 1 / (1 + np.exp(-logits))
    converted = rng.binomial(1, probability)

    order_value = np.where(
        converted == 1,
        np.clip(rng.normal(86, 24, size=n_users) + np.where(group == 'B', 2.5, 0), 18, 240),
        0,
    ).round(2)

    df = pd.DataFrame({
        'user_id': user_id,
        'timestamp': pd.to_datetime(timestamps),
        'group': group,
        'variant': variant,
        'device': device,
        'country': country,
        'traffic_source': traffic_source,
        'converted': converted.astype(int),
        'conversion_probability_simulated': probability.round(4),
        'revenue': order_value,
    })
    return df


def prepare_ab_test_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add analysis-ready date fields and basic revenue metrics."""
    out = df.copy()
    out['timestamp'] = pd.to_datetime(out['timestamp'])
    out['date'] = out['timestamp'].dt.date
    out['day_of_week'] = out['timestamp'].dt.day_name()
    out['is_treatment'] = (out['group'] == 'B').astype(int)
    out['converted_bool'] = out['converted'].astype(bool)
    out['revenue_per_user'] = out['revenue'].astype(float)
    return out


def save_datasets(raw_path: str | Path, processed_path: str | Path, n_users: int = 50000, seed: int = 42) -> pd.DataFrame:
    """Simulate, prepare, and save raw and processed datasets."""
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    raw = simulate_ab_test_data(n_users=n_users, seed=seed)
    processed = prepare_ab_test_data(raw)
    raw.to_csv(raw_path, index=False)
    processed.to_csv(processed_path, index=False)
    return processed
