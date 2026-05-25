import pandas as pd
from sklearn.decomposition import PCA


def fit_pca(X, n_components=None, random_state: int = 42):
    """Fit PCA and return model plus transformed dataframe."""
    pca = PCA(n_components=n_components, random_state=random_state)
    transformed = pca.fit_transform(X)
    columns = [f"PC{i}" for i in range(1, transformed.shape[1] + 1)]
    return pca, pd.DataFrame(transformed, columns=columns, index=X.index)


def explained_variance_table(pca) -> pd.DataFrame:
    """Return explained and cumulative variance."""
    table = pd.DataFrame(
        {
            "component": [f"PC{i}" for i in range(1, len(pca.explained_variance_ratio_) + 1)],
            "explained_variance_ratio": pca.explained_variance_ratio_,
        }
    )
    table["cumulative_variance"] = table["explained_variance_ratio"].cumsum()
    return table

