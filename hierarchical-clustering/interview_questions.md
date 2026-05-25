# Hierarchical Clustering Interview Questions

## Conceptual Questions

### 1. What is Hierarchical Clustering?

Hierarchical Clustering is an unsupervised learning method that builds nested groups of similar data points.

Instead of producing only one flat set of clusters, it creates a hierarchy that shows how clusters merge or split.

### 2. What is Agglomerative Clustering?

Agglomerative Clustering is the bottom-up version of Hierarchical Clustering.

Every point starts as its own cluster. The closest clusters merge step by step until one large hierarchy is formed.

### 3. What is a dendrogram?

A dendrogram is a tree diagram that shows how clusters merge.

The vertical height of a merge represents the distance between the groups being merged.

### 4. How does Hierarchical Clustering work?

It calculates distances between points or clusters, merges the closest groups, updates distances, and repeats.

The process creates a tree of relationships.

### 5. What are linkage methods?

Linkage methods define how distance between two clusters is calculated.

They control which clusters merge at each step.

### 6. Difference between single, complete, average, and Ward linkage?

Single linkage uses the closest pair between clusters.

Complete linkage uses the farthest pair.

Average linkage uses average pairwise distance.

Ward linkage merges clusters in a way that minimizes within-cluster variance.

### 7. Why is scaling important?

Hierarchical Clustering is distance-based.

If features are on different scales, larger-scale features can dominate the distance calculation.

### 8. What is cluster hierarchy?

Cluster hierarchy is the nested structure of groups.

Small clusters merge into larger clusters, creating multiple levels of grouping.

### 9. Difference between KMeans and Hierarchical Clustering?

KMeans is centroid-based and requires choosing K upfront.

Hierarchical Clustering builds a relationship tree and can be cut at different levels to produce different numbers of clusters.

### 10. Why is Hierarchical Clustering interpretable?

It produces a dendrogram that shows how groups form.

This makes it easier to explain relationships between data points and clusters.

## Practical Questions

### 1. How do you choose the number of clusters?

You can cut the dendrogram at a meaningful height, inspect large merge-distance jumps, use silhouette scores, and apply business judgment.

### 2. How do you cut a dendrogram?

Draw a horizontal line across the dendrogram.

The number of branches crossed by the line gives the number of clusters.

### 3. What distance metrics can be used?

Common distance metrics include Euclidean, Manhattan, cosine distance, and correlation distance.

Ward linkage specifically requires Euclidean distance.

### 4. Why is Hierarchical Clustering expensive?

It often requires calculating and storing many pairwise distances.

This can become expensive as the dataset grows.

### 5. Can it handle large datasets?

It can struggle with very large datasets.

For large-scale clustering, KMeans or approximate methods are often more practical.

### 6. How do outliers affect clustering?

Outliers can create strange merges or isolated branches.

They can distort the hierarchy, especially with certain linkage methods.

### 7. Why are merges irreversible?

Agglomerative clustering commits to each merge.

Once two clusters merge, the algorithm does not later split them apart.

### 8. When should you use Hierarchical Clustering over KMeans?

Use Hierarchical Clustering when interpretability, nested relationships, and dendrogram visualization matter.

Use KMeans when speed and scalability matter more.

### 9. How does linkage affect results?

Linkage changes how clusters measure distance to one another.

Different linkage methods can produce different hierarchies and cluster shapes.

### 10. How do you interpret dendrograms?

Look at merge heights, large vertical gaps, and where a horizontal cut creates meaningful groups.

Long vertical jumps often suggest strong separation.

## Business Questions

### 1. Why is segmentation important?

Segmentation helps businesses tailor marketing, products, offers, and customer experiences to different behavior groups.

### 2. How would you explain hierarchical clustering to a stakeholder?

I would say:

> It builds a family tree of customers based on behavior, showing which customers are most similar and how small groups combine into larger segments.

### 3. Why are nested relationships useful?

Nested relationships let teams analyze customers at different levels of detail.

You can inspect broad groups or zoom into smaller subsegments.

### 4. Why is interpretability valuable in clustering?

Clustering is often exploratory.

If stakeholders cannot understand why groups exist, they are less likely to trust or use the segmentation.

