# Logistic Regression Project Summary

## Executive Summary

This project builds a beginner-friendly Logistic Regression model to predict employee attrition using the IBM HR Analytics Employee Attrition dataset.

The goal is to show how a binary classification model can estimate whether an employee is likely to leave the company, while keeping the modeling approach simple, interpretable, and portfolio-ready.

The final baseline Logistic Regression model achieved a ROC-AUC score of approximately `0.8107`, which suggests the model has useful ability to rank employees by attrition risk.

## Dataset Used

Dataset:

```text
IBM HR Analytics Employee Attrition & Performance
```

Raw file:

```text
data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv
```

The dataset contains:

- 1,470 employee records
- HR, compensation, satisfaction, and work-history features
- a binary attrition target

## Target Variable

Target column:

```text
Attrition
```

The target values are:

- `Yes`: employee left the company
- `No`: employee stayed with the company

For modeling:

- `Yes` is encoded as `1`
- `No` is encoded as `0`

## Features

The model uses features such as:

- age
- business travel
- department
- distance from home
- education field
- environment satisfaction
- job involvement
- job level
- job role
- job satisfaction
- marital status
- monthly income
- overtime
- total working years
- years at company
- years since last promotion
- years with current manager

Additional engineered features include:

- `income_per_job_level`
- `years_without_promotion_ratio`
- `early_career_flag`
- `long_commute_flag`

## Model Performance

Baseline Logistic Regression performance on the test set:

```text
Accuracy:  0.8639
Precision: 0.6667
Recall:    0.2979
F1-score:  0.4118
ROC-AUC:   0.8107
```

## Key Findings

- The dataset is imbalanced: only about 16% of employees left the company.
- The model has good overall accuracy, but accuracy alone is not enough for this problem.
- Recall is modest at the default `0.5` threshold, meaning the model misses some employees who actually leave.
- ROC-AUC is stronger than recall, which means the probability rankings are useful even if the default threshold is conservative.
- Threshold tuning can improve recall when the business goal is to catch more at-risk employees.
- Logistic Regression coefficients provide a clear way to explain which features push predictions toward attrition or staying.

## Limitations

- The dataset is a public HR analytics dataset and may not fully represent a real company's current workforce.
- The model identifies associations, not causal relationships.
- Some important attrition drivers may not be captured in structured HR fields.
- The baseline model uses a single train-test split.
- The model does not yet include cost-sensitive evaluation.

## Future Improvements

Future improvements could include:

- cross-validation
- class-weighted Logistic Regression
- threshold selection based on business cost
- probability calibration
- feature selection
- regularization comparison
- SHAP-based explanations
- comparison with Random Forest or Gradient Boosting as optional advanced models

The main teaching model should remain Logistic Regression so the project stays focused on classification fundamentals.

