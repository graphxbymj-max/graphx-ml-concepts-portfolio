"""Visualization helpers."""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score


def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
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


def plot_roc_curve(y_true, probabilities_by_model, save_path=None):
    plt.figure(figsize=(7, 5))
    for label, probabilities in probabilities_by_model.items():
        fpr, tpr, _ = roc_curve(y_true, probabilities)
        auc = roc_auc_score(y_true, probabilities)
        plt.plot(fpr, tpr, label=f"{label} AUC = {auc:.3f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_feature_importance(importance_df, top_n=20, save_path=None):
    plot_df = importance_df.head(top_n).sort_values("importance")
    plt.figure(figsize=(9, 8))
    sns.barplot(data=plot_df, x="importance", y="feature", color="#2F80ED")
    plt.title("Top XGBoost Feature Importances")
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
