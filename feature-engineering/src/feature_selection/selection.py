"""Feature selection helpers."""

import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_classif


def select_top_mutual_information_features(X, y, k=50, random_state=42):
    """Select top k features using mutual information."""
    selector = SelectKBest(score_func=mutual_info_classif, k=min(k, X.shape[1]))
    X_selected = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support()].tolist()
    scores = pd.DataFrame({"feature": X.columns, "score": selector.scores_}).sort_values("score", ascending=False)
    return X_selected, selected_features, scores, selector


def high_correlation_pairs(df, threshold=0.9):
    """Return pairs of numerical features with high absolute correlation."""
    corr = df.corr(numeric_only=True).abs()
    pairs = []
    for i, col in enumerate(corr.columns):
        for other in corr.columns[i + 1:]:
            if corr.loc[col, other] >= threshold:
                pairs.append((col, other, corr.loc[col, other]))
    return pairs
