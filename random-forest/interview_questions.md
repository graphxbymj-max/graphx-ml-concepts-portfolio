# Random Forest Interview Questions and Answers

## Conceptual Questions

## 1. What is Random Forest?

Random Forest is an ensemble machine learning algorithm that trains many Decision Trees and combines their predictions.

For classification, the trees vote. The class with the most votes becomes the final prediction.

## 2. Why is it called Random Forest?

It is a forest because it contains many trees. It is random because each tree is trained on a random bootstrap sample, and each split considers a random subset of features.

## 3. What is ensemble learning?

Ensemble learning combines multiple models to create a stronger model.

The idea is simple: many imperfect models can often make a better collective decision than one model alone.

## 4. What is bagging?

Bagging means bootstrap aggregating.

It trains models on different bootstrap samples and then averages or votes across their predictions.

## 5. Why does Random Forest reduce overfitting?

A single Decision Tree can overfit because it is sensitive to the training data.

Random Forest reduces overfitting by averaging many trees. Individual tree mistakes often cancel out.

## 6. Difference between Decision Tree and Random Forest?

A Decision Tree is one model. It is easy to interpret but unstable.

Random Forest is many Decision Trees working together. It is usually more accurate and stable but less transparent.

## 7. What is bootstrap sampling?

Bootstrap sampling means sampling rows from the training data with replacement.

Each tree gets a slightly different dataset.

## 8. What is feature randomness?

Feature randomness means each split considers only a random subset of features.

This keeps trees from all becoming too similar.

## 9. What is feature importance?

Feature importance estimates which features contributed most to the forest's predictions.

It is useful, but it does not prove causation.

## 10. Why are Random Forests powerful?

They are powerful because they combine flexibility, strong performance, low preprocessing needs, and robustness.

## Practical Questions

## 1. What is n_estimators?

`n_estimators` is the number of trees in the forest.

More trees usually improve stability, but they increase training time.

## 2. What is max_depth?

`max_depth` limits how deep each tree can grow.

It controls complexity and helps reduce overfitting.

## 3. What is min_samples_split?

`min_samples_split` is the minimum number of samples required to split a node.

Higher values make trees less specific.

## 4. Does Random Forest need feature scaling?

No. Random Forest uses tree splits, not distance calculations.

## 5. Can Random Forest handle missing values?

Some implementations can, but scikit-learn's classic RandomForestClassifier expects missing values to be handled before training.

## 6. How do you tune Random Forest?

Tune parameters such as `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, and `max_features`.

## 7. What are OOB samples?

OOB means out-of-bag.

These are training rows not included in a tree's bootstrap sample.

## 8. What is OOB score?

OOB score estimates model performance using out-of-bag samples, giving a built-in validation signal.

## Business Questions

## 1. How would you explain Random Forest to a stakeholder?

I would say: instead of trusting one decision tree, we ask many slightly different trees to vote. The crowd is usually more reliable than one tree alone.

## 2. Why is Random Forest widely used in industry?

It performs well on many tabular datasets, handles nonlinear relationships, needs little preprocessing, and is more stable than a single tree.

## 3. When should you avoid Random Forest?

Avoid it when you need a very small model, very fast predictions, or highly transparent rules.

## 4. When would you use XGBoost instead?

Use XGBoost when you need stronger performance on tabular data and can invest in more careful tuning.
