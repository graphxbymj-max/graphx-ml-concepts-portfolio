# Feature Engineering Interview Questions and Answers

## Conceptual

## 1. What is feature engineering?

Feature engineering is the process of transforming raw data into useful signals that machine learning models can learn from.

## 2. Why is feature engineering important?

Better features can make patterns easier for models to discover. Often, better features improve performance more than switching algorithms.

## 3. Raw features vs engineered features?

Raw features come directly from the dataset. Engineered features are created by transforming, combining, or extracting information from raw features.

## 4. What is feature scaling?

Scaling changes numerical feature ranges so models sensitive to magnitude can train better.

## 5. Normalization vs standardization?

Normalization usually rescales values to a fixed range such as 0 to 1. Standardization centers values around 0 with standard deviation 1.

## 6. What is one-hot encoding?

One-hot encoding converts categories into binary indicator columns.

## 7. What is label encoding?

Label encoding converts categories into integer labels. It should be used carefully because it can imply order.

## 8. What is skewness?

Skewness describes an asymmetric distribution with a long tail.

## 9. Why use log transformation?

Log transformation can reduce skewness and make extreme values less dominant.

## 10. What is feature selection?

Feature selection chooses the most useful features and removes irrelevant or noisy ones.

## Practical

## 1. How do you handle missing values?

Use strategies such as median imputation, mode imputation, explicit missing categories, dropping columns, or model-based imputation.

## 2. When should you scale features?

Scale features for models such as Logistic Regression, KNN, SVM, PCA, and neural networks.

## 3. Why don’t tree models need scaling?

Trees split on thresholds, so feature magnitude does not affect distance or gradient optimization.

## 4. How do you engineer date features?

Extract month, quarter, day of week, weekend flags, season, recency, or time gaps.

## 5. How do you create interaction features?

Combine two or more variables, such as price per guest or lead time multiplied by stay length.

## 6. How do you identify useful features?

Use domain knowledge, EDA, feature importance, validation performance, and stability checks.

## 7. What is multicollinearity?

Multicollinearity means features are highly correlated with each other, which can make linear model coefficients unstable.

## 8. What is dimensionality reduction?

Dimensionality reduction compresses many features into fewer representations while trying to preserve signal.

## 9. What is PCA intuitively?

PCA rotates the feature space to find directions that capture the most variation.

## 10. What is target leakage?

Target leakage happens when features contain information that would not be available at prediction time.

## Business

## 1. Why is feature engineering often more important than model choice?

Models can only learn from the signals they are given. Better features give the model better signal.

## 2. How would you explain feature engineering to a stakeholder?

Feature engineering turns raw business data into meaningful clues the model can use.

## 3. Risks of poor feature engineering?

Poor features can create noise, bias, leakage, instability, and misleading model performance.

## 4. When can feature engineering hurt performance?

It can hurt when features are noisy, leaky, redundant, or overfit to validation data.
