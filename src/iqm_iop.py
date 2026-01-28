"""
Interquartile Mean (IQM) IOP Calculation Module
================================================

Implements IQM calculation for robust IOP estimation.
Eliminates both upper and lower quartiles.

Author: edujbarrios
"""

import numpy as np


def calculate_iqm_iop(measurements: np.ndarray) -> float:
    """
    Calculate Interquartile Mean (IQM) IOP.
    
    Averages the middle 50% of data, eliminating both upper and lower
    quartiles. Highly resistant to corneal thickness variations and
    extreme biomechanical responses.
    
    Formula:
        IOP_IQM = (2/n) Σ IOP_(i) for i in [n/4, 3n/4]
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        IQM IOP value in mmHg
        
    Clinical rationale:
        - Eliminates extreme biomechanical responses
        - Ideal for corneal pathology (keratoconus, ectasia)
        - Reduces impact of measurement angle errors
        - Superior for irregular corneal surfaces
    """
    sorted_data = np.sort(measurements)
    n = len(sorted_data)
    
    # Calculate quartile boundaries
    lower_idx = int(np.floor(n / 4))
    upper_idx = int(np.ceil(3 * n / 4))
    
    # Extract interquartile range
    iqr_data = sorted_data[lower_idx:upper_idx]
    
    if len(iqr_data) == 0:
        return round(np.mean(measurements), 1)
    
    iqm = np.mean(iqr_data)
    
    return round(iqm, 1)
