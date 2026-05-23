"""
Evaluation utilities for the GraphX Labs Decision Trees project.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
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
    """Return sklearn classification report as a DataFrame."""
    report = classification_report(
        y_true,
        y_pred,
        output_dict=True,
        zero_division=0
    )
    return pd.DataFrame(report).transpose()


def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    """Plot and optionally save a confusion matrix."""
    labels = labels or ["No", "Yes"]
    matrix = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels,
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Decision Tree Confusion Matrix")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_roc_curve(y_true, y_prob, save_path=None):
    """Plot and optionally save a ROC curve for binary classification."""
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    auc = roc_auc_score(y_true, y_prob)
    plt.figure(figsize=(7, 5))
    plt.plot(fpr, tpr, label=f"Decision Tree (AUC = {auc:.3f})")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def train_vs_test_comparison(model, X_train, y_train, X_test, y_test):
    """Compare train and test accuracy to diagnose overfitting."""
    return {
        "train_accuracy": accuracy_score(y_train, model.predict(X_train)),
        "test_accuracy": accuracy_score(y_test, model.predict(X_test)),
    }


def feature_importance_plot(importance_df, top_n=15, save_path=None):
    """Plot top Decision Tree feature importances."""
    plot_df = importance_df.head(top_n).sort_values("importance")
    plt.figure(figsize=(9, 7))
    sns.barplot(data=plot_df, x="importance", y="feature", color="#2F80ED")
    plt.title("Top Decision Tree Feature Importances")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
