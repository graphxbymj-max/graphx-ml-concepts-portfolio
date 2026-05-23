"""
Data preprocessing utilities for the GraphX Labs Decision Trees project.
"""

from pathlib import Path
import pandas as pd


def load_data(file_path, sep=","):
    """Load a CSV dataset into a pandas DataFrame."""
    return pd.read_csv(file_path, sep=sep)


def clean_column_names(df):
    """Standardize column names for easier analysis."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def check_missing_values(df):
    """Return a missing-value summary sorted by missing percentage."""
    summary = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percentage": df.isna().mean() * 100
    })
    return summary.sort_values("missing_percentage", ascending=False)


def handle_missing_values(df):
    """Fill missing values using median for numeric and mode for categorical."""
    df = df.copy()
    numeric_columns = df.select_dtypes(include=["number"]).columns
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    for column in categorical_columns:
        mode_value = df[column].mode(dropna=True)
        fill_value = mode_value.iloc[0] if not mode_value.empty else "unknown"
        df[column] = df[column].fillna(fill_value)

    return df


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates().copy()


def save_processed_data(df, file_path):
    """Save processed data to CSV."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
    return file_path
