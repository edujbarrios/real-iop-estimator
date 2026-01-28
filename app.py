"""
IOP Estimator Application Launcher
===================================

Launch script for the Real IOP Estimator Streamlit application.

This application estimates real intraocular pressure (IOP) from multiple
iCare tonometer measurements using robust mathematical methods.

Author: edujbarrios
License: Open Source

Usage:
    python app.py
    
    Or directly with streamlit:
    streamlit run src/app_main.py
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

# Import and run the Streamlit app
if __name__ == "__main__":
    import streamlit.web.cli as stcli
    
    # Path to the streamlit app
    app_path = src_path / 'app_main.py'
    
    # Run streamlit
    sys.argv = ["streamlit", "run", str(app_path), "--server.headless=true"]
    sys.exit(stcli.main())
