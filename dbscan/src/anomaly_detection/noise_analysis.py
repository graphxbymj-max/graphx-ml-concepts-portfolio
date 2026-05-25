import pandas as pd


def noise_summary(df: pd.DataFrame, labels) -> dict:
    """Summarize DBSCAN noise points."""
    noise_mask = labels == -1
    return {
        "total_points": len(labels),
        "noise_points": int(noise_mask.sum()),
        "noise_rate": float(noise_mask.mean()),
    }


def attach_cluster_labels(df: pd.DataFrame, labels) -> pd.DataFrame:
    """Attach cluster labels and human-readable point type."""
    labeled = df.copy()
    labeled["cluster"] = labels
    labeled["point_type"] = labeled["cluster"].map(lambda x: "noise" if x == -1 else "clustered")
    return labeled

