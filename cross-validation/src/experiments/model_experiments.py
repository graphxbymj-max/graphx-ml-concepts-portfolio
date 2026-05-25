from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from src.preprocessing.data_preprocessing import build_preprocessor


def logistic_model(X):
    """Logistic Regression pipeline."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(X)),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]
    )


def decision_tree_model(X, max_depth=None, min_samples_leaf=1):
    """Decision Tree pipeline."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(X)),
            (
                "model",
                DecisionTreeClassifier(
                    max_depth=max_depth,
                    min_samples_leaf=min_samples_leaf,
                    random_state=42,
                    class_weight="balanced",
                ),
            ),
        ]
    )


def random_forest_model(X, n_estimators=200, max_depth=None, min_samples_leaf=1):
    """Random Forest pipeline."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(X)),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_leaf=min_samples_leaf,
                    random_state=42,
                    class_weight="balanced",
                    n_jobs=-1,
                ),
            ),
        ]
    )

