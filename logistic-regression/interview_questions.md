# Logistic Regression Interview Questions and Answers

## 1. What is Logistic Regression?

Logistic Regression is a supervised machine learning algorithm used for classification problems, especially binary classification.

Instead of predicting a continuous number, it predicts the probability that an observation belongs to a class.

Example:

> There is a 72% chance this employee will leave the company.

## 2. Why is it called regression if it is used for classification?

It is called regression because the model learns a regression-style equation with coefficients.

The difference is that Logistic Regression applies the sigmoid function to convert the output into a probability between 0 and 1.

So the model learns a numeric score, converts it into a probability, and then classifies using a threshold.

## 3. What is the sigmoid function?

The sigmoid function converts any real number into a value between 0 and 1.

That makes it useful for probability prediction.

If the model's raw score is very high, sigmoid moves the probability close to 1. If the raw score is very low, sigmoid moves the probability close to 0.

## 4. What is log odds?

Odds compare the probability that something happens to the probability that it does not happen.

Log odds are the natural log of those odds.

Logistic Regression models log odds as a linear combination of features.

In simple terms:

> The model learns how each feature pushes the odds of the positive class up or down.

## 5. What is a probability threshold?

A probability threshold is the cutoff used to convert predicted probabilities into class labels.

The default threshold is usually `0.5`.

Example:

- probability >= 0.5 means predict attrition
- probability < 0.5 means predict no attrition

Changing the threshold changes precision and recall.

## 6. What is a confusion matrix?

A confusion matrix is a table that compares actual classes with predicted classes.

For binary classification, it contains:

- true positives
- true negatives
- false positives
- false negatives

In this project:

- true positive: employee left and model predicted left
- true negative: employee stayed and model predicted stayed
- false positive: employee stayed but model predicted left
- false negative: employee left but model predicted stayed

## 7. Accuracy vs precision vs recall vs F1

Accuracy measures the percentage of all predictions that were correct.

Precision measures how many predicted positives were actually positive.

Recall measures how many actual positives the model successfully found.

F1-score balances precision and recall into one metric.

Use accuracy carefully when classes are imbalanced.

## 8. When is recall more important than precision?

Recall is more important when missing a positive case is costly.

Examples:

- disease detection
- fraud detection
- employee attrition risk
- loan default risk

In employee attrition, low recall means the company misses employees who may leave.

## 9. When is precision more important than recall?

Precision is more important when false alarms are costly.

Examples:

- sending expensive retention offers
- flagging legitimate transactions as fraud
- approving a limited manual review queue

High precision means that when the model predicts a positive case, it is more likely to be correct.

## 10. What is ROC-AUC?

ROC-AUC measures how well the model separates the positive class from the negative class across different thresholds.

AUC values:

- `0.5`: close to random guessing
- `0.7` to `0.8`: useful signal
- `0.8+`: strong separation

ROC-AUC is useful because it evaluates ranking ability, not just one threshold.

## 11. What is class imbalance?

Class imbalance happens when one class appears much more often than another.

In this project, most employees stayed and fewer employees left.

That means a model can get high accuracy by mostly predicting the majority class.

## 12. How do you handle class imbalance?

Common approaches include:

- use better metrics such as recall, precision, F1, and ROC-AUC
- tune the probability threshold
- use class weights
- oversample the minority class
- undersample the majority class
- collect more minority-class examples

The right approach depends on the business cost of different mistakes.

## 13. What assumptions does Logistic Regression make?

Logistic Regression assumes:

- the target is categorical
- observations are independent
- features have a roughly linear relationship with log-odds
- there is limited multicollinearity among features
- there are no extreme influential outliers
- the dataset is large enough for stable coefficient estimates

These assumptions do not need to be perfect, but they should be considered.

## 14. Difference between Linear and Logistic Regression

Linear Regression predicts a continuous value.

Example:

> Predict house price.

Logistic Regression predicts a probability for a class.

Example:

> Predict whether an employee will leave.

Linear Regression output can be any number. Logistic Regression output is transformed into a probability between 0 and 1.

## 15. Why do we scale numerical features for Logistic Regression?

Scaling helps Logistic Regression train more smoothly and makes coefficients easier to compare.

Features measured on large scales can otherwise dominate the optimization process.

## 16. What does a positive coefficient mean?

A positive coefficient means that as the feature increases, the log-odds of the positive class increase, assuming other features are held constant.

In this project, a positive coefficient pushes the prediction toward attrition.

## 17. What does a negative coefficient mean?

A negative coefficient means that as the feature increases, the log-odds of the positive class decrease, assuming other features are held constant.

In this project, a negative coefficient pushes the prediction toward staying.

## 18. What is an odds ratio?

An odds ratio is calculated by exponentiating a Logistic Regression coefficient.

If the odds ratio is above 1, the feature increases the odds of the positive class.

If the odds ratio is below 1, the feature decreases the odds of the positive class.

## 19. Business interpretation: what does recall mean in this project?

Recall answers:

> Of all employees who actually left, how many did the model identify as likely to leave?

High recall is useful when HR wants to catch as many at-risk employees as possible.

## 20. Business interpretation: what does precision mean in this project?

Precision answers:

> Of all employees flagged as likely to leave, how many actually left?

High precision is useful when HR has limited time or budget for retention interventions.

## 21. Business interpretation: should HR always use a 0.5 threshold?

No.

The `0.5` threshold is only a default. HR may choose a lower threshold if missing at-risk employees is expensive.

Threshold choice should reflect business priorities.

## 22. Can Logistic Regression prove why employees leave?

No.

Logistic Regression can show patterns and associations, but it does not prove causation.

To understand why employees leave, the company may need experiments, surveys, interviews, or causal analysis.

## 23. Why is Logistic Regression a good baseline model?

It is:

- simple
- fast
- interpretable
- probability-based
- widely understood
- useful for many binary classification problems

Even when advanced models are tested later, Logistic Regression is a strong first benchmark.

