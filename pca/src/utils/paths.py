from pathlib import Path


def project_root() -> Path:
    """Return project root."""
    return Path(__file__).resolve().parents[2]


def image_path(filename: str) -> Path:
    """Return image output path."""
    return project_root() / "images" / filename

