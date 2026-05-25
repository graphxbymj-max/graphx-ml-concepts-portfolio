# Evaluation Metrics Interview Questions Explained Like a Real ML Engineer

Evaluation metrics are where machine learning stops being a modeling exercise and becomes a decision system.

Interviewers ask about accuracy, precision, recall, F1-score, ROC-AUC, and PR curves because they want to know whether you understand model usefulness.

A weak answer defines the formula.

A strong answer explains when the metric matters, what failure it catches, and what business mistake it represents.

## What is a confusion matrix?

A confusion matrix shows how predicted classes compare with actual classes.

It has four outcomes:

- true positives
- true negatives
- false positives
- false negatives

It is useful because it shows the type of mistakes the model makes.

In churn prediction, false positives waste retention budget. False negatives miss customers who actually leave.

## What is accuracy?

Accuracy is the percentage of predictions the model got right.

It is simple and useful when classes are balanced and all mistakes have similar cost.

But accuracy can be dangerous when the target is imbalanced or when one mistake matters more than another.

## Why can accuracy be misleading?

Accuracy can hide failure on the minority class.

If 99% of transactions are legitimate, a model can predict "legitimate" every time and achieve 99% accuracy.

That model catches no fraud.

In business terms, it looks good while failing the mission.

## What is precision?

Precision answers:

> When the model predicts positive, how often is it right?

Precision matters when false positives are expensive.

In spam filtering, high precision means emails marked as spam are usually spam. In churn prediction, high precision means customers flagged for retention are truly at risk.

## What is recall?

Recall answers:

> Of all actual positive cases, how many did the model catch?

Recall matters when false negatives are expensive.

In medical diagnosis, recall is critical because missing a sick patient can be dangerous. In fraud detection, recall matters because missed fraud can create direct loss.

## What is F1-score?

F1-score is the harmonic mean of precision and recall.

It is useful when you want a single metric that balances false positives and false negatives.

F1 is strict. A model cannot get a strong F1-score by having great precision and terrible recall, or great recall and terrible precision.

## What is ROC-AUC?

ROC-AUC measures how well the model separates positive and negative classes across thresholds.

It is often interpreted as ranking ability:

> How often does the model rank a random positive example higher than a random negative example?

ROC-AUC is useful, but it should not be the only metric for imbalanced data.

## What is a Precision-Recall curve?

A PR curve shows precision and recall across thresholds.

It focuses on the positive class, which makes it especially useful when positives are rare.

For fraud, disease, churn, and conversion problems, PR curves can be more informative than ROC curves.

## What is threshold tuning?

Threshold tuning changes the cutoff used to convert probabilities into class predictions.

The default threshold is often 0.5, but that is not always the right business decision.

Lower thresholds catch more positives and usually increase recall.

Higher thresholds create fewer positive predictions and usually increase precision.

## What is class imbalance?

Class imbalance happens when one class is much more common than another.

Examples:

- fraud vs non-fraud
- disease vs no disease
- churn vs stay
- conversion vs no conversion

Imbalance makes accuracy less reliable because majority-class predictions can dominate the score.

## When should you prioritize recall?

Prioritize recall when missing positive cases is expensive or dangerous.

Examples:

- medical screening
- fraud detection
- safety alerts
- churn prevention when lost customers are costly

Recall is about catching as many true positives as possible.

## When should you prioritize precision?

Prioritize precision when false positives are expensive.

Examples:

- spam filtering
- fraud investigation with limited analysts
- retention campaigns with limited budget
- legal or compliance reviews

Precision is about making sure positive predictions are trustworthy.

## Why does threshold matter?

The threshold controls model behavior.

A model does not only produce labels. It often produces probabilities. The threshold decides when a probability becomes an action.

Changing the threshold changes precision, recall, false positives, false negatives, and business cost.

## How do you evaluate imbalanced datasets?

Do not rely only on accuracy.

Use:

- confusion matrix
- precision
- recall
- F1-score
- ROC-AUC
- PR curve
- average precision
- threshold analysis
- business-cost analysis

Also inspect class distribution and calibration if probabilities are used for decisions.

## Difference between ROC and PR curves?

ROC curves plot true positive rate against false positive rate.

PR curves plot precision against recall.

ROC curves measure separation across both classes. PR curves focus on positive-class performance.

For imbalanced datasets, PR curves are often more revealing.

## What does AUC mean?

AUC is area under a curve.

For ROC-AUC, it summarizes how well the model ranks positives above negatives across thresholds.

A higher AUC means stronger class separation.

## How do you choose evaluation metrics?

Start with the business problem.

Ask:

- Which mistake costs more?
- Is the target imbalanced?
- Are we ranking or making hard decisions?
- Is there a capacity limit?
- Will probabilities drive actions?

Then choose metrics that match the decision.

## Why is F1-score useful?

F1-score is useful when both precision and recall matter.

It gives one balanced score while punishing models that perform poorly on either precision or recall.

## What are false positives?

False positives are cases where the model predicts positive but the actual class is negative.

In churn, this means flagging a customer as likely to leave when they would have stayed.

## What are false negatives?

False negatives are cases where the model predicts negative but the actual class is positive.

In churn, this means missing a customer who actually leaves.

## Difference between MAE and RMSE?

MAE is the average absolute error.

RMSE is the square root of mean squared error. It penalizes large errors more strongly.

MAE is easier to explain. RMSE is useful when large mistakes are especially costly.

## What does R2 mean?

R2 measures how much variance in the target is explained by the model compared with a baseline.

It is useful, but it should be interpreted with domain context and error metrics like MAE or RMSE.

## How would you explain precision vs recall to a stakeholder?

Precision means:

> When we act, how often are we right?

Recall means:

> Of all the cases we should have acted on, how many did we catch?

That explanation usually lands better than formulas.

## Why can "99% accuracy" be dangerous?

Because it may hide failure on the rare class.

If the rare class is the business-critical class, the model can look excellent while missing the entire point.

## Why do evaluation metrics matter in production?

Production models guide real decisions.

Wrong metrics can optimize the wrong behavior. A model may look strong during development but waste money, miss risk, or damage trust after deployment.

Metrics matter because they define what success means.

