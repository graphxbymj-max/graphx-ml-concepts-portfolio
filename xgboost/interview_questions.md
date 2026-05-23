# XGBoost Interview Questions and Answers

## Conceptual

## 1. What is XGBoost?

XGBoost is an optimized gradient boosting algorithm that builds many small Decision Trees sequentially. Each new tree tries to correct the mistakes made by the previous trees.

## 2. What is boosting?

Boosting is an ensemble technique where models are trained one after another. Later models focus more on the errors of earlier models.

## 3. Difference between bagging and boosting?

Bagging trains models independently and averages them. Random Forest is bagging.

Boosting trains models sequentially and corrects mistakes. XGBoost is boosting.

## 4. Why does XGBoost perform so well?

It combines sequential learning, regularization, efficient optimization, missing-value handling, and strong tree-based modeling.

## 5. What is sequential learning?

Sequential learning means each model is trained after the previous model and uses information about previous errors.

## 6. What are weak learners?

Weak learners are simple models that perform slightly better than random guessing. Boosting combines many weak learners into a strong model.

## 7. Why is XGBoost better than Random Forest sometimes?

Random Forest averages independent trees. XGBoost builds trees that intentionally fix previous mistakes, which can reduce bias and improve performance.

## 8. What is regularization in XGBoost?

Regularization penalizes overly complex trees so the model does not memorize noise.

## 9. What is learning_rate?

`learning_rate` controls how much each new tree contributes. Smaller values make learning slower but often more stable.

## 10. What is gradient boosting?

Gradient boosting is boosting guided by the gradient of a loss function. Each new model moves predictions in the direction that reduces error.

## Practical

## 1. Important XGBoost hyperparameters

Important parameters include `n_estimators`, `learning_rate`, `max_depth`, `subsample`, `colsample_bytree`, `reg_alpha`, and `reg_lambda`.

## 2. What is n_estimators?

The number of boosting rounds or trees.

## 3. What is max_depth?

The maximum depth of each tree. Deeper trees capture more complexity but can overfit.

## 4. What is subsample?

The fraction of rows used for each tree. It adds randomness and helps reduce overfitting.

## 5. What is colsample_bytree?

The fraction of features used for each tree.

## 6. How do you tune XGBoost?

Tune learning rate and number of trees together, then tree depth, sampling, and regularization.

## 7. Why does smaller learning_rate help?

It makes each tree contribute less, so the model learns more carefully.

## 8. Can XGBoost overfit?

Yes. It is powerful and can overfit if trees are too deep, learning rate is too high, or regularization is weak.

## 9. How do you prevent overfitting?

Use smaller `learning_rate`, shallower trees, subsampling, column sampling, regularization, and early stopping.

## 10. Does XGBoost need feature scaling?

No. Tree-based XGBoost does not require feature scaling.

## Explainability

## 1. What is SHAP?

SHAP explains how each feature contributes to an individual prediction.

## 2. Why is SHAP important?

It helps make powerful models more understandable and trustworthy.

## 3. Difference between feature importance and SHAP?

Feature importance is global and model-level. SHAP can explain both global patterns and individual predictions.

## Business

## 1. Why is XGBoost widely used in Kaggle?

It performs extremely well on structured tabular data and has many tuning options.

## 2. Why do businesses use XGBoost?

It is accurate, scalable, strong on tabular data, and explainable with SHAP.

## 3. When should you avoid XGBoost?

Avoid it when interpretability, simplicity, or very fast training matters more than maximum performance.

## 4. When is interpretability more important than accuracy?

In regulated, high-stakes, or stakeholder-sensitive decisions where the business must explain why a prediction was made.
