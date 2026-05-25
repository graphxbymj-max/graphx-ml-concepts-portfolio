from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_elbow(k_results, output_path=None):
    """Plot inertia across K values."""
    plt.figure(figsize=(9, 5))
    sns.lineplot(data=k_results, x="k", y="inertia", marker="o")
    plt.title("Elbow Method: When More Clusters Stop Buying Much Clarity")
    plt.xlabel("Number of clusters (K)")
    plt.ylabel("Inertia")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_silhouette(k_results, output_path=None):
    """Plot silhouette score across K values."""
    plt.figure(figsize=(9, 5))
    sns.lineplot(data=k_results, x="k", y="silhouette_score", marker="o", color="#2ca25f")
    plt.title("Silhouette Scores: Are Clusters Cohesive and Separate?")
    plt.xlabel("Number of clusters (K)")
    plt.ylabel("Silhouette score")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_clusters(df, labels, output_path=None, centers=None):
    """Plot income vs spending clusters."""
    plot_df = df.copy()
    plot_df["cluster"] = labels
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=plot_df,
        x="annual_income",
        y="spending_score",
        hue="cluster",
        palette="tab10",
        s=80,
        edgecolor="white",
    )
    if centers is not None:
        plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=240, c="black", label="Centroids")
    plt.title("Customer Segments Emerging from Income and Spending Behavior")
    plt.xlabel("Annual income")
    plt.ylabel("Spending score")
    plt.legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_pca_clusters(pca_df, labels, output_path=None):
    """Plot clusters in PCA space."""
    plot_df = pca_df.copy()
    plot_df["cluster"] = labels
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=plot_df, x="PC1", y="PC2", hue="cluster", palette="tab10", s=80, edgecolor="white")
    plt.title("PCA Cluster Visualization: Compressing Behavior into Two Dimensions")
    plt.legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

