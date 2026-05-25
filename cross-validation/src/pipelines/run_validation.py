from src.experiments.model_experiments import decision_tree_model, logistic_model, random_forest_model
from src.preprocessing.data_preprocessing import split_features_target
from src.validation.cross_validation import fold_scores, stratified_kfold


def run_core_validation(df):
    """Run a compact StratifiedKFold comparison for the main models."""
    X, y = split_features_target(df)
    cv = stratified_kfold()
    models = {
        "Logistic Regression": logistic_model(X),
        "Decision Tree": decision_tree_model(X, max_depth=4, min_samples_leaf=25),
        "Random Forest": random_forest_model(X, max_depth=8, min_samples_leaf=10),
    }
    return [fold_scores(model, X, y, cv, label=name) for name, model in models.items()]

