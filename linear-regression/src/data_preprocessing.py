"""
GraphX Labs Linear Regression Project

Data preprocessing utilities for:
- loading datasets
- cleaning column names
- handling missing values
- converting data types
- basic preprocessing workflows
"""

import pandas as pd
import numpy as np


def load_data(file_path):
    """
    Load CSV dataset into a pandas DataFrame.

    Parameters:
    -----------
    file_path : str
        Path to CSV file

    Returns:
    --------
    pd.DataFrame
    """

    df = pd.read_csv(file_path)

    return df


def clean_column_names(df):
    """
    Clean and standardize column names.

    Converts:
    - spaces to underscores
    - lowercase formatting
    - removes brackets

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )

    return df


def convert_release_date(df, column_name="release_date_datetime"):
    """
    Convert release date column to datetime format.

    Parameters:
    -----------
    df : pd.DataFrame
    column_name : str

    Returns:
    --------
    pd.DataFrame
    """

    df[column_name] = pd.to_datetime(
        df[column_name],
        errors="coerce"
    )

    return df


def create_date_features(df, column_name="release_date_datetime"):
    """
    Create additional date-based features.

    Features:
    - release_year
    - release_month
    - release_decade

    Parameters:
    -----------
    df : pd.DataFrame
    column_name : str

    Returns:
    --------
    pd.DataFrame
    """

    df["release_year"] = df[column_name].dt.year

    df["release_month"] = df[column_name].dt.month

    df["release_decade"] = (
        df["release_year"] // 10
    ) * 10

    return df


def clean_rotten_tomatoes_score(df):
    """
    Convert Rotten Tomatoes score from string
    percentage to numeric.

    Example:
    '95%' -> 95

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    df["rotten_tomatoes_score"] = (
        df["rotten_tomatoes"]
        .str.replace("%", "", regex=False)
        .astype(float)
    )

    return df


def check_missing_values(df):
    """
    Return missing value summary.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    missing_count = df.isnull().sum()

    missing_percentage = (
        df.isnull().mean() * 100
    )

    missing_summary = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percentage": missing_percentage
    })

    return missing_summary.sort_values(
        by="missing_percentage",
        ascending=False
    )


def drop_missing_rows(df):
    """
    Remove rows containing missing values.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    return df.dropna()


def select_model_features(df):
    """
    Select features for Linear Regression model.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    selected_columns = [
        "running_time_minutes",
        "budget",
        "imdb",
        "release_year",
        "box_office"
    ]

    return df[selected_columns].copy()


def create_log_features(df):
    """
    Create log-transformed features.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    df["log_budget"] = np.log1p(df["budget"])

    df["log_box_office"] = np.log1p(
        df["box_office"]
    )

    return df


if __name__ == "__main__":

    print("Data preprocessing module loaded successfully.")