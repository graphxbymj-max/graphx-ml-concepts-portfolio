"""Data cleaning helpers."""

from pathlib import Path
import pandas as pd


def load_data(file_path):
    """Load a CSV file."""
    return pd.read_csv(file_path)


def missing_value_summary(df):
    """Return missing value counts and percentages."""
    return pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percentage": df.isna().mean() * 100,
    }).sort_values("missing_percentage", ascending=False)


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates().copy()


def handle_missing_values(df, numeric_strategy="median", categorical_strategy="mode"):
    """Fill missing values with simple, explicit strategies."""
    df = df.copy()
    for column in df.select_dtypes(include=["number"]).columns:
        if numeric_strategy == "mean":
            df[column] = df[column].fillna(df[column].mean())
        else:
            df[column] = df[column].fillna(df[column].median())
    for column in df.select_dtypes(include=["object", "category"]).columns:
        if categorical_strategy == "missing":
            df[column] = df[column].fillna("Unknown")
        else:
            mode_value = df[column].mode(dropna=True)
            df[column] = df[column].fillna(mode_value.iloc[0] if not mode_value.empty else "Unknown")
    return df


def save_processed_data(df, file_path):
    """Save a processed DataFrame."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
    return file_path
