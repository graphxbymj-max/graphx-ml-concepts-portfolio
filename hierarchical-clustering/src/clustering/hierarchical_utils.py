import pandas as pd
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering


def compute_linkage_matrix(X, method: str = "ward", metric: str = "euclidean"):
    """Compute a scipy linkage matrix."""
    if method == "ward":
        return linkage(X, method=method)
    return linkage(X, method=method, metric=metric)


def fit_agglomerative(X, n_clusters: int = 5, linkage_method: str = "ward"):
    """Fit AgglomerativeClustering and return model plus labels."""
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage_method)
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

