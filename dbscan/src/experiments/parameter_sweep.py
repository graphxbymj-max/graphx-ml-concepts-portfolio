from src.evaluation.cluster_metrics import evaluate_dbscan_grid


def run_parameter_sweep(X):
    """Run a compact DBSCAN parameter sweep."""
    eps_values = [0.12, 0.16, 0.20, 0.24, 0.28, 0.34, 0.42]
    min_samples_values = [4, 6, 10]
    return evaluate_dbscan_grid(X, eps_values, min_samples_values)

