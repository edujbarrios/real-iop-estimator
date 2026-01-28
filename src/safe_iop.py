"""
Safe IOP Calculation Module
============================

Implements trimmed mean calculation for robust IOP estimation.
This is the primary and most reliable estimate.

Author: edujbarrios
"""

import numpy as np


def calculate_safe_iop(measurements: np.ndarray) -> float:
    """
    Calculate Safe IOP using trimmed mean method.
    
    This is the PRIMARY and MOST RELIABLE estimate of real IOP.
    Removes minimum and maximum values (outliers) and averages the rest.
    
    Formula:
        IOP_safe = (Σ IOP_i - IOP_min - IOP_max) / (n - 2)
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Safe IOP value in mmHg
        
    References:
        - European Glaucoma Society Guidelines
        - Robust statistics methodology
    """
    n = len(measurements)
    
    if n < 3:
        return round(np.mean(measurements), 1)
    
    total_sum = np.sum(measurements)
    min_val = np.min(measurements)
    max_val = np.max(measurements)
    
    safe_iop = (total_sum - min_val - max_val) / (n - 2)
    
    return round(safe_iop, 1)
