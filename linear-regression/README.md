# 🎬 Can Machine Learning Predict Disney Movie Success?

## Linear Regression Explained Intuitively with Real Disney Movie Data

Welcome to the first project in the GraphX Labs ML Concepts Portfolio.

This project explores how Linear Regression can be used to predict Disney movie box office revenue using real-world movie-related features such as:

- budget
- runtime
- IMDb ratings
- release year
- critic scores

The goal of this project is not just to build a model, but to deeply understand:
- how Linear Regression works
- how machine learning models learn relationships
- how to evaluate regression models
- how preprocessing impacts performance
- how to interpret results critically

---

# 🚀 Project Objective

The objective of this project is to answer the question:

> Can machine learning predict Disney movie success?

More specifically:

> Can we predict Disney movie box office revenue using movie metadata and ratings?

This project uses Linear Regression as the foundational machine learning model to explore:
- prediction
- feature relationships
- coefficient interpretation
- residual analysis
- model assumptions

---

# 📊 Dataset

## Dataset Source

Disney Movies Dataset

The dataset contains information about Disney movies, including:
- title
- budget
- runtime
- IMDb ratings
- Metascore
- Rotten Tomatoes score
- release dates
- box office revenue

---

# 🧠 Machine Learning Problem Type

This is a:

## Supervised Regression Problem

Why?

Because:
- the target variable (`box_office`) is continuous
- we are predicting a numerical value

---

# 📦 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 📂 Project Structure

```text
linear-regression/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── disney_linear_regression.ipynb
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
│   └── linear_regression_summary.md
│
├── README.md
├── requirements.txt
├── article_outline.md
└── interview_questions.md