"""Plotting helpers for explainability visuals."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


def save_current_figure(path, dpi: int = 160):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, bbox_inches='tight')


def plot_feature_importance(importance_df, image_path=None, top_n: int = 12):
    fig, ax = plt.subplots(figsize=(9, 6))
    data = importance_df.head(top_n).iloc[::-1]
    sns.barplot(data=data, x='importance', y='feature', color='#4C78A8', ax=ax)
    ax.set_title('Traditional Model Feature Importance')
    ax.set_xlabel('Importance')
    ax.set_ylabel('Feature')
    if image_path:
        save_current_figure(image_path)
    return ax


def plot_local_force_like(contrib_df, image_path=None, top_n: int = 12):
    fig, ax = plt.subplots(figsize=(10, 6))
    data = contrib_df.head(top_n).sort_values('shap_value')
    colors = ['#E45756' if v > 0 else '#4C78A8' for v in data['shap_value']]
    ax.barh(data['feature'], data['shap_value'], color=colors)
    ax.axvline(0, color='#333333', linewidth=1)
    ax.set_title('Local Explanation: Feature Pushes for One Prediction')
    ax.set_xlabel('SHAP contribution toward malignant prediction')
    ax.set_ylabel('Feature')
    if image_path:
        save_current_figure(image_path)
    return ax
