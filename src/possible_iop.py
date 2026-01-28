"""
Possible IOP Calculation Module
================================

Implements median calculation for IOP estimation.

Author: edujbarrios
"""

import numpy as np


def calculate_possible_iop(measurements: np.ndarray) -> float:
    """
    Calculate Possible IOP using median.
    
    The median is less affected by extreme values than the arithmetic mean.
    Represents the middle value in the distribution.
    
    Formula:
        IOP_possible = median(IOP_1, ..., IOP_n)
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Median IOP value in mmHg
    """
    return round(np.median(measurements), 1)
