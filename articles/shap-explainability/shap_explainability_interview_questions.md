# SHAP & Explainable AI Interview Questions Explained Like a Real ML Engineer

Explainability interviews are not just about defining SHAP.

They test whether you understand trust.

A real ML engineer knows that a model score is only part of the story. In production, people ask why a prediction happened, whether the reasoning is defensible, whether the model learned shortcuts, and whether the decision can be audited.

This guide explains SHAP and explainable AI with practical, business-aware intuition.

## 1. What Is Explainable AI?

Explainable AI is the practice of making model decisions understandable to humans.

It helps answer:

- what the model learned
- which features matter
- why one prediction happened
- whether the model is relying on sensible patterns
- where the model might be failing

Explainability matters because real AI systems affect real decisions.

## 2. Why Do Black-Box Models Create Problems?

Black-box models create problems because they can make high-confidence predictions without showing their reasoning.

That is risky in finance, healthcare, hiring, insurance, fraud detection, and other high-stakes domains.

A model can be accurate overall but still fail unfairly for certain groups, rely on proxy variables, or make decisions that stakeholders cannot defend.

## 3. What Is SHAP?

SHAP is an explainability method that assigns contribution values to features.

It explains how much each feature pushed a prediction away from the baseline.

In plain English:

> SHAP shows which factors pushed the model toward or away from a prediction.

## 4. What Are SHAP Values?

SHAP values are numerical feature contributions.

A positive SHAP value pushes the prediction upward for the class being explained.

A negative SHAP value pushes it downward.

For example, in a credit-risk model, high debt-to-income ratio might push risk up, while long payment history might push risk down.

## 5. What Is Local Explainability?

Local explainability explains one individual prediction.

It answers questions like:

- Why was this loan rejected?
- Why did this customer receive a churn warning?
- Why did this patient get a high-risk score?

Local explanations are critical when decisions affect individuals.

## 6. What Is Global Explainability?

Global explainability explains model behavior across many predictions.

It answers:

- Which features matter most overall?
- How do feature values usually affect predictions?
- Does the model rely on plausible signals?

Global explanations are useful for model auditing and stakeholder communication.

## 7. What Is a SHAP Summary Plot?

A SHAP summary plot shows feature importance and direction across many observations.

It reveals which features have the strongest impact and whether high or low feature values push predictions up or down.

It is one of the most useful first visuals for understanding global model behavior.

## 8. What Is a SHAP Dependence Plot?

A dependence plot shows how a feature's value relates to its SHAP contribution.

It helps reveal nonlinear effects, thresholds, and interactions.

For example, fraud risk may rise sharply only after transaction amount crosses a certain range.

## 9. How Can SHAP Help Debug Models?

SHAP helps engineers inspect wrong predictions.

If a model makes a false positive or false negative, SHAP can show which features drove the mistake. This helps identify suspicious shortcuts, missing features, unstable behavior, or legitimate ambiguity.

## 10. How Can SHAP Help Detect Bias?

SHAP can reveal whether sensitive attributes or proxy variables influence predictions.

It can also show whether different subgroups receive different explanation patterns.

However, SHAP does not prove fairness by itself. It is a tool for investigation, not a complete fairness audit.

## 11. SHAP vs Traditional Feature Importance

Traditional feature importance usually gives one global ranking.

SHAP provides both global and local explanations. It shows not only which features matter, but how they push predictions for individual cases.

That makes SHAP much richer for debugging and decision support.

## 12. SHAP vs LIME

LIME explains one prediction by fitting a simple local surrogate model around that prediction.

SHAP is based on Shapley-value intuition and provides additive feature contribution explanations.

Both are local explanation methods, but SHAP often provides more consistent contribution accounting.

## 13. What Is the Game Theory Intuition Behind SHAP?

SHAP comes from Shapley values in cooperative game theory.

Imagine features as players in a game and the prediction as the payout. SHAP fairly divides credit among the features based on how much each contributed.

The practical intuition is simpler:

> Each feature gets a fair share of responsibility for the prediction.

## 14. Why Can Correlated Features Complicate SHAP?

When features are correlated, they carry overlapping information.

SHAP may split contribution between them in ways that are mathematically consistent but hard to interpret casually.

This is why SHAP explanations should be paired with domain knowledge and correlation analysis.

## 15. When Should Businesses Prioritize Interpretability?

Interpretability matters most when decisions are high-stakes, regulated, customer-facing, ethically sensitive, expensive to reverse, or likely to be challenged.

Examples include healthcare, lending, hiring, insurance, criminal justice, and safety systems.

## 16. How Would You Explain SHAP to a Stakeholder?

I would say:

SHAP helps us understand the model's reasoning. It shows which factors pushed a prediction higher or lower, both across the whole model and for one specific case.

It turns a model output from “the system said so” into “these factors drove the decision.”

## 17. What Are Limitations of SHAP?

SHAP can be computationally expensive, especially for large datasets or complex models.

It can be difficult to interpret with correlated features.

It explains model behavior, not real-world causality.

It requires domain knowledge.

And it can reveal unfairness without automatically fixing it.

## Final Takeaway

Explainability is not a luxury feature.

It is how machine learning systems earn trust, survive scrutiny, and become safer to use in real decisions.

A strong ML engineer does not only ask whether the model predicts well.

They ask whether the model can be understood, challenged, and responsibly deployed.
