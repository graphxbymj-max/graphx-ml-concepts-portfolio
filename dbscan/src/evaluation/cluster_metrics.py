import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors

from src.clustering.dbscan_utils import fit_dbscan


def k_distance_values(X, k: int = 6):
    """Return sorted k-nearest-neighbor distances for eps selection."""
    neighbors = NearestNeighbors(n_neighbors=k)
    neighbors.fit(X)
    distances, _ = neighbors.kneighbors(X)
    return np.sort(distances[:, -1])


def evaluate_dbscan_grid(X, eps_values, min_samples_values):
    """Evaluate DBSCAN across eps and min_samples combinations."""
    rows = []
    for min_samples in min_samples_values:
        for eps in eps_values:
            _, labels = fit_dbscan(X, eps=eps, min_samples=min_samples)
            clusters = len(set(labels)) - (1 if -1 in labels else 0)
            noise_rate = float(np.mean(labels == -1))
            score = np.nan
            if clusters >= 2 and np.sum(labels != -1) > clusters:
                score = silhouette_score(X[labels != -1], labels[labels != -1])
            rows.append(
                {
                    "eps": eps,
                    "min_samples": min_samples,
                    "clusters": clusters,
                    "noise_rate": noise_rate,
                    "silhouette_score": score,
                }
            )
    return pd.DataFrame(rows)

