"""
Weighted Mean IOP Calculation Module
=====================================

Implements consistency-weighted mean calculation for IOP estimation.
Gives more weight to values near the median.

Author: edujbarrios
"""

import numpy as np


def calculate_weighted_iop(measurements: np.ndarray) -> float:
    """
    Calculate Weighted Mean IOP by consistency.
    
    Assigns weights based on distance from median. Values closer to
    median receive higher weights. Automatically downweights outliers
    from corneal irregularities without completely discarding them.
    
    Formula:
        IOP_weighted = Σ(w_i · IOP_i) / Σ(w_i)
        where w_i = 1 / (1 + |IOP_i - Median|)
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Weighted mean IOP value in mmHg
        
    Clinical rationale:
        - Soft outlier rejection (no hard cutoffs)
        - Preserves all measurement information
        - Optimal for variable corneal hydration states
        - Adaptive to measurement consistency
        - Useful for diurnal IOP fluctuation patterns
    """
    median = np.median(measurements)
    
    # Calculate weights based on distance from median
    weights = 1.0 / (1.0 + np.abs(measurements - median))
    
    # Weighted average
    weighted_mean = np.sum(weights * measurements) / np.sum(weights)
    
    return round(weighted_mean, 1)
