# KMeans Clustering Project Summary

## Executive Summary

This project demonstrates how KMeans clustering can discover hidden customer segments in unlabeled data. Using the Mall Customers dataset, it explores income, age, and spending behavior, then applies KMeans to identify interpretable customer groups.

The central lesson:

> Unsupervised learning is not about predicting known answers. It is about discovering structure that was already hiding in the data.

## Dataset

Dataset: Mall Customers Segmentation Dataset

Rows: 200

Features:

- `customer_id`
- `gender`
- `age`
- `annual_income`
- `spending_score`

The main clustering experiment uses annual income and spending score because they produce visually meaningful and business-interpretable customer segments.

## Clustering Experiments

The notebook performs:

- exploratory data analysis
- feature distribution visualization
- income vs spending scatterplot
- feature scaling comparison
- centroid movement visualization
- elbow method
- silhouette score analysis
- final KMeans clustering
- cluster profile interpretation
- PCA visualization

## Chosen K

The final model uses:

```text
K = 5
```

This choice is supported by the classic mall customer structure, the elbow curve, silhouette scores, and business interpretability.

## Silhouette Findings

Silhouette score helps evaluate whether clusters are cohesive and separated.

In the notebook, silhouette scores are compared across multiple K values. The final K balances score quality with business usefulness.

## Cluster Interpretations

The resulting customer segments are interpreted as:

- Premium high-value customers
- High-income cautious spenders
- Budget enthusiastic shoppers
- Low-income careful shoppers
- Balanced everyday customers

These labels are business interpretations, not ground truth.

## Business Insights

The segmentation suggests different marketing strategies:

- Premium high-value customers may deserve loyalty programs and exclusive offers.
- High-income cautious spenders may need targeted persuasion or premium positioning.
- Budget enthusiastic shoppers may respond to promotions.
- Low-income careful shoppers may require price-sensitive campaigns.
- Balanced everyday customers may benefit from broad engagement strategies.

## Limitations

KMeans has important limitations:

- sensitive to feature scaling
- sensitive to initialization
- requires choosing K manually
- assumes compact, roughly spherical clusters
- can be affected by outliers
- does not naturally handle categorical variables
- cluster interpretation can be subjective

## Practical Lessons

- Always scale features before distance-based clustering.
- Use multiple methods to choose K.
- Visualize clusters whenever possible.
- Interpret clusters with business context.
- Do not treat clusters as absolute truth.
- Clustering is a discovery tool, not a final decision by itself.

## Final Takeaway

KMeans turns similarity into structure.

It helps teams discover meaningful groups in unlabeled data, but the real value comes from interpreting those groups and connecting them to action.

