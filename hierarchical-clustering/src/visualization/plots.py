from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_dendrogram(linkage_matrix, output_path=None, truncate_mode=None, p=30, title="Dendrogram"):
    """Plot a dendrogram from a linkage matrix."""
    plt.figure(figsize=(13, 6))
    dendrogram(linkage_matrix, truncate_mode=truncate_mode, p=p, leaf_rotation=90, leaf_font_size=9)
    plt.title(title)
    plt.xlabel("Customers or merged customer groups")
    plt.ylabel("Merge distance")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_clusters(df, labels, output_path=None):
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
    plt.title("Hierarchical Customer Segments from Income and Spending Behavior")
    plt.xlabel("Annual income")
    plt.ylabel("Spending score")
    plt.legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_linkage_comparison(df, label_map, output_path=None):
    """Plot cluster assignments for multiple linkage methods."""
    methods = list(label_map.keys())
    fig, axes = plt.subplots(1, len(methods), figsize=(5 * len(methods), 4), sharex=True, sharey=True)
    if len(methods) == 1:
        axes = [axes]
    for ax, method in zip(axes, methods):
        sns.scatterplot(
            data=df.assign(cluster=label_map[method]),
            x="annual_income",
            y="spending_score",
            hue="cluster",
            palette="tab10",
            s=55,
            legend=False,
            ax=ax,
        )
        ax.set_title(f"{method.title()} linkage")
        ax.set_xlabel("Annual income")
    axes[0].set_ylabel("Spending score")
    plt.suptitle("Linkage Methods Change How Relationships Are Merged")
    if output_path:
        save_current_figure(output_path)
    return axes


def plot_silhouette_scores(scores_df, output_path=None):
    """Plot silhouette scores by number of clusters."""
    plt.figure(figsize=(9, 5))
    sns.lineplot(data=scores_df, x="n_clusters", y="silhouette_score", marker="o")
    plt.title("Choosing Clusters with Silhouette Score")
    plt.xlabel("Number of clusters")
    plt.ylabel("Silhouette score")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_pca_clusters(pca_df, labels, output_path=None):
    """Plot clusters in PCA space."""
    plot_df = pca_df.copy()
    plot_df["cluster"] = labels
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=plot_df, x="PC1", y="PC2", hue="cluster", palette="tab10", s=80, edgecolor="white")
    plt.title("PCA View of Hierarchical Clusters")
    plt.legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

