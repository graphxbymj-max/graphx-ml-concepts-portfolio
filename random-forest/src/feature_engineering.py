"""Feature engineering helpers for Random Forest modeling."""

import pandas as pd
from sklearn.model_selection import train_test_split


def identify_categorical_columns(df, target_column=None):
    """Return categorical feature names."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["object", "category"]).columns.tolist()


def identify_numerical_columns(df, target_column=None):
    """Return numerical feature names."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["number", "bool"]).columns.tolist()


def encode_categorical_features(df, categorical_columns=None):
    """One-hot encode categorical features."""
    if categorical_columns is None:
        categorical_columns = identify_categorical_columns(df)
    return pd.get_dummies(df, columns=categorical_columns, drop_first=True)


def prepare_features_target(df, target_column):
    """Split a DataFrame into X and y."""
    return df.drop(columns=[target_column]), df[target_column]


def prepare_train_test_split(X, y, test_size=0.2, random_state=42, stratify=True):
    """Create a reproducible train-test split."""
    stratify_values = y if stratify else None
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_values,
    )


def scaling_note():
    """Return a short explanation of why scaling is not required."""
    return "Random Forests do not require feature scaling because trees split using thresholds, not distance."
