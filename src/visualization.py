"""
Visualization Module
====================

Handles all plotting and data visualization.

Author: edujbarrios
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
from config import PLOT_STYLE, CLINICAL_ZONES


def create_visualization(measurements: List[float], results: Dict[str, float]):
    """
    Create comprehensive visualization of IOP measurements.
    
    Args:
        measurements: List of IOP measurements
        results: Dictionary of calculated results
        
    Returns:
        Matplotlib figure object
    """
    fig, (ax1, ax2) = plt.subplots(
        1, 2, 
        figsize=PLOT_STYLE['figure_size'],
        dpi=PLOT_STYLE['dpi']
    )
    
    # Configure dark background for medical professionalism
    fig.patch.set_facecolor('#0e1117')
    ax1.set_facecolor('#262730')
    ax2.set_facecolor('#262730')
    
    _plot_measurements(ax1, measurements, results)
    _plot_distribution(ax2, measurements)
    
    plt.tight_layout()
    return fig


def _plot_measurements(ax, measurements: List[float], results: Dict[str, float]):
    """
    Create scatter plot of measurements with reference lines.
    
    Args:
        ax: Matplotlib axis object
        measurements: List of IOP measurements
        results: Dictionary of calculated results
    """
    x_pos = range(1, len(measurements) + 1)
    
    # Plot measurements
    ax.scatter(
        x_pos, 
        measurements, 
        s=100, 
        alpha=0.7, 
        color=PLOT_STYLE['scatter_color'],
        edgecolors='white',
        linewidth=1.5,
        label='Measurements',
        zorder=3
    )
    
    # Reference lines
    ax.axhline(
        y=results['safe_iop'], 
        color=PLOT_STYLE['safe_iop_color'], 
        linestyle='--', 
        linewidth=2.5,
        alpha=0.8,
        label=f"Safe IOP: {results['safe_iop']} mmHg",
        zorder=2
    )
    
    ax.axhline(
        y=results['mean_iop'], 
        color=PLOT_STYLE['mean_color'], 
        linestyle=':', 
        linewidth=1.5,
        alpha=0.6,
        label=f"Mean: {results['mean_iop']} mmHg",
        zorder=1
    )
    
    ax.axhline(
        y=results['possible_iop'], 
        color=PLOT_STYLE['median_color'], 
        linestyle=':', 
        linewidth=1.5,
        alpha=0.6,
        label=f"Median: {results['possible_iop']} mmHg",
        zorder=1
    )
    
    # Styling
    ax.set_xlabel('Measurement Number', fontsize=11, color='#fafafa')
    ax.set_ylabel('IOP (mmHg)', fontsize=11, color='#fafafa')
    ax.set_title('IOP Measurements with Estimates', fontsize=12, fontweight='bold', color='#fafafa')
    ax.legend(loc='best', fontsize=9, facecolor='#262730', edgecolor='#fafafa', labelcolor='#fafafa')
    ax.grid(True, alpha=PLOT_STYLE['grid_alpha'], color='#fafafa', linestyle=':')
    ax.tick_params(colors='#fafafa')
    
    # Set spine colors
    for spine in ax.spines.values():
        spine.set_edgecolor('#fafafa')
        spine.set_alpha(0.3)


def _plot_distribution(ax, measurements: List[float]):
    """
    Create box plot showing distribution with clinical zones.
    
    Args:
        ax: Matplotlib axis object
        measurements: List of IOP measurements
    """
    # Clinical zone backgrounds
    for zone_name, zone_data in CLINICAL_ZONES.items():
        min_range, max_range = zone_data['range']
        ax.axhspan(
            min_range, 
            max_range, 
            alpha=zone_data['alpha'], 
            color=zone_data['color'],
            zorder=0
        )
    
    # Box plot
    bp = ax.boxplot(
        measurements, 
        vert=True, 
        patch_artist=True,
        widths=0.6,
        boxprops=dict(facecolor='#1f77b4', alpha=0.7, edgecolor='white', linewidth=1.5),
        medianprops=dict(color='#ff4444', linewidth=2.5),
        whiskerprops=dict(linewidth=1.5, color='white'),
        capprops=dict(linewidth=1.5, color='white'),
        flierprops=dict(marker='o', markerfacecolor='#ff4444', markersize=8, alpha=0.6)
    )
    
    # Styling
    ax.set_ylabel('IOP (mmHg)', fontsize=11, color='#fafafa')
    ax.set_title('Distribution Analysis', fontsize=12, fontweight='bold', color='#fafafa')
    ax.set_xticklabels([''], color='#fafafa')
    ax.grid(True, alpha=PLOT_STYLE['grid_alpha'], axis='y', color='#fafafa', linestyle=':')
    ax.tick_params(colors='#fafafa')
    
    # Legend for zones
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=CLINICAL_ZONES['hypotony']['color'], alpha=0.3, label='Hypotony Zone'),
        Patch(facecolor=CLINICAL_ZONES['normal']['color'], alpha=0.3, label='Normal Zone'),
        Patch(facecolor=CLINICAL_ZONES['elevated']['color'], alpha=0.3, label='Elevated Zone')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9, 
             facecolor='#262730', edgecolor='#fafafa', labelcolor='#fafafa')
    
    # Set spine colors
    for spine in ax.spines.values():
        spine.set_edgecolor('#fafafa')
        spine.set_alpha(0.3)
