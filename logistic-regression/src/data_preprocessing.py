"""
GraphX Labs Logistic Regression Project

Data preprocessing utilities for:
- loading datasets
- cleaning column names
- checking missing values
- removing duplicate rows
- preparing a binary classification target
"""

import pandas as pd


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

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
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

    missing_percentage = df.isnull().mean() * 100

    missing_summary = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percentage": missing_percentage
    })

    return missing_summary.sort_values(
        by="missing_percentage",
        ascending=False
    )


def remove_duplicate_rows(df):
    """
    Remove duplicate rows from a DataFrame.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    return df.drop_duplicates().copy()


def encode_binary_target(
    df,
    target_column="attrition",
    positive_label="Yes"
):
    """
    Encode a Yes/No target as 1/0.

    Parameters:
    -----------
    df : pd.DataFrame
    target_column : str
    positive_label : str

    Returns:
    --------
    pd.DataFrame
    """

    df = df.copy()

    df[target_column] = (
        df[target_column]
        .astype(str)
        .str.strip()
        .eq(positive_label)
        .astype(int)
    )

    return df


def drop_constant_columns(df):
    """
    Drop columns that have only one unique value.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    df = df.copy()

    constant_columns = [
        column
        for column in df.columns
        if df[column].nunique(dropna=False) == 1
    ]

    return df.drop(columns=constant_columns)


def basic_cleaning_pipeline(
    df,
    target_column="attrition"
):
    """
    Run the basic cleaning steps for this project.

    Parameters:
    -----------
    df : pd.DataFrame
    target_column : str

    Returns:
    --------
    pd.DataFrame
    """

    df = clean_column_names(df)

    df = remove_duplicate_rows(df)

    df = encode_binary_target(
        df,
        target_column=target_column
    )

    df = drop_constant_columns(df)

    return df


if __name__ == "__main__":

    print("Data preprocessing module loaded successfully.")

