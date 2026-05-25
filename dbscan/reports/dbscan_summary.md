# DBSCAN Project Summary

## Executive Summary

This project demonstrates how DBSCAN discovers dense communities and isolates noise in messy data. Using a noisy customer activity map with irregular moon-shaped communities and rare activity points, it compares DBSCAN with KMeans and shows why density-based clustering is useful when clusters are not round.

The central lesson:

> DBSCAN does not force every point into a group. It lets dense regions become clusters and leaves isolated points as noise.

## Dataset

Dataset: Noisy Customer Activity Map

Rows: 545

Features:

- `customer_event_id`
- `x_activity`
- `y_activity`
- `activity_intensity`
- `source`
- `reference_pattern`

The main clustering features are `x_activity` and `y_activity`.

## DBSCAN Experiments

The notebook performs:

- exploratory data analysis
- density visualization
- feature scaling comparison
- DBSCAN clustering
- core/border/noise explanation
- k-distance graph
- eps/min_samples parameter sweep
- final DBSCAN model
- noise profile analysis
- KMeans comparison
- silhouette evaluation
- PCA visualization

## Parameter Tuning Findings

DBSCAN is sensitive to `eps` and `min_samples`.

Small eps values create too much noise because neighborhoods are too strict.

Large eps values can merge separate communities.

The k-distance graph helps identify a reasonable eps value by looking for a bend in nearest-neighbor distances.

## Outlier Detection Insights

DBSCAN labels isolated points as noise.

In practical workflows, these points can be investigated as anomalies:

- suspicious transactions
- rare customer behavior
- network intrusions
- unusual geospatial movement
- healthcare anomalies

## KMeans Comparison

KMeans struggles with the irregular moon-shaped activity communities because it prefers round-ish partitions and forces every point into a cluster.

DBSCAN follows the curved density regions and leaves isolated points unassigned.

## Business Insights

DBSCAN is useful when the business needs to identify natural communities and unusual behavior.

Examples include:

- finding dense customer activity zones
- detecting rare or suspicious behavior
- identifying geographic hotspots
- filtering noisy events before downstream modeling

## Limitations

DBSCAN has limitations:

- sensitive to eps
- sensitive to min_samples
- struggles with varying density
- less effective in high dimensions
- can be computationally expensive on very large datasets

## Practical Lessons

- Scale features before using DBSCAN.
- Use k-distance plots to guide eps selection.
- Evaluate noise rate as part of model behavior.
- Compare DBSCAN against KMeans when shapes are irregular.
- Treat noise as useful signal, not automatic trash.
- Combine visual inspection, metrics, and business context.

## Final Takeaway

DBSCAN is valuable because it respects messy data.

It discovers dense communities naturally and refuses to force isolated points where they do not belong.

