"""Cleaning helpers for the XGBoost churn project."""

from pathlib import Path
import pandas as pd


def load_data(file_path):
    """Load a CSV file."""
    return pd.read_csv(file_path)


def clean_column_names(df):
    """Clean column names into lowercase snake_case."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    return df


def clean_telco_churn(df):
    """Clean the Telco churn dataset for modeling."""
    df = clean_column_names(df)
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")
    df["totalcharges"] = df["totalcharges"].fillna(df["totalcharges"].median())
    df = df.drop_duplicates().copy()
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})
    return df.drop(columns=["customerid"], errors="ignore")


def missing_value_summary(df):
    """Return missing counts and percentages."""
    return pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percentage": df.isna().mean() * 100,
    }).sort_values("missing_percentage", ascending=False)


def save_processed_data(df, file_path):
    """Save processed data."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)
    return file_path
