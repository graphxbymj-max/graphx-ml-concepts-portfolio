import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def metrics_at_threshold(y_true, y_proba, threshold: float = 0.5) -> dict:
    """Calculate classification metrics at a probability threshold."""
    y_pred = (y_proba >= threshold).astype(int)
    return {
        "threshold": threshold,
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_true, y_proba),
        "predicted_positive_rate": y_pred.mean(),
    }


def threshold_table(y_true, y_proba, thresholds) -> pd.DataFrame:
    """Return metrics for many thresholds."""
    return pd.DataFrame([metrics_at_threshold(y_true, y_proba, t) for t in thresholds])


def business_cost(y_true, y_proba, threshold: float, fp_cost: float = 25, fn_cost: float = 200) -> dict:
    """Estimate a simple business cost from false positives and false negatives."""
    y_pred = (y_proba >= threshold).astype(int)
    fp = int(((y_pred == 1) & (y_true == 0)).sum())
    fn = int(((y_pred == 0) & (y_true == 1)).sum())
    return {
        "threshold": threshold,
        "false_positives": fp,
        "false_negatives": fn,
        "estimated_cost": fp * fp_cost + fn * fn_cost,
    }

