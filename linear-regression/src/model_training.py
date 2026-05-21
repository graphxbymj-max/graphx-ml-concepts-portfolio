"""
GraphX Labs Linear Regression Project

Model training utilities for:
- train/test splitting
- Linear Regression model training
- prediction generation
- model pipeline preparation
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def split_features_target(
    df,
    target_column="box_office"
):
    """
    Split dataframe into features (X)
    and target variable (y).

    Parameters:
    -----------
    df : pd.DataFrame
    target_column : str

    Returns:
    --------
    X : pd.DataFrame
    y : pd.Series
    """

    X = df.drop(target_column, axis=1)

    y = df[target_column]

    return X, y


def perform_train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
):
    """
    Split data into train and test sets.

    Parameters:
    -----------
    X : pd.DataFrame
    y : pd.Series
    test_size : float
    random_state : int

    Returns:
    --------
    X_train, X_test, y_train, y_test
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )


def initialize_linear_regression():
    """
    Initialize Linear Regression model.

    Returns:
    --------
    sklearn.linear_model.LinearRegression
    """

    model = LinearRegression()

    return model


def train_linear_regression_model(
    model,
    X_train,
    y_train
):
    """
    Train Linear Regression model.

    Parameters:
    -----------
    model : sklearn model
    X_train : pd.DataFrame
    y_train : pd.Series

    Returns:
    --------
    trained model
    """

    model.fit(X_train, y_train)

    return model


def generate_predictions(
    model,
    X_test
):
    """
    Generate predictions using trained model.

    Parameters:
    -----------
    model : trained sklearn model
    X_test : pd.DataFrame

    Returns:
    --------
    np.array
    """

    predictions = model.predict(X_test)

    return predictions


def create_feature_target_sets(
    df,
    feature_columns,
    target_column
):
    """
    Create feature matrix and target vector.

    Parameters:
    -----------
    df : pd.DataFrame
    feature_columns : list
    target_column : str

    Returns:
    --------
    X : pd.DataFrame
    y : pd.Series
    """

    X = df[feature_columns]

    y = df[target_column]

    return X, y


def print_dataset_shapes(
    X_train,
    X_test,
    y_train,
    y_test
):
    """
    Print train/test dataset shapes.

    Parameters:
    -----------
    X_train, X_test, y_train, y_test
    """

    print("Training Features Shape:", X_train.shape)

    print("Testing Features Shape:", X_test.shape)

    print("Training Target Shape:", y_train.shape)

    print("Testing Target Shape:", y_test.shape)


def get_model_intercept(model):
    """
    Return model intercept.

    Parameters:
    -----------
    model : trained sklearn model

    Returns:
    --------
    float
    """

    return model.intercept_


def get_model_coefficients(
    model,
    feature_names
):
    """
    Return dataframe of model coefficients.

    Parameters:
    -----------
    model : trained sklearn model
    feature_names : list

    Returns:
    --------
    pd.DataFrame
    """

    coefficients = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": model.coef_
    })

    return coefficients.sort_values(
        by="Coefficient",
        ascending=False
    )


if __name__ == "__main__":

    print("Model training module loaded successfully.")