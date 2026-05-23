# Decision Trees Project Summary

## Executive Summary

This project builds a beginner-friendly Decision Tree classifier to predict whether a banking customer will subscribe to a term deposit after a marketing campaign.

The project focuses on interpretability. Instead of treating the model as a black box, it shows how trees split data, why impurity matters, how overfitting appears, and how pruning improves generalization.

## Dataset Used

Dataset:

```text
UCI Bank Marketing Dataset
```

Source:

```text
https://archive.ics.uci.edu/dataset/222/bank+marketing
```

Raw file:

```text
data/raw/bank-additional/bank-additional-full.csv
```

Processed file:

```text
data/processed/bank_marketing_processed.csv
```

The dataset contains 41,188 campaign records with customer attributes, contact details, previous campaign history, and economic indicators.

## Target Variable

Target column:

```text
subscribed
```

The original `y` column is encoded as:

- `yes`: 1
- `no`: 0

## Features Used

The model uses features such as:

- age
- job
- marital status
- education
- credit default status
- housing loan
- personal loan
- contact type
- month
- day of week
- campaign contact count
- previous campaign outcome
- employment variation rate
- consumer price index
- consumer confidence index
- Euribor 3-month rate
- number of employees

The `duration` column is removed from the processed modeling dataset to avoid leakage.

## Baseline Model Results

    The baseline Decision Tree uses:

```text
DecisionTreeClassifier(criterion="gini", random_state=42)
```

    Baseline test-set performance:

    ```text
    Accuracy:  0.8390
    Precision: 0.3018
    Recall:    0.3265
    F1-score:  0.3137
    ROC-AUC:   0.6177
    ```

    A fully grown tree achieves very high training accuracy but weaker test performance. This is the central overfitting lesson in the project.

## Final Model Results

The final model uses regularization parameters such as:

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- optional `ccp_alpha`

    Final performance from the notebook run:

    ```text
    Accuracy:  0.9004
    Precision: 0.6357
    Recall:    0.2726
    F1-score:  0.3816
    ROC-AUC:   0.8020
    ```

    Selected parameters:

    ```text
    criterion: entropy
    max_depth: 8
    min_samples_leaf: 25
    min_samples_split: 250
    ```

## Key Findings

- A deep tree can memorize the training dataset.
- A shallow tree is easier to explain but may miss subtle patterns.
- Regularization creates a better balance between interpretability and performance.
- Previous campaign outcome and economic context variables are strong predictors.
- Accuracy alone is not enough because most customers do not subscribe.

## Business Interpretation

In business language, the model helps answer:

> Which customers look more likely to respond to a marketing campaign?

The model can support campaign prioritization, but it should not be used as the only decision rule. The bank should combine model output with campaign capacity, customer experience considerations, and compliance checks.

## Limitations

- Decision Trees can be unstable: small data changes may produce a different tree.
- Fully grown trees overfit easily.
- The target class is imbalanced.
- The public dataset may not represent every bank or every campaign period.
- A single train-test split does not fully measure model stability.
- Decision Trees often underperform ensemble methods such as Random Forest and Gradient Boosting.

## Future Improvements

- Add cross-validation
- Tune thresholds based on campaign economics
- Compare against Logistic Regression
- Compare against Random Forest
- Use cost-sensitive learning
- Add probability calibration
- Add SHAP explanations for local interpretability
