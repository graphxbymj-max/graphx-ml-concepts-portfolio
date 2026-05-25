# KMeans Clustering Interview Questions

## Conceptual Questions

### 1. What is clustering?

Clustering is an unsupervised learning technique that groups similar data points together.

The goal is to discover structure in data without predefined labels.

### 2. What is unsupervised learning?

Unsupervised learning is machine learning without target labels.

The model is not told the correct answer. It tries to find patterns, groups, or structure from the features alone.

### 3. What is KMeans?

KMeans is a clustering algorithm that partitions data into `K` clusters by assigning points to the nearest centroid and repeatedly updating those centroids.

### 4. What is a centroid?

A centroid is the center of a cluster.

In KMeans, each point is assigned to the nearest centroid, and each centroid moves to the average position of the points assigned to it.

### 5. How does KMeans work?

KMeans works in five steps:

1. Choose K.
2. Initialize K centroids.
3. Assign each point to the nearest centroid.
4. Move each centroid to the center of its assigned points.
5. Repeat until assignments stabilize.

### 6. Why does KMeans use distance?

KMeans uses distance to measure similarity.

Points closer together are treated as more similar. This is why feature scaling is so important.

### 7. What is inertia?

Inertia is the sum of squared distances between points and their assigned cluster centroid.

Lower inertia means points are closer to their centroids, but inertia always decreases as K increases.

### 8. What is the elbow method?

The elbow method plots inertia for different K values.

The goal is to find the point where adding more clusters stops reducing inertia dramatically.

### 9. What is silhouette score?

Silhouette score measures how well a point fits inside its cluster compared with other clusters.

It combines cohesion and separation. Higher values usually mean better-defined clusters.

### 10. Why does scaling matter in KMeans?

KMeans is distance-based.

If one feature has a much larger scale than another, it can dominate distance calculations and distort the clusters.

## Practical Questions

### 1. How do you choose K?

Use a combination of:

- elbow method
- silhouette score
- business interpretability
- visual inspection
- domain knowledge

### 2. Why is KMeans sensitive to initialization?

KMeans starts with initial centroids.

Different starting positions can lead to different final clusters, especially when clusters overlap. Using `k-means++`, multiple initializations, and a fixed random state helps.

### 3. What happens if K is too small?

If K is too small, different groups get forced together.

The clustering oversimplifies the data and may hide meaningful segments.

### 4. What happens if K is too large?

If K is too large, natural groups may be split into tiny segments.

This can make the result harder to interpret and less useful for business action.

### 5. How do you interpret clusters?

Profile each cluster by calculating feature averages, sizes, and distributions.

Then translate those patterns into business-friendly segment names.

### 6. Can KMeans handle categorical variables?

Not directly.

KMeans relies on numeric distance. Categorical variables need encoding, and even then, KMeans may not be the best choice for mixed data.

### 7. Why is PCA used with clustering?

PCA reduces high-dimensional data into fewer dimensions for visualization.

It helps us see cluster structure on a two-dimensional plot.

### 8. What are the limitations of KMeans?

KMeans limitations include:

- requires choosing K
- sensitive to scaling
- sensitive to outliers
- assumes compact, roughly spherical clusters
- can be sensitive to initialization
- struggles with categorical features

### 9. How do outliers affect KMeans?

Outliers can pull centroids away from the true center of a cluster.

Because centroids are averages, extreme values can distort cluster placement.

### 10. Difference between clustering and classification?

Classification uses labeled data to predict predefined classes.

Clustering uses unlabeled data to discover groups.

## Business Questions

### 1. Why is customer segmentation important?

Customer segmentation helps businesses personalize marketing, offers, product strategy, and customer experience.

It turns one broad audience into more meaningful groups.

### 2. How would you explain clustering to a stakeholder?

I would say:

> Clustering groups customers with similar behavior so we can understand different types of customers without manually labeling them first.

### 3. Why is unsupervised learning difficult?

There is no answer key.

Without labels, evaluation is less direct, and cluster interpretation requires domain knowledge.

### 4. Why are clusters sometimes subjective?

Clusters are patterns, not absolute truth.

Different feature choices, scaling choices, algorithms, and K values can produce different segmentations. Human interpretation is part of the workflow.

