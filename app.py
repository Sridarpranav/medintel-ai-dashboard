import streamlit as st
import pandas as pd

# Page setup for premium aesthetic
st.set_page_config(
    page_title="MedIntel AI - Decision Support", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Custom Bluish High-Class Styling Matrix (CSS Injection)
st.markdown("""
    <style>
    /* Dark Deep Blue background theme */
    .stApp {
        background-color: #070b19;
        color: #e2e8f0;
    }
    /* SideBar Custom styling */
    [data-testid="stSidebar"] {
        background-color: #0d1527;
        border-right: 1px solid #1e3a8a;
    }
    /* Custom Metric Cards */
    .metric-card {
        background-color: #0d1527;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1e3a8a;
        margin-bottom: 10px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
    }
    .metric-label {
        font-size: 12px;
        color: #94a3b8;
    }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#3b82f6;'>🧠 MedIntel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:11px; color:#60a5fa;'>Clinical Intelligence</p>", unsafe_allow_html=True)
    st.write("---")
    
    navigation = st.radio(
        "Main Diagnostics",
        ['Overview', 'Predictive Analytics', 'Report Analysis (PDF)', 'Treatment Recs', 'Explainable AI (SHAP)']
    )
    
    st.write("---")
    st.markdown("<small>Logged in as:<br><b>Dr. Alex Sterling</b><br>Attending Clinician</small>", unsafe_allow_html=True)

# MAIN INTERFACE
st.markdown("<h1 style='color:white;'>Global Decision Support Panel</h1>", unsafe_allow_html=True)
st.caption("Combining advanced Machine Learning architectures (XGBoost, Scikit-learn, TensorFlow) with Explainable AI.")

# TOP HIGH LEVEL METRICS ROW
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-label">Avg Diagnostic Accuracy</div><div class="metric-value">93.8%</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-label">Active Assessments</div><div class="metric-value">1,248</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-label">High Risk Alert Flags</div><div class="metric-value" style="color:#fbbf24;">14</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-label">Processed PDF Reports</div><div class="metric-value">89</div></div>', unsafe_allow_html=True)

st.write("### Live ML Predictive Capabilities")

# DATA ARRAY MATCHING YOUR PROJECT IMAGE FEATURES
features_data = {
    "Disease Prediction Vector": [
        "Disease Prediction", "Disease Stage Prediction", "Mortality Risk Prediction", 
        "Recovery Prediction", "Hospital Readmission Prediction", "Disease Progression Analysis"
    ],
    "Engine Architecture": ["TensorFlow", "Scikit-learn", "XGBoost", "PyTorch", "FastAPI Core", "XGBoost"],
    "Confidence Vector": ["94.2%", "89.7%", "96.5%", "91.0%", "88.4%", "93.1%"],
    "Status Pipeline": ["Optimal", "Active", "Critical Monitor", "Stable", "Optimal", "Processing"]
}

df = pd.DataFrame(features_data)
st.dataframe(df, use_container_width=True)

# EXPLAINABLE AI SECTION
st.write("### SHAP Explainer Matrix")
shap_data = pd.DataFrame({
    'Feature Profile': ['Patient Age Profile', 'Lab Biomarkers (Serum)', 'Comorbidity Indexes'],
    'SHAP Value Contribution': [0.24, 0.18, 0.12]
})
st.bar_chart(shap_data.set_index('Feature Profile'))
