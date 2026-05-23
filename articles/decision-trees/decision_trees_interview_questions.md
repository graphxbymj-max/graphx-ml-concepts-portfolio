# Decision Trees Interview Questions Explained Intuitively

Decision Trees are popular in interviews because they test both machine learning intuition and practical modeling judgment.

They look simple, but they open the door to many important ideas:

- impurity
- information gain
- overfitting
- pruning
- feature importance
- interpretability
- ensembles

![Decision Tree Visualization](../../decision-trees/images/decision_tree_visualization.png)

## What is a Decision Tree?

A Decision Tree is a supervised learning model that predicts by asking a sequence of questions.

Each question splits the data. Each answer moves the observation down a branch. The final leaf gives the prediction.

## How does a Decision Tree make predictions?

It starts at the root node and follows split rules until it reaches a leaf node.

For classification, the leaf usually predicts the majority class among training examples that reached that leaf.

## What is Gini impurity?

Gini impurity measures how mixed the classes are inside a node.

A pure node has Gini impurity of 0.

A mixed node has higher impurity.

The tree chooses splits that reduce impurity.

## What is entropy?

Entropy measures uncertainty.

If a node contains a balanced mix of classes, entropy is high. If it contains only one class, entropy is 0.

## What is information gain?

Information gain measures how much entropy decreases after a split.

A high information gain means the split made the child nodes cleaner.

## Gini vs Entropy

Gini and entropy are both impurity measures.

Gini is faster and is the default in scikit-learn. Entropy comes from information theory.

In many practical datasets, the difference is small.

## Why do Decision Trees overfit?

Decision Trees can keep splitting until they memorize training examples.

This creates rules that are too specific and do not generalize well.

## What is max_depth?

`max_depth` limits the number of levels in the tree.

Lower depth creates a simpler model. Higher depth allows more complexity.

## What is min_samples_split?

`min_samples_split` controls how many samples are required before a node can be split.

Increasing it reduces overly tiny splits.

## What is min_samples_leaf?

`min_samples_leaf` controls the minimum number of samples required in a leaf node.

It prevents leaves from representing only a handful of records.

## What is pruning?

Pruning means simplifying the tree by removing branches that do not improve generalization.

In scikit-learn, cost-complexity pruning uses `ccp_alpha`.

## Do Decision Trees need feature scaling?

No.

Trees use threshold-based splits, not distance calculations. Scaling is usually unnecessary.

## Can Decision Trees handle categorical variables?

Conceptually yes, but scikit-learn requires numeric input.

In practice, we encode categorical variables using one-hot encoding or ordinal encoding.

## How do you interpret feature importance?

Feature importance tells us which features contributed most to reducing impurity across the tree.

![Feature Importance](../../decision-trees/images/feature_importance.png)

It is useful for explanation, but it does not prove causation.

## Decision Trees vs Logistic Regression

Logistic Regression learns a linear relationship between features and log-odds.

Decision Trees learn rule-based, nonlinear splits.

Logistic Regression is often more stable. Decision Trees are often easier to explain visually.

## Decision Trees vs Random Forest

A Random Forest trains many trees and averages their predictions.

A single Decision Tree is interpretable but unstable. A Random Forest is usually more accurate and robust, but less transparent.

## Business Interpretation

To a stakeholder, a Decision Tree can be explained as:

> A structured checklist that uses customer information to reach a prediction.

This makes Decision Trees useful when the business needs a model that can be discussed, audited, and translated into rules.

## When would you avoid a single Decision Tree?

Avoid a single tree when:

- the data is very noisy
- maximum accuracy matters more than interpretability
- small model changes would create operational risk
- an ensemble model is acceptable

## Final Interview Takeaway

A strong Decision Tree answer should mention both sides:

- Decision Trees are intuitive and interpretable.
- Decision Trees can overfit and become unstable.

That balance is what interviewers are usually looking for.
