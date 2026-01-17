import streamlit as st
import pandas as pd

st.set_page_config(page_title="Travel Costs Table – Manitoba First Nations", layout="wide")

# ── Custom CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        margin: 0 8px;
    }
    .metric-value { font-size: 36px; font-weight: bold; margin: 0; }
    .metric-label { font-size: 14px; color: #4b5563; margin-top: 6px; }
    .stDataFrame [data-testid="stTable"] {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    .stDataFrame th { background-color: #1e40af !important; color: white !important; font-weight: bold; }
    .stDataFrame tr:hover { background-color: #f1f5f9 !important; }
</style>
""", unsafe_allow_html=True)

# ── Full Data ───────────────────────────────────────────────────────────
travel_data = [
    ('Garden Hill', 'Oji-Cree', 154, 293, 613982, '2018/2019', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 171, 323, 703851, '2019/2020', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 140, 204, 828735, '2020/2021', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 139, 202, 710473, '2021/2022', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 158, 243, 664229, '2022/2023', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 143, 208, 702710, '2023/2024', 485, 'No', 'Yes'),
    ('Garden Hill', 'Oji-Cree', 119, 174, 637863, '2024/2025', 485, 'No', 'Yes'),
    ('Cross Lake', 'Cree', 362, 1282, 417828, '2018/2019', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 365, 1377, 446559, '2019/2020', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 284, 787, 399227, '2020/2021', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 225, 531, 360245, '2021/2022', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 230, 397, 500840, '2022/2023', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 249, 419, 505914, '2023/2024', 525, 'Yes', 'No'),
    ('Cross Lake', 'Cree', 174, 301, 634574, '2024/2025', 525, 'Yes', 'No'),
    ('St. Theresa Point', 'Oji-Cree', 165, 376, 639100, '2018/2019', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 172, 351, 802703, '2019/2020', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 135, 171, 675306, '2020/2021', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 142, 220, 724292, '2021/2022', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 159, 296, 835818, '2022/2023', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 106, 160, 368480, '2023/2024', 510, 'No', 'Yes'),
    ('St. Theresa Point', 'Oji-Cree', 106, 165, 579727, '2024/2025', 510, 'No', 'Yes'),
    ('Bunibonibee', 'Cree', 171, 545, 434700, '2018/2019', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 160, 519, 520741, '2019/2020', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 129, 412, 492477, '2020/2021', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 116, 345, 415147, '2021/2022', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 104, 183, 338498, '2022/2023', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 119, 241, 385893, '2023/2024', 450, 'Yes', 'No'),
    ('Bunibonibee', 'Cree', 130, 299, 556238, '2024/2025', 450, 'Yes', 'No'),
    ('Mathias Colomb', 'Cree', 141, 336, 432148, '2018/2019', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 156, 384, 632095, '2019/2020', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 142, 265, 630723, '2020/2021', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 125, 294, 517737, '2021/2022', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 139, 325, 493190, '2022/2023', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 146, 281, 510189, '2023/2024', 680, 'Seasonal', 'Partial'),
    ('Mathias Colomb', 'Cree', 112, 197, 471571, '2024/2025', 680, 'Seasonal', 'Partial'),
]

df = pd.DataFrame(travel_data, columns=[
    'Community', 'Affiliation', 'Clients', 'Trips', 'Cost', 'Year', 'Distance_KM', 'Road_Access', 'Fly_In'
])

# ── Sidebar Filters ─────────────────────────────────────────────────────
with st.sidebar.expander("Filters", expanded=True):
    communities = ['All'] + sorted(df['Community'].unique().tolist())
    selected_community = st.selectbox("Community", communities)

    years = ['All'] + sorted(df['Year'].unique().tolist())
    selected_year = st.selectbox("Fiscal Year", years)

    affiliations = ['All'] + sorted(df['Affiliation'].unique().tolist())
    selected_affiliation = st.selectbox("Affiliation", affiliations)

# ── Apply filters ───────────────────────────────────────────────────────
df_filtered = df.copy()
if selected_community != 'All':
    df_filtered = df_filtered[df_filtered['Community'] == selected_community]
if selected_year != 'All':
    df_filtered = df_filtered[df_filtered['Year'] == selected_year]
if selected_affiliation != 'All':
    df_filtered = df_filtered[df_filtered['Affiliation'] == selected_affiliation]

# ── Format numbers correctly for display ────────────────────────────────
df_display = df_filtered.copy()
df_display['Cost'] = df_display['Cost'].apply(lambda x: f"${x:,.0f}")
df_display['Clients'] = df_display['Clients'].apply(lambda x: f"{x:,}")
df_display['Trips'] = df_display['Trips'].apply(lambda x: f"{x:,}")
df_display['Distance_KM'] = df_display['Distance_KM'].apply(lambda x: f"{x:,}")

# ── Header & Metrics Cards ──────────────────────────────────────────────
st.title("Medical Travel Costs – Manitoba First Nations")
st.caption("NIHB transportation data for maternal evacuations | Filter to explore")

col1, col2, col3 = st.columns(3)
with col1:
    total_cost = df_filtered['Cost'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${total_cost:,.0f}</div>
        <div class="metric-label">Total Travel Cost</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    total_clients = df_filtered['Clients'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_clients:,}</div>
        <div class="metric-label">Total Clients</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_trips = df_filtered['Trips'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_trips:,}</div>
        <div class="metric-label">Total Trips</div>
    </div>
    """, unsafe_allow_html=True)

# ── Filtered Table ──────────────────────────────────────────────────────
st.markdown("### Filtered Travel Data")

st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True,
    height=550,
    column_config={
        "Cost": st.column_config.TextColumn("Cost"),
        "Clients": st.column_config.TextColumn("Clients"),
        "Trips": st.column_config.TextColumn("Trips"),
        "Community": st.column_config.TextColumn("Community"),
        "Affiliation": st.column_config.TextColumn("Affiliation"),
        "Year": st.column_config.TextColumn("Year"),
        "Distance_KM": st.column_config.TextColumn("Distance (km)"),
        "Road_Access": st.column_config.TextColumn("Road Access"),
        "Fly_In": st.column_config.TextColumn("Fly-In")
    }
)

# ── Export Button ───────────────────────────────────────────────────────
csv = df_display.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name="travel_costs_filtered.csv",
    mime="text/csv"
)

if df_filtered.empty:
    st.warning("No records match the selected filters.")
else:
    st.success(f"Showing {len(df_filtered)} records")
