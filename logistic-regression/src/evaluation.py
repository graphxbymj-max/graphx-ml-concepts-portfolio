"""
GraphX Labs Logistic Regression Project

Model evaluation utilities for:
- classification metrics
- confusion matrix visualization
- ROC curve visualization
- coefficient interpretation
- threshold tuning
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve
)


def evaluate_classification_model(
    y_true,
    y_pred,
    y_prob
):
    """
    Compute classification evaluation metrics.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like
    y_prob : array-like

    Returns:
    --------
    dict
    """

    metrics = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1": f1_score(y_true, y_pred, zero_division=0),
        "ROC_AUC": roc_auc_score(y_true, y_prob)
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


def get_classification_report(
    y_true,
    y_pred
):
    """
    Return classification report as a DataFrame.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like

    Returns:
    --------
    pd.DataFrame
    """

    report = classification_report(
        y_true,
        y_pred,
        output_dict=True,
        zero_division=0
    )

    return pd.DataFrame(report).transpose()


def plot_confusion_matrix(
    y_true,
    y_pred,
    labels=None,
    save_path=None
):
    """
    Plot confusion matrix.

    Parameters:
    -----------
    y_true : array-like
    y_pred : array-like
    labels : list
    save_path : str
    """

    if labels is None:
        labels = ["Stayed", "Left"]

    matrix = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels
    )

    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.title("Confusion Matrix")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def plot_roc_curve(
    y_true,
    y_prob,
    save_path=None
):
    """
    Plot ROC curve.

    Parameters:
    -----------
    y_true : array-like
    y_prob : array-like
    save_path : str
    """

    false_positive_rate, true_positive_rate, _ = roc_curve(
        y_true,
        y_prob
    )

    auc_score = roc_auc_score(y_true, y_prob)

    plt.figure(figsize=(7, 5))

    plt.plot(
        false_positive_rate,
        true_positive_rate,
        label=f"Logistic Regression (AUC = {auc_score:.3f})"
    )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        color="gray"
    )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def get_coefficients(
    model_pipeline,
    feature_names
):
    """
    Create coefficient dataframe from a fitted pipeline.

    Parameters:
    -----------
    model_pipeline : fitted sklearn pipeline
    feature_names : list

    Returns:
    --------
    pd.DataFrame
    """

    coefficients = model_pipeline.named_steps["model"].coef_[0]

    coefficients_df = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": coefficients,
        "Odds_Ratio": np.exp(coefficients)
    })

    coefficients_df["Absolute_Coefficient"] = (
        coefficients_df["Coefficient"].abs()
    )

    return coefficients_df.sort_values(
        by="Absolute_Coefficient",
        ascending=False
    )


def plot_top_coefficients(
    coefficients_df,
    top_n=15,
    save_path=None
):
    """
    Plot strongest Logistic Regression coefficients.

    Parameters:
    -----------
    coefficients_df : pd.DataFrame
    top_n : int
    save_path : str
    """

    plot_df = coefficients_df.head(top_n).sort_values(
        by="Coefficient"
    )

    plt.figure(figsize=(9, 7))

    sns.barplot(
        data=plot_df,
        x="Coefficient",
        y="Feature"
    )

    plt.axvline(0, color="black", linewidth=1)
    plt.title("Top Logistic Regression Coefficients")
    plt.xlabel("Coefficient")
    plt.ylabel("Feature")

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def threshold_summary(
    y_true,
    y_prob,
    thresholds=None
):
    """
    Compare classification metrics across thresholds.

    Parameters:
    -----------
    y_true : array-like
    y_prob : array-like
    thresholds : list

    Returns:
    --------
    pd.DataFrame
    """

    if thresholds is None:
        thresholds = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    rows = []

    for threshold in thresholds:
        y_pred = (y_prob >= threshold).astype(int)

        rows.append({
            "Threshold": threshold,
            "Accuracy": accuracy_score(y_true, y_pred),
            "Precision": precision_score(y_true, y_pred, zero_division=0),
            "Recall": recall_score(y_true, y_pred, zero_division=0),
            "F1": f1_score(y_true, y_pred, zero_division=0)
        })

    return pd.DataFrame(rows)


def plot_precision_recall_by_threshold(
    y_true,
    y_prob,
    save_path=None
):
    """
    Plot precision and recall across thresholds.

    Parameters:
    -----------
    y_true : array-like
    y_prob : array-like
    save_path : str
    """

    precision, recall, thresholds = precision_recall_curve(
        y_true,
        y_prob
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        thresholds,
        precision[:-1],
        label="Precision"
    )

    plt.plot(
        thresholds,
        recall[:-1],
        label="Recall"
    )

    plt.xlabel("Classification Threshold")
    plt.ylabel("Score")
    plt.title("Precision and Recall by Threshold")
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


if __name__ == "__main__":

    print("Evaluation module loaded successfully.")

