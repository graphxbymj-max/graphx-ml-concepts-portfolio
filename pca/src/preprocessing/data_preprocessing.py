from pathlib import Path

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler


TARGET_COLUMN = "is_benign"


def load_healthcare_dataset() -> pd.DataFrame:
    """Load Breast Cancer Wisconsin data as a tidy dataframe."""
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame.copy()
    df[TARGET_COLUMN] = df["target"].astype(int)
    return df.drop(columns=["target"])


def save_raw_and_processed(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save raw and processed dataset copies."""
    df = load_healthcare_dataset()
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(raw_path, index=False)
    df.to_csv(processed_path, index=False)
    return df


def split_features_target(df: pd.DataFrame, target: str = TARGET_COLUMN):
    """Split dataframe into features and target."""
    return df.drop(columns=[target]), df[target]


def scale_features(X: pd.DataFrame):
    """Standardize features for PCA."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)
    return pd.DataFrame(scaled, columns=X.columns, index=X.index), scaler

