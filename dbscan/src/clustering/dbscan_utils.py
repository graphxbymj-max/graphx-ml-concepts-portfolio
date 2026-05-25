import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from contextlib import nullcontext
import sklearn.cluster._kmeans as sklearn_kmeans


def fit_dbscan(X, eps: float = 0.22, min_samples: int = 6):
    """Fit DBSCAN and return model plus labels."""
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(X)
    return model, labels


def fit_kmeans(X, n_clusters: int = 2, random_state: int = 42):
    """Fit KMeans with a local macOS threadpool compatibility patch."""
    sklearn_kmeans.threadpool_info = lambda: []
    sklearn_kmeans.threadpool_limits = lambda *args, **kwargs: nullcontext()
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=20)
    labels = model.fit_predict(X)
    return model, labels


def cluster_counts(labels) -> pd.DataFrame:
    """Return counts for clusters and noise."""
    return (
        pd.Series(labels)
        .value_counts()
        .sort_index()
        .rename_axis("cluster")
        .reset_index(name="points")
        .assign(cluster_type=lambda d: d["cluster"].map(lambda x: "noise" if x == -1 else "cluster"))
    )

