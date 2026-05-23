"""XGBoost model helpers."""

import pandas as pd
from xgboost import XGBClassifier


def train_xgboost(X_train, y_train, random_state=42, **kwargs):
    """Train an XGBClassifier with practical defaults."""
    params = {
        "n_estimators": 300,
        "learning_rate": 0.05,
        "max_depth": 3,
        "subsample": 0.9,
        "colsample_bytree": 0.9,
        "eval_metric": "logloss",
        "random_state": random_state,
        "n_jobs": 1,
    }
    params.update(kwargs)
    model = XGBClassifier(**params)
    model.fit(X_train, y_train)
    return model


def get_xgboost_importance(model, feature_names, importance_type="gain"):
    """Return XGBoost feature importance as a DataFrame."""
    booster = model.get_booster()
    score = booster.get_score(importance_type=importance_type)
    rows = [{"feature": feature, "importance": score.get(feature, 0)} for feature in feature_names]
    return pd.DataFrame(rows).sort_values("importance", ascending=False)
