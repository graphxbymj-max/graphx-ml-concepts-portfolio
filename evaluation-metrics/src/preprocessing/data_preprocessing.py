from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


TARGET_COLUMN = "churn"


def load_telco_dataset(path: str | Path) -> pd.DataFrame:
    """Load and normalize Telco churn data."""
    df = pd.read_csv(path)
    df.columns = (
        df.columns.str.strip()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
        .str.lower()
    )
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")
    df[TARGET_COLUMN] = df["churn"].map({"No": 0, "Yes": 1}).astype(int)
    return df.drop(columns=["customerid"])


def save_processed(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save a processed copy for reproducible notebooks."""
    df = load_telco_dataset(raw_path)
    processed_path = Path(processed_path)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_path, index=False)
    return df


def split_features_target(df: pd.DataFrame, target: str = TARGET_COLUMN):
    """Split dataframe into features and target."""
    return df.drop(columns=[target]), df[target]


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing for mixed numeric and categorical data."""
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )

