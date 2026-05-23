"""Hyperparameter tuning helpers."""

from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier


def tune_xgboost(X_train, y_train, param_grid, scoring="roc_auc", cv=3, random_state=42):
    model = XGBClassifier(eval_metric="logloss", random_state=random_state, n_jobs=1)
    search = GridSearchCV(model, param_grid=param_grid, scoring=scoring, cv=cv, n_jobs=1)
    search.fit(X_train, y_train)
    return search
