# 🧠 Linear Regression Interview Questions Explained Intuitively

## From residuals and R² to Ridge, Lasso, and real-world model interpretation

Linear Regression looks simple.

Almost suspiciously simple.

You see the equation:

$$
y = w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + b
$$

And you think:

> “Okay… it’s just a line. How hard can it be?”

But then interviews start asking:

- What does R² actually mean?
- Why does multicollinearity matter?
- Why is RMSE more sensitive to outliers?
- When would you use Ridge Regression?
- What does Lasso do differently?
- Why did your log transformation worsen the model?
- How would you explain Linear Regression to a business stakeholder?

And suddenly, Linear Regression is not so “basic” anymore.

This article is a companion to my Disney movie revenue prediction project, where I used Linear Regression to predict Disney box office revenue using features like budget, runtime, IMDb rating, and release year.

You can find the full project here:

👉 GitHub Project:  
https://github.com/graphxbymj/graphx-ml-concepts-portfolio

In this article, we’ll go through Linear Regression interview questions in a way that is:

- intuitive
- practical
- interview-friendly
- connected to real ML projects

Let’s begin.

---

# 1. What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value.

It learns the relationship between input features and a target variable.

For example, we may want to predict:

- house price
- salary
- customer lifetime value
- movie revenue
- medical cost
- sales

The model assumes that the target can be approximated as a linear combination of the input features.

In simple form:

$$
y = mx + b
$$

In multiple-feature form:

$$
y = w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + b
$$

Where:

- \(y\) = predicted output
- \(x_{1}, x_{2}, x_{3}\) = input features
- \(w_{1}, w_{2}, w_{3}\) = learned coefficients
- \(b\) = intercept

In my Disney movie project:

- \(y\) = predicted box office revenue
- \(x_{1}\) = budget
- \(x_{2}\) = runtime
- \(x_{3}\) = IMDb rating
- \(x_{4}\) = release year

So the model is trying to learn:

> “How do these movie features combine to explain box office revenue?”

That’s Linear Regression.

---

# 2. What is the difference between simple and multiple Linear Regression?

Simple Linear Regression uses one input feature.

Example:

$$
y = mx + b
$$

A practical example:

> Predict box office revenue using only budget.

Multiple Linear Regression uses more than one input feature.

Example:

$$
y = w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + b
$$

A practical example:

> Predict box office revenue using budget, runtime, IMDb rating, and release year.

The idea is the same.

The model still tries to find the best relationship between inputs and output.

The only difference is that instead of drawing a line in 2D, multiple regression fits a hyperplane in higher-dimensional space.

That sounds fancy, but intuitively it means:

> The model is balancing multiple signals at once.

---

# 3. What does the coefficient of a feature mean?

A coefficient tells us how much the prediction changes when that feature increases by one unit, assuming all other features remain constant.

Example:

Suppose the coefficient for budget is positive.

That means:

> As budget increases, predicted box office revenue tends to increase.

If the coefficient is negative, it means:

> As that feature increases, predicted revenue tends to decrease.

This is one of the biggest strengths of Linear Regression:

# interpretability.

Unlike some complex models, Linear Regression gives us a direct way to inspect how features influence predictions.

But there is one warning.

Coefficient interpretation becomes tricky when features are highly correlated.

For example, in my Disney project:

- IMDb rating
- Metascore
- Rotten Tomatoes score

were strongly correlated.

That means the model may struggle to decide which rating variable deserves credit.

This is called multicollinearity, and we’ll discuss it shortly.

---

# 4. What is the intercept?

The intercept is the model’s predicted value when all input features are zero.

In the equation:

$$
y = w_{1}x_{1} + w_{2}x_{2} + b
$$

the intercept is:

$$
b
$$

Intuitively, it is the baseline prediction before feature contributions are added.

However, in many real-world problems, the intercept may not have a meaningful business interpretation.

For example, in the Disney movie project, “budget = 0, runtime = 0, IMDb rating = 0” is not a realistic movie.

So the intercept exists mathematically, but we should be careful about over-interpreting it.

---

# 5. What are residuals?

Residuals are the errors made by the model.

$$
Residual = Actual - Predicted
$$

If a movie actually made \$900 million and the model predicted \$750 million:

$$
Residual = 900M - 750M = 150M
$$

Residuals tell us:

- where the model is wrong
- how large the errors are
- whether the errors follow a pattern
- whether Linear Regression assumptions may be violated

Ideally, residuals should look random.

If residuals show a clear pattern, it usually means:

> the model is missing something important.

Maybe the relationship is nonlinear.

Maybe an important feature is missing.

Maybe outliers are dominating.

Residuals are like your model’s complaint box.

They tell you what the model is struggling with.

---

# 6. What does R² measure?

R² measures how much of the variation in the target variable is explained by the model.

If:

$$
R^{2} = 0.80
$$

then the model explains about 80% of the variation in the target.

In my Disney project, the baseline Linear Regression model had:

$$
R^{2} \approx 0.56
$$

That means:

> The model explained around 56% of the variation in Disney movie box office revenue.

For a simple model with limited features, that was a reasonable result.

