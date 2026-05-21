# Linear Regression Project Summary

# 🎬 Can Machine Learning Predict Disney Movie Success?

## Project Overview

This project explores how Linear Regression can be used to predict Disney movie box office revenue using real-world movie metadata and rating-related features.

The project was created as part of the GraphX Labs ML Concepts Portfolio to understand:
- the intuition behind Linear Regression
- regression model evaluation
- feature relationships
- multicollinearity
- preprocessing effects
- business interpretation of machine learning models

The goal was not only to build a predictive model, but also to understand the reasoning and assumptions behind regression modeling.

---

# 📊 Dataset

## Dataset Used
Disney Movies Dataset

The dataset contains:
- movie titles
- release dates
- budgets
- runtime
- IMDb ratings
- Metascore
- Rotten Tomatoes scores
- box office revenue

---

# 🎯 Problem Statement

The objective of this project was to predict Disney movie box office revenue using Linear Regression.

This is a:
- supervised learning problem
- regression problem

because the target variable (`box_office`) is continuous.

---

# 🧠 Features Used

Final model features:
- budget
- running_time_minutes
- imdb
- release_year

Target variable:
- box_office

---

# 🔥 Exploratory Data Analysis

Key EDA findings:

## Budget Had Strong Predictive Signal

Budget showed the strongest correlation with box office revenue:

\[
Correlation = 0.74
\]

This suggests that larger-budget Disney movies generally earned higher revenue.

---

## Ratings Variables Were Highly Correlated

IMDb rating, Metascore, and Rotten Tomatoes score showed strong correlation with each other.

This indicated:
- overlapping information
- multicollinearity risk

---

## Revenue Distribution Was Highly Skewed

A few blockbuster movies earned extremely high revenue compared to the majority of movies.

This created:
- skewed distributions
- outlier sensitivity
- large residuals

---

# 🤖 Models Built

## Model 1 — Baseline Linear Regression

Features:
- running time
- budget
- IMDb rating
- Metascore
- Rotten Tomatoes score
- release year

### Results

- MAE: ~172 million
- RMSE: ~260 million
- R²: ~0.56

### Interpretation

The model explained approximately 56% of the variance in Disney movie box office revenue.

This was a reasonable result for:
- a relatively small dataset
- a simple Linear Regression model
- limited feature engineering

---

## Model 2 — Log-Transformed Model

Experiment:
- applied log transformation to:
  - box office revenue
  - budget

### Observation

The transformed model performed worse:
- R² became negative

### Key Learning

This experiment demonstrated that:
> preprocessing techniques should always be tested rather than blindly applied.

Log transformation does not universally improve model performance.

---

## Model 3 — Reduced Multicollinearity Model

To improve interpretability:
- removed Metascore
- removed Rotten Tomatoes score

Final features:
- budget
- runtime
- IMDb rating
- release year

### Results

- MAE: ~183 million
- RMSE: ~272 million
- R²: ~0.52

### Interpretation

The simplified model slightly reduced predictive performance but improved:
- feature interpretability
- model simplicity
- coefficient stability

This demonstrated an important machine learning principle:

> Simpler models can sometimes be preferable to more complex models with redundant features.

---

# 📈 Evaluation Metrics Used

## MAE — Mean Absolute Error

Measures average prediction error.

---

## RMSE — Root Mean Squared Error

Penalizes large errors more heavily.

Useful for understanding:
- outlier impact
- blockbuster prediction difficulty

---

## R² Score

Measures how much variance in the target variable is explained by the model.

---

# 🔥 Key Machine Learning Concepts Covered

This project explored:
- Linear Regression
- Exploratory Data Analysis
- Feature Selection
- Correlation Analysis
- Multicollinearity
- Residual Analysis
- Model Evaluation
- Log Transformation
- Regression Assumptions
- Business Interpretation

---

# 🧠 Major Learnings

## 1. Budget Is a Strong Predictor

Movie budget was the strongest predictor of Disney movie revenue.

---

## 2. Real-World Data Is Messy

The dataset contained:
- outliers
- skewed distributions
- correlated features
- incomplete information

This reflects real machine learning workflows.

---

## 3. Transformations Require Validation

Log transformations did not improve performance in this case.

This highlighted the importance of:
- experimentation
- critical evaluation
- understanding data distributions

---

## 4. Multicollinearity Matters

Highly correlated features can destabilize coefficient interpretation in Linear Regression models.

---

## 5. Interpretability Is Important

A slightly simpler model may sometimes be preferred if it:
- improves clarity
- reduces redundancy
- stabilizes interpretation

---

# 🚀 Future Improvements

Potential future improvements:
- Ridge Regression
- Lasso Regression
- Feature Scaling
- Additional Feature Engineering
- Franchise Detection
- Genre Encoding
- Ensemble Models
- Time-Based Features
- Nonlinear Models

---

# 📚 Final Takeaway

Linear Regression may appear simple, but it teaches many of the foundational ideas behind machine learning:

- prediction
- optimization
- feature relationships
- model assumptions
- evaluation
- interpretability

Understanding these deeply builds a strong foundation for more advanced machine learning techniques.

Most importantly:

> Machine learning becomes far less mysterious when you understand the intuition behind the math.