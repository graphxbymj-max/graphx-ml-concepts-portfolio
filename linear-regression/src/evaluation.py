"""
GraphX Labs Linear Regression Project

Model evaluation utilities for:
- regression metrics
- residual analysis
- coefficient interpretation
- prediction visualization
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_regression_model(y_true, y_pred):
    """
    Compute regression evaluation metrics.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like

    Returns:
    --------
    dict
    """

    mae = mean_absolute_error(y_true, y_pred)

    mse = mean_squared_error(y_true, y_pred)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_true, y_pred)

    metrics = {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }

    return metrics


def print_metrics(metrics):
    """
    Print evaluation metrics neatly.

    Parameters:
    -----------
    metrics : dict
    """

    print("Model Evaluation Metrics")
    print("-" * 30)

    for metric, value in metrics.items():
        print(f"{metric}: {value:,.4f}")


def plot_actual_vs_predicted(y_true, y_pred):
    """
    Plot actual vs predicted values.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like
    """

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        x=y_true,
        y=y_pred
    )

    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")

    plt.title("Actual vs Predicted Values")

    plt.show()


def calculate_residuals(y_true, y_pred):
    """
    Calculate residuals.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like

    Returns:
    --------
    np.array
    """

    residuals = y_true - y_pred

    return residuals


def plot_residual_distribution(residuals):
    """
    Plot residual distribution.

    Parameters:
    -----------
    residuals : array-like
    """

    plt.figure(figsize=(8, 6))

    sns.histplot(
        residuals,
        kde=True
    )

    plt.title("Residual Distribution")

    plt.xlabel("Residual Error")

    plt.show()


def plot_residuals_vs_predictions(y_pred, residuals):
    """
    Plot residuals against predictions.

    Parameters:
    -----------
    y_pred : array-like
    residuals : array-like
    """

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        x=y_pred,
        y=residuals
    )

    plt.axhline(
        y=0,
        color="red",
        linestyle="--"
    )

    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")

    plt.title("Residuals vs Predicted Values")

    plt.show()


def get_coefficients(model, feature_names):
    """
    Create coefficient dataframe.

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

    coefficients = coefficients.sort_values(
        by="Coefficient",
        ascending=False
    )

    return coefficients


def plot_coefficients(coefficients_df):
    """
    Plot feature coefficients.

    Parameters:
    -----------
    coefficients_df : pd.DataFrame
    """

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=coefficients_df,
        x="Coefficient",
        y="Feature"
    )

    plt.title("Linear Regression Coefficients")

    plt.show()


def compare_models(model_results):
    """
    Compare multiple model evaluation results.

    Parameters:
    -----------
    model_results : pd.DataFrame
    """

    comparison_melted = model_results.melt(
        id_vars="Model",
        var_name="Metric",
        value_name="Value"
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=comparison_melted,
        x="Metric",
        y="Value",
        hue="Model"
    )

    plt.title("Model Comparison")

    plt.show()


if __name__ == "__main__":

    print("Evaluation module loaded successfully.")