"""Encoding helpers."""

import pandas as pd


def identify_categorical_columns(df, target_column=None):
    """Return categorical feature names."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["object", "category"]).columns.tolist()


def encode_categorical_features(df, categorical_columns=None):
    """One-hot encode categorical features."""
    if categorical_columns is None:
        categorical_columns = identify_categorical_columns(df)
    return pd.get_dummies(df, columns=categorical_columns, drop_first=True)


def prepare_features_target(df, target_column):
    """Split features and target."""
    return df.drop(columns=[target_column]), df[target_column]
