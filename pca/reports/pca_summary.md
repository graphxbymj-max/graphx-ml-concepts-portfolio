# PCA Project Summary

## Executive Summary

This project demonstrates how Principal Component Analysis compresses high-dimensional medical data into fewer informative components. Using the Breast Cancer Wisconsin dataset, it shows feature correlation, scaling effects, explained variance, 2D/3D PCA visualization, reconstruction error, model comparison, and component loadings.

The central lesson:

> PCA compresses complexity by finding the directions where the strongest patterns live.

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset

Rows: 569

Features: 30 numerical measurements

Target: `is_benign`, used for visualization and model comparison only

## PCA Experiments

The notebook performs:

- correlation analysis
- pairplots of correlated features
- PCA before and after scaling
- explained variance analysis
- cumulative variance analysis
- 2D PCA visualization
- 3D PCA visualization
- reconstruction error analysis
- model comparison before and after PCA
- component loading analysis

## Explained Variance Findings

The first few components capture a large share of the dataset's information because many original features are correlated.

Cumulative explained variance helps choose how many components are needed to preserve a target amount of information, such as 90% or 95%.

## Dimensionality Reduction Insights

PCA reduces 30 original features into a smaller set of principal components.

This makes the data easier to visualize, faster to model, and less redundant.

## Visualization Improvements

The 2D PCA plot makes hidden diagnostic structure visible.

Although PCA does not use labels to create components, benign and malignant cases separate meaningfully in the compressed space.

## Model Performance Comparisons

The notebook compares Logistic Regression on original features and Logistic Regression after PCA.

The PCA model uses fewer features while retaining strong predictive performance, demonstrating compression without major information loss.

## Business Insights

PCA is valuable when data has many correlated features and teams need:

- faster modeling
- simpler representations
- better visualization
- reduced redundancy
- noise reduction

## Limitations

PCA has limitations:

- sensitive to scaling
- linear method
- can lose information
- components are harder to interpret
- may miss nonlinear structure

## Practical Lessons

- Always scale before PCA.
- Use explained variance to choose components.
- Use PCA for visualization and compression.
- Inspect loadings carefully.
- Do not treat PCA components as easily interpretable business features.
- Compare model performance before and after PCA.

