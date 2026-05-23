"""
Model training utilities for the GraphX Labs Decision Trees project.
"""

import pandas as pd
from sklearn.model_selection import train_test_split as sklearn_train_test_split
from sklearn.tree import DecisionTreeClassifier


def train_test_split(X, y, test_size=0.2, random_state=42, stratify=True):
    """Create a reproducible train-test split."""
    stratify_values = y if stratify else None
    return sklearn_train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_values
    )


def train_decision_tree(X_train, y_train, criterion="gini", random_state=42, **kwargs):
    """Train a Decision Tree classifier."""
    model = DecisionTreeClassifier(
        criterion=criterion,
        random_state=random_state,
        **kwargs
    )
    model.fit(X_train, y_train)
    return model


def train_shallow_tree(X_train, y_train, max_depth=3, random_state=42, **kwargs):
    """Train a shallow Decision Tree for interpretation and overfitting control."""
    return train_decision_tree(
        X_train,
        y_train,
        max_depth=max_depth,
        random_state=random_state,
        **kwargs
    )


def generate_predictions(model, X):
    """Generate class predictions."""
    return model.predict(X)


def generate_prediction_probabilities(model, X):
    """Generate positive-class probabilities when available."""
    return model.predict_proba(X)[:, 1]


def get_feature_importance(model, feature_names):
    """Return Decision Tree feature importances as a sorted DataFrame."""
    importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": model.feature_importances_
    })
    return importance_df.sort_values("importance", ascending=False)
