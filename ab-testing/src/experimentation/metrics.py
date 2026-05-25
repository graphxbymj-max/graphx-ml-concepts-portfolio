"""Experiment metric helpers."""
from __future__ import annotations

import pandas as pd


def conversion_summary(df: pd.DataFrame, group_col: str = 'group', outcome_col: str = 'converted') -> pd.DataFrame:
    """Return users, conversions, conversion rate, revenue, and ARPU by experiment group."""
    summary = (
        df.groupby(group_col)
        .agg(
            users=(outcome_col, 'size'),
            conversions=(outcome_col, 'sum'),
            conversion_rate=(outcome_col, 'mean'),
            total_revenue=('revenue', 'sum'),
            avg_revenue_per_user=('revenue', 'mean'),
            avg_order_value=('revenue', lambda s: s[s > 0].mean()),
        )
        .reset_index()
    )
    return summary


def calculate_lift(control_rate: float, treatment_rate: float) -> dict[str, float]:
    """Calculate absolute and relative lift between treatment and control."""
    absolute_lift = treatment_rate - control_rate
    relative_lift = absolute_lift / control_rate if control_rate else float('nan')
    return {'absolute_lift': absolute_lift, 'relative_lift': relative_lift}


def business_impact(control_rate: float, treatment_rate: float, monthly_users: int, avg_order_value: float) -> dict[str, float]:
    """Estimate incremental conversions and revenue from rolling out treatment."""
    absolute_lift = treatment_rate - control_rate
    incremental_conversions = absolute_lift * monthly_users
    incremental_revenue = incremental_conversions * avg_order_value
    return {
        'monthly_users': monthly_users,
        'absolute_lift': absolute_lift,
        'incremental_conversions': incremental_conversions,
        'incremental_revenue': incremental_revenue,
    }
