from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def save_current_figure(path: str | Path):
    """Save the active matplotlib figure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_cluster_scatter(df, labels, output_path=None, title="DBSCAN clusters"):
    """Plot DBSCAN-style clusters with noise highlighted."""
    plot_df = df.copy()
    plot_df["cluster"] = labels
    plot_df["cluster_label"] = plot_df["cluster"].map(lambda x: "Noise" if x == -1 else f"Cluster {x}")
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=plot_df,
        x="x_activity",
        y="y_activity",
        hue="cluster_label",
        style=plot_df["cluster"].eq(-1),
        palette="tab10",
        s=70,
        edgecolor="white",
    )
    plt.title(title)
    plt.xlabel("Activity dimension 1")
    plt.ylabel("Activity dimension 2")
    plt.legend(title="DBSCAN label", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_k_distance(distances, output_path=None):
    """Plot sorted k-distance values."""
    plt.figure(figsize=(9, 5))
    plt.plot(range(len(distances)), distances)
    plt.title("K-Distance Graph: Looking for the eps Bend")
    plt.xlabel("Points sorted by neighbor distance")
    plt.ylabel("Distance to kth nearest neighbor")
    plt.grid(alpha=0.25)
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_parameter_heatmap(results_df, output_path=None):
    """Plot DBSCAN cluster count over eps/min_samples."""
    pivot = results_df.pivot(index="min_samples", columns="eps", values="clusters")
    plt.figure(figsize=(10, 4))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title("DBSCAN Parameter Sweep: Number of Clusters")
    plt.xlabel("eps")
    plt.ylabel("min_samples")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()


def plot_kmeans_vs_dbscan(df, kmeans_labels, dbscan_labels, output_path=None):
    """Plot KMeans and DBSCAN results side by side."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True)
    sns.scatterplot(data=df.assign(cluster=kmeans_labels), x="x_activity", y="y_activity", hue="cluster", palette="tab10", s=60, ax=axes[0], legend=False)
    axes[0].set_title("KMeans: Forced round-ish partitions")
    sns.scatterplot(data=df.assign(cluster=dbscan_labels), x="x_activity", y="y_activity", hue="cluster", palette="tab10", s=60, ax=axes[1], legend=False)
    axes[1].set_title("DBSCAN: Dense communities plus noise")
    for ax in axes:
        ax.set_xlabel("Activity dimension 1")
        ax.set_ylabel("Activity dimension 2")
    if output_path:
        save_current_figure(output_path)
    return axes


def plot_pca_clusters(pca_df, labels, output_path=None):
    """Plot clusters in PCA space."""
    plot_df = pca_df.copy()
    plot_df["cluster"] = labels
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=plot_df, x="PC1", y="PC2", hue="cluster", palette="tab10", s=70, edgecolor="white")
    plt.title("PCA View of DBSCAN Labels")
    plt.legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
    if output_path:
        save_current_figure(output_path)
    return plt.gca()

