"""Data preprocessing helpers for the Random Forest project."""

from pathlib import Path
import pandas as pd


def load_data(file_path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def clean_column_names(df):
    """Convert column names to lowercase snake_case."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def check_missing_values(df):
    """Return missing-value counts and percentages."""
    return pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percentage": df.isna().mean() * 100,
    }).sort_values("missing_percentage", ascending=False)


def handle_missing_values(df):
    """Fill numeric missing values with median and categorical with mode."""
    df = df.copy()
    for column in df.select_dtypes(include=["number"]).columns:
        df[column] = df[column].fillna(df[column].median())
    for column in df.select_dtypes(include=["object", "category"]).columns:
        mode_value = df[column].mode(dropna=True)
        df[column] = df[column].fillna(mode_value.iloc[0] if not mode_value.empty else "unknown")
    return df


def remove_duplicates(df):
    """Drop duplicate rows."""
    return df.drop_duplicates().copy()


def save_processed_data(df, file_path):
    """Save a processed DataFrame to CSV."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
    return file_path
