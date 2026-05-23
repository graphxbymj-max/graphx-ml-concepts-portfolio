# Decision Tree Interview Questions and Answers

## Conceptual Questions

## 1. What is a Decision Tree?

A Decision Tree is a supervised machine learning model that makes predictions by splitting data into smaller groups using feature-based questions.

It looks like a flowchart: start at the top, answer questions, follow branches, and end at a prediction.

## 2. How does a Decision Tree make predictions?

A Decision Tree starts at the root node and checks a condition such as:

> Is previous campaign outcome equal to success?

Based on the answer, the observation moves left or right. This continues until it reaches a leaf node, where the model outputs a class.

## 3. What is a root node?

The root node is the first split in the tree. It contains the full training dataset before any decisions have been made.

## 4. What is a leaf node?

A leaf node is an ending point in the tree. It gives the final prediction.

## 5. What is a split?

A split is a rule that divides data into two or more groups. In scikit-learn Decision Trees, each split is binary.

## 6. What is Gini impurity?

Gini impurity measures how mixed the classes are inside a node.

A Gini score of 0 means the node is pure. Higher values mean the node contains a stronger mix of classes.

## 7. What is entropy?

Entropy measures uncertainty or disorder in a node.

If a node has a mix of classes, entropy is higher. If a node is pure, entropy is 0.

## 8. What is information gain?

Information gain measures how much uncertainty is reduced after a split.

A good split produces high information gain because it creates cleaner child nodes.

## 9. Difference between Gini and entropy?

Both measure impurity.

Gini is slightly faster to compute and is the default in scikit-learn. Entropy is based on information theory and uses logarithms.

In many practical projects, they produce similar trees.

## 10. Why do Decision Trees overfit?

Decision Trees overfit because they can keep splitting until they memorize tiny patterns or noise in the training data.

A fully grown tree may perform extremely well on training data but poorly on new data.

## Practical Questions

## 1. How do you control overfitting in Decision Trees?

Common methods include:

- limit `max_depth`
- increase `min_samples_split`
- increase `min_samples_leaf`
- use cost-complexity pruning with `ccp_alpha`
- use cross-validation
- switch to ensembles such as Random Forest

## 2. What is max_depth?

`max_depth` controls how many levels the tree can grow.

Lower depth creates simpler trees. Higher depth allows more complex patterns but increases overfitting risk.

## 3. What is min_samples_split?

`min_samples_split` is the minimum number of samples required to split an internal node.

Increasing it prevents the model from creating splits based on very small groups.

## 4. What is min_samples_leaf?

`min_samples_leaf` is the minimum number of samples allowed in a final leaf node.

It helps prevent overly specific rules such as a leaf based on only one or two records.

## 5. What is pruning?

Pruning means simplifying a tree by removing branches that do not improve generalization.

In scikit-learn, cost-complexity pruning is controlled with `ccp_alpha`.

## 6. Do Decision Trees need feature scaling?

No.

Decision Trees split features using thresholds. They do not rely on distance or gradient magnitude, so scaling is usually unnecessary.

## 7. Can Decision Trees handle categorical variables?

Conceptually, yes. Practically, scikit-learn Decision Trees require numeric input, so categorical variables are usually one-hot encoded or ordinal encoded.

## 8. How do you interpret feature importance?

Feature importance shows which features reduced impurity the most across the tree.

It is useful for interpretation, but it does not prove causation.

## Business Questions

## 1. How would you explain a Decision Tree to a non-technical stakeholder?

I would say:

> A Decision Tree is like a structured checklist. It asks a sequence of questions and uses the answers to reach a prediction.

## 2. Why are Decision Trees useful in business?

They are easy to explain, quick to train, and useful for turning data patterns into understandable decision rules.

## 3. What are the risks of using Decision Trees?

The biggest risks are overfitting, instability, and oversimplifying complex business behavior.

## 4. When would you avoid Decision Trees?

I would avoid a single Decision Tree when maximum predictive accuracy is the main goal, when the data is very noisy, or when the model must produce highly stable predictions.

## Comparison With Logistic Regression

Logistic Regression learns a linear relationship between features and log-odds. It is excellent when interpretability and probability estimates matter.

Decision Trees learn nonlinear rules automatically. They are easier to visualize as business rules but can overfit more easily.

## Comparison With Random Forest

A Random Forest combines many Decision Trees to reduce instability and improve performance.

A single Decision Tree is easier to explain. A Random Forest is usually more accurate and robust.

## When to Use Decision Trees vs Ensembles

Use a single Decision Tree when:

- interpretability is the top priority
- the audience needs simple rules
- the model is used for teaching or baseline analysis

Use ensembles when:

- predictive performance matters more
- the data is noisy
- a single tree is unstable
- the project can tolerate less transparent models
