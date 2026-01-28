"""
Mean IOP Calculation Module
============================

Implements simple arithmetic mean calculation.

Author: edujbarrios
"""

import numpy as np


def calculate_mean_iop(measurements: np.ndarray) -> float:
    """
    Calculate simple arithmetic mean IOP.
    
    Standard average of all measurements. More sensitive to
    outliers than median or trimmed mean.
    
    Formula:
        IOP_mean = (1/n) Σ IOP_i
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Mean IOP value in mmHg
    """
    return round(np.mean(measurements), 1)
