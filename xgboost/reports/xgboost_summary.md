# XGBoost Project Summary

## Executive Summary

This project builds an XGBoost classifier to predict telecom customer churn. It is designed as the next learning step after Random Forest: instead of training many trees independently, XGBoost trains trees sequentially so each new tree focuses on previous errors.

## Dataset

IBM Telco Customer Churn dataset.

## Target Variable

`churn`

- `1`: customer churned
- `0`: customer stayed

    ## Model Comparison

    The notebook compares:

    - Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
    - tuned XGBoost

    ## XGBoost Performance

    Executed notebook results:

    ```text
    Logistic Regression
    Test accuracy: 0.8070
    Precision:     0.6584
    Recall:        0.5668
    F1-score:      0.6092
    ROC-AUC:       0.8416

    Decision Tree
    Test accuracy: 0.7388
    Precision:     0.5079
    Recall:        0.5134
    F1-score:      0.5106
    ROC-AUC:       0.6664

    Random Forest
    Test accuracy: 0.8062
    Precision:     0.6747
    Recall:        0.5214
    F1-score:      0.5882
    ROC-AUC:       0.8435

    XGBoost
    Test accuracy: 0.7999
    Precision:     0.6544
    Recall:        0.5214
    F1-score:      0.5804
    ROC-AUC:       0.8444

    Tuned XGBoost
    Test accuracy: 0.8006
    Precision:     0.6620
    Recall:        0.5080
    F1-score:      0.5749
    ROC-AUC:       0.8461
    ```

    Best tuned XGBoost parameters:

    ```text
    n_estimators: 300
    learning_rate: 0.05
    max_depth: 2
    subsample: 0.8
    colsample_bytree: 1.0
    ```

    XGBoost provides the strongest ROC-AUC in this run, which means it is slightly better at ranking churn risk across thresholds.

## Key Findings

- Boosting improves by correcting previous mistakes.
- Contract type, tenure, charges, and service/support features are important churn drivers.
- SHAP helps explain how features push predictions toward or away from churn.
- XGBoost is powerful but more sensitive to tuning than Random Forest.

## SHAP Insights

SHAP provides both global and local interpretability. It explains how each feature contributes to each prediction, making XGBoost easier to trust in a business context.

## Limitations

- More complex than simpler baselines
- Sensitive to hyperparameters
- Can overfit without regularization
- Less directly interpretable than Logistic Regression or a single Decision Tree

## Future Improvements

- Add early stopping with a validation set
- Tune thresholds based on retention cost
- Add permutation importance
- Compare with LightGBM and CatBoost
- Add model calibration
