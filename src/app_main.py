"""
Streamlit Frontend for IOP Calculator
======================================

Professional medical interface for robust IOP estimation from iCare measurements.
Configured for dark mode with clinical-grade presentation.

Author: edujbarrios
"""

import streamlit as st
import sys
from pathlib import Path

# Add src to path if needed
src_path = Path(__file__).parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from iop_calculator import IOPCalculator
from validation import validate_measurements
from interpretation import get_status_color
from config import STREAMLIT_CONFIG, MIN_MEASUREMENTS


def setup_page():
    """Configure Streamlit page settings with dark theme."""
    st.set_page_config(**STREAMLIT_CONFIG)
    
    # Custom CSS for dark medical theme
    st.markdown("""
        <style>
        .main {
            background-color: #0e1117;
        }
        .stAlert {
            background-color: #262730;
        }
        h1, h2, h3 {
            color: #fafafa;
            font-family: 'Segoe UI', sans-serif;
        }
        .medical-card {
            background-color: #262730;
            padding: 20px;
            border-radius: 5px;
            border-left: 4px solid #1f77b4;
            margin: 10px 0;
        }
        .primary-result {
            background-color: #1a4d2e;
            padding: 15px;
            border-radius: 5px;
            border: 2px solid #4ade80;
        }
        </style>
    """, unsafe_allow_html=True)


