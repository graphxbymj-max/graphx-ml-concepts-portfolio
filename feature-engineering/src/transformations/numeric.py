"""Numerical transformation helpers."""

import numpy as np


def log_transform(series):
    """Apply log1p after clipping negative values to zero."""
    return np.log1p(series.clip(lower=0))


def cap_outliers_iqr(series, factor=1.5):
    """Cap outliers using the IQR rule."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - factor * iqr
    upper = q3 + factor * iqr
    return series.clip(lower, upper)
