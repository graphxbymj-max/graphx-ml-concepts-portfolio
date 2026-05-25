"""Plotting utilities for the A/B testing project."""
from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


def save_current_figure(path, dpi: int = 160):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, bbox_inches='tight')


def plot_conversion_rates(summary, image_path=None):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=summary, x='group', y='conversion_rate', hue='group', palette=['#4C78A8', '#F58518'], legend=False, ax=ax)
    ax.set_title('Conversion Rate by Experiment Group')
    ax.set_xlabel('Experiment Group')
    ax.set_ylabel('Conversion Rate')
    ax.bar_label(ax.containers[0], fmt='%.2f') if ax.containers else None
    ax.yaxis.set_major_formatter(lambda x, pos: f'{x:.1%}')
    if image_path:
        save_current_figure(image_path)
    return ax


def plot_confidence_intervals(ci_df, image_path=None):
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#4C78A8', '#F58518']
    for i, row in ci_df.iterrows():
        ax.errorbar(row['group'], row['conversion_rate'], yerr=[[row['conversion_rate'] - row['ci_low']], [row['ci_high'] - row['conversion_rate']]], fmt='o', capsize=8, color=colors[i % len(colors)], markersize=10)
    ax.set_title('Conversion Rate Confidence Intervals')
    ax.set_xlabel('Experiment Group')
    ax.set_ylabel('Conversion Rate')
    ax.yaxis.set_major_formatter(lambda x, pos: f'{x:.1%}')
    ax.grid(axis='y', alpha=0.25)
    if image_path:
        save_current_figure(image_path)
    return ax


def plot_simulation_distribution(sim_df, image_path=None):
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.histplot(sim_df['observed_lift'] * 100, bins=35, kde=True, color='#54A24B', ax=ax)
    ax.axvline(sim_df['observed_lift'].mean() * 100, color='#E45756', linestyle='--', label='Average observed lift')
    ax.axvline(0, color='#333333', linewidth=1, label='No lift')
    ax.set_title('Repeated Experiment Simulation: Observed Lift Moves Around')
    ax.set_xlabel('Observed lift in percentage points')
    ax.set_ylabel('Number of simulated experiments')
    ax.legend()
    if image_path:
        save_current_figure(image_path)
    return ax
