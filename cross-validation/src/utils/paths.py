from pathlib import Path


def project_root() -> Path:
    """Return the Cross Validation project root."""
    return Path(__file__).resolve().parents[2]


def image_path(filename: str) -> Path:
    """Return a path inside the images folder."""
    return project_root() / "images" / filename

