# Logistic Regression Explained Intuitively: Predicting Real-World Outcomes with Python

## Employee Attrition Prediction with Logistic Regression

Welcome to the Logistic Regression project in the GraphX Labs ML Concepts Portfolio.

This project explores how Logistic Regression can be used to predict employee attrition using real-world HR data such as:

- age
- overtime status
- monthly income
- job role
- job satisfaction
- distance from home
- years at company
- work-life balance

The goal of this project is not just to build a model, but to deeply understand:

- how Logistic Regression works
- why it is used for binary classification
- how probabilities become class predictions
- how to evaluate classification models
- how precision, recall, and thresholds connect to business decisions
- how to interpret model coefficients in simple language

---

# Project Objective

The objective of this project is to answer the question:

> Can machine learning predict whether an employee is likely to leave a company?

More specifically:

> Can we use employee HR data to estimate the probability of attrition?

This project uses Logistic Regression as the foundational machine learning model to explore:

- binary classification
- probability prediction
- confusion matrix interpretation
- ROC-AUC
- threshold tuning
- coefficient interpretation
- business-friendly model explanation

---

# Dataset

## Dataset Source

IBM HR Analytics Employee Attrition & Performance Dataset

The raw CSV used in this repository is saved at:

```text
logistic-regression/data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv
```

The dataset contains employee-level information, including:

- demographic features
- job role and department
- salary and compensation features
- job satisfaction and work-life balance
- work history
- overtime status
- attrition outcome

## Target Variable

```text
Attrition
```

The target is binary:

- `Yes`: employee left the company
- `No`: employee stayed with the company

In the modeling workflow:

- `Yes` is encoded as `1`
- `No` is encoded as `0`

---

# Machine Learning Problem Type

This is a:

## Supervised Binary Classification Problem

Why?

Because:

- the model learns from labeled historical data
- the target variable has two possible outcomes
- the goal is to predict a class and probability

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Statsmodels
- Plotly
- SciPy

---

# Project Structure

```text
logistic-regression/
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   └── processed/
│       └── employee_attrition_processed.csv
│
├── notebooks/
│   └── logistic_regression_project.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
│
├── images/
│
├── reports/
│   └── logistic_regression_summary.md
│
├── README.md
├── requirements.txt
├── article_outline.md
└── interview_questions.md
```

---

# Workflow

The project follows this workflow:

1. Define the business problem
2. Load the employee attrition dataset
3. Inspect rows, columns, missing values, and target distribution
4. Perform exploratory data analysis
5. Clean the dataset
6. Create intuitive HR features
7. Encode categorical variables
8. Scale numerical variables
9. Split data into training and testing sets
10. Train a baseline Logistic Regression model
11. Evaluate using classification metrics
12. Interpret the confusion matrix
13. Compare precision and recall
14. Plot ROC curve and calculate ROC-AUC
15. Interpret coefficients and odds ratios
16. Tune the classification threshold
17. Summarize learnings and business meaning

---

# Model Built

## Baseline Logistic Regression

The main model is intentionally simple:

```text
Preprocessing Pipeline + Logistic Regression
```

Preprocessing includes:

- StandardScaler for numerical features
- OneHotEncoder for categorical features

The goal is to make Logistic Regression easy to understand, not to hide the concept behind a complex model.

---

# Evaluation Metrics

The model is evaluated using:

- accuracy
- precision
- recall
- F1-score
- confusion matrix
- ROC-AUC
- classification report

Baseline test performance:

```text
Accuracy:  0.8639
Precision: 0.6667
Recall:    0.2979
F1-score:  0.4118
ROC-AUC:   0.8107
```

---

# Key Insights

- The dataset is imbalanced: only about 16% of employees in the dataset left the company.
- Accuracy looks strong, but recall is modest at the default 0.5 threshold.
- ROC-AUC shows the model has useful signal for ranking attrition risk.
- Overtime, income, job level, and work-history variables are useful signals.
- Threshold tuning is important because HR teams may prefer catching more at-risk employees, even if precision decreases.

---

# Future Improvements

Future versions of this project could explore:

- class weighting
- more systematic threshold selection
- cross-validation
- regularization comparison
- calibration curves
- SHAP explanations
- business cost matrix for false positives and false negatives
- comparison with tree-based models

The main model should still remain Logistic Regression because this project is focused on concept mastery.

---

# Medium Article Placeholder

Medium article title:

> Logistic Regression Explained Intuitively: The Classification Model Every ML Beginner Should Understand

Article outline is available in:

```text
article_outline.md
```

---

# GraphX Labs Branding

This project is part of the GraphX Labs ML Concepts Portfolio.

The learning style is:

- intuitive first
- code second
- business interpretation always
- beginner-friendly without being shallow

