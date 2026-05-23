"""Plotting helpers."""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


def plot_missing_values(missing_df, save_path=None):
    """Plot top missing value percentages."""
    plot_df = missing_df[missing_df["missing_percentage"] > 0].head(15).sort_values("missing_percentage")
    plt.figure(figsize=(8, 5))
    sns.barplot(data=plot_df, x="missing_percentage", y=plot_df.index, color="#2F80ED")
    plt.xlabel("Missing Percentage")
    plt.ylabel("Feature")
    plt.title("Missing Values by Feature")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    """Plot confusion matrix."""
    labels = labels or ["Not Canceled", "Canceled"]
    matrix = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
