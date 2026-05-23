# Random Forest Explained Intuitively

## Customer Churn Prediction with Random Forest

Welcome to the Random Forest project in the GraphX Labs ML Concepts Portfolio.

This project is designed as the natural next step after Decision Trees.

The core idea:

> One Decision Tree is smart. A forest of them is powerful.

A single tree can learn useful rules, but it can also overfit. Random Forest improves on that idea by training many trees and letting them vote.

---

# Business Problem

Customer churn is one of the most important problems in subscription businesses.

The question:

> Can we predict whether a telecom customer is likely to leave?

If a company can identify high-risk customers early, it can design better retention campaigns, improve service, and reduce revenue loss.

---

# Dataset

Dataset:

```text
IBM Telco Customer Churn Dataset
```

Raw file:

```text
random-forest/data/raw/telco_customer_churn.csv
```

Processed file:

```text
random-forest/data/processed/telco_customer_churn_processed.csv
```

Target variable:

```text
churn
```

The target is binary:

- `1`: customer churned
- `0`: customer stayed

---

# Why Random Forest Matters

Decision Trees are easy to explain, but they are fragile.

Random Forest reduces that fragility by:

- training many trees
- using bootstrap samples
- giving each tree a random subset of features
- combining predictions through voting

This reduces variance and usually improves generalization.

---

# Workflow

1. Define the churn problem
2. Load the Telco Customer Churn dataset
3. Inspect missing values, duplicates, and target balance
4. Explore churn patterns visually
5. Clean `TotalCharges` and encode categorical features
6. Train a baseline Decision Tree
7. Train a Random Forest
8. Compare overfitting behavior
9. Evaluate with classification metrics
10. Interpret feature importance
11. Tune hyperparameters
12. Summarize business insights

---

# Folder Structure

```text
random-forest/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── random_forest_project.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   ├── preprocessing/
│   ├── models/
│   ├── visualization/
│   ├── evaluation/
│   └── pipelines/
├── images/
├── reports/
│   └── random_forest_summary.md
├── README.md
├── requirements.txt
├── article_outline.md
└── interview_questions.md
```

The notebook is the main educational walkthrough. The `src/` folder contains reusable functions and a light real-world structure for future expansion.

---

# Model Comparison

Typical notebook results:

```text
    Decision Tree train accuracy: 0.9980
    Decision Tree test accuracy:  0.7388
    Decision Tree ROC-AUC:        0.6664

    Random Forest train accuracy: 0.8575
    Random Forest test accuracy:  0.8062
    Random Forest ROC-AUC:        0.8435
```

The Random Forest usually generalizes better because it averages many imperfect trees instead of trusting one highly flexible tree.

---

# Key Insights

- Contract type is usually one of the strongest churn signals.
- Tenure matters because newer customers often churn at higher rates.
- Monthly charges and total charges provide useful behavioral context.
- Random Forest reduces the overfitting seen in a single Decision Tree.
- Feature importance is helpful, but it should not be interpreted as causation.

---

# Medium Articles

Project article:

```text
articles/random-forest/random_forest_project_article.md
```

Interview article:

```text
articles/random-forest/random_forest_interview_questions.md
```

---

Built with care for the GraphX Labs ML Concepts Portfolio.
