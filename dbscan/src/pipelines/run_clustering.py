from src.anomaly_detection.noise_analysis import attach_cluster_labels, noise_summary
from src.clustering.dbscan_utils import fit_dbscan
from src.preprocessing.data_preprocessing import FEATURE_COLUMNS, scale_features


def run_default_dbscan(df, eps: float = 0.22, min_samples: int = 6):
    """Scale features, fit DBSCAN, and return labeled data plus noise summary."""
    scaled_df, scaler = scale_features(df, FEATURE_COLUMNS)
    model, labels = fit_dbscan(scaled_df, eps=eps, min_samples=min_samples)
    labeled = attach_cluster_labels(df, labels)
    return labeled, noise_summary(df, labels), model, scaler

