import streamlit as st

st.set_page_config(
    page_title="Manitoba Indigenous Maternal Health",
    layout="wide"
)

# ── Custom CSS for the exact card style you showed ──────────────────────
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1e3a8a;
        margin: 40px 0 30px 0;
    }
    .metrics-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin: 0 auto;
        max-width: 1200px;
    }
    .metric-card {
        width: 220px;
        height: 140px;
        border-radius: 16px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .metric-value {
        font-size: 48px;
        font-weight: bold;
        margin: 0;
        line-height: 1;
    }
    .metric-label {
        font-size: 18px;
        margin-top: 8px;
        opacity: 0.95;
    }
    /* Specific colors matching your screenshot */
    .blue { background-color: #3b82f6; }
    .red   { background-color: #ef4444; }
    .green { background-color: #22c55e; }
    .orange{ background-color: #f97316; }
    .purple{ background-color: #a855f7; }
</style>
""", unsafe_allow_html=True)

# ── Hardcoded values from your screenshot ───────────────────────────────
st.markdown('<div class="title">Manitoba Indigenous Maternal Health</div>', unsafe_allow_html=True)

st.markdown("""
<div class="metrics-container">
    <div class="metric-card blue">
        <div class="metric-value">45</div>
        <div class="metric-label">Communities</div>
    </div>
    <div class="metric-card red">
        <div class="metric-value">10</div>
        <div class="metric-label">Hospitals</div>
    </div>
    <div class="metric-card green">
        <div class="metric-value">9</div>
        <div class="metric-label">Midwifery Clinics</div>
    </div>
    <div class="metric-card orange">
        <div class="metric-value">$19.6M</div>
        <div class="metric-label">Travel Costs</div>
    </div>
    <div class="metric-card purple">
        <div class="metric-value">530 km</div>
        <div class="metric-label">Avg Distance</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Small spacing at bottom
st.markdown("<br><br><br>", unsafe_allow_html=True)
