import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def compare_model_with_without_pca(X, y, n_components: int = 6, random_state: int = 42):
    """Compare Logistic Regression before and after PCA."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=random_state)
    models = {
        "Original features": Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression(max_iter=3000))]),
        f"PCA {n_components} components": Pipeline(
            [("scaler", StandardScaler()), ("pca", PCA(n_components=n_components)), ("model", LogisticRegression(max_iter=3000))]
        ),
    }
    rows = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        proba = model.predict_proba(X_test)[:, 1]
        rows.append(
            {
                "model": name,
                "features_used": X.shape[1] if name == "Original features" else n_components,
                "accuracy": accuracy_score(y_test, pred),
                "f1": f1_score(y_test, pred),
                "roc_auc": roc_auc_score(y_test, proba),
            }
        )
    return pd.DataFrame(rows)

