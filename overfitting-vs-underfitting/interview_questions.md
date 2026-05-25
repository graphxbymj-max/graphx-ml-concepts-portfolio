# Overfitting vs Underfitting Interview Questions

## Conceptual Questions

### 1. What is overfitting?

Overfitting happens when a model learns the training data too specifically. It captures not only the real signal, but also noise, accidents, and quirks that do not generalize.

The easiest symptom is a large train/test gap: training performance is excellent, but validation or test performance is weaker.

### 2. What is underfitting?

Underfitting happens when a model is too simple to capture the real pattern in the data.

It usually produces poor training performance and poor test performance. The model is not memorizing. It is not learning enough in the first place.

### 3. What is generalization?

Generalization is a model's ability to perform well on new, unseen data.

In real ML systems, generalization matters more than training performance because production data is never exactly the same as the training set.

### 4. What is bias?

Bias is error from overly simple assumptions.

A high-bias model has a rigid view of the world. It may ignore important patterns because its structure is not flexible enough.

### 5. What is variance?

Variance is error from being too sensitive to the training data.

A high-variance model changes a lot when the training data changes. It may perform extremely well on one training set and poorly on new data.

### 6. What is the bias-variance tradeoff?

The bias-variance tradeoff is the balance between being too simple and being too reactive.

Low-complexity models often have high bias and low variance. High-complexity models often have low bias and high variance. Strong ML work is about finding the useful middle.

### 7. Why do complex models overfit?

Complex models have enough flexibility to fit tiny details in the training data. Some of those details are real signal, but some are noise.

If the model cannot tell the difference, it may treat random fluctuations as meaningful patterns.

### 8. Why do simple models underfit?

Simple models underfit because they cannot represent the shape of the true relationship.

For example, a decision tree with only one split cannot capture multiple interacting medical signals. It is forced to compress a complicated problem into one rule.

### 9. What are learning curves?

Learning curves show training and validation performance as the amount of training data increases.

They help diagnose whether a model is underfitting, overfitting, or likely to improve with more data.

### 10. What is regularization?

Regularization is a technique for controlling model complexity.

It discourages overly complicated solutions, such as extreme coefficients in linear models or excessively deep trees. Regularization helps reduce overfitting.

## Practical Questions

### 1. How do you detect overfitting?

Compare training performance with validation or test performance.

If training performance is much better than test performance, the model may be overfitting. Cross-validation, learning curves, and checking performance stability across splits can confirm the diagnosis.

### 2. How do you reduce overfitting?

Common approaches include:

- collect more data
- simplify the model
- add regularization
- reduce tree depth
- increase `min_samples_leaf`
- use cross-validation
- remove leakage
- use dropout or early stopping in neural networks
- improve feature selection

### 3. How do you fix underfitting?

Underfitting usually requires more learning capacity or better signal.

Options include:

- use a more flexible model
- reduce regularization
- add useful features
- add interaction terms
- train longer
- improve preprocessing

### 4. What is cross validation?

Cross-validation evaluates a model across multiple train/validation splits.

Instead of trusting one split, it rotates which part of the data acts as validation data. This gives a more reliable estimate of generalization.

### 5. Why is train accuracy not enough?

Train accuracy measures performance on data the model already saw.

A model can get high train accuracy by memorizing. The real question is whether it performs well on unseen data.

### 6. What is data leakage?

Data leakage happens when information from outside the training process sneaks into the model.

Examples include scaling before splitting, including future information, or using a feature that directly reveals the target. Leakage can make validation performance look unrealistically strong.

### 7. What is early stopping?

Early stopping stops training when validation performance stops improving.

It is common in boosting and neural networks. It prevents the model from continuing to optimize training performance after generalization has started to degrade.

### 8. How does `max_depth` affect overfitting?

In Decision Trees, `max_depth` controls how many layers of decisions the tree can make.

Higher depth allows more complex rules, which can improve learning but also increase overfitting. Lower depth adds restraint but may underfit if it is too low.

### 9. How does Ridge help?

Ridge regularization penalizes large coefficients using an L2 penalty.

It helps when a model is relying too heavily on individual features and creating unstable coefficient values.

### 10. How does Lasso help?

Lasso regularization penalizes coefficients using an L1 penalty.

It can shrink some coefficients all the way to zero, which makes it useful for feature selection and reducing model complexity.

## Business Questions

### 1. Why is overfitting dangerous in production?

Overfitting is dangerous because it creates false confidence.

The model may look excellent during development, but fail on future customers, patients, transactions, or market conditions. In production, that can lead to bad decisions at scale.

### 2. Why can high accuracy be misleading?

High accuracy can be misleading if it comes from training performance, data leakage, class imbalance, or a lucky validation split.

Accuracy must be interpreted with context: train/test gap, confusion matrix, class balance, business cost, and validation design.

### 3. How would you explain overfitting to a stakeholder?

I would say:

> The model may be learning the exact history we gave it instead of the repeatable patterns that will help with future cases.

Then I would show the train/test gap visually.

### 4. Why does generalization matter more than memorization?

Memorization helps only on examples the model already saw.

Generalization helps on future examples, which is where business value lives. A model is useful only if it can make reliable decisions when the answer is not already known.

