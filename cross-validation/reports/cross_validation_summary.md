# Cross Validation Project Summary

## Executive Summary

This project demonstrates why one train-test split is not enough to trust a machine learning model. Using the IBM Telco Customer Churn dataset, it compares single split evaluation, repeated train-test splits, KFold Cross Validation, StratifiedKFold, GridSearchCV tuning, learning curves, and validation curves.

The core lesson:

> Model reliability is not one good score. It is consistent performance across multiple views of the data.

## Dataset

Dataset: IBM Telco Customer Churn Dataset

Rows: 7,043

Target variable: `churn`

- `1`: customer churned
- `0`: customer stayed

The dataset includes numerical and categorical customer attributes, including tenure, charges, contract type, internet service, payment method, and support services.

## Validation Experiments

The notebook performs:

- baseline single train-test split
- repeated train-test splits across 30 random states
- 5-fold KFold Cross Validation
- 5-fold StratifiedKFold Cross Validation
- fold class-balance comparison
- Logistic Regression, Decision Tree, and Random Forest CV comparison
- fold score distribution visualization
- GridSearchCV Decision Tree tuning
- train vs validation score analysis
- learning curve diagnostics
- validation curve diagnostics

## Train-Test Instability Findings

The repeated split experiment shows that accuracy changes when the random state changes. This does not mean the model is broken. It means one split is an incomplete estimate of generalization.

A single test score can be:

- lucky
- unlucky
- overly optimistic
- overly pessimistic
- unrepresentative of future data

## Cross Validation Findings

Cross Validation creates a distribution of scores across folds. This gives a more realistic view of model quality.

Useful outputs include:

- mean fold score
- standard deviation
- minimum fold score
- maximum fold score
- score range

The mean estimates typical performance. The standard deviation estimates stability.

## KFold vs StratifiedKFold

KFold rotates validation folds but does not guarantee target balance in classification tasks.

StratifiedKFold preserves the churn rate across folds. This is especially important because churn is imbalanced: most customers stay, fewer customers leave.

For classification, StratifiedKFold is usually the safer default.

## Tuning Insights

The project uses `GridSearchCV` to tune Decision Tree depth and minimum samples per leaf.

Cross-validated tuning is more trustworthy than tuning on a single split because it selects hyperparameters that perform consistently across folds.

The tuning section also compares mean train score and mean validation score to expose overfitting behavior.

## Model Stability Analysis

A model should be evaluated by both performance and stability.

Strong model:

- high mean validation score
- low standard deviation
- reasonable train/validation gap
- stable fold performance

Risky model:

- strong score on one split
- high fold variance
- large train/validation gap
- unstable tuning results

## Practical Lessons

- Do not trust one train-test split blindly.
- Always inspect variance across folds.
- Use StratifiedKFold for imbalanced classification.
- Tune hyperparameters with Cross Validation.
- Keep a final test set for the last unbiased check.
- Use learning curves and validation curves for diagnosis.
- Treat model evaluation as reliability engineering, not scoreboard watching.

## Final Takeaway

Cross Validation helps machine learning teams avoid false confidence.

One score can be a lucky snapshot. Cross Validation reveals whether the model keeps working when the data is rearranged.

