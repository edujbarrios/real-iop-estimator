"""
Winsorized Mean IOP Calculation Module
=======================================

Implements Winsorized mean calculation for IOP estimation.
Replaces extremes instead of removing them.

Author: edujbarrios
"""

import numpy as np


def calculate_winsorized_iop(measurements: np.ndarray) -> float:
    """
    Calculate Winsorized Mean IOP.
    
    Replaces the minimum and maximum values with the adjacent values,
    then calculates the mean. Preserves sample size while reducing
    outlier influence from corneal measurement artifacts.
    
    Formula:
        IOP_wins = (1/n) * (IOP_(2) + Σ IOP_(i) + IOP_(n-1))
        where IOP_(k) denotes k-th ordered value
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Winsorized mean IOP value in mmHg
        
    Clinical rationale:
        - Maintains sample size (important for n < 10)
        - Reduces tear film artifact impact
        - Smooths corneal hydration effects
        - Better for sequential daily measurements
    """
    if len(measurements) < 3:
        return round(np.mean(measurements), 1)
    
    sorted_data = np.sort(measurements)
    n = len(sorted_data)
    
    # Replace extremes with adjacent values
    winsorized = sorted_data.copy()
    winsorized[0] = sorted_data[1]      # Replace min with 2nd smallest
    winsorized[-1] = sorted_data[-2]    # Replace max with 2nd largest
    
    return round(np.mean(winsorized), 1)
