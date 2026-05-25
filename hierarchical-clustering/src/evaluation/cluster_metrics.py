import pandas as pd
from sklearn.metrics import silhouette_score

from src.clustering.hierarchical_utils import fit_agglomerative


def evaluate_cluster_counts(X, cluster_counts=range(2, 9), linkage_method: str = "ward"):
    """Calculate silhouette score across cluster counts."""
    rows = []
    for k in cluster_counts:
        _, labels = fit_agglomerative(X, n_clusters=k, linkage_method=linkage_method)
        rows.append({"n_clusters": k, "linkage": linkage_method, "silhouette_score": silhouette_score(X, labels)})
    return pd.DataFrame(rows)


def compare_linkages(X, n_clusters: int = 5, linkage_methods=("single", "complete", "average", "ward")):
    """Compare silhouette score across linkage methods."""
    rows = []
    for method in linkage_methods:
        _, labels = fit_agglomerative(X, n_clusters=n_clusters, linkage_method=method)
        rows.append({"linkage": method, "n_clusters": n_clusters, "silhouette_score": silhouette_score(X, labels)})
    return pd.DataFrame(rows)

