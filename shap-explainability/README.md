# SHAP & Explainability Explained Intuitively

## Peeking Inside the Black Box of Machine Learning

Welcome to the SHAP & Explainability project in the GraphX Labs ML Concepts Portfolio.

This project is built around one central idea:

> What if we could finally ask a machine learning model WHY it made a prediction?

Explainability is not decoration. It is how teams build trust, debug models, investigate bias, and make responsible AI decisions when predictions affect people.

---

# Business Problem

This project uses a healthcare-style prediction task: identifying whether a breast cancer diagnostic sample is malignant or benign.

The model question:

> Can we predict malignant cases accurately?

The explainability question:

> Can we understand which measurements pushed the model toward that prediction?

In real healthcare, finance, insurance, and hiring systems, both questions matter.

---

# Dataset

Dataset:

```text
Breast Cancer Wisconsin Diagnostic Dataset
```

Raw file:

```text
shap-explainability/data/raw/breast_cancer_wisconsin.csv
```

Processed file:

```text
shap-explainability/data/processed/breast_cancer_wisconsin_processed.csv
```

Target variable:

```text
is_malignant
```

Target meaning:

- `1`: malignant
- `0`: benign

---

# Explainable AI Intuition

A model score is not the same as an explanation.

Explainable AI helps answer:

- What does the model care about overall?
- Why did this individual prediction happen?
- Which features pushed the prediction higher or lower?
- Is the model relying on patterns we trust?
- Are there signs of hidden bias or suspicious shortcuts?

---

# The Black-Box Problem

Black-box models can be accurate and still dangerous.

They can learn shortcuts. They can over-rely on proxy variables. They can make decisions that are difficult to defend to customers, clinicians, regulators, or internal stakeholders.

This project shows how SHAP helps turn model behavior into something visible.

---

# SHAP Explanation

SHAP explains predictions as feature contributions.

Start with a baseline prediction. Then each feature pushes the prediction up or down.

For this project:

- positive SHAP values push toward malignant
- negative SHAP values push away from malignant

SHAP breaks the model's prediction into understandable pieces.

---

# Local vs Global Interpretability

Global explainability asks:

> What does the model generally rely on?

Local explainability asks:

> Why did this specific prediction happen?

The notebook includes both.

---

# Visuals Created

The notebook saves:

- `feature_importance.png`
- `shap_summary_plot.png`
- `shap_bar_plot.png`
- `shap_force_plot.png`
- `shap_waterfall_plot.png`
- `shap_dependence_plot.png`
- `confusion_matrix.png`
- `correlation_heatmap.png`

---

# Responsible AI

Explainability does not automatically make a model fair.

But it makes better questions possible:

- Is the model relying on clinically meaningful features?
- Are explanations stable?
- Are there suspicious proxy variables?
- Do errors concentrate in certain subgroups?
- Can the prediction be defended to a human decision-maker?

---

# Medium Articles

Companion article drafts live in:

```text
articles/shap-explainability/
```

Included:

- `shap_explainability_project_article.md`
- `shap_explainability_interview_questions.md`
- `medium_publishing_notes.md`

---

# Key Learning

GraphX Labs takeaway:

> A black-box model may predict. An explainable model can be questioned.
