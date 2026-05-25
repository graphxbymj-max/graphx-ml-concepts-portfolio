from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay,
    confusion_matrix,
)


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_confusion_matrix(y_true, y_pred, output_path=None, labels=("Stayed", "Churned")):
    """Plot a confusion matrix heatmap."""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.title("Confusion Matrix: The Four Ways a Model Can Be Right or Wrong")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_metric_bars(metrics_df, output_path=None):
    """Plot a compact metric comparison."""
    plot_df = metrics_df.melt(
        id_vars="threshold",
        value_vars=["accuracy", "precision", "recall", "f1"],
        var_name="metric",
        value_name="score",
    )
    plt.figure(figsize=(9, 5))
    sns.barplot(data=plot_df, x="metric", y="score", palette="Set2")
    plt.title("Metric Comparison at the Default Threshold")
    plt.xlabel("")
    plt.ylabel("Score")
    plt.ylim(0, 1)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_precision_recall_tradeoff(threshold_df, output_path=None):
    """Plot precision and recall across thresholds."""
    plt.figure(figsize=(10, 5))
    plt.plot(threshold_df["threshold"], threshold_df["precision"], marker="o", label="Precision")
    plt.plot(threshold_df["threshold"], threshold_df["recall"], marker="o", label="Recall")
    plt.plot(threshold_df["threshold"], threshold_df["f1"], marker="o", label="F1-score")
    plt.title("Precision-Recall Tradeoff: The Threshold Is a Business Decision")
    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_roc_curve(y_true, y_proba, output_path=None):
    """Plot ROC curve."""
    RocCurveDisplay.from_predictions(y_true, y_proba)
    plt.title("ROC Curve: How Well the Model Separates Classes")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_pr_curve(y_true, y_proba, output_path=None):
    """Plot precision-recall curve."""
    PrecisionRecallDisplay.from_predictions(y_true, y_proba)
    plt.title("Precision-Recall Curve: More Honest for Imbalanced Problems")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_business_cost(threshold_df, output_path=None):
    """Plot estimated cost across thresholds."""
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=threshold_df, x="threshold", y="estimated_cost", marker="o")
    plt.title("Business Cost by Threshold")
    plt.xlabel("Threshold")
    plt.ylabel("Estimated cost")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

