import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import cross_val_score


def evaluate_classifier(model, X_train, X_test, y_train, y_test, label: str) -> dict:
    """Evaluate a classifier on train and test data."""
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        test_score = model.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test, test_score)
    else:
        roc_auc = None

    return {
        "model": label,
        "train_accuracy": accuracy_score(y_train, train_pred),
        "test_accuracy": accuracy_score(y_test, test_pred),
        "generalization_gap": accuracy_score(y_train, train_pred) - accuracy_score(y_test, test_pred),
        "precision": precision_score(y_test, test_pred),
        "recall": recall_score(y_test, test_pred),
        "f1": f1_score(y_test, test_pred),
        "roc_auc": roc_auc,
    }


def evaluate_many(models: dict, X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """Fit and evaluate multiple models."""
    rows = []
    for label, model in models.items():
        model.fit(X_train, y_train)
        rows.append(evaluate_classifier(model, X_train, X_test, y_train, y_test, label))
    return pd.DataFrame(rows)


def cross_validation_table(models: dict, X, y, cv: int = 5, scoring: str = "accuracy") -> pd.DataFrame:
    """Return mean and standard deviation from cross-validation."""
    rows = []
    for label, model in models.items():
        scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
        rows.append(
            {
                "model": label,
                "cv_mean": scores.mean(),
                "cv_std": scores.std(),
                "scores": scores,
            }
        )
    return pd.DataFrame(rows)

