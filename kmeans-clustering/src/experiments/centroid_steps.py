import numpy as np
import sklearn.cluster._kmeans as sklearn_kmeans
from sklearn.cluster import KMeans
from contextlib import nullcontext


def centroid_snapshots(X, n_clusters: int = 5, max_steps: int = 5, random_state: int = 42):
    """Fit KMeans with increasing iterations to create centroid movement snapshots."""
    sklearn_kmeans.threadpool_info = lambda: []
    sklearn_kmeans.threadpool_limits = lambda *args, **kwargs: nullcontext()
    snapshots = []
    previous_centers = None
    for step in range(1, max_steps + 1):
        model = KMeans(
            n_clusters=n_clusters,
            random_state=random_state,
            n_init=1,
            init="random",
            max_iter=step,
        )
        labels = model.fit_predict(X)
        centers = model.cluster_centers_.copy()
        movement = np.nan
        if previous_centers is not None and previous_centers.shape == centers.shape:
            movement = float(np.linalg.norm(np.sort(centers, axis=0) - np.sort(previous_centers, axis=0)))
        snapshots.append({"step": step, "labels": labels, "centers": centers, "movement": movement})
        previous_centers = centers
    return snapshots
