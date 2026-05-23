"""
GraphX Labs Logistic Regression Project

Model training utilities for:
- train/test splitting
- Logistic Regression pipeline creation
- prediction generation
- probability generation
"""

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def split_features_target(
    df,
    target_column="attrition"
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
    random_state=42,
    stratify=True
):
    """
    Split data into train and test sets.

    Parameters:
    -----------
    X : pd.DataFrame
    y : pd.Series
    test_size : float
    random_state : int
    stratify : bool

    Returns:
    --------
    X_train, X_test, y_train, y_test
    """

    stratify_values = y if stratify else None

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_values
    )


def initialize_logistic_regression(
    class_weight=None,
    random_state=42
):
    """
    Initialize Logistic Regression model.

    Parameters:
    -----------
    class_weight : str or dict
    random_state : int

    Returns:
    --------
    sklearn.linear_model.LogisticRegression
    """

    model = LogisticRegression(
        max_iter=1000,
        class_weight=class_weight,
        random_state=random_state
    )

    return model


def build_model_pipeline(
    preprocessor,
    model=None
):
    """
    Build a preprocessing + Logistic Regression pipeline.

    Parameters:
    -----------
    preprocessor : sklearn transformer
    model : sklearn model

    Returns:
    --------
    sklearn.pipeline.Pipeline
    """

    if model is None:
        model = initialize_logistic_regression()

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    return pipeline


def train_logistic_regression_model(
    model,
    X_train,
    y_train
):
    """
    Train Logistic Regression model or pipeline.

    Parameters:
    -----------
    model : sklearn model or pipeline
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
    X_test,
    threshold=0.5
):
    """
    Generate class predictions using a probability threshold.

    Parameters:
    -----------
    model : trained sklearn model
    X_test : pd.DataFrame
    threshold : float

    Returns:
    --------
    pd.Series
    """

    probabilities = generate_prediction_probabilities(
        model,
        X_test
    )

    predictions = (
        probabilities >= threshold
    ).astype(int)

    return predictions


def generate_prediction_probabilities(
    model,
    X_test
):
    """
    Generate positive-class probabilities.

    Parameters:
    -----------
    model : trained sklearn model
    X_test : pd.DataFrame

    Returns:
    --------
    np.array
    """

    probabilities = model.predict_proba(X_test)[:, 1]

    return probabilities


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


if __name__ == "__main__":

    print("Model training module loaded successfully.")

