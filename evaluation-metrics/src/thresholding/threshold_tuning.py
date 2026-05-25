import pandas as pd

from src.metrics.classification_metrics import business_cost, threshold_table


def tune_thresholds(y_true, y_proba, thresholds, fp_cost: float = 25, fn_cost: float = 200):
    """Combine metric and business-cost views across thresholds."""
    metrics_df = threshold_table(y_true, y_proba, thresholds)
    cost_df = pd.DataFrame([business_cost(y_true, y_proba, t, fp_cost, fn_cost) for t in thresholds])
    return metrics_df.merge(cost_df, on="threshold")

