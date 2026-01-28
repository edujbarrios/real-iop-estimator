"""
Trimean IOP Calculation Module
================================

Implements Tukey's Trimean calculation for robust IOP estimation.
Excellent for corneal biomechanical variability.

Author: edujbarrios
"""

import numpy as np


def calculate_trimean_iop(measurements: np.ndarray) -> float:
    """
    Calculate Trimean IOP using Tukey's Trimean method.
    
    Combines quartiles and median with weighted average. Highly robust
    against outliers from corneal biomechanical variations and 
    measurement angle inconsistencies.
    
    Formula:
        IOP_trimean = (Q1 + 2·Median + Q3) / 4
    
    Args:
        measurements: Array of IOP measurements
        
    Returns:
        Trimean IOP value in mmHg
        
    Clinical rationale:
        - Resistant to corneal biomechanical outliers
        - Balances median robustness with quartile context
        - Optimal for post-surgical and keratoconus patients
    """
    q1 = np.percentile(measurements, 25)
    median = np.median(measurements)
    q3 = np.percentile(measurements, 75)
    
    trimean = (q1 + 2 * median + q3) / 4
    
    return round(trimean, 1)
