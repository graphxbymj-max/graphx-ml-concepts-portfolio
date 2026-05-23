"""
Feature engineering utilities for the GraphX Labs Decision Trees project.
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def identify_categorical_columns(df, target_column=None):
    """Identify categorical feature columns."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["object", "category"]).columns.tolist()


def identify_numerical_columns(df, target_column=None):
    """Identify numerical feature columns."""
    feature_df = df.drop(columns=[target_column]) if target_column else df
    return feature_df.select_dtypes(include=["number", "bool"]).columns.tolist()


def encode_categorical_features(df, categorical_columns=None):
    """One-hot encode categorical variables for scikit-learn models."""
    if categorical_columns is None:
        categorical_columns = identify_categorical_columns(df)
    return pd.get_dummies(df, columns=categorical_columns, drop_first=True)


def prepare_features_target(df, target_column):
    """Split a DataFrame into feature matrix X and target vector y."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def scale_features(X_train, X_test):
    """
    Scale numerical features.

    Decision Trees do not require feature scaling because they split on
    thresholds, not distances. This helper is included for comparison with
    models such as Logistic Regression, SVM, or KNN.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler
