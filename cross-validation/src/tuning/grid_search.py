from sklearn.model_selection import GridSearchCV


def tune_decision_tree(model, X, y, cv, scoring: str = "accuracy"):
    """Tune a Decision Tree pipeline with cross-validation."""
    param_grid = {
        "model__max_depth": [2, 3, 4, 5, 6, 8, None],
        "model__min_samples_leaf": [1, 5, 10, 25, 50],
    }
    search = GridSearchCV(
        model,
        param_grid=param_grid,
        cv=cv,
        scoring=scoring,
        return_train_score=True,
        n_jobs=-1,
    )
    search.fit(X, y)
    return search

