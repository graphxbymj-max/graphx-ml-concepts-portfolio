import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


def decision_tree_complexity_curve(X_train, X_test, y_train, y_test, depths=range(1, 16)):
    """Measure train and test accuracy as tree depth increases."""
    rows = []
    for depth in depths:
        model = DecisionTreeClassifier(max_depth=depth, random_state=42)
        model.fit(X_train, y_train)
        rows.append(
            {
                "max_depth": depth,
                "train_accuracy": accuracy_score(y_train, model.predict(X_train)),
                "test_accuracy": accuracy_score(y_test, model.predict(X_test)),
            }
        )
    return pd.DataFrame(rows)


def regularization_curve(model_factory, X_train, X_test, y_train, y_test, values):
    """Measure performance while changing a regularization parameter."""
    rows = []
    for value in values:
        model = model_factory(value)
        model.fit(X_train, y_train)
        rows.append(
            {
                "regularization_value": value,
                "train_accuracy": accuracy_score(y_train, model.predict(X_train)),
                "test_accuracy": accuracy_score(y_test, model.predict(X_test)),
            }
        )
    return pd.DataFrame(rows)

