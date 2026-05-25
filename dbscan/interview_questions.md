# DBSCAN Interview Questions

## Conceptual Questions

### 1. What is DBSCAN?

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise.

It groups points that are close together in dense regions and labels isolated points as noise.

### 2. What is density-based clustering?

Density-based clustering finds clusters by looking for crowded regions of data.

Instead of assuming clusters are round, it asks where points are packed closely together.

### 3. What are core points?

Core points have at least `min_samples` points within their `eps` neighborhood.

They are the dense centers that allow clusters to grow.

### 4. What are border points?

Border points are close to a core point but do not have enough neighbors to be core points themselves.

They belong to a cluster because they are connected to density.

### 5. What are noise points?

Noise points are not close enough to dense regions.

DBSCAN labels them as `-1`. They can be interpreted as outliers or anomalies.

### 6. What is eps?

`eps` is the neighborhood radius.

It controls how far a point looks to find neighbors.

### 7. What is min_samples?

`min_samples` is the number of nearby points required to form a dense region.

Higher values require stronger density before a cluster forms.

### 8. Why does DBSCAN handle irregular clusters well?

DBSCAN grows clusters through density connectivity.

Because clusters expand from connected dense neighborhoods, they can follow curved or irregular shapes.

### 9. Why does DBSCAN detect outliers naturally?

Points that do not belong to any dense region are labeled as noise.

This makes DBSCAN useful for anomaly detection.

### 10. Difference between DBSCAN and KMeans?

KMeans requires choosing K and assigns every point to a cluster.

DBSCAN does not require K, can find irregular shapes, and can label points as noise.

## Practical Questions

### 1. How do you choose eps?

Use domain knowledge, visual inspection, and a k-distance graph.

The k-distance graph helps identify a bend where neighbor distances start increasing sharply.

### 2. What happens if eps is too small?

Too many points become noise because neighborhoods are too strict.

Clusters may fragment into tiny pieces.

### 3. What happens if eps is too large?

Separate clusters may merge together.

The model may treat most of the data as one large cluster.

### 4. Why does scaling matter?

DBSCAN uses distance.

If features are on different scales, one feature can dominate the neighborhood calculation.

### 5. What is the k-distance graph?

The k-distance graph plots each point's distance to its kth nearest neighbor.

It helps choose eps by looking for a bend in the sorted distances.

### 6. Can DBSCAN handle high-dimensional data?

DBSCAN can struggle in high dimensions because distances become less meaningful.

Dimensionality reduction or careful feature selection may be needed.

### 7. How does DBSCAN handle noise?

DBSCAN assigns noise points the label `-1`.

These points are not forced into clusters.

### 8. When should you use DBSCAN instead of KMeans?

Use DBSCAN when clusters are irregular, noise matters, outlier detection is important, or you do not want to choose K upfront.

Use KMeans when clusters are compact, roughly spherical, and scalability is the priority.

### 9. What are the limitations of DBSCAN?

DBSCAN is sensitive to eps and min_samples.

It struggles with varying densities, high-dimensional data, and very large datasets without optimized implementations.

### 10. Why is DBSCAN useful for anomaly detection?

Because it explicitly labels isolated points as noise.

Those points can represent rare or suspicious behavior.

## Business Questions

### 1. Why is outlier detection important?

Outliers can reveal fraud, system failures, rare customer behavior, network intrusions, or data quality issues.

Ignoring them can hide important risks.

### 2. How would you explain DBSCAN to a stakeholder?

I would say:

> DBSCAN finds crowded communities in the data and leaves isolated unusual points aside for investigation.

### 3. Why are density-based methods useful in real-world data?

Real-world data often forms irregular shapes and contains noise.

Density-based methods can discover those shapes without forcing every point into a neat cluster.

### 4. Why can forcing clusters be dangerous?

Forcing clusters can hide anomalies by assigning unusual points to normal groups.

In fraud, cybersecurity, and risk detection, those unusual points may be the most important cases.

