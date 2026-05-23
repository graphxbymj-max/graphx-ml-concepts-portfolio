"""
GraphX Labs Logistic Regression Project

Feature engineering utilities for:
- creating intuitive employee-risk features
- identifying numeric and categorical columns
- building preprocessing transformers
"""

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def create_employee_features(df):
    """
    Create simple HR features that are easy to explain.

    Parameters:
    -----------
    df : pd.DataFrame

    Returns:
    --------
    pd.DataFrame
    """

    df = df.copy()

    df["income_per_job_level"] = (
        df["monthlyincome"] / df["joblevel"].replace(0, np.nan)
    )

    df["years_without_promotion_ratio"] = (
        df["yearssincelastpromotion"] /
        df["yearsatcompany"].replace(0, np.nan)
    )

    df["early_career_flag"] = (
        df["totalworkingyears"] <= 3
    ).astype(int)

    df["long_commute_flag"] = (
        df["distancefromhome"] >= 15
    ).astype(int)

    df = df.fillna(0)

    return df


def drop_identifier_columns(
    df,
    columns_to_drop=None
):
    """
    Drop identifier or low-value columns before modeling.

    Parameters:
    -----------
    df : pd.DataFrame
    columns_to_drop : list

    Returns:
    --------
    pd.DataFrame
    """

    df = df.copy()

    if columns_to_drop is None:
        columns_to_drop = ["employeenumber"]

    existing_columns = [
        column for column in columns_to_drop
        if column in df.columns
    ]

    return df.drop(columns=existing_columns)


def get_feature_types(
    df,
    target_column="attrition"
):
    """
    Identify numerical and categorical feature columns.

    Parameters:
    -----------
    df : pd.DataFrame
    target_column : str

    Returns:
    --------
    numerical_features : list
    categorical_features : list
    """

    feature_df = df.drop(columns=[target_column])

    numerical_features = (
        feature_df
        .select_dtypes(include=["int64", "float64"])
        .columns
        .tolist()
    )

    categorical_features = (
        feature_df
        .select_dtypes(include=["object", "category"])
        .columns
        .tolist()
    )

    return numerical_features, categorical_features


def build_preprocessor(
    numerical_features,
    categorical_features
):
    """
    Build preprocessing transformer for Logistic Regression.

    Numerical features are scaled.
    Categorical features are one-hot encoded.

    Parameters:
    -----------
    numerical_features : list
    categorical_features : list

    Returns:
    --------
    sklearn.compose.ColumnTransformer
    """

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                numerical_features
            ),
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore",
                    drop="first"
                ),
                categorical_features
            )
        ]
    )

    return preprocessor


def get_processed_feature_names(
    preprocessor,
    numerical_features,
    categorical_features
):
    """
    Return feature names after preprocessing.

    Parameters:
    -----------
    preprocessor : fitted ColumnTransformer
    numerical_features : list
    categorical_features : list

    Returns:
    --------
    list
    """

    categorical_names = (
        preprocessor
        .named_transformers_["cat"]
        .get_feature_names_out(categorical_features)
        .tolist()
    )

    return numerical_features + categorical_names


if __name__ == "__main__":

    print("Feature engineering module loaded successfully.")

