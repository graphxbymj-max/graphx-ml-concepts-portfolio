from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import learning_curve, validation_curve


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_repeated_splits(split_df, output_path=None):
    """Plot repeated train/test split results."""
    plt.figure(figsize=(10, 5))
    plt.plot(split_df["random_state"], split_df["test_accuracy"], marker="o", label="Test accuracy")
    plt.axhline(split_df["test_accuracy"].mean(), color="#2c7fb8", linestyle="--", label="Mean test accuracy")
    plt.fill_between(
        split_df["random_state"],
        split_df["test_accuracy"].mean() - split_df["test_accuracy"].std(),
        split_df["test_accuracy"].mean() + split_df["test_accuracy"].std(),
        alpha=0.18,
        color="#2c7fb8",
        label="+/- 1 std",
    )
    plt.title("One Train-Test Split Can Be Lucky or Unlucky")
    plt.xlabel("Random state")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_fold_scores(scores_df, output_path=None):
    """Plot fold-level cross-validation scores."""
    plt.figure(figsize=(10, 5))
    sns.barplot(data=scores_df, x="fold", y="score", hue="model")
    plt.title("Cross-Validation Scores by Fold")
    plt.xlabel("Fold")
    plt.ylabel("Accuracy")
    plt.ylim(max(0, scores_df["score"].min() - 0.05), min(1.0, scores_df["score"].max() + 0.05))
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_score_boxplot(scores_df, output_path=None):
    """Plot distribution of fold scores by model."""
    plt.figure(figsize=(9, 5))
    sns.boxplot(data=scores_df, x="model", y="score")
    sns.stripplot(data=scores_df, x="model", y="score", color="black", alpha=0.55)
    plt.title("Fold Score Distribution: Reliability Is a Range, Not One Number")
    plt.xlabel("")
    plt.ylabel("Accuracy")
    plt.xticks(rotation=12, ha="right")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_kfold_visualization(n_samples=30, n_splits=5, output_path=None):
    """Create a simple visual explanation of KFold rotation."""
    fold_ids = np.arange(n_samples) % n_splits
    matrix = []
    for fold in range(n_splits):
        matrix.append(np.where(fold_ids == fold, 1, 0))
    matrix = np.array(matrix)
    plt.figure(figsize=(10, 3.6))
    sns.heatmap(matrix, cmap=["#d9ead3", "#e06666"], cbar=False, linewidths=0.5, linecolor="white")
    plt.title("KFold Visualization: Each Fold Takes a Turn as Validation Data")
    plt.xlabel("Sample index")
    plt.ylabel("Validation fold")
    plt.yticks(np.arange(n_splits) + 0.5, [f"Fold {i}" for i in range(1, n_splits + 1)], rotation=0)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_learning_curves(model, X, y, cv, output_path=None):
    """Plot learning curves."""
    train_sizes, train_scores, validation_scores = learning_curve(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy",
        train_sizes=np.linspace(0.1, 1.0, 8),
        n_jobs=-1,
    )
    plt.figure(figsize=(10, 5))
    plt.plot(train_sizes, train_scores.mean(axis=1), marker="o", label="Training score")
    plt.plot(train_sizes, validation_scores.mean(axis=1), marker="o", label="Validation score")
    plt.fill_between(
        train_sizes,
        validation_scores.mean(axis=1) - validation_scores.std(axis=1),
        validation_scores.mean(axis=1) + validation_scores.std(axis=1),
        alpha=0.18,
    )
    plt.title("Learning Curves: Does More Data Make Validation More Trustworthy?")
    plt.xlabel("Training examples")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_validation_curves(model, X, y, cv, param_name, param_range, output_path=None):
    """Plot validation curves."""
    train_scores, validation_scores = validation_curve(
        model,
        X,
        y,
        param_name=param_name,
        param_range=param_range,
        cv=cv,
        scoring="accuracy",
        n_jobs=-1,
    )
    plt.figure(figsize=(10, 5))
    plt.plot(param_range, train_scores.mean(axis=1), marker="o", label="Training score")
    plt.plot(param_range, validation_scores.mean(axis=1), marker="o", label="Validation score")
    plt.title("Validation Curve: Complexity vs Reliability")
    plt.xlabel(param_name)
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

