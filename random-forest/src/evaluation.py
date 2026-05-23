"""Evaluation and plotting utilities for the Random Forest project."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
    roc_curve,
)


def classification_metrics(y_true, y_pred, y_prob=None):
    """Return common classification metrics."""
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }
    if y_prob is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_prob)
    return metrics


def classification_report_df(y_true, y_pred):
    """Return classification report as a DataFrame."""
    return pd.DataFrame(
        classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    ).transpose()


def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    """Plot and optionally save a confusion matrix."""
    labels = labels or ["No Churn", "Churn"]
    matrix = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_roc_curve(y_true, y_prob, label="Model", save_path=None):
    """Plot and optionally save a ROC curve."""
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    auc = roc_auc_score(y_true, y_prob)
    plt.figure(figsize=(7, 5))
    plt.plot(fpr, tpr, label=f"{label} AUC = {auc:.3f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def feature_importance_plot(importance_df, top_n=20, save_path=None):
    """Plot top feature importances."""
    plot_df = importance_df.head(top_n).sort_values("importance")
    plt.figure(figsize=(9, 8))
    sns.barplot(data=plot_df, x="importance", y="feature", color="#2F80ED")
    plt.title("Top Random Forest Feature Importances")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_model_comparison(results_df, metric="roc_auc", save_path=None):
    """Plot model comparison for a selected metric."""
    plt.figure(figsize=(8, 5))
    sns.barplot(data=results_df, x="model", y=metric, color="#56CC9D")
    plt.title(f"Model Comparison by {metric.upper()}")
    plt.xlabel("")
    plt.ylabel(metric.upper())
    plt.xticks(rotation=15)
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
