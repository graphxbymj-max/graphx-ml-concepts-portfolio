from src.clustering.kmeans_utils import assign_segment_names, cluster_summary, fit_kmeans
from src.preprocessing.data_preprocessing import FEATURE_COLUMNS, scale_features


def run_default_clustering(df, n_clusters: int = 5):
    """Scale features, fit KMeans, and return labeled data plus summary."""
    scaled_df, scaler = scale_features(df, FEATURE_COLUMNS)
    model, labels = fit_kmeans(scaled_df, n_clusters=n_clusters)
    summary = assign_segment_names(cluster_summary(df, labels, FEATURE_COLUMNS))
    labeled = df.copy()
    labeled["cluster"] = labels
    return labeled, summary, model, scaler

