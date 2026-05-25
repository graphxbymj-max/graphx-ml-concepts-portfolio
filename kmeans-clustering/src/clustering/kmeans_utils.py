import pandas as pd
import sklearn.cluster._kmeans as sklearn_kmeans
from sklearn.cluster import KMeans
from contextlib import nullcontext


def patch_threadpoolctl_for_macos():
    """Avoid a local macOS/OpenBLAS threadpool introspection issue."""
    sklearn_kmeans.threadpool_info = lambda: []
    sklearn_kmeans.threadpool_limits = lambda *args, **kwargs: nullcontext()


def fit_kmeans(X, n_clusters: int, random_state: int = 42, n_init: int = 20):
    """Fit KMeans and return model plus labels."""
    patch_threadpoolctl_for_macos()
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    labels = model.fit_predict(X)
    return model, labels


def cluster_summary(df: pd.DataFrame, labels, features):
    """Summarize cluster size and feature profiles."""
    profiled = df.copy()
    profiled["cluster"] = labels
    summary = profiled.groupby("cluster")[features].mean().round(2)
    summary["customers"] = profiled["cluster"].value_counts().sort_index()
    return summary.reset_index()


def assign_segment_names(summary: pd.DataFrame) -> pd.DataFrame:
    """Attach simple business-friendly names from income/spending patterns."""
    named = summary.copy()
    names = []
    for _, row in named.iterrows():
        income = row.get("annual_income", 0)
        spend = row.get("spending_score", 0)
        if income >= 70 and spend >= 65:
            names.append("Premium high-value customers")
        elif income >= 70 and spend <= 35:
            names.append("High-income cautious spenders")
        elif income <= 40 and spend >= 60:
            names.append("Budget enthusiastic shoppers")
        elif income <= 45 and spend <= 40:
            names.append("Low-income careful shoppers")
        else:
            names.append("Balanced everyday customers")
    named["segment_name"] = names
    return named
