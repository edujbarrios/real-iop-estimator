"""
Statistical Analysis Module
============================

Calculates statistical measures for IOP measurements.

Author: edujbarrios
"""

import numpy as np
from typing import Tuple


def get_range(measurements: np.ndarray) -> Tuple[float, float]:
    """
    Get minimum and maximum values.
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Tuple of (min, max) IOP values
    """
    return (round(np.min(measurements), 1), 
            round(np.max(measurements), 1))


def get_variability(measurements: np.ndarray) -> float:
    """
    Calculate range of measurements (max - min).
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Variability in mmHg
    """
    return round(np.max(measurements) - np.min(measurements), 1)


def get_standard_deviation(measurements: np.ndarray) -> float:
    """
    Calculate standard deviation of measurements.
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Standard deviation in mmHg
    """
    return round(np.std(measurements, ddof=1), 2)
