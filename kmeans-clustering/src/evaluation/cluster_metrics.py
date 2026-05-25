import pandas as pd
import sklearn.cluster._kmeans as sklearn_kmeans
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from contextlib import nullcontext


def evaluate_k_range(X, k_values=range(2, 11), random_state: int = 42):
    """Calculate inertia and silhouette score across K values."""
    sklearn_kmeans.threadpool_info = lambda: []
    sklearn_kmeans.threadpool_limits = lambda *args, **kwargs: nullcontext()
    rows = []
    for k in k_values:
        model = KMeans(n_clusters=k, random_state=random_state, n_init=20)
        labels = model.fit_predict(X)
        rows.append(
            {
                "k": k,
                "inertia": model.inertia_,
                "silhouette_score": silhouette_score(X, labels),
            }
        )
    return pd.DataFrame(rows)
