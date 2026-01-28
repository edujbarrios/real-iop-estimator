"""
Configuration Module
====================

Centralizes application configuration including Streamlit theme settings,
clinical constants, and display parameters.

Author: edujbarrios
"""

# Streamlit theme configuration (dark mode)
STREAMLIT_CONFIG = {
    "page_title": "IOP Estimator - iCare Tonometer",
    "page_icon": "⚕️",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'About': "Real IOP Estimator - Robust estimation from iCare measurements"
    }
}

# Dark theme configuration
THEME_CONFIG = """
[theme]
primaryColor="#1f77b4"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#fafafa"
font="sans serif"
"""

# Clinical interpretation ranges (mmHg)
CLINICAL_RANGES = {
    'severe_hypotony': (0, 6),
    'moderate_hypotony': (6, 8),
    'mild_hypotony': (8, 10),
    'normal': (10, 21),
    'borderline_elevated': (21, 24),
    'elevated': (24, 30),
    'severely_elevated': (30, 100)
}

# Clinical interpretation labels
INTERPRETATION_LABELS = {
    'severe_hypotony': 'Severe Hypotony',
    'moderate_hypotony': 'Moderate Hypotony',
    'mild_hypotony': 'Mild Hypotony',
    'normal': 'Normal Range',
    'borderline_elevated': 'Borderline Elevated',
    'elevated': 'Elevated',
    'severely_elevated': 'Severely Elevated'
}

# Variability confidence thresholds (mmHg)
VARIABILITY_THRESHOLDS = {
    'excellent': 2,
    'good': 4,
    'fair': 6
}

# Measurement constraints
MIN_MEASUREMENTS = 3
MIN_IOP_VALUE = 0
MAX_IOP_VALUE = 100

# Plot styling
PLOT_STYLE = {
    'figure_size': (12, 4),
    'dpi': 100,
    'scatter_color': 'steelblue',
    'safe_iop_color': 'green',
    'mean_color': 'orange',
    'median_color': 'purple',
    'grid_alpha': 0.3
}

# Clinical zones for visualization
CLINICAL_ZONES = {
    'hypotony': {'range': (0, 10), 'color': '#ff4444', 'alpha': 0.1},
    'normal': {'range': (10, 21), 'color': '#44ff44', 'alpha': 0.1},
    'elevated': {'range': (21, 100), 'color': '#ffaa44', 'alpha': 0.1}
}
