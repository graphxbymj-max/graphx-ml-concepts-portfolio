import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def evaluate_classifier(model, X_train, X_test, y_train, y_test, label: str) -> dict:
    """Fit and evaluate a classifier on train and test data."""
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    test_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    return {
        "model": label,
        "train_accuracy": accuracy_score(y_train, train_pred),
        "test_accuracy": accuracy_score(y_test, test_pred),
        "generalization_gap": accuracy_score(y_train, train_pred) - accuracy_score(y_test, test_pred),
        "precision": precision_score(y_test, test_pred),
        "recall": recall_score(y_test, test_pred),
        "f1": f1_score(y_test, test_pred),
        "roc_auc": roc_auc_score(y_test, test_proba) if test_proba is not None else None,
    }


def summarize_scores(scores, label: str) -> dict:
    """Summarize cross-validation scores."""
    return {
        "model": label,
        "mean_score": scores.mean(),
        "std_score": scores.std(),
        "min_score": scores.min(),
        "max_score": scores.max(),
        "range": scores.max() - scores.min(),
    }


def comparison_frame(rows) -> pd.DataFrame:
    """Return a rounded comparison dataframe."""
    return pd.DataFrame(rows).sort_values("mean_score", ascending=False)

