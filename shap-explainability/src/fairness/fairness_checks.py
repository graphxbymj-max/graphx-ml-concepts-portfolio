"""Simple fairness-style diagnostics for explainability discussions."""
from __future__ import annotations
import pandas as pd


def subgroup_prediction_summary(df: pd.DataFrame, subgroup_col: str, outcome_col: str = 'actual', pred_col: str = 'predicted') -> pd.DataFrame:
    """Summarize prediction rates and error rates by subgroup-like feature."""
    return df.groupby(subgroup_col).agg(
        rows=(outcome_col, 'size'),
        actual_positive_rate=(outcome_col, 'mean'),
        predicted_positive_rate=(pred_col, 'mean'),
        error_rate=('is_error', 'mean'),
    ).reset_index()
