from src.evaluation.metrics import evaluate_many
from src.models.model_factory import balanced_tree, overfit_tree, regularized_logistic, underfit_tree
from src.preprocessing.data_preprocessing import make_train_test_split


def run_core_experiment(df):
    """Run the core underfit/balanced/overfit comparison."""
    X_train, X_test, y_train, y_test = make_train_test_split(df)
    models = {
        "Underfit Tree": underfit_tree(),
        "Balanced Tree": balanced_tree(),
        "Overfit Tree": overfit_tree(),
        "Regularized Logistic": regularized_logistic(C=0.5),
    }
    return evaluate_many(models, X_train, X_test, y_train, y_test)

