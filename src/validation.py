"""
Input Validation Module
========================

Handles validation of IOP measurement inputs.

Author: edujbarrios
"""

from typing import List
from config import MIN_MEASUREMENTS, MIN_IOP_VALUE, MAX_IOP_VALUE


def parse_iop_input(input_string: str) -> List[float]:
    """
    Parse and validate comma-separated IOP values.
    
    Args:
        input_string: String containing comma-separated numbers
        
    Returns:
        List of validated float values
        
    Raises:
        ValueError: If input cannot be parsed or values are invalid
    """
    if not input_string or not input_string.strip():
        raise ValueError("Input cannot be empty")
    
    try:
        # Split by comma and convert to float
        values = [float(x.strip()) for x in input_string.split(',') if x.strip()]
        
        if not values:
            raise ValueError("No valid values found in input")
        
        # Validate each value
        for val in values:
            if val < MIN_IOP_VALUE or val > MAX_IOP_VALUE:
                raise ValueError(
                    f"IOP value {val} is out of acceptable range "
                    f"({MIN_IOP_VALUE}-{MAX_IOP_VALUE} mmHg)"
                )
        
        return values
        
    except ValueError as e:
        if "could not convert" in str(e):
            raise ValueError("Invalid number format. Use comma-separated numeric values.")
        raise


def validate_measurement_count(measurements: List[float]) -> None:
    """
    Validate that sufficient measurements are provided.
    
    Args:
        measurements: List of IOP measurements
        
    Raises:
        ValueError: If insufficient measurements
    """
    if len(measurements) < MIN_MEASUREMENTS:
        raise ValueError(
            f"At least {MIN_MEASUREMENTS} measurements are required "
            f"for robust estimation. Provided: {len(measurements)}"
        )


def validate_measurements(input_string: str) -> List[float]:
    """
    Complete validation pipeline for IOP measurements.
    
    Args:
        input_string: Raw input string
        
    Returns:
        Validated list of measurements
        
    Raises:
        ValueError: If validation fails
    """
    measurements = parse_iop_input(input_string)
    validate_measurement_count(measurements)
    return measurements
