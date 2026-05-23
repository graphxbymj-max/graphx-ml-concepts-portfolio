"""SHAP explainability helpers."""

import shap


def compute_tree_shap_values(model, X_sample):
    """Compute SHAP values for a tree-based model."""
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)
    return explainer, shap_values
