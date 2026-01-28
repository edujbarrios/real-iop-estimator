"""
IOP Calculator Module
=====================

Main calculator class that coordinates all IOP estimation methods.
This module integrates the various calculation modules.

Sources:
- iCare Finland Oy — iCare Tonometer User Manual
- European Glaucoma Society — Terminology and Guidelines for Glaucoma

Author: edujbarrios
License: Open Source
"""

import numpy as np
from typing import List, Dict, Tuple

from safe_iop import calculate_safe_iop
from possible_iop import calculate_possible_iop
from clinical_iop import calculate_clinical_iop
from mean_iop import calculate_mean_iop
from trimean_iop import calculate_trimean_iop
from iqm_iop import calculate_iqm_iop
from winsorized_iop import calculate_winsorized_iop
from weighted_iop import calculate_weighted_iop
from statistics import get_range, get_variability, get_standard_deviation
from interpretation import interpret_iop, get_confidence_note


class IOPCalculator:
    """
    Calculator for estimating real IOP from multiple iCare measurements.
    
    iCare tonometer measurements show inherent variability due to:
    - Corneal impact point variations
    - Measurement angle differences
    - Tear film effects
    - Corneal irregularities
    - Prior ocular surgery effects
    
    Therefore, robust mathematical methods are essential for reliable IOP estimation.
    """
    
    def __init__(self, measurements: List[float]):
        """
        Initialize the calculator with IOP measurements.
        
        Args:
            measurements: List of IOP values in mmHg
            
        Raises:
            ValueError: If fewer than 3 measurements are provided
        """
        if len(measurements) < 3:
            raise ValueError("At least 3 measurements are required for robust estimation")
        
        self.measurements = np.array(sorted(measurements))
        self.n = len(self.measurements)
    
    def calculate_safe_iop(self) -> float:
        """Calculate Safe IOP using trimmed mean method."""
        return calculate_safe_iop(self.measurements)
    
    def calculate_possible_iop(self) -> float:
        """Calculate Possible IOP using median."""
        return calculate_possible_iop(self.measurements)
    
    def calculate_clinical_iop(self) -> float:
        """Calculate Clinical IOP as functional range midpoint."""
        return calculate_clinical_iop(self.measurements)
    
    def calculate_mean_iop(self) -> float:
        """Calculate simple arithmetic mean IOP."""
        return calculate_mean_iop(self.measurements)
    
    def calculate_trimean_iop(self) -> float:
        """Calculate Trimean IOP using Tukey's method."""
        return calculate_trimean_iop(self.measurements)
    
    def calculate_iqm_iop(self) -> float:
        """Calculate Interquartile Mean IOP."""
        return calculate_iqm_iop(self.measurements)
    
    def calculate_winsorized_iop(self) -> float:
        """Calculate Winsorized Mean IOP."""
        return calculate_winsorized_iop(self.measurements)
    
    def calculate_weighted_iop(self) -> float:
        """Calculate Weighted Mean IOP by consistency."""
        return calculate_weighted_iop(self.measurements)
    
    def get_range(self) -> Tuple[float, float]:
        """Get minimum and maximum values."""
        return get_range(self.measurements)
    
    def get_variability(self) -> float:
        """Calculate range of measurements (max - min)."""
        return get_variability(self.measurements)
    
    def get_standard_deviation(self) -> float:
        """Calculate standard deviation of measurements."""
        return get_standard_deviation(self.measurements)
    
    def calculate_all(self) -> Dict[str, float]:
        """
        Calculate all IOP estimates and statistics.
        
        Returns:
            Dictionary containing all calculated values
        """
        min_val, max_val = self.get_range()
        
        return {
            'safe_iop': self.calculate_safe_iop(),
            'possible_iop': self.calculate_possible_iop(),
            'clinical_iop': self.calculate_clinical_iop(),
            'mean_iop': self.calculate_mean_iop(),
            'trimean_iop': self.calculate_trimean_iop(),
            'trimean_iop': self.calculate_trimean_iop(),
            'iqm_iop': self.calculate_iqm_iop(),
            'winsorized_iop': self.calculate_winsorized_iop(),
            'weighted_iop': self.calculate_weighted_iop(),
            'min_iop': min_val,
            'max_iop': max_val,
            'variability': self.get_variability(),
            'std_dev': self.get_standard_deviation(),
            'n_measurements': self.n
        }
    
    def interpret_iop(self, iop_value: float) -> str:
        """Provide clinical interpretation of IOP value."""
        return interpret_iop(iop_value)
    
    def get_confidence_note(self) -> str:
        """Provide measurement confidence assessment."""
        variability = self.get_variability()
        return get_confidence_note(variability)