def display_header():
    """Display minimal application header."""
    st.markdown("<h1 style='text-align: center;'>Real IOP Estimator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Robust intraocular pressure estimation from multiple measurements</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


def display_abstract():
    """Display minimal info - removed from main view."""
    pass


def display_disclaimer():
    """Display medical and legal disclaimer."""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚠️ Disclaimer")
    st.sidebar.caption("""
    **NOT a medical device. NOT for diagnosis.**
    
    Does NOT replace clinical judgment. Author assumes NO LIABILITY.
    
    Consult a qualified ophthalmologist for medical advice.
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.caption("""
    This tool uses robust statistical methods to estimate real IOP from multiple iCare tonometer measurements.
    
    **Safe IOP** (trimmed mean) is the primary and most reliable estimate.
    """)


def display_input_interface():
    """Display simplified measurement input interface in main area."""
    # Center the input form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Enter IOP Measurements")
        
        iop_input = st.text_area(
            "Comma-separated values (mmHg)",
            height=100,
            placeholder="Example: 12, 14, 13, 15, 12",
            help=f"Enter at least {MIN_MEASUREMENTS} measurements separated by commas",
            label_visibility="collapsed"
        )
        
        st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>Separate measurements with commas • Minimum 3 values required</p>", unsafe_allow_html=True)
        
        calculate_button = st.button(
            "Calculate Real IOP",
            type="primary",
            use_container_width=True
        )
    
    return iop_input, calculate_button


def display_primary_result(safe_iop: float, interpretation: str, confidence: str):
    """
    Display primary Safe IOP result with clinical interpretation and formula.
    
    Args:
        safe_iop: Calculated Safe IOP value
        interpretation: Clinical interpretation
        confidence: Measurement confidence assessment
    """
    st.markdown("### Primary Estimate: Safe IOP (Trimmed Mean)")
    
    col1, col2, col3 = st.columns([2, 2, 3])
    
    with col1:
        st.metric(
            label="Safe IOP",
            value=f"{safe_iop} mmHg",
            help="Most reliable estimate - removes outliers"
        )
    
    with col2:
        color = get_status_color(interpretation)
        if color == 'red':
            st.markdown(f"**Clinical Status:** :red[{interpretation}]")
        elif color == 'green':
            st.markdown(f"**Clinical Status:** :green[{interpretation}]")
        else:
            st.markdown(f"**Clinical Status:** :orange[{interpretation}]")
    
    with col3:
        st.info(confidence)
    
    # Display formula
    st.markdown("**Formula Used:**")
    st.latex(r"IOP_{safe} = \frac{\sum IOP_i - IOP_{min} - IOP_{max}}{n - 2}")
    
    st.markdown("""
    **Clinical Note:** Safe IOP provides the most robust estimate by excluding 
    statistical outliers (minimum and maximum values) while preserving central tendency. 
    This method is recommended for clinical decision-making.
    """)


def display_secondary_estimates(results: dict):
    """
    Display additional IOP estimates with formulas.
    
    Args:
        results: Dictionary containing all calculated values
    """
    st.markdown("---")
    st.markdown("### Additional Estimates")
    
    # Create expandable sections for each method
    with st.expander("Trimean IOP (Tukey's Method) - " + str(results['trimean_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Trimean IOP",
                value=f"{results['trimean_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{trimean} = \frac{Q_1 + 2 \cdot \text{Median} + Q_3}{4}")
    
    with st.expander("IQM IOP (Interquartile Mean) - " + str(results['iqm_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="IQM IOP",
                value=f"{results['iqm_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{IQM} = \frac{2}{n} \sum_{i=\lfloor n/4 \rfloor}^{\lceil 3n/4 \rceil} IOP_{(i)}")
    
    with st.expander("Winsorized IOP (Trimmed Extremes) - " + str(results['winsorized_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Winsorized IOP",
                value=f"{results['winsorized_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{wins} = \frac{1}{n}\left(IOP_{(2)} + \sum_{i=2}^{n-1} IOP_{(i)} + IOP_{(n-1)}\right)")
    
    with st.expander("Weighted IOP (Consistency-Based) - " + str(results['weighted_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Weighted IOP",
                value=f"{results['weighted_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{weighted} = \frac{\sum_{i=1}^{n} w_i \cdot IOP_i}{\sum_{i=1}^{n} w_i}, \quad w_i = \frac{1}{1 + |IOP_i - \text{Median}|}")
    
    with st.expander("Possible IOP (Median) - " + str(results['possible_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Possible IOP",
                value=f"{results['possible_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{possible} = \text{median}(IOP_1, IOP_2, \ldots, IOP_n)")
    
    with st.expander("Clinical IOP (Range Midpoint) - " + str(results['clinical_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Clinical IOP",
                value=f"{results['clinical_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{clinical} = \frac{IOP_{min} + IOP_{max}}{2}")
    
    with st.expander("Mean IOP (Arithmetic Average) - " + str(results['mean_iop']) + " mmHg", expanded=False):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                label="Mean IOP",
                value=f"{results['mean_iop']} mmHg"
            )
        with col2:
            st.latex(r"IOP_{mean} = \frac{1}{n}\sum_{i=1}^{n} IOP_i")
    
    # Summary metrics row
    st.markdown("**Measurement Variability:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Range",
            value=f"{results['variability']} mmHg",
            help="Difference between maximum and minimum values"
        )
    
    with col2:
        st.metric(
            label="Minimum",
            value=f"{results['min_iop']} mmHg"
        )
    
    with col3:
        st.metric(
            label="Maximum",
            value=f"{results['max_iop']} mmHg"
        )


def display_statistics(results: dict):
    """
    Display detailed measurement statistics with formulas.
    
    Args:
        results: Dictionary containing statistical values
    """
    st.markdown("---")
    st.markdown("### Statistical Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Descriptive Statistics:**")
        stats_data = {
            "Metric": ["Sample Size", "Minimum", "Maximum", "Range", "Standard Deviation"],
            "Value": [
                f"{results['n_measurements']} measurements",
                f"{results['min_iop']} mmHg",
                f"{results['max_iop']} mmHg",
                f"{results['variability']} mmHg",
                f"{results['std_dev']} mmHg"
            ]
        }
        
        for metric, value in zip(stats_data["Metric"], stats_data["Value"]):
            st.metric(label=metric, value=value)
    
    with col2:
        st.markdown("**Variability Formula:**")
        st.latex(r"\text{Range} = IOP_{max} - IOP_{min}")
        
        st.markdown("**Standard Deviation:**")
        st.latex(r"\sigma = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(IOP_i - \bar{IOP})^2}")
        
        st.markdown("---")
        
        # Variability interpretation
        variability = results['variability']
        if variability <= 2:
            st.success(f"Excellent consistency (σ = {variability} mmHg)")
        elif variability <= 4:
            st.info(f"Good consistency (σ = {variability} mmHg)")
        elif variability <= 6:
            st.warning(f"Fair consistency (σ = {variability} mmHg)")
        else:
            st.error(f"High variability (σ = {variability} mmHg) - Consider additional measurements")


def display_clinical_notes():
    """Display simplified clinical interpretation guidelines."""
    st.markdown("---")
    st.info("""
    **Remember:** These are mathematical estimates to support clinical decisions.
    
    - **Safe IOP** is most reliable for decision-making
    - Low variability (< 4 mmHg) = High confidence  
    - High variability (> 6 mmHg) = Consider more measurements
    """)


def display_welcome_screen():
    """Display welcome message."""
    st.markdown("""
    <div style='text-align: center; padding: 40px 20px;'>
        <p style='font-size: 16px; color: #888;'>Enter your measurements above and click the button to calculate</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application entry point."""
    setup_page()
    display_disclaimer()
    display_header()
    
    # Main input interface
    iop_input, calculate_button = display_input_interface()
    
    # Process calculation only when button is clicked
    if calculate_button:
        if not iop_input.strip():
            st.error("⚠️ Please enter IOP measurements above.")
            return
        
        try:
            # Validate and parse input
            measurements = validate_measurements(iop_input)
            
            # Perform calculations
            calculator = IOPCalculator(measurements)
            results = calculator.calculate_all()
            
            # Display results
            st.header("Results")
            
            interpretation = calculator.interpret_iop(results['safe_iop'])
            confidence = calculator.get_confidence_note()
            
            display_primary_result(results['safe_iop'], interpretation, confidence)
            display_secondary_estimates(results)
            display_statistics(results)
            
            # Show input measurements recap
            st.markdown("---")
            st.markdown("### Input Measurements")
            st.write(f"**Raw measurements:** {', '.join(map(str, measurements))} mmHg")
            st.write(f"**Total measurements:** {len(measurements)}")
            
            display_clinical_notes()
            
            st.success("Calculation completed successfully.")
            
        except ValueError as e:
            st.error(f"INPUT ERROR: {str(e)}")
        except Exception as e:
            st.error(f"SYSTEM ERROR: {str(e)}")
            st.error("Please verify input format and try again.")
    
    else:
        # Show minimal welcome screen when no calculation
        display_welcome_screen()


if __name__ == "__main__":
    main()
