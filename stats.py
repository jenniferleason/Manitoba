import streamlit as st

# --------------------------------------------------
# Page config (MUST be first Streamlit call)
# --------------------------------------------------
st.set_page_config(
    page_title="Key Stats",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# FORCE HIDE STREAMLIT BRANDING (UGLY BUT WORKS)
# --------------------------------------------------
st.markdown(
    """
    <style>
        /* Hide Streamlit menu */
        #MainMenu {
            display: none !important;
        }

        /* Hide all known footer / toolbar injections */
        footer,
        div[data-testid="stToolbar"],
        div[data-testid="stStatusWidget"],
        div[data-testid="stDecoration"],
        div[class*="streamlit"] footer,
        div[class*="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            overflow: hidden !important;
        }

        /* Hide fullscreen button explicitly */
        button[title="View fullscreen"],
        button[aria-label="View fullscreen"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Remove extra spacing */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* Metric card styles */
        .metric-card {
            padding: 25px;
            border-radius: 16px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.25);
            margin-bottom: 16px;
        }

        .metric-card-blue {
            background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);
        }

        .metric-card-red {
            background: linear-gradient(135deg, #e53935 0%, #c62828 100%);
        }

        .metric-card-green {
            background: linear-gradient(135deg, #43a047 0%, #2e7d32 100%);
        }

        .metric-card-orange {
            background: linear-gradient(135deg, #fb8c00 0%, #ef6c00 100%);
        }

        .metric-card-purple {
            background: linear-gradient(135deg, #8e24aa 0%, #6a1b9a 100%);
        }

        .metric-value {
            font-size: 42px;
            font-weight: 700;
            margin: 0;
        }

        .metric-label {
            font-size: 14px;
            opacity: 0.9;
            margin-top: 8px;
        }

        /* Mobile scaling */
        @media (max-width: 768px) {
            .metric-value {
                font-size: 32px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# METRIC CARDS (RESPONSIVE LAYOUT)
# --------------------------------------------------

# Row 1 (3 cards)
col1, col2, col3 = st.columns(3)

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

# Row 2 (2 cards)
col4, col5 = st.columns(2)

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
