"""Fonctions de visualisation réutilisables."""

import matplotlib.pyplot as plt


def set_style():
    """Applique le style standard aux graphiques."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12


def plot_kpi_dashboard(df, metrics: list, save_path: str = None):
    """Génère un dashboard KPI."""
    set_style()
    fig, axes = plt.subplots(1, len(metrics), figsize=(5*len(metrics), 5))

    for ax, metric in zip(axes, metrics):
        df[metric].plot(ax=ax)
        ax.set_title(metric)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig
