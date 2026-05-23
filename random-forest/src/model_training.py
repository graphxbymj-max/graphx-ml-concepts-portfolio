"""Model training helpers for Decision Tree and Random Forest models."""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def train_decision_tree(X_train, y_train, random_state=42, **kwargs):
    """Train a single Decision Tree classifier."""
    model = DecisionTreeClassifier(random_state=random_state, **kwargs)
    model.fit(X_train, y_train)
    return model


def train_random_forest(
    X_train,
    y_train,
    n_estimators=300,
    max_depth=None,
    random_state=42,
    n_jobs=1,
    **kwargs
):
    """Train a Random Forest classifier."""
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=n_jobs,
        **kwargs
    )
    model.fit(X_train, y_train)
    return model


def generate_predictions(model, X):
    """Generate class predictions."""
    return model.predict(X)


def generate_prediction_probabilities(model, X):
    """Generate positive-class probabilities."""
    return model.predict_proba(X)[:, 1]


def tune_random_forest(X_train, y_train, param_grid, scoring="roc_auc", cv=5, random_state=42):
    """Tune a Random Forest with GridSearchCV."""
    search = GridSearchCV(
        RandomForestClassifier(random_state=random_state, n_jobs=1),
        param_grid=param_grid,
        scoring=scoring,
        cv=cv,
        n_jobs=1,
    )
    search.fit(X_train, y_train)
    return search


def get_feature_importance(model, feature_names):
    """Return sorted feature importances."""
    return pd.DataFrame({
        "feature": feature_names,
        "importance": model.feature_importances_,
    }).sort_values("importance", ascending=False)
