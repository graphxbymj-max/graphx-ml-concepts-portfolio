# Cross Validation Interview Questions

## Conceptual Questions

### 1. What is Cross Validation?

Cross Validation is a model evaluation technique where the model is trained and validated multiple times on different splits of the data.

Instead of trusting one train-test split, Cross Validation rotates validation responsibility across folds and gives a distribution of scores.

### 2. Why is train-test split not enough?

A single train-test split can be lucky or unlucky.

If the test set is unusually easy, the model may look stronger than it is. If the test set is unusually hard, the model may look weaker than it is. Cross Validation gives a broader estimate of performance.

### 3. What is KFold Cross Validation?

KFold splits the dataset into `k` folds.

The model trains on `k-1` folds and validates on the remaining fold. This repeats until every fold has served as validation data.

### 4. What is Stratified KFold?

Stratified KFold is a version of KFold that preserves the target class distribution in each fold.

It is especially useful for classification problems with imbalanced classes.

### 5. Why does Cross Validation improve trust?

Cross Validation improves trust because it tests the model across multiple partitions of the data.

If the model performs consistently across folds, we have stronger evidence that it is learning patterns that generalize.

### 6. What is variance across folds?

Variance across folds describes how much model performance changes from one validation fold to another.

Low variance suggests stable performance. High variance suggests the model may be sensitive to the exact data split.

### 7. What does a high standard deviation mean?

A high standard deviation means fold scores are spread out.

This is a warning sign. It may indicate an unstable model, too little data, class imbalance, outliers, or a validation setup that is not robust.

### 8. Why does model stability matter?

Model stability matters because production data changes.

A model that performs well only on one split may fail when customer mix, seasonality, or behavior changes. Stable validation performance gives more confidence in future reliability.

### 9. What is validation data?

Validation data is data used to evaluate and tune a model during development.

It helps compare models, tune hyperparameters, and detect overfitting before the final test set is used.

### 10. Difference between train, validation, and test sets?

Training data teaches the model.

Validation data helps choose models and hyperparameters.

Test data is held back for the final unbiased evaluation after decisions have been made.

## Practical Questions

### 1. How do you implement Cross Validation?

In scikit-learn, common tools include:

- `cross_val_score`
- `KFold`
- `StratifiedKFold`
- `GridSearchCV`
- `RandomizedSearchCV`

For classification, `StratifiedKFold` is often a strong default.

### 2. When should you use Stratified KFold?

Use Stratified KFold when the target is categorical, especially when classes are imbalanced.

It keeps each fold's class distribution close to the overall dataset distribution.

### 3. What is GridSearchCV?

`GridSearchCV` tests every combination in a hyperparameter grid using Cross Validation.

It returns the parameter set with the best average validation performance across folds.

### 4. What is RandomizedSearchCV?

`RandomizedSearchCV` samples a fixed number of hyperparameter combinations from distributions or lists.

It is useful when the search space is large and testing every combination would be expensive.

### 5. Why is tuning with Cross Validation important?

Tuning on one split can choose hyperparameters that perform well only on that split.

Cross-validated tuning searches for hyperparameters that work consistently across multiple validation folds.

### 6. How do you detect instability?

Look at:

- high standard deviation across folds
- large difference between minimum and maximum fold score
- unstable results across random seeds
- large train/validation gaps
- learning curves with noisy validation performance

### 7. What are learning curves?

Learning curves show training and validation performance as the training set size increases.

They help diagnose underfitting, overfitting, and whether more data may improve validation performance.

### 8. What are validation curves?

Validation curves show training and validation performance as one hyperparameter changes.

They help reveal whether increasing model complexity improves generalization or causes overfitting.

### 9. How does Cross Validation help detect overfitting?

Cross Validation can compare training scores and validation scores across folds.

If training performance is high while validation performance is much lower, the model may be overfitting.

### 10. What are the limitations of Cross Validation?

Cross Validation is powerful, but not perfect.

Limitations include:

- higher computation cost
- leakage risk if preprocessing is done incorrectly
- not always suitable for time series without special splitting
- can still be optimistic if the dataset is not representative
- final test evaluation is still needed

## Business Questions

### 1. Why is robust evaluation important in production?

Production models influence real decisions.

If evaluation is weak, teams may deploy a model that looked good during development but fails on future customers, patients, transactions, or market conditions.

### 2. Why can one train-test split be misleading?

One split may not represent the full variety of future data.

It can make a model look better or worse depending on which examples landed in the test set.

### 3. How would you explain Cross Validation to a stakeholder?

I would say:

> Instead of judging the model from one test, we test it several times on different slices of the data to see whether its performance is consistent.

Then I would show the average score and the variation across folds.

### 4. Why does model reliability matter more than one good score?

One good score may be luck.

Reliability means the model performs consistently across different samples. In business, consistency is what makes a model trustworthy enough to guide decisions.

