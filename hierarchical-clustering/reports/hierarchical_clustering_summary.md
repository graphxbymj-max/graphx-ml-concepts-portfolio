# Hierarchical Clustering Project Summary

## Executive Summary

This project demonstrates how Hierarchical Clustering discovers nested relationships inside customer data. Using the Mall Customers dataset, it builds dendrograms, compares linkage methods, creates final customer segments, and compares Hierarchical Clustering with KMeans.

The central lesson:

> Hierarchical Clustering does not just assign groups. It shows how groups form.

## Dataset

Dataset: Mall Customers Segmentation Dataset

Rows: 200

Features:

- `customer_id`
- `gender`
- `age`
- `annual_income`
- `spending_score`

The main segmentation experiment uses annual income and spending score because they produce clear, interpretable customer relationship patterns.

## Clustering Experiments

The notebook performs:

- exploratory data analysis
- feature scaling comparison
- Euclidean and Manhattan distance demonstration
- linkage method comparison
- full dendrogram
- truncated dendrogram
- silhouette score by cluster count
- final AgglomerativeClustering model
- customer segment interpretation
- KMeans comparison

## Linkage Comparisons

The project compares:

- single linkage
- complete linkage
- average linkage
- Ward linkage

Ward linkage is selected for the final model because it tends to create compact, interpretable customer groups in this dataset.

## Dendrogram Findings

The dendrogram shows how individual customers merge into small groups and how those groups merge into larger branches.

Large vertical jumps suggest meaningful separation between groups.

Cutting the dendrogram around a business-friendly level supports a 5-cluster segmentation.

## Cluster Interpretations

The final clusters are interpreted as:

- Premium high-value customers
- High-income cautious spenders
- Budget enthusiastic shoppers
- Low-income careful shoppers
- Balanced everyday customers

These names are business interpretations based on cluster profiles, not ground-truth labels.

## Business Insights

Hierarchical segmentation helps teams understand relationships between customer groups.

Possible actions:

- premium loyalty campaigns for high-value customers
- conversion campaigns for high-income cautious spenders
- promotion-sensitive offers for budget enthusiastic shoppers
- value-focused messaging for careful shoppers
- broad engagement for balanced everyday customers

## Limitations

Hierarchical Clustering has limitations:

- computationally expensive for large datasets
- sensitive to scaling
- sensitive to outliers
- merges are irreversible
- linkage choices change results
- cluster interpretation is subjective

## Practical Lessons

- Scale features before distance-based clustering.
- Use dendrograms to understand relationship structure.
- Compare linkage methods before choosing a final model.
- Use silhouette scores as guidance, not absolute truth.
- Translate clusters into business meaning.
- Use Hierarchical Clustering when interpretability and relationship structure matter.

## Final Takeaway

Hierarchical Clustering is powerful because it makes clustering explainable.

It shows not only which customers belong together, but how those relationships emerged layer by layer.

