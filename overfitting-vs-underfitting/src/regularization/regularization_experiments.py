from src.experiments.complexity import regularization_curve
from src.models.model_factory import regularized_logistic


def logistic_regularization_experiment(X_train, X_test, y_train, y_test, c_values):
    """Evaluate logistic regression across different C values."""
    return regularization_curve(
        lambda c: regularized_logistic(C=c),
        X_train,
        X_test,
        y_train,
        y_test,
        values=c_values,
    )

