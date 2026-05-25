from pathlib import Path


def project_root() -> Path:
    """Return the project root from anywhere inside this project."""
    return Path(__file__).resolve().parents[2]


def image_path(filename: str) -> Path:
    """Return an image output path."""
    return project_root() / "images" / filename

