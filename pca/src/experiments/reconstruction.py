import pandas as pd
from sklearn.decomposition import PCA


def reconstruction_error_by_components(X, component_counts):
    """Calculate mean squared reconstruction error across component counts."""
    rows = []
    for n in component_counts:
        pca = PCA(n_components=n, random_state=42)
        transformed = pca.fit_transform(X)
        reconstructed = pca.inverse_transform(transformed)
        mse = ((X.values - reconstructed) ** 2).mean()
        rows.append({"n_components": n, "reconstruction_mse": mse, "cumulative_variance": pca.explained_variance_ratio_.sum()})
    return pd.DataFrame(rows)

