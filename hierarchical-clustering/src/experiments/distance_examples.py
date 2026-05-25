import numpy as np


def euclidean_distance(a, b) -> float:
    """Calculate Euclidean distance between two vectors."""
    return float(np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2)))


def manhattan_distance(a, b) -> float:
    """Calculate Manhattan distance between two vectors."""
    return float(np.sum(np.abs(np.array(a) - np.array(b))))

