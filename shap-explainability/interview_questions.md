# SHAP & Explainability Interview Questions and Answers

## Conceptual Questions

### 1. What is explainable AI?

Explainable AI is the practice of making model behavior understandable to humans. It helps teams understand what a model learned, which features influence predictions, and why individual predictions happen.

### 2. Why do black-box models create problems?

Black-box models create problems because they can be accurate without being understandable. In high-stakes domains like healthcare, finance, hiring, and insurance, stakeholders need to know why a prediction happened before trusting or acting on it.

### 3. What is SHAP?

SHAP is an explainability method that assigns each feature a contribution value for a model prediction. It explains how much each feature pushed the prediction higher or lower relative to a baseline.

### 4. What are SHAP values?

SHAP values are feature-level contribution scores. A positive SHAP value pushes the prediction upward for the class being explained. A negative SHAP value pushes it downward.

### 5. What is local explainability?

Local explainability explains one individual prediction. It answers questions like: why was this customer predicted to churn, or why was this patient predicted high-risk?

### 6. What is global explainability?

Global explainability explains model behavior across many predictions. It shows which features matter most overall and how feature values generally affect predictions.

### 7. Why is interpretability important?

Interpretability matters because people need to trust, audit, debug, and govern model decisions. It is especially important when predictions affect people or business risk.

### 8. What is feature importance?

Feature importance ranks features by how much they influence the model. Traditional importance is usually global, while SHAP can provide both global and local importance.

### 9. What is a baseline prediction in SHAP?

The baseline prediction is the model's average starting point before considering a specific row's features. SHAP values explain how each feature moves the prediction away from that baseline.

### 10. Why is explainability important in production AI?

Production models drift, fail, interact with changing users, and face stakeholder scrutiny. Explainability helps teams debug behavior, monitor trust, detect suspicious patterns, and respond to business or regulatory questions.

## Practical Questions

### 1. How do you use SHAP?

Train a model, create a SHAP explainer for that model, calculate SHAP values for data points, then visualize global and local explanations with summary, bar, dependence, waterfall, or force plots.

### 2. How do you explain individual predictions?

Use local SHAP values. Start from the baseline prediction, then show which features pushed the prediction up or down and by how much.

### 3. What are SHAP summary plots?

A SHAP summary plot shows each feature's impact across many observations. It combines feature importance, direction, spread, and value patterns in one visual.

### 4. What are SHAP dependence plots?

Dependence plots show how a feature's value relates to its SHAP contribution. They can reveal nonlinear behavior, thresholds, and interactions.

### 5. How can SHAP help debug models?

SHAP helps inspect wrong predictions, suspicious feature reliance, unexpected interactions, and model shortcuts. It can show whether a model is making mistakes for understandable reasons or questionable ones.

### 6. How can SHAP detect bias?

SHAP can reveal whether sensitive attributes or proxy variables strongly influence predictions. It can also help compare explanation patterns across subgroups. But SHAP alone does not prove fairness.

### 7. Difference between SHAP and traditional feature importance?

Traditional feature importance usually gives one global ranking. SHAP explains both global behavior and individual predictions, including direction and magnitude of feature contributions.

### 8. Why are tree models harder to interpret?

Tree ensembles combine many trees. Each individual split may be simple, but the final prediction comes from many interactions across many trees, making the overall decision path hard to inspect manually.

### 9. What are limitations of SHAP?

SHAP can be computationally expensive, difficult to interpret with correlated features, and easy to overread as causal. It explains the model, not necessarily the real world.

### 10. When should businesses prioritize interpretability?

Businesses should prioritize interpretability when decisions are high-stakes, regulated, customer-facing, ethically sensitive, or difficult to reverse.

## Advanced Questions

### 1. What is the game theory intuition behind SHAP?

SHAP is inspired by Shapley values from cooperative game theory. The idea is to fairly distribute credit for a prediction among features based on their contribution across possible feature coalitions.

### 2. Difference between SHAP and LIME?

LIME explains predictions by fitting a simple local surrogate model around one prediction. SHAP uses contribution values grounded in Shapley-value intuition and often provides more consistent additive explanations.

### 3. Difference between local and global explanations?

Local explanations describe one prediction. Global explanations describe the model's behavior across many predictions.

### 4. Why can correlated features complicate SHAP?

When features are correlated, credit can be split in ways that are hard to interpret. Two features may carry similar information, so their individual SHAP values may not map cleanly to separate real-world causes.

## Business Questions

### 1. Why does explainability matter in finance and healthcare?

Finance and healthcare decisions affect people's money, treatment, access, and safety. Stakeholders need explanations for trust, compliance, auditability, and ethical decision-making.

### 2. How would you explain SHAP to a stakeholder?

I would say: SHAP shows which factors pushed a model's prediction up or down. It lets us move from “the model said no” to “the model said no mainly because of these factors.”

### 3. Why is trust important in AI systems?

Trust determines whether people will use, challenge, monitor, or reject AI systems. A model that cannot be questioned is difficult to govern responsibly.

### 4. Why are regulators increasingly demanding explainability?

Regulators care because automated decisions can create harm, discrimination, and accountability gaps. Explainability helps organizations justify decisions and audit model behavior.
