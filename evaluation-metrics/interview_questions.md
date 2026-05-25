# Evaluation Metrics Interview Questions

## Conceptual Questions

### 1. What is a confusion matrix?

A confusion matrix shows how a classification model's predictions compare with actual outcomes.

It contains true positives, true negatives, false positives, and false negatives. It is the foundation for accuracy, precision, recall, and F1-score.

### 2. What is accuracy?

Accuracy is the proportion of total predictions the model got right.

It is useful when classes are balanced and mistake costs are similar.

### 3. Why can accuracy be misleading?

Accuracy can be misleading when the dataset is imbalanced.

If 99% of cases are negative, a model can predict negative for everyone and still get 99% accuracy while catching none of the positive cases.

### 4. What is precision?

Precision answers:

> When the model predicts positive, how often is it correct?

Precision matters when false positives are expensive.

### 5. What is recall?

Recall answers:

> Of all actual positive cases, how many did the model catch?

Recall matters when false negatives are expensive.

### 6. What is F1-score?

F1-score is the harmonic mean of precision and recall.

It is useful when both false positives and false negatives matter and you want one balanced metric.

### 7. What is ROC-AUC?

ROC-AUC measures how well a model separates positive and negative classes across thresholds.

It can be interpreted as the probability that the model ranks a random positive example higher than a random negative example.

### 8. What is a PR curve?

A Precision-Recall curve shows the tradeoff between precision and recall across thresholds.

It is especially useful for imbalanced classification because it focuses on positive-class performance.

### 9. What is threshold tuning?

Threshold tuning means changing the probability cutoff used to convert probabilities into class predictions.

The default is often `0.5`, but the best threshold depends on business cost and risk tolerance.

### 10. What is class imbalance?

Class imbalance happens when one class is much more common than another.

Examples include fraud detection, rare disease diagnosis, churn prediction, and conversion prediction.

## Practical Questions

### 1. When should you prioritize recall?

Prioritize recall when false negatives are expensive or dangerous.

Examples include cancer screening, fraud detection, safety alerts, and churn retention when missing a churner is costly.

### 2. When should you prioritize precision?

Prioritize precision when false positives are expensive.

Examples include spam filtering, fraud investigations with limited analyst capacity, and retention offers with limited budget.

### 3. Why does threshold matter?

The threshold controls how aggressive the model is.

Lower thresholds usually increase recall and false positives. Higher thresholds usually increase precision and false negatives.

### 4. How do you evaluate imbalanced datasets?

Use metrics beyond accuracy:

- confusion matrix
- precision
- recall
- F1-score
- ROC-AUC
- Precision-Recall curve
- average precision
- business-cost analysis

### 5. Difference between ROC and PR curves?

ROC curves plot true positive rate against false positive rate.

PR curves plot precision against recall.

PR curves are often more informative when the positive class is rare.

### 6. What does AUC mean?

AUC summarizes curve performance across thresholds.

For ROC-AUC, it measures how well the model ranks positives above negatives.

### 7. How do you choose evaluation metrics?

Start with the business problem.

Ask which mistake is more costly: false positives or false negatives. Then choose metrics that reflect that cost.

### 8. Why is F1-score useful?

F1-score is useful when precision and recall both matter.

It avoids rewarding models that are excellent at one while terrible at the other.

### 9. What are false positives?

False positives are cases where the model predicts positive but the actual class is negative.

In churn, this means flagging a loyal customer as likely to churn.

### 10. What are false negatives?

False negatives are cases where the model predicts negative but the actual class is positive.

In churn, this means missing a customer who actually leaves.

## Regression Questions

### 1. Difference between MAE and RMSE?

MAE is the average absolute error.

RMSE is the square root of mean squared error and penalizes large errors more strongly.

### 2. When is RMSE preferred?

RMSE is preferred when large errors are especially harmful and should be penalized more.

### 3. What does R2 mean?

R2 measures how much variance in the target is explained by the model compared with a simple baseline.

## Business Questions

### 1. Why is evaluation context-dependent?

Different businesses care about different mistakes.

A fraud team, medical team, spam team, and sales team may all need different metrics because their costs and risks differ.

### 2. How would you explain precision vs recall to a stakeholder?

Precision means: when we act, how often are we right?

Recall means: of all the cases we should have acted on, how many did we catch?

### 3. Why can "99% accuracy" be dangerous?

It can hide total failure on the minority class.

If the rare class is the business-critical class, high accuracy can create false confidence.

### 4. Why do evaluation metrics matter in production?

Production models drive decisions.

Wrong metrics can lead teams to deploy models that look good in notebooks but fail in real workflows.

