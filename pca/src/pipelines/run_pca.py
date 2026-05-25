from src.dimensionality_reduction.pca_utils import explained_variance_table, fit_pca
from src.preprocessing.data_preprocessing import scale_features, split_features_target


def run_default_pca(df, n_components: int = 2):
    """Run default PCA workflow."""
    X, y = split_features_target(df)
    X_scaled, scaler = scale_features(X)
    pca, pca_df = fit_pca(X_scaled, n_components=n_components)
    return pca_df, y, explained_variance_table(pca), pca, scaler

