"""Categorical encoding helpers."""

import pandas as pd


def identify_categorical_columns(df, target_column=None):
    """Return categorical feature columns."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["object", "category"]).columns.tolist()


def one_hot_encode(df, columns=None, drop_first=True):
    """One-hot encode selected categorical columns."""
    if columns is None:
        columns = identify_categorical_columns(df)
    return pd.get_dummies(df, columns=columns, drop_first=drop_first)


def group_rare_categories(df, column, min_frequency=0.01, other_label="Other"):
    """Group rare categories into an Other bucket."""
    df = df.copy()
    frequencies = df[column].value_counts(normalize=True)
    common_values = frequencies[frequencies >= min_frequency].index
    df[column] = df[column].where(df[column].isin(common_values), other_label)
    return df
