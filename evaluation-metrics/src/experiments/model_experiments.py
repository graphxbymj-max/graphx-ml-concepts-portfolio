from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from src.preprocessing.data_preprocessing import build_preprocessor


def logistic_model(X):
    """Logistic Regression pipeline for probability-based evaluation."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(X)),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]
    )


def random_forest_model(X):
    """Random Forest pipeline for metric comparison."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor(X)),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=220,
                    max_depth=8,
                    min_samples_leaf=8,
                    random_state=42,
                    class_weight="balanced",
                    n_jobs=-1,
                ),
            ),
        ]
    )