But R² should not be treated as the only truth.

A higher R² does not automatically mean a better model.

You also need to consider:

- model interpretability
- outlier behavior
- residual patterns
- business usefulness
- test set performance

Also, R² can be negative.

A negative R² means:

> The model performs worse than simply predicting the average target value.

That happened in my log-transformed experiment — and it was an important learning moment.

---

# 7. What is the difference between MAE, MSE, and RMSE?

These are common regression evaluation metrics.

## MAE — Mean Absolute Error

MAE tells us the average absolute error.

It answers:

> “On average, how far are predictions from actual values?”

If MAE is \$172 million, then the model is off by about \$172 million on average.

MAE is easy to explain to business stakeholders.

## MSE — Mean Squared Error

MSE squares errors before averaging them.

This means large errors are punished more heavily.

MSE is useful mathematically, but harder to interpret because the units are squared.

## RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

It is in the same unit as the target variable.

RMSE also penalizes large errors more than MAE.

In the Disney project:

- MAE was around \$172 million
- RMSE was around \$260 million

Since RMSE was much larger than MAE, it suggested:

> The model struggled with large blockbuster outliers.

That makes sense because a few Disney movies earn unusually massive revenue.

---

# 8. What assumptions does Linear Regression make?

Linear Regression makes several assumptions.

The major ones are:

## 1. Linear relationship

The relationship between features and target should be approximately linear.

If the relationship is curved or complex, Linear Regression may underperform.

## 2. Independent errors

The errors should not be dependent on each other.

## 3. Constant variance of residuals

This is called homoscedasticity.

It means the spread of residuals should be roughly constant across prediction values.

## 4. Residuals should be approximately normally distributed

This is especially important for statistical inference.

## 5. Low multicollinearity

Features should not be extremely correlated with each other.

In real-world datasets, these assumptions are often imperfect.

That’s okay.

The goal is not to find a magical perfect dataset.

The goal is to understand what assumptions are being violated and what impact that has on the model.

---

# 9. What is multicollinearity?

Multicollinearity happens when two or more input features are highly correlated.

Example:

In the Disney project:

- IMDb rating
- Metascore
- Rotten Tomatoes score

all measured some version of movie quality or reception.

So they naturally overlapped.

Why is this a problem?

Because Linear Regression tries to assign a coefficient to each feature.

If two features carry similar information, the model struggles to separate their individual effects.

This can cause:

- unstable coefficients
- confusing interpretation
- inflated variance
- misleading feature importance

A model may still predict reasonably well with multicollinearity, but interpretation becomes weaker.

---

# 10. What is Ridge Regression?

Ridge Regression is a regularized version of Linear Regression.

It adds a penalty to large coefficients.

The goal is to prevent the model from relying too heavily on any one feature.

Ridge uses L2 regularization.

Its cost function adds a penalty based on squared coefficient values:

$$
Loss = MSE + \lambda \sum_{j=1}^{p} w_j^2
$$

Where:

- \(MSE\) = model error
- \(w_j\) = coefficients
- \(\lambda\) = regularization strength

Intuitively:

> Ridge Regression tells the model: “Fit the data, but don’t let your coefficients become too extreme.”

This is useful when:

- features are correlated
- model is overfitting
- coefficients are unstable
- you want smoother predictions

Ridge does not usually shrink coefficients all the way to zero.

It reduces them, but keeps all features in the model.

---

# 11. What is Lasso Regression?

Lasso Regression is another regularized version of Linear Regression.

It also penalizes large coefficients, but in a different way.

Lasso uses L1 regularization:

$$
Loss = MSE + \lambda \sum_{j=1}^{p} |w_j|
$$

The key difference:

> Lasso can shrink some coefficients exactly to zero.

That means Lasso can perform feature selection.

If a feature is not useful, Lasso may effectively remove it from the model.

This is useful when:

- you have many features
- you suspect some features are irrelevant
- you want a simpler model
- you want automatic feature selection

In short:

- Ridge shrinks coefficients
- Lasso can eliminate features

---

# 12. Ridge vs Lasso — What’s the Difference?

Both Ridge and Lasso are regularization techniques.

Both help reduce overfitting.

But they behave differently.

## Ridge Regression

Uses L2 penalty:

$$
\sum w_j^2
$$

Effect:

- shrinks coefficients
- keeps all features
- works well with multicollinearity
- useful when many features matter a little

## Lasso Regression

Uses L1 penalty:

$$
\sum |w_j|
$$

Effect:

- shrinks coefficients
- can set some coefficients to zero
- performs feature selection
- useful when only a few features matter strongly

Simple intuition:

> Ridge is like turning down the volume on all features.  
> Lasso is like muting some features completely.

---

# Final Takeaway

Linear Regression is often called a beginner algorithm.

But that does not mean it is shallow.

It teaches some of the most important ideas in machine learning:

- prediction
- error
- optimization
- interpretability
- assumptions
- multicollinearity
- regularization
- model evaluation

If you understand Linear Regression deeply, you are not just learning one algorithm.

You are learning the foundation of machine learning itself.

And that is why this model deserves more respect than it usually gets.