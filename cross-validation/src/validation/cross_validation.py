import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score, train_test_split


def repeated_train_test_scores(model, X, y, random_states=range(20), test_size: float = 0.25):
    """Run many train/test splits to show single-split instability."""
    rows = []
    for seed in random_states:
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=seed,
            stratify=y,
        )
        fitted = clone(model)
        fitted.fit(X_train, y_train)
        train_accuracy = accuracy_score(y_train, fitted.predict(X_train))
        test_accuracy = accuracy_score(y_test, fitted.predict(X_test))
        rows.append(
            {
                "random_state": seed,
                "train_accuracy": train_accuracy,
                "test_accuracy": test_accuracy,
                "generalization_gap": train_accuracy - test_accuracy,
            }
        )
    return pd.DataFrame(rows)


def fold_scores(model, X, y, cv, scoring: str = "accuracy", label: str = "model"):
    """Return fold-level scores for a supplied CV splitter."""
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    return pd.DataFrame(
        {
            "model": label,
            "fold": np.arange(1, len(scores) + 1),
            "score": scores,
        }
    )


def kfold(n_splits: int = 5, shuffle: bool = True, random_state: int = 42):
    """Create a KFold splitter."""
    return KFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)


def stratified_kfold(n_splits: int = 5, shuffle: bool = True, random_state: int = 42):
    """Create a StratifiedKFold splitter."""
    return StratifiedKFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)


def fold_class_balance(y, cv, label: str):
    """Measure target rate in each validation fold."""
    rows = []
    dummy_X = np.zeros(len(y))
    for fold, (_, valid_idx) in enumerate(cv.split(dummy_X, y), start=1):
        y_valid = y.iloc[valid_idx] if hasattr(y, "iloc") else y[valid_idx]
        rows.append(
            {
                "method": label,
                "fold": fold,
                "validation_churn_rate": float(np.mean(y_valid)),
                "validation_size": len(valid_idx),
            }
        )
    return pd.DataFrame(rows)

