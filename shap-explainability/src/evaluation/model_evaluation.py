"""Evaluation helpers for classification models."""
from __future__ import annotations
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, precision_score, recall_score, confusion_matrix


def evaluate_classifier(model, X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """Return train/test classification metrics."""
    rows = []
    for split, X, y in [('train', X_train, y_train), ('test', X_test, y_test)]:
        pred = model.predict(X)
        proba = model.predict_proba(X)[:, 1]
        rows.append({
            'split': split,
            'accuracy': accuracy_score(y, pred),
            'precision': precision_score(y, pred),
            'recall': recall_score(y, pred),
            'f1': f1_score(y, pred),
            'roc_auc': roc_auc_score(y, proba),
        })
    return pd.DataFrame(rows)


def misclassification_frame(model, X_test, y_test) -> pd.DataFrame:
    """Return test rows with prediction diagnostics."""
    out = X_test.copy()
    out['actual'] = y_test.values
    out['predicted'] = model.predict(X_test)
    out['probability_malignant'] = model.predict_proba(X_test)[:, 1]
    out['is_error'] = out['actual'] != out['predicted']
    return out
