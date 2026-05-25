# PCA Interview Questions Explained Like a Real ML Engineer

PCA is often taught with eigenvectors and covariance matrices.

Those ideas matter, but the practical intuition comes first:

> PCA compresses many correlated features into fewer signals while preserving as much important variation as possible.

That is why it shows up in visualization, compression, noise reduction, and high-dimensional machine learning.

## What is PCA?

PCA stands for Principal Component Analysis.

It transforms the original feature space into new directions called principal components.

These components are ordered by how much variance they explain.

## Why do we need dimensionality reduction?

High-dimensional data can be redundant, noisy, expensive to model, and impossible to visualize.

Dimensionality reduction makes the data smaller while trying to preserve the important structure.

## What are principal components?

Principal components are new features created from combinations of original features.

The first component captures the strongest direction of variation. The second captures the next strongest direction, and so on.

## What is explained variance?

Explained variance tells us how much of the original data's variation is captured by a component.

If the first few components explain most of the variance, the dataset can be compressed effectively.

## Why does PCA maximize variance?

PCA assumes that directions with more spread contain more useful information.

It finds the directions where examples differ the most and keeps those directions first.

## Why is scaling important in PCA?

PCA is based on variance.

If features are on different scales, large-scale features can dominate the components.

Scaling ensures PCA is comparing patterns rather than units.

## What does PCA actually do to the data?

PCA rotates the data into a new coordinate system.

Then it orders the new axes by importance.

Keeping fewer axes gives us a compressed representation.

## What is feature redundancy?

Feature redundancy happens when multiple features carry overlapping information.

For example, radius, perimeter, and area may repeat similar size information.

PCA can summarize that overlap.

## What is the curse of dimensionality?

The curse of dimensionality describes problems that appear as feature count grows.

Data becomes sparse, distances become less meaningful, computation increases, and models may overfit more easily.

## How do you choose number of components?

Use cumulative explained variance, reconstruction error, model performance, and business needs.

A common approach is keeping enough components to explain 90% or 95% of variance.

## How do you interpret PCA components?

Use loadings.

Loadings show how strongly each original feature contributes to each component.

But components can still be hard to interpret because they mix many features.

## Can PCA reduce overfitting?

Sometimes.

By removing noisy or redundant dimensions, PCA can simplify the input space and reduce overfitting risk.

But it should be validated with model performance.

## How does PCA speed up ML?

PCA reduces feature count.

Fewer features can mean faster training, faster prediction, and simpler pipelines.

## What happens if you skip scaling?

PCA may overemphasize features with larger numeric ranges.

The components may reflect scale, not real importance.

## Can PCA handle nonlinear relationships?

Standard PCA is linear.

It cannot fully capture nonlinear manifolds. Methods like t-SNE, UMAP, kernel PCA, or autoencoders may work better for nonlinear structure.

## Difference between PCA and feature selection?

PCA creates new features by combining original ones.

Feature selection keeps original features and removes others.

PCA compresses. Feature selection filters.

## Difference between PCA and t-SNE?

PCA is linear and preserves broad global structure.

t-SNE is nonlinear and focuses on local neighborhoods for visualization.

## Difference between PCA and UMAP?

PCA is linear, fast, and interpretable.

UMAP is nonlinear and often better at revealing complex manifold structure in visualization.

## PCA vs autoencoders?

PCA is linear and deterministic.

Autoencoders are neural networks that can learn nonlinear compressed representations.

## Why is PCA considered unsupervised learning?

PCA does not use target labels.

It learns structure from the feature matrix alone.

## How would you explain PCA to a stakeholder?

I would say:

> PCA compresses many overlapping measurements into fewer summary signals while keeping most of the important patterns.

That explanation avoids math and focuses on usefulness.

## Why can too many features hurt models?

Too many features can add noise, redundancy, slower computation, overfitting risk, and harder interpretation.

PCA helps when those features contain compressible structure.

