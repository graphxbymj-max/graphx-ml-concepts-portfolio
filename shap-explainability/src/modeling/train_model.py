"""Model training helpers for SHAP explainability."""
from __future__ import annotations
from xgboost import XGBClassifier


def train_xgboost_classifier(X_train, y_train, random_state: int = 42) -> XGBClassifier:
    """Train a compact XGBoost model that remains strong but explainable with SHAP."""
    model = XGBClassifier(
        n_estimators=160,
        max_depth=3,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric='logloss',
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    return model
