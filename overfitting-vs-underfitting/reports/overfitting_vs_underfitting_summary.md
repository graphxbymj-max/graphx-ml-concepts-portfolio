# Overfitting vs Underfitting Project Summary

## Executive Summary

This project demonstrates how machine learning models fail when they are either too simple or too flexible. Using the Breast Cancer Wisconsin diagnostic dataset, it compares underfit, balanced, overfit, and regularized models through train/test performance, model complexity curves, cross-validation, regularization experiments, and learning curves.

The project is designed around a practical engineering question:

> Did the model learn reusable signal, or did it memorize the training data?

## Dataset

Dataset: Breast Cancer Wisconsin Diagnostic Dataset from scikit-learn.

Rows: 569

Features: 30 numeric medical measurements

Target variable: `is_benign`

- `1`: benign
- `0`: malignant

Raw data:

```text
overfitting-vs-underfitting/data/raw/breast_cancer_wisconsin.csv
```

Processed data:

```text
overfitting-vs-underfitting/data/processed/breast_cancer_wisconsin_processed.csv
```

## Experiments Performed

- Exploratory data analysis
- Feature distribution visualizations
- Target correlation visualization
- Underfit Decision Tree with `max_depth=1`
- Balanced Decision Tree with controlled depth and leaf size
- Overfit Decision Tree with unlimited depth
- Regularized Logistic Regression
- Train vs test comparison
- Decision Tree complexity curve
- Synthetic polynomial fitting visual
- 5-fold cross-validation comparison
- Logistic regularization curve
- Learning curve diagnostics

## Underfitting Observations

The intentionally shallow Decision Tree is constrained to a single split. It can capture one useful distinction, but it cannot model the richer structure in the healthcare features.

Underfitting appears as:

- weaker training accuracy
- weaker test accuracy
- small train/test gap
- high bias

The lesson is that simplicity is useful only until it prevents the model from hearing the signal.

## Overfitting Observations

The unrestricted Decision Tree can keep splitting until it explains the training set in extreme detail. This creates high training performance, but it may produce a larger generalization gap.

Overfitting appears as:

- very high training accuracy
- lower test accuracy
- larger train/test gap
- high variance

The lesson is that memorization often looks like intelligence until new data arrives.

## Balanced Model Findings

The balanced tree and regularized logistic model demonstrate the practical sweet spot. They are flexible enough to learn meaningful medical patterns while still controlled enough to avoid chasing every small training-set irregularity.

Good generalization is not perfect memory. It is durable learning.

## Regularization Insights

Regularization adds restraint.

For Logistic Regression, lower `C` means stronger regularization. The model is discouraged from assigning extreme weights to features.

For Decision Trees, regularization appears through controls such as:

- `max_depth`
- `min_samples_leaf`
- pruning
- minimum split requirements

Regularization is useful when training performance is much stronger than test performance.

## Cross-Validation Insights

A single train/test split can be lucky or unlucky. Cross-validation tests the model across multiple validation slices and gives a more stable estimate of generalization.

If cross-validation scores vary widely, the model may be unstable, the dataset may be small, or the model may be too sensitive to the exact split.

## Practical Debugging Lessons

When debugging model quality:

- Poor train and test performance usually suggests underfitting.
- Strong train performance but weak test performance suggests overfitting.
- Suspiciously strong validation performance may indicate leakage.
- A large train/test gap means the model may be memorizing.
- Learning curves reveal whether more data is likely to help.
- Regularization and simpler models help when variance is too high.
- Better features and more flexible models help when bias is too high.

## Final Takeaway

The central skill is not knowing that overfitting and underfitting exist. The central skill is recognizing them in model behavior.

Machine learning succeeds when a model learns what still matters after the training data is gone.

