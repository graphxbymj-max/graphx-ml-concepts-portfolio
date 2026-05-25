from sklearn.metrics import classification_report


def text_classification_report(y_true, y_pred) -> str:
    """Return a text classification report with stable zero-division behavior."""
    return classification_report(y_true, y_pred, zero_division=0)

