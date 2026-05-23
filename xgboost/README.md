# XGBoost Explained Intuitively

## Customer Churn Prediction with XGBoost

Welcome to the XGBoost project in the GraphX Labs ML Concepts Portfolio.

This project is the next evolution after Random Forest.

The educational theme:

> What happens when machine learning starts learning from its own mistakes?

Random Forest builds many trees independently. XGBoost goes further: it builds trees sequentially, where each new tree tries to correct the mistakes of the previous ones.

## Business Problem

Customer churn is a major subscription-business problem. A telecom company wants to identify customers who are likely to leave so it can prioritize retention action.

Target variable:

```text
churn
```

- `1`: customer churned
- `0`: customer stayed

## Dataset

Dataset: IBM Telco Customer Churn

Raw file:

```text
xgboost/data/raw/telco_customer_churn.csv
```

Processed file:

```text
xgboost/data/processed/telco_customer_churn_processed.csv
```

## Why XGBoost Matters

XGBoost matters because it combines:

- sequential error correction
- weak learners becoming a strong learner
- regularization
- strong performance on tabular data
- feature importance
- compatibility with SHAP explanations

## Workflow

1. Load and inspect churn data
2. Clean `TotalCharges` and encode categorical variables
3. Train baseline Logistic Regression, Decision Tree, and Random Forest models
4. Train XGBoost
5. Compare models with classification metrics and ROC-AUC
6. Interpret feature importance
7. Tune XGBoost hyperparameters
8. Explain predictions with SHAP

    ## Model Comparison

    The notebook compares Logistic Regression, Decision Tree, Random Forest, baseline XGBoost, and tuned XGBoost.

    The core lesson is not just which model wins. The lesson is why boosting can improve performance by learning from previous errors.

    Typical executed notebook results:

    ```text
    Logistic Regression ROC-AUC: 0.8416
    Decision Tree ROC-AUC:       0.6664
    Random Forest ROC-AUC:       0.8435
    XGBoost ROC-AUC:             0.8444
    Tuned XGBoost ROC-AUC:       0.8461
    ```

    Tuned XGBoost selected:

    ```text
    n_estimators: 300
    learning_rate: 0.05
    max_depth: 2
    subsample: 0.8
    colsample_bytree: 1.0
    ```

## Images

- `roc_curve.png`
- `feature_importance.png`
- `shap_summary.png`
- EDA and model comparison plots

## Medium Articles

Project article:

```text
articles/xgboost/xgboost_project_article.md
```

Interview article:

```text
articles/xgboost/xgboost_interview_questions.md
```

Built with care for the GraphX Labs ML Concepts Portfolio.
