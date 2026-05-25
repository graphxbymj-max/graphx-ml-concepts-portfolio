"""SHAP helper functions."""
from __future__ import annotations
import numpy as np
import pandas as pd
import shap


def compute_tree_shap(model, X):
    """Compute SHAP explanation object for a tree model."""
    explainer = shap.Explainer(model, X)
    explanation = explainer(X)
    return explainer, explanation


def mean_abs_shap(explanation, feature_names) -> pd.DataFrame:
    """Summarize global importance as mean absolute SHAP value."""
    values = explanation.values
    if values.ndim == 3:
        values = values[:, :, 1]
    importance = np.abs(values).mean(axis=0)
    return pd.DataFrame({'feature': feature_names, 'mean_abs_shap': importance}).sort_values('mean_abs_shap', ascending=False)


def local_contribution_frame(explanation, X, index: int) -> pd.DataFrame:
    """Return feature-level contributions for one prediction."""
    values = explanation[index].values
    if values.ndim > 1:
        values = values[:, 1]
    return pd.DataFrame({
        'feature': X.columns,
        'value': X.iloc[index].values,
        'shap_value': values,
        'abs_shap': np.abs(values),
    }).sort_values('abs_shap', ascending=False)
