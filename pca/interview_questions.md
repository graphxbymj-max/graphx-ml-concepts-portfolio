# PCA Interview Questions

## Conceptual Questions

### 1. What is PCA?

PCA, or Principal Component Analysis, is a dimensionality reduction technique that transforms correlated features into new uncorrelated components.

These components capture the strongest directions of variation in the data.

### 2. Why do we need dimensionality reduction?

Dimensionality reduction helps reduce redundancy, noise, computational cost, and visualization difficulty.

It is useful when many features contain overlapping information.

### 3. What are principal components?

Principal components are new features created by combining original features.

The first component captures the most variance, the second captures the next most, and so on.

### 4. What is explained variance?

Explained variance tells us how much of the original data's variation is captured by each component.

Higher explained variance means the component preserves more information.

### 5. Why does PCA maximize variance?

PCA treats high variance as a signal of important structure.

It finds directions where the data spreads the most because those directions often capture the strongest differences between examples.

### 6. Why is scaling important in PCA?

PCA is variance-sensitive.

If features are on different scales, large-scale features can dominate the components.

### 7. What does PCA actually do to the data?

PCA rotates the feature space into new axes and orders those axes by how much variance they capture.

Then we can keep only the top components.

### 8. What is feature redundancy?

Feature redundancy happens when multiple features carry overlapping information.

PCA can compress redundant features into fewer components.

### 9. What is the curse of dimensionality?

The curse of dimensionality describes problems that appear as feature count grows, including sparse data, harder distance calculations, slower modeling, and overfitting risk.

### 10. Why is PCA useful?

PCA is useful for compression, visualization, noise reduction, faster modeling, and understanding hidden structure.

## Practical Questions

### 1. How do you choose number of components?

Use cumulative explained variance, reconstruction error, model performance, and business needs.

Common thresholds are 90% or 95% explained variance.

### 2. What is cumulative explained variance?

Cumulative explained variance is the total variance captured by the first N components.

It helps decide how many components to keep.

### 3. How do you interpret PCA components?

Use component loadings to see how original features contribute.

However, components can be hard to interpret because each one mixes many features.

### 4. Can PCA reduce overfitting?

Sometimes.

By reducing noisy or redundant dimensions, PCA can simplify the model input and reduce overfitting risk.

### 5. How does PCA speed up ML?

PCA reduces feature count.

Fewer features can make training and prediction faster, especially on high-dimensional datasets.

### 6. What are PCA loadings?

Loadings show how strongly each original feature contributes to a principal component.

### 7. What happens if you skip scaling?

Features with larger numeric ranges may dominate PCA.

The components may reflect measurement scale instead of meaningful structure.

### 8. Can PCA handle nonlinear relationships?

Standard PCA is linear.

It may miss nonlinear structures that methods like t-SNE, UMAP, kernel PCA, or autoencoders can capture.

### 9. What are the limitations of PCA?

PCA is sensitive to scaling, assumes linear structure, can lose information, and creates components that are less interpretable than original features.

### 10. Difference between PCA and feature selection?

PCA creates new features from combinations of original features.

Feature selection keeps a subset of original features.

## Advanced/Comparison Questions

### 1. Difference between PCA and t-SNE?

PCA is linear and preserves broad global structure.

t-SNE is nonlinear and focuses on local neighborhood visualization.

### 2. Difference between PCA and UMAP?

PCA is linear and fast.

UMAP is nonlinear and often captures complex manifold structure for visualization.

### 3. PCA vs autoencoders?

PCA is linear and deterministic.

Autoencoders are neural networks that can learn nonlinear compressed representations.

### 4. Why is PCA considered unsupervised learning?

PCA does not use target labels.

It learns structure from the feature matrix alone.

## Business Questions

### 1. Why is dimensionality reduction useful in production?

It can reduce storage, speed up models, simplify pipelines, reduce noise, and make monitoring easier.

### 2. How would you explain PCA to a stakeholder?

I would say:

> PCA compresses many overlapping measurements into fewer summary signals while keeping most of the important patterns.

### 3. Why does visualization matter in ML?

Visualization helps teams understand structure, detect outliers, communicate patterns, and debug models.

### 4. Why can too many features hurt models?

Too many features can add noise, redundancy, slower training, overfitting risk, and harder interpretation.

