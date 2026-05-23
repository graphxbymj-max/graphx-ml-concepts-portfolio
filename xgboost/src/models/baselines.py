"""Baseline model training helpers."""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def train_logistic_regression(X_train, y_train, random_state=42):
    model = LogisticRegression(max_iter=1000, random_state=random_state)
    model.fit(X_train, y_train)
    return model


def train_decision_tree(X_train, y_train, random_state=42, **kwargs):
    model = DecisionTreeClassifier(random_state=random_state, **kwargs)
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train, random_state=42, n_jobs=1, **kwargs):
    model = RandomForestClassifier(random_state=random_state, n_jobs=n_jobs, **kwargs)
    model.fit(X_train, y_train)
    return model
