# Evaluation Metrics Project Summary

## Executive Summary

This project demonstrates why accuracy alone is not enough to judge a machine learning model. Using the IBM Telco Customer Churn dataset, it explains confusion matrices, accuracy, precision, recall, F1-score, ROC-AUC, Precision-Recall curves, threshold tuning, class imbalance, and business-cost tradeoffs.

The central lesson:

> A model can look accurate and still fail the decision it was built to support.

## Dataset

Dataset: IBM Telco Customer Churn Dataset

Rows: 7,043

Target variable: `churn`

- `1`: customer churned
- `0`: customer stayed

The data includes customer tenure, monthly charges, total charges, contract type, internet service, payment method, and service adoption features.

## Class Imbalance Findings

The churn dataset is imbalanced. More customers stay than churn.

This makes accuracy incomplete because a model can perform well overall while still missing too many churned customers.

The notebook also includes a simulated 99% non-fraud example showing how a model can achieve 99% accuracy while catching zero positive cases.

## Metric Comparison

The notebook evaluates Logistic Regression using:

- accuracy
- precision
- recall
- F1-score
- ROC-AUC
- average precision
- confusion matrix

Each metric answers a different question. Accuracy measures total correctness. Precision measures trust in positive predictions. Recall measures how many true positive cases the model caught. F1 balances precision and recall.

## Threshold Tuning Insights

Changing the probability threshold changes model behavior.

Lower thresholds increase recall but can create more false positives.

Higher thresholds increase precision but can create more false negatives.

The notebook includes a simple business-cost model where false negatives are more expensive than false positives, demonstrating how the best threshold depends on business priorities.

## ROC-AUC Observations

ROC-AUC measures class separation across thresholds.

It is useful for evaluating ranking ability, but it should not be the only metric for imbalanced classification because it can look strong even when positive-class precision is weak.

## PR Curve Observations

Precision-Recall curves focus on the positive class and are especially useful for imbalanced datasets.

For churn, the PR curve helps show how much precision must be sacrificed to catch more churners.

## Business Interpretation

In churn prediction:

- False positives waste retention budget.
- False negatives lose customers who might have been saved.

Metric choice depends on campaign capacity, customer lifetime value, outreach cost, and risk tolerance.

## Practical Lessons

- Accuracy is useful but incomplete.
- Confusion matrices explain the types of mistakes.
- Precision matters when false positives are expensive.
- Recall matters when false negatives are expensive.
- F1-score is useful when precision and recall both matter.
- ROC-AUC measures separation.
- PR curves are valuable for imbalanced datasets.
- Threshold tuning should reflect business cost.
- Production monitoring should track metric drift over time.

## Final Takeaway

Evaluation metrics are not about memorizing formulas.

They are about choosing the model behavior that best fits the real-world decision.

