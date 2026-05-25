from sklearn.model_selection import train_test_split

from src.experiments.model_experiments import logistic_model
from src.metrics.classification_metrics import metrics_at_threshold
from src.preprocessing.data_preprocessing import split_features_target


def run_default_evaluation(df):
    """Train the default model and return metrics at threshold 0.5."""
    X, y = split_features_target(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
    model = logistic_model(X)
    model.fit(X_train, y_train)
    y_proba = model.predict_proba(X_test)[:, 1]
    return metrics_at_threshold(y_test, y_proba, 0.5)

