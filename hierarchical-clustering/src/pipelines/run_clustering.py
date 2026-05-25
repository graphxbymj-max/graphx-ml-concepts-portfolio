from src.clustering.hierarchical_utils import assign_segment_names, cluster_summary, fit_agglomerative
from src.preprocessing.data_preprocessing import FEATURE_COLUMNS, scale_features


def run_default_clustering(df, n_clusters: int = 5, linkage_method: str = "ward"):
    """Scale features, fit hierarchical clustering, and return labeled data plus summary."""
    scaled_df, scaler = scale_features(df, FEATURE_COLUMNS)
    model, labels = fit_agglomerative(scaled_df, n_clusters=n_clusters, linkage_method=linkage_method)
    summary = assign_segment_names(cluster_summary(df, labels, FEATURE_COLUMNS))
    labeled = df.copy()
    labeled["cluster"] = labels
    return labeled, summary, model, scaler

