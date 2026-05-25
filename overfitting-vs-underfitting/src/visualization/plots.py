from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import learning_curve


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure with project defaults."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_train_test_bars(results_df, output_path=None):
    """Create a grouped train/test accuracy comparison."""
    plot_df = results_df.melt(
        id_vars="model",
        value_vars=["train_accuracy", "test_accuracy"],
        var_name="split",
        value_name="accuracy",
    )
    plt.figure(figsize=(10, 5))
    sns.barplot(data=plot_df, x="model", y="accuracy", hue="split", palette=["#34495e", "#2ca25f"])
    plt.ylim(0.75, 1.02)
    plt.title("Train vs Test Performance: Memorization Shows Up as a Gap")
    plt.xlabel("")
    plt.ylabel("Accuracy")
    plt.xticks(rotation=15, ha="right")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_complexity_curve(curve_df, output_path=None):
    """Plot model complexity against train and test accuracy."""
    plt.figure(figsize=(10, 5))
    plt.plot(curve_df["max_depth"], curve_df["train_accuracy"], marker="o", label="Train accuracy")
    plt.plot(curve_df["max_depth"], curve_df["test_accuracy"], marker="o", label="Test accuracy")
    plt.xlabel("Decision Tree max_depth")
    plt.ylabel("Accuracy")
    plt.title("Model Complexity Curve: Too Simple, Balanced, Too Flexible")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_learning_curves(model, X, y, output_path=None, cv=5, scoring="accuracy"):
    """Plot learning curves for a model."""
    train_sizes, train_scores, validation_scores = learning_curve(
        model,
        X,
        y,
        cv=cv,
        scoring=scoring,
        train_sizes=np.linspace(0.1, 1.0, 8),
        n_jobs=None,
    )
    train_mean = train_scores.mean(axis=1)
    validation_mean = validation_scores.mean(axis=1)

    plt.figure(figsize=(10, 5))
    plt.plot(train_sizes, train_mean, marker="o", label="Training score")
    plt.plot(train_sizes, validation_mean, marker="o", label="Validation score")
    plt.xlabel("Training examples")
    plt.ylabel("Accuracy")
    plt.title("Learning Curves: Is the Model Learning or Memorizing?")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

