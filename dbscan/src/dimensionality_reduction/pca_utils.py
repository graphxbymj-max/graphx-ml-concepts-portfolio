import pandas as pd
from sklearn.decomposition import PCA


def run_pca(X, n_components: int = 2):
    """Reduce data to principal components for visualization."""
    pca = PCA(n_components=n_components, random_state=42)
    components = pca.fit_transform(X)
    columns = [f"PC{i}" for i in range(1, n_components + 1)]
    return pd.DataFrame(components, columns=columns), pca

