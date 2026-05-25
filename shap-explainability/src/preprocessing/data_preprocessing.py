"""Dataset loading and preprocessing helpers for SHAP explainability."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


def load_breast_cancer_dataframe() -> pd.DataFrame:
    """Load the Breast Cancer Wisconsin Diagnostic dataset as an interpretable DataFrame."""
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=[c.replace(' ', '_') for c in data.feature_names])
    df['diagnosis'] = data.target
    df['diagnosis_label'] = df['diagnosis'].map({0: 'malignant', 1: 'benign'})
    df['is_malignant'] = (df['diagnosis'] == 0).astype(int)
    return df


def save_datasets(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save raw and processed versions of the project dataset."""
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df = load_breast_cancer_dataframe()
    df.to_csv(raw_path, index=False)
    processed = df.drop(columns=['diagnosis']).copy()
    processed.to_csv(processed_path, index=False)
    return processed


def split_features_target(df: pd.DataFrame, target: str = 'is_malignant', test_size: float = 0.25, random_state: int = 42):
    """Split features and target for classification."""
    drop_cols = [target, 'diagnosis_label']
    X = df.drop(columns=[c for c in drop_cols if c in df.columns])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
