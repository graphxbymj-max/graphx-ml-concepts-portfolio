from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = ["age", "annual_income", "spending_score"]
SEGMENT_FEATURES = ["annual_income", "spending_score"]


def load_mall_customers(path: str | Path) -> pd.DataFrame:
    """Load and normalize the Mall Customers dataset."""
    df = pd.read_csv(path)
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("-", "_", regex=False)
    )
    df["customer_id"] = df["customer_id"].astype(str).str.zfill(4)
    return df


def save_processed(raw_path: str | Path, processed_path: str | Path) -> pd.DataFrame:
    """Save a clean processed copy of the dataset."""
    df = load_mall_customers(raw_path)
    processed_path = Path(processed_path)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_path, index=False)
    return df


def scale_features(df: pd.DataFrame, features=None):
    """Scale selected numeric features for distance-based clustering."""
    features = features or FEATURE_COLUMNS
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[features])
    scaled_df = pd.DataFrame(scaled, columns=features, index=df.index)
    return scaled_df, scaler

