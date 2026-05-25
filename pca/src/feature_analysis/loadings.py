import pandas as pd


def component_loadings(pca, feature_names, n_components: int = 5) -> pd.DataFrame:
    """Return PCA component loadings."""
    rows = []
    for i in range(min(n_components, pca.components_.shape[0])):
        for feature, loading in zip(feature_names, pca.components_[i]):
            rows.append({"component": f"PC{i + 1}", "feature": feature, "loading": loading})
    return pd.DataFrame(rows)


def top_loadings(loadings_df: pd.DataFrame, component: str, n: int = 10) -> pd.DataFrame:
    """Return top absolute loadings for one component."""
    subset = loadings_df[loadings_df["component"] == component].copy()
    subset["abs_loading"] = subset["loading"].abs()
    return subset.sort_values("abs_loading", ascending=False).head(n)

