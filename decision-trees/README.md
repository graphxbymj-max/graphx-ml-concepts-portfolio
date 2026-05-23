# Decision Trees Explained Intuitively

## Bank Marketing Subscription Prediction with Decision Trees

Welcome to the Decision Trees project in the GraphX Labs ML Concepts Portfolio.

This project explores how a Decision Tree classifier can predict whether a banking client will subscribe to a term deposit after a marketing campaign.

The goal is not only to train a model. The goal is to understand how trees think:

- how a model asks yes-or-no style questions
- how Gini impurity and entropy help choose splits
- why tree depth matters
- how overfitting happens
- how pruning makes trees more reliable
- how feature importance supports business interpretation

---

# Project Objective

The main question is:

> Can we predict whether a customer will subscribe to a bank term deposit?

This is a practical marketing problem. A bank has limited time and budget for outreach, so it wants to identify customers who are more likely to respond.

---

# Dataset

## Dataset Source

UCI Machine Learning Repository: Bank Marketing Dataset

Source URL:

```text
https://archive.ics.uci.edu/dataset/222/bank+marketing
```

Raw file used:

```text
decision-trees/data/raw/bank-additional/bank-additional-full.csv
```

Processed file:

```text
decision-trees/data/processed/bank_marketing_processed.csv
```

The dataset contains direct marketing campaign data from a Portuguese banking institution.

## Target Variable

```text
subscribed
```

The original target column is `y`.

- `yes` becomes `1`
- `no` becomes `0`

## Important Modeling Note

The original dataset includes `duration`, which is the length of the last contact call. This project removes `duration` from the processed modeling dataset because it is only known after a call is completed. Keeping it would create leakage for a realistic pre-call targeting model.

---

# Machine Learning Problem Type

This is a supervised binary classification problem.

The model learns from historical campaign outcomes and predicts whether a future customer is likely to subscribe.

---

# Project Structure

```text
decision-trees/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── bank_marketing_processed.csv
│
├── notebooks/
│   └── decision_trees_project.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
│
├── images/
│   ├── target_distribution.png
│   ├── categorical_feature_counts.png
│   ├── numerical_feature_distributions.png
│   ├── correlation_heatmap.png
│   ├── decision_tree_visualization.png
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
├── reports/
│   └── decision_trees_summary.md
│
├── README.md
├── requirements.txt
├── article_outline.md
└── interview_questions.md
```

---

# Workflow

1. Define the business problem
2. Load the Bank Marketing dataset
3. Inspect rows, columns, missing values, duplicates, and target balance
4. Explore numerical and categorical patterns
5. Remove leakage-prone and irrelevant columns
6. Encode categorical features
7. Split into training and testing data
8. Train a baseline Decision Tree
9. Evaluate classification performance
10. Visualize a shallow tree
11. Interpret feature importance
12. Compare deep and shallow trees
13. Tune regularization and pruning parameters
14. Select a final interpretable model

---

# Model Summary

The project trains:

- a baseline Decision Tree using `criterion="gini"`
- an unrestricted tree to show overfitting
- a shallow tree for interpretability
- a regularized/pruned final tree

Decision Trees are useful here because the model can be explained as a sequence of business questions.

---

# Model Results

The final model is selected in the notebook based on test-set performance and interpretability.

Typical results from the included run:

```text
    Baseline test accuracy: 0.8390
    Baseline ROC-AUC: 0.6177
    Final test accuracy: 0.9004
    Final ROC-AUC: 0.8020
```

Accuracy is high partly because the dataset is imbalanced, so precision, recall, F1-score, and ROC-AUC are also used.

---

# Key Insights

- Previous campaign outcome is one of the strongest signals.
- Economic context variables such as employment variation rate and Euribor rate matter.
- Contact month and number of previous contacts help the model identify response patterns.
- A fully grown tree memorizes training data too easily.
- A shallow or pruned tree is easier to explain and generalizes better.

---

# Images

![Decision Tree Visualization](images/decision_tree_visualization.png)

![Feature Importance](images/feature_importance.png)

---

# Future Improvements

- Use cross-validation for more stable model selection
- Tune probability thresholds based on marketing campaign cost
- Compare Decision Trees with Logistic Regression, Random Forest, and Gradient Boosting
- Add calibration if predicted probabilities are used for campaign budgeting
- Use SHAP for deeper feature-level explanations

---

# Medium Article

Medium article draft:

```text
articles/decision-trees/decision_trees_project_article.md
```

Companion interview article:

```text
articles/decision-trees/decision_trees_interview_questions.md
```

---

Built with care for the GraphX Labs ML Concepts Portfolio.
