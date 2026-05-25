# SHAP & Explainability Summary Report

## Executive Summary

This project demonstrates how SHAP makes a machine learning model more transparent by breaking predictions into feature-level contributions.

Using the Breast Cancer Wisconsin Diagnostic dataset, the project trains an XGBoost classifier to predict malignant cases and then uses SHAP to explain both global model behavior and individual predictions.

Core lesson:

> Model performance tells us whether predictions are accurate. Explainability helps us understand whether predictions are trustworthy.

## Dataset

Dataset:

```text
Breast Cancer Wisconsin Diagnostic Dataset
```

Rows:

```text
569 diagnostic samples
```

Features:

```text
30 numerical medical measurements
```

Target:

```text
is_malignant
```

## Predictive Model Findings

The project trains an XGBoost classifier, chosen because boosted tree models are powerful but not naturally transparent.

The notebook evaluates:

- accuracy
- precision
- recall
- F1-score
- ROC-AUC
- confusion matrix

## SHAP Insights

SHAP converts model output into additive feature contributions.

Each prediction can be read as:

```text
baseline prediction + feature pushes = final prediction
```

This allows users to see which measurements pushed the model toward malignant or benign.

## Global Feature Importance

The SHAP summary and bar plots identify the measurements the model relies on most across the test set.

These global explanations are useful for model auditing, stakeholder communication, and sanity-checking whether the model is learning medically plausible patterns.

## Local Prediction Analysis

The local explanation section selects an individual high-risk prediction and shows feature-by-feature pushes using force-style and waterfall-style visuals.

This answers the human question:

> Why did the model make this specific prediction?

## Bias and Fairness Observations

The dataset does not include demographic sensitive attributes, so it cannot support a full fairness audit.

That limitation is important. Explainability can reveal model behavior, but fairness analysis requires the right context, data, and governance process.

## Business Interpretation

Explainability matters in regulated or high-stakes domains because stakeholders need more than a score.

They need to know:

- why a model made a prediction
- whether the reasoning is plausible
- whether the model is relying on risky shortcuts
- whether errors can be diagnosed
- whether the prediction can be defended

## Practical Lessons

Key lessons:

- Traditional feature importance is helpful but incomplete.
- SHAP provides both global and local explanations.
- Local explanations are essential for individual decisions.
- SHAP can help debug wrong predictions.
- Explainability supports trust, but does not guarantee fairness.
- Correlated features can complicate interpretation.

## Final Takeaway

GraphX Labs takeaway:

> Explainability is how machine learning moves from prediction to accountability.
