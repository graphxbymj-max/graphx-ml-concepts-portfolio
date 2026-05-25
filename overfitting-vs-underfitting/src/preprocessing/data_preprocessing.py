from pathlib import Path

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


TARGET_COLUMN = "is_benign"


def load_healthcare_dataset() -> pd.DataFrame:
    """Load the Breast Cancer Wisconsin dataset as a tidy dataframe."""
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame.copy()
    df[TARGET_COLUMN] = df["target"].astype(int)
    df = df.drop(columns=["target"])
    return df


def save_raw_and_processed(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save raw and lightly processed copies of the dataset."""
    df = load_healthcare_dataset()
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(raw_path, index=False)
    df.to_csv(processed_path, index=False)
    return df


def make_train_test_split(
    df: pd.DataFrame,
    target: str = TARGET_COLUMN,
    test_size: float = 0.25,
    random_state: int = 42,
):
    """Return a stratified train/test split."""
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


def scale_train_test(X_train, X_test):
    """Fit a StandardScaler on training data and transform both splits."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

