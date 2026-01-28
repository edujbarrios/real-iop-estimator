"""
Clinical Interpretation Module
===============================

Provides clinical interpretation of IOP values and measurement quality.

Author: edujbarrios
"""

from config import CLINICAL_RANGES, INTERPRETATION_LABELS, VARIABILITY_THRESHOLDS


def interpret_iop(iop_value: float) -> str:
    """
    Provide clinical interpretation of IOP value.
    
    Args:
        iop_value: IOP value in mmHg
        
    Returns:
        Clinical interpretation string
    """
    for category, (min_val, max_val) in CLINICAL_RANGES.items():
        if min_val <= iop_value < max_val:
            return INTERPRETATION_LABELS[category]
    
    return INTERPRETATION_LABELS['severely_elevated']


def get_confidence_note(variability: float) -> str:
    """
    Assess measurement confidence based on variability.
    
    Args:
        variability: Range of measurements (max - min)
        
    Returns:
        Confidence assessment string
    """
    if variability <= VARIABILITY_THRESHOLDS['excellent']:
        return "Excellent measurement consistency - High confidence"
    elif variability <= VARIABILITY_THRESHOLDS['good']:
        return "Good measurement consistency - Moderate confidence"
    elif variability <= VARIABILITY_THRESHOLDS['fair']:
        return "Fair measurement consistency - Consider additional measurements"
    else:
        return "High variability detected - Additional measurements recommended"


def get_status_color(interpretation: str) -> str:
    """
    Get color designation for clinical status.
    
    Args:
        interpretation: Clinical interpretation string
        
    Returns:
        Color designation ('red', 'green', 'orange')
    """
    if 'Hypotony' in interpretation:
        return 'red'
    elif 'Normal' in interpretation:
        return 'green'
    else:
        return 'orange'
