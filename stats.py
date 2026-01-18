st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1">
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(page_title="Key Stats", layout="wide")

st.markdown("""
<style>
    .metric-card {
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .metric-card-blue { background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%); }
    .metric-card-green { background: linear-gradient(135deg, #43a047 0%, #2e7d32 100%); }
    .metric-card-orange { background: linear-gradient(135deg, #fb8c00 0%, #ef6c00 100%); }
    .metric-card-red { background: linear-gradient(135deg, #e53935 0%, #c62828 100%); }
    .metric-card-purple { background: linear-gradient(135deg, #8e24aa 0%, #6a1b9a 100%); }
    .metric-value { font-size: 42px; font-weight: bold; margin: 0; }
    .metric-label { font-size: 14px; opacity: 0.9; margin-top: 8px; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card metric-card-blue">
        <p class="metric-value">45</p>
        <p class="metric-label">FN Communities</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card metric-card-red">
        <p class="metric-value">10</p>
        <p class="metric-label">Hospitals</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card metric-card-green">
        <p class="metric-value">9</p>
        <p class="metric-label">Midwifery Clinics</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card metric-card-orange">
        <p class="metric-value">$19.4M</p>
        <p class="metric-label">Travel Costs</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card metric-card-purple">
        <p class="metric-value">530 km</p>
        <p class="metric-label">Avg Distance</p>
    </div>
    """, unsafe_allow_html=True)
