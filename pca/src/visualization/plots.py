from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def save_current_figure(path: str | Path):
    """Save active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_explained_variance(table, output_path=None):
    """Plot component explained variance."""
    plt.figure(figsize=(10, 5))
    sns.barplot(data=table.head(15), x="component", y="explained_variance_ratio", color="#2c7fb8")
    plt.title("Explained Variance: How Much Information Each Component Captures")
    plt.xlabel("Principal component")
    plt.ylabel("Explained variance ratio")
    plt.xticks(rotation=45)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_cumulative_variance(table, output_path=None):
    """Plot cumulative explained variance."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(table) + 1), table["cumulative_variance"], marker="o")
    plt.axhline(0.90, color="red", linestyle="--", label="90% variance")
    plt.axhline(0.95, color="purple", linestyle="--", label="95% variance")
    plt.title("Cumulative Explained Variance: Compression vs Information")
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative explained variance")
    plt.legend()
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_pca_scatter(pca_df, y, output_path=None):
    """Plot first two principal components."""
    plot_df = pca_df.copy()
    plot_df["target"] = y.map({0: "malignant", 1: "benign"}) if hasattr(y, "map") else y
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=plot_df, x="PC1", y="PC2", hue="target", s=70, edgecolor="white")
    plt.title("PCA Visualization: Complex Medical Data in Two Dimensions")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_loadings_heatmap(loadings_df, output_path=None):
    """Plot loadings heatmap."""
    pivot = loadings_df.pivot(index="feature", columns="component", values="loading")
    plt.figure(figsize=(8, max(7, 0.25 * len(pivot))))
    sns.heatmap(pivot, cmap="vlag", center=0)
    plt.title("Principal Component Loadings")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

