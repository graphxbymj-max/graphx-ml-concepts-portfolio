from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def underfit_tree(random_state: int = 42) -> DecisionTreeClassifier:
    """A deliberately constrained tree that usually underfits."""
    return DecisionTreeClassifier(max_depth=1, random_state=random_state)


def balanced_tree(random_state: int = 42) -> DecisionTreeClassifier:
    """A modest tree that balances flexibility and control."""
    return DecisionTreeClassifier(max_depth=4, min_samples_leaf=8, random_state=random_state)


def overfit_tree(random_state: int = 42) -> DecisionTreeClassifier:
    """A highly flexible tree that can memorize training examples."""
    return DecisionTreeClassifier(max_depth=None, min_samples_leaf=1, random_state=random_state)


def regularized_logistic(C: float = 1.0, penalty: str = "l2", random_state: int = 42) -> Pipeline:
    """Scaled logistic regression with configurable regularization strength."""
    solver = "liblinear" if penalty == "l1" else "lbfgs"
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "model",
                LogisticRegression(
                    C=C,
                    penalty=penalty,
                    solver=solver,
                    max_iter=5000,
                    random_state=random_state,
                ),
            ),
        ]
    )

