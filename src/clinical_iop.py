"""
Clinical IOP Calculation Module
================================

Implements functional range midpoint calculation.

Author: edujbarrios
"""

import numpy as np


def calculate_clinical_iop(measurements: np.ndarray) -> float:
    """
    Calculate Clinical IOP as functional range midpoint.
    
    Represents the center of the functional pressure range
    observed during measurements.
    
    Formula:
        IOP_clinical = (IOP_min + IOP_max) / 2
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Clinical IOP value in mmHg
    """
    return round((np.min(measurements) + np.max(measurements)) / 2, 1)
