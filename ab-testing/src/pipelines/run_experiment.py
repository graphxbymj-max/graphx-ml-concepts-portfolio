"""Small end-to-end pipeline for the A/B testing project."""
from __future__ import annotations

from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from preprocessing.data_preprocessing import save_datasets


def run_pipeline(raw_path: str | Path, processed_path: str | Path):
    """Generate the reproducible checkout A/B testing dataset."""
    return save_datasets(raw_path, processed_path)
