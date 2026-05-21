# Linear Regression Interview Questions

---

# Conceptual Questions

## 1. What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value by learning the relationship between input features and a target variable.

It tries to fit the best possible line (or hyperplane in higher dimensions) through the data by minimizing prediction error.

Mathematically:

\[
y = Xw + b
\]

Where:
- `X` = input features
- `w` = coefficients/weights
- `b` = intercept
- `y` = predicted value

Example use cases:
- predicting house prices
- sales forecasting
- revenue prediction
- insurance cost estimation

---

## 2. What is the difference between simple and multiple Linear Regression?

### Simple Linear Regression
Uses only one input feature to predict the target.

Example:
\[
y = mx + b
\]

Example:
Predicting salary using years of experience.

---

### Multiple Linear Regression
Uses multiple input features.

Example:
\[
y = w_1x_1 + w_2x_2 + w_3x_3 + b
\]

Example:
Predicting movie revenue using:
- budget
- runtime
- ratings
- release year

---

## 3. What does the coefficient of a feature mean?

A coefficient represents the expected change in the target variable for a one-unit increase in the feature, assuming all other features remain constant.

Example:
If the coefficient for budget is:

\[
2.5
\]

it means:
- increasing budget by 1 unit increases predicted revenue by 2.5 units on average.

Positive coefficient:
- increases prediction

Negative coefficient:
- decreases prediction

---

## 4. What is the intercept?

The intercept is the predicted value of the target when all input features are zero.

It represents the baseline prediction of the model.

Mathematically:
\[
y = Xw + b
\]

where:
- `b` is the intercept.

---

## 5. What are residuals?

Residuals are the differences between actual and predicted values.

\[
Residual = Actual - Predicted
\]

Residuals help us understand:
- model errors
- bias
- assumption violations
- whether the model is fitting well

Ideally:
- residuals should be randomly distributed around zero.

---

## 6. What does R² measure?

R² (R-squared) measures how much variance in the target variable is explained by the model.

Example:
\[
R^2 = 0.80
\]

means:
- the model explains 80% of the variation in the target variable.

Interpretation:
- closer to 1 → better fit
- closer to 0 → weak explanatory power
- negative → model performs worse than predicting the mean

---

## 7. What is the difference between MAE, MSE, and RMSE?

### MAE (Mean Absolute Error)
Average absolute difference between actual and predicted values.

- easy to interpret
- treats all errors equally

---

### MSE (Mean Squared Error)
Squares errors before averaging.

- penalizes large errors heavily
- sensitive to outliers

---

### RMSE (Root Mean Squared Error)
Square root of MSE.

- same unit as target variable
- commonly used in regression evaluation

RMSE is often preferred because it heavily penalizes large mistakes.

---

## 8. What assumptions does Linear Regression make?

Linear Regression assumes:

1. Linear relationship between features and target
2. Residuals are normally distributed
3. Constant variance of residuals (homoscedasticity)
4. Features are not highly correlated
5. Errors are independent

Violating these assumptions can reduce model reliability.

---

## 9. What is multicollinearity?

Multicollinearity occurs when input features are highly correlated with each other.

Example:
- IMDb score
- Metascore
- Rotten Tomatoes score

all measure similar concepts.

Problems caused:
- unstable coefficients
- difficult interpretation
- increased variance
- unreliable feature importance

Common solutions:
- remove correlated features
- use regularization
- apply dimensionality reduction

---

## 10. When should you avoid Linear Regression?

Linear Regression may not work well when:
- relationships are highly nonlinear
- there are many extreme outliers
- features are highly correlated
- residual assumptions are violated
- target distribution is extremely skewed
- the dataset is very complex

In such cases:
- tree-based models
- ensemble models
- neural networks

may perform better.

---

# Practical Questions

## 1. How do you evaluate a regression model?

Common regression evaluation metrics include:

- MAE
- MSE
- RMSE
- R² score

I also evaluate:
- residual distributions
- actual vs predicted plots
- outlier behavior
- model interpretability

A good evaluation combines both:
- numerical metrics
- visual diagnostics

---

## 2. Why do we split data into train and test sets?

We split data to evaluate how well the model generalizes to unseen data.

- training set → used to learn patterns
- test set → used to evaluate performance

Without a test set:
- the model may overfit
- evaluation becomes overly optimistic

---

## 3. How do outliers affect Linear Regression?

Outliers can strongly influence Linear Regression because the model minimizes squared error.

Effects:
- distorted regression line
- inflated error metrics
- unstable coefficients

Common solutions:
- remove outliers
- apply transformations
- use robust regression methods

---

## 4. How do you interpret a negative coefficient?

A negative coefficient means:

> as the feature increases, the predicted target decreases.

Example:
If a feature has coefficient:

\[
-5
\]

then increasing that feature by 1 unit decreases the prediction by 5 units on average.

---

## 5. What does it mean if residuals show a pattern?

Residual patterns often indicate that model assumptions are violated.

Possible causes:
- nonlinear relationships
- missing features
- heteroscedasticity
- unhandled interactions

Ideally:
- residuals should appear random.

Patterns suggest the model is missing important structure in the data.

---

# Business Interpretation Questions

## 1. How would you explain Linear Regression to a non-technical stakeholder?

I would explain it as:

> a method that learns relationships between business variables in order to make predictions.

Example:
- how marketing spend affects sales
- how movie budget affects revenue

The model identifies trends in historical data and uses them to estimate future outcomes.

---

## 2. How would you explain model error to a business team?

I would explain that:

> no prediction model is perfect because real-world outcomes are influenced by many hidden factors.

Error metrics help us understand:
- how close predictions are on average
- how reliable the model is
- whether the model is useful for decision-making

I would focus on:
- practical business impact
- acceptable error ranges
- model limitations

rather than only technical metrics.

---

## 3. How would you decide whether a regression model is good enough for production?

I would evaluate:

1. Prediction accuracy
2. Stability on unseen data
3. Business usefulness
4. Interpretability
5. Error tolerance
6. Scalability
7. Monitoring capability

A model does not need perfect accuracy to be useful.

The key question is:

> Does the model improve business decision-making reliably enough to justify deployment?
