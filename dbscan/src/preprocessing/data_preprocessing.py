from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = ["x_activity", "y_activity"]


def create_noisy_customer_activity(random_state: int = 42) -> pd.DataFrame:
    """Create a noisy irregular customer activity map for density clustering."""
    X, community = make_moons(n_samples=500, noise=0.075, random_state=random_state)
    rng = np.random.default_rng(random_state)
    outliers = rng.uniform(low=[-1.6, -1.0], high=[2.6, 1.7], size=(45, 2))
    X_all = np.vstack([X, outliers])
    source = np.r_[np.repeat("dense_activity", len(X)), np.repeat("rare_activity", len(outliers))]
    community_all = np.r_[community, np.repeat(-1, len(outliers))]
    df = pd.DataFrame(X_all, columns=FEATURE_COLUMNS)
    df["customer_event_id"] = [f"EVT-{i:04d}" for i in range(1, len(df) + 1)]
    df["source"] = source
    df["reference_pattern"] = community_all
    df["activity_intensity"] = np.round(
        50 + 18 * df["x_activity"] + 12 * df["y_activity"] + rng.normal(0, 6, len(df)),
        2,
    )
    return df[["customer_event_id", "x_activity", "y_activity", "activity_intensity", "source", "reference_pattern"]]


def save_raw_and_processed(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save raw and processed copies of the synthetic customer activity data."""
    df = create_noisy_customer_activity()
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(raw_path, index=False)
    df.to_csv(processed_path, index=False)
    return df


def scale_features(df: pd.DataFrame, features=None):
    """Scale selected numeric features for density-based clustering."""
    features = features or FEATURE_COLUMNS
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[features])
    scaled_df = pd.DataFrame(scaled, columns=features, index=df.index)
    return scaled_df, scaler

