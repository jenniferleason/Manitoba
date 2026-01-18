st.markdown(
    """
    <style>
        #MainMenu { display: none !important; }

        footer,
        div[data-testid="stToolbar"],
        div[data-testid="stStatusWidget"],
        div[data-testid="stDecoration"] {
            display: none !important;
            height: 0 !important;
        }

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 0.5rem;
        }

        section.main > div {
            overflow: visible !important;
        }

        div[data-testid="column"] {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }

        .metric-card {
            padding: 16px;
            border-radius: 16px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.25);
            margin-bottom: 8px;
        }

        .metric-value {
            font-size: 34px;
            font-weight: 700;
            margin: 0;
        }

        .metric-label {
            font-size: 13px;
            opacity: 0.9;
            margin-top: 6px;
        }

        @media (max-width: 768px) {
            .metric-value {
                font-size: 28px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)
