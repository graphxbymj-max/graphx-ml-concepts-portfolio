# Random Forest Project Summary

## Executive Summary

This project builds a Random Forest classifier to predict customer churn using the IBM Telco Customer Churn dataset.

The educational goal is to show why Random Forest is a natural evolution from Decision Trees. A single tree is interpretable, but it can overfit. A forest trains many trees and combines their votes, which usually reduces variance and improves generalization.

## Dataset Used

Dataset:

```text
IBM Telco Customer Churn
```

Raw data:

```text
data/raw/telco_customer_churn.csv
```

Processed data:

```text
data/processed/telco_customer_churn_processed.csv
```

## Target Variable

Target:

```text
churn
```

- `1`: customer churned
- `0`: customer stayed

## Baseline Decision Tree Results

    ```text
    Train accuracy: 0.9980
    Test accuracy:  0.7388
    Precision:      0.5079
    Recall:         0.5134
    F1-score:       0.5106
    ROC-AUC:        0.6664
    ```

The single Decision Tree demonstrates the overfitting problem: training performance is much stronger than test performance.

## Random Forest Results

    ```text
    Train accuracy: 0.8575
    Test accuracy:  0.8062
    Precision:      0.6747
    Recall:         0.5214
    F1-score:       0.5882
    ROC-AUC:        0.8435
    ```

    The Random Forest improves stability by training many trees on bootstrap samples and random feature subsets.

    ## Tuned Random Forest Results

    Best tuned parameters from cross-validation:

    ```text
    n_estimators: 300
    max_depth: 6
    min_samples_split: 10
    min_samples_leaf: 3
    ```

    Test performance:

    ```text
    Train accuracy: 0.8067
    Test accuracy:  0.7942
    Precision:      0.6707
    Recall:         0.4412
    F1-score:       0.5323
    ROC-AUC:        0.8429
    ```

    The tuned model slightly reduces test accuracy and recall compared with the baseline forest, but it also reduces the train-test accuracy gap. This is a useful real-world reminder: tuning is not about blindly maximizing one metric. It is about choosing the best tradeoff for the business goal.

## Comparison

The Random Forest generally performs better than the single Decision Tree because it reduces variance. Each individual tree may be noisy, but averaging their predictions produces a more reliable model.

## Feature Importance Summary

Commonly important churn predictors include:

- contract type
- tenure
- monthly charges
- total charges
- internet service
- online security and tech support

These features help explain customer relationship strength, cost sensitivity, and service experience.

## Limitations

- Random Forest is less interpretable than a single tree.
- Feature importance can be biased toward features with many split opportunities.
- The model can be slower and larger than simpler baselines.
- Business action still requires cost-sensitive threshold selection.

## Future Improvements

- Add cross-validation-based threshold selection
- Compare with Logistic Regression and Gradient Boosting
- Use permutation importance
- Add SHAP explanations
- Evaluate retention campaign costs
- Calibrate probabilities
