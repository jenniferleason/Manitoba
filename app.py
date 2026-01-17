import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Manitoba Indigenous Maternal Health",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 5px;
    }
    .metric-card-blue {
        background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);
    }
    .metric-card-green {
        background: linear-gradient(135deg, #43a047 0%, #2e7d32 100%);
    }
    .metric-card-orange {
        background: linear-gradient(135deg, #fb8c00 0%, #ef6c00 100%);
    }
    .metric-card-red {
        background: linear-gradient(135deg, #e53935 0%, #c62828 100%);
    }
    .metric-card-purple {
        background: linear-gradient(135deg, #8e24aa 0%, #6a1b9a 100%);
    }
    .metric-value {
        font-size: 36px;
        font-weight: bold;
        margin: 0;
    }
    .metric-label {
        font-size: 14px;
        opacity: 0.9;
        margin-top: 5px;
    }
    .section-header {
        background-color: #f8f9fa;
        padding: 10px 15px;
        border-radius: 8px;
        border-left: 4px solid #1e88e5;
        margin: 20px 0 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# DATA
# =============================================================================

# First Nations Communities
communities_data = """Name,Traditional_Name,Affiliation,Longitude,Latitude
Northlands Denesuline,Dahlu T'ua,Dene,-101.494724,58.618842
Sayisi Dene,Tes-He-Olie Twe,Dene,-98.485499,58.714481
Barren Lands,Kisipakamak,Cree,-101.640712,57.916603
Marcel Colomb,Marcel Colomb,Cree,-100.579422,56.823329
O-Pipon-Na-Piwin,O-Pipon-Na-Piwin,Cree,-98.930525,56.762525
Mathias Colomb,Mathias Colomb,Cree,-101.316876,55.741918
Nisichawayasihk,Nisichawayasihk,Cree,-98.887434,55.78362
Tataskweyak,Tataskweyak,Cree,-96.09362,56.245033
York Factory,Kischewaskahegan,Cree,-96.133096,56.074296
War Lake,Mooseocoot,Cree,-95.592906,56.070051
Fox Lake,Makaso Sakahigan,Cree,-94.077538,56.534081
Shamattawa,Kisematawa,Cree,-92.091086,55.856025
Manto Sipi,Manto Sipi,Cree,-94.056469,54.837947
Bunibonibee,Bunibonibee,Cree,-95.265839,54.949964
God's Lake,Manto Sakahigan,Cree,-94.45939,54.551483
Cross Lake,Pimicikamak,Cree,-97.753973,54.620881
Norway House,Kinosao Sipi,Cree,-97.796073,53.982033
Opaskwayak,Opaskwayak,Cree,-101.261308,53.831244
Mosakahiken,Mosakahiken,Cree,-100.318146,53.703723
Misipawistik,Misipawistik,Cree,-99.258746,53.149589
Chemawawin,Chemawawin,Cree,-99.812842,53.107416
Sapotaweyak,Sapotaweyak,Cree,-100.685118,52.701118
Wuskwi Sipihk,Wuskwi Sipihk,Cree,-101.101796,52.547805
Fisher River,Ochekiwi Sipi,Cree,-97.356313,51.424169
Red Sucker Lake,Mithkwamepin,Oji-Cree,-93.568552,54.159679
Garden Hill,Kistiganwacheeng,Oji-Cree,-94.650573,53.873498
Wasagamack,Wasagamack,Oji-Cree,-94.960916,53.882792
St. Theresa Point,Minithayinikam,Oji-Cree,-94.851849,53.815883
Poplar River,Azaadiwi-ziibiing,Ojibway,-97.28068,52.988903
Berens River,Mememwi-ziibiing,Ojibway,-97.002648,52.352983
Pauingassi,Pauingassi,Ojibway,-95.37738,52.15359
Little Grand Rapids,Mishi-baawitigong,Ojibway,-95.429825,52.008468
Bloodvein,Miskoseepi,Ojibway,-96.704568,51.790317
Hollow Water,Wanipigow,Ojibway,-96.302603,51.191642
Black River,Makadewaagamijiwanoonsing,Ojibway,-96.310215,50.830212
Fort Alexander,Sagkeeng,Ojibway,-96.27602,50.576856
Brokenhead,Baaskaandibewi-ziibiing,Ojibway,-96.619142,50.343734
Peguis,Peguis,Ojibway,-97.565095,51.310408
Lake St. Martin,Obashkodeyaang,Ojibway,-98.367508,51.730273
Sandy Bay,Gaa-wiikwedaawangaag,Ojibway,-98.667747,50.541492
Long Plain,Gaa-ginooshkodeyaag,Ojibway,-98.490188,49.845048
Swan Lake,Gaa-biskigamaag,Ojibway,-98.8413,49.397085
Roseau River,Bigwan Shkoo Ziibi,Ojibway,-97.246928,49.14836
Dakota Tipi,Dakota Tipi,Dakota,-98.350718,49.946533
Sioux Valley,Wipazoka Wakpa,Dakota,-100.497113,49.849205"""

df_communities = pd.read_csv(pd.io.common.StringIO(communities_data))

# Hospitals
hospitals_data = """Name,City,Latitude,Longitude,Level,Region
Health Sciences Centre,Winnipeg,49.9030,-97.1574,Level 3,Southern
St. Boniface Hospital,Winnipeg,49.8833,-97.0975,Level 3,Southern
Grace Hospital,Winnipeg,49.8818,-97.2459,Level 2,Southern
Victoria General Hospital,Winnipeg,49.8088,-97.1537,Level 2,Southern
Thompson General Hospital,Thompson,55.7439,-97.8328,Level 2,Northern
Flin Flon General Hospital,Flin Flon,54.7671,-101.8761,Level 1,Northern
The Pas Hospital,The Pas,53.8253,-101.2522,Level 1,Northern
Brandon Regional Health Centre,Brandon,49.8486,-99.9508,Level 2,Southern
Dauphin Regional Health Centre,Dauphin,51.1496,-100.0501,Level 1,Central
Portage District General Hospital,Portage la Prairie,49.9726,-98.2920,Level 1,Southern"""

df_hospitals = pd.read_csv(pd.io.common.StringIO(hospitals_data))

# Midwifery
midwifery_data = """Name,City,Latitude,Longitude,Region
Brandon Midwifery Services,Brandon,49.8486,-99.9508,Southern
Winkler Midwifery Services,Winkler,49.1817,-97.9414,Southern
Steinbach Midwifery Services,Steinbach,49.5258,-96.6839,Southern
Thompson Midwifery Services,Thompson,55.7439,-97.8328,Northern
Access Downtown Midwifery,Winnipeg,49.9000,-97.1380,Southern
Access River East Midwifery,Winnipeg,49.9217,-97.0533,Southern
Access Winnipeg West Midwifery,Winnipeg,49.8750,-97.2700,Southern
Mount Carmel Clinic Midwifery,Winnipeg,49.9133,-97.1350,Southern
Women's Health Clinic Birth Centre,Winnipeg,49.8683,-97.1183,Southern"""

df_midwifery = pd.read_csv(pd.io.common.StringIO(midwifery_data))

# Travel cost data
travel_cost_data = [
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

df_travel = pd.DataFrame(travel_cost_data, columns=[
    'Community', 'Affiliation', 'Clients', 'Trips', 'Cost', 'Year', 'Distance_KM', 'Road_Access', 'Fly_In'
])

community_coords = {
    'Garden Hill': (-94.650573, 53.873498),
    'Cross Lake': (-97.753973, 54.620881),
    'St. Theresa Point': (-94.851849, 53.815883),
    'Bunibonibee': (-95.265839, 54.949964),
    'Mathias Colomb': (-101.316876, 55.741918)
}

df_travel['Longitude'] = df_travel['Community'].map(lambda x: community_coords.get(x, (0,0))[0])
df_travel['Latitude'] = df_travel['Community'].map(lambda x: community_coords.get(x, (0,0))[1])

# Color mapping
affiliation_colors = {
    'Cree': '#1E88E5',
    'Oji-Cree': '#8E24AA',
    'Ojibway': '#43A047',
    'Dene': '#FB8C00',
    'Dakota': '#E53935'
}

# =============================================================================
# SIDEBAR
# =============================================================================

st.sidebar.title("Filters")

# Affiliation filter
affiliations = ['All'] + sorted(df_communities['Affiliation'].unique().tolist())
selected_affiliation = st.sidebar.selectbox("Filter by Affiliation", affiliations)

# Year filter
years = ['All Years'] + sorted(df_travel['Year'].unique().tolist())
selected_year = st.sidebar.selectbox("Fiscal Year", years)

# Community filter
communities_list = ['All'] + sorted(df_travel['Community'].unique().tolist())
selected_community = st.sidebar.selectbox("Community (Travel Data)", communities_list)

st.sidebar.markdown("---")

# Layer toggles
st.sidebar.markdown("**Map Layers**")
show_communities = st.sidebar.checkbox("Communities", value=True)
show_hospitals = st.sidebar.checkbox("Hospitals", value=True)
show_midwifery = st.sidebar.checkbox("Midwifery Clinics", value=True)
show_travel_lines = st.sidebar.checkbox("Travel Routes", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown("**Legend**")
for aff, color in affiliation_colors.items():
    st.sidebar.markdown(f'<span style="color:{color};">●</span> {aff}', unsafe_allow_html=True)
st.sidebar.markdown('<span style="color:red;">▲</span> Hospital', unsafe_allow_html=True)
st.sidebar.markdown('<span style="color:green;">▲</span> Midwifery', unsafe_allow_html=True)

# =============================================================================
# APPLY FILTERS TO ALL DATA
# =============================================================================

# Filter communities
if selected_affiliation != 'All':
    df_communities_filtered = df_communities[df_communities['Affiliation'] == selected_affiliation]
else:
    df_communities_filtered = df_communities.copy()

# Filter travel data
df_travel_filtered = df_travel.copy()

if selected_affiliation != 'All':
    df_travel_filtered = df_travel_filtered[df_travel_filtered['Affiliation'] == selected_affiliation]

if selected_year != 'All Years':
    df_travel_filtered = df_travel_filtered[df_travel_filtered['Year'] == selected_year]

if selected_community != 'All':
    df_travel_filtered = df_travel_filtered[df_travel_filtered['Community'] == selected_community]

# =============================================================================
# HEADER
# =============================================================================

st.title("Manitoba Indigenous Maternal Health")

# =============================================================================
# METRIC CARDS
# =============================================================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="metric-card metric-card-blue">
        <p class="metric-value">{len(df_communities_filtered)}</p>
        <p class="metric-label">Communities</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card metric-card-red">
        <p class="metric-value">{len(df_hospitals)}</p>
        <p class="metric-label">Hospitals</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card metric-card-green">
        <p class="metric-value">{len(df_midwifery)}</p>
        <p class="metric-label">Midwifery Clinics</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    total_cost = df_travel_filtered['Cost'].sum()
    if total_cost >= 1000000:
        cost_display = f"${total_cost/1000000:.1f}M"
    else:
        cost_display = f"${total_cost/1000:.0f}K"
    st.markdown(f"""
    <div class="metric-card metric-card-orange">
        <p class="metric-value">{cost_display}</p>
        <p class="metric-label">Travel Costs</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    if len(df_travel_filtered) > 0:
        avg_dist = df_travel_filtered.groupby('Community')['Distance_KM'].first().mean()
    else:
        avg_dist = 0
    st.markdown(f"""
    <div class="metric-card metric-card-purple">
        <p class="metric-value">{avg_dist:.0f} km</p>
        <p class="metric-label">Avg Distance</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# MAP
# =============================================================================

st.markdown('<div class="section-header"><strong>Map</strong></div>', unsafe_allow_html=True)

m = folium.Map(
    location=[54.0, -98.0],
    zoom_start=5,
    tiles='CartoDB positron'
)

m.fit_bounds([[49.0, -102.0], [60.0, -89.0]])

# Communities
if show_communities:
    for idx, row in df_communities_filtered.iterrows():
        color = affiliation_colors.get(row['Affiliation'], '#666666')
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=8,
            color=color,
            weight=2,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip=f"{row['Name']} ({row['Affiliation']})"
        ).add_to(m)

# Hospitals
if show_hospitals:
    for idx, row in df_hospitals.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f"{row['Name']} - {row['Level']}",
            icon=folium.Icon(color='red', icon='plus', prefix='fa')
        ).add_to(m)

# Midwifery
if show_midwifery:
    for idx, row in df_midwifery.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon=folium.Icon(color='green', icon='user', prefix='fa')
        ).add_to(m)

# Travel lines
if show_travel_lines and len(df_travel_filtered) > 0:
    winnipeg = [49.9030, -97.1574]
    travel_summary = df_travel_filtered.groupby('Community').agg({
        'Cost': 'sum', 'Latitude': 'first', 'Longitude': 'first'
    }).reset_index()
    
    for idx, row in travel_summary.iterrows():
        folium.PolyLine(
            locations=[[row['Latitude'], row['Longitude']], winnipeg],
            color='#D32F2F',
            weight=3,
            opacity=0.6,
            tooltip=f"{row['Community']}: ${row['Cost']:,.0f}"
        ).add_to(m)

st_folium(m, width=1100, height=450, returned_objects=[])

# =============================================================================
# CHARTS
# =============================================================================

st.markdown('<div class="section-header"><strong>Analytics</strong></div>', unsafe_allow_html=True)

# Row 1: Two charts
col1, col2 = st.columns(2)

with col1:
    aff_counts = df_communities_filtered['Affiliation'].value_counts().reset_index()
    aff_counts.columns = ['Affiliation', 'Count']
    
    fig1 = go.Figure(data=[go.Pie(
        labels=aff_counts['Affiliation'],
        values=aff_counts['Count'],
        hole=0.5,
        marker_colors=[affiliation_colors.get(a, '#666') for a in aff_counts['Affiliation']]
    )])
    fig1.update_layout(
        title='Communities by Affiliation',
        height=350,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    if len(df_travel_filtered) > 0:
        cost_by_community = df_travel_filtered.groupby('Community')['Cost'].sum().reset_index()
        cost_by_community = cost_by_community.sort_values('Cost', ascending=True)
        
        fig2 = go.Figure(data=[go.Bar(
            x=cost_by_community['Cost'],
            y=cost_by_community['Community'],
            orientation='h',
            marker_color='#E53935',
            text=[f"${x:,.0f}" for x in cost_by_community['Cost']],
            textposition='outside'
        )])
        fig2.update_layout(
            title='Travel Costs by Community',
            height=350,
            xaxis_title='Cost ($)',
            yaxis_title='',
            margin=dict(l=10, r=100)
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No travel data for selected filters")

# Row 2: Trend
if len(df_travel_filtered) > 0:
    yearly = df_travel_filtered.groupby('Year').agg({'Cost': 'sum', 'Clients': 'sum', 'Trips': 'sum'}).reset_index()
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=yearly['Year'], y=yearly['Cost'],
        mode='lines+markers', name='Cost',
        line=dict(color='#E53935', width=3),
        marker=dict(size=10)
    ))
    fig3.update_layout(
        title='Travel Costs Over Time',
        height=300,
        xaxis_title='Fiscal Year',
        yaxis_title='Cost ($)',
        hovermode='x unified'
    )
    st.plotly_chart(fig3, use_container_width=True)

# Row 3: Clients and Trips
if len(df_travel_filtered) > 0:
    col1, col2 = st.columns(2)
    
    with col1:
        clients = df_travel_filtered.groupby('Community')['Clients'].sum().reset_index()
        clients = clients.sort_values('Clients', ascending=False)
        
        fig4 = go.Figure(data=[go.Bar(
            x=clients['Community'], y=clients['Clients'],
            marker_color='#1E88E5',
            text=clients['Clients'], textposition='outside'
        )])
        fig4.update_layout(title='Total Clients by Community', height=300, xaxis_title='', yaxis_title='Clients')
        st.plotly_chart(fig4, use_container_width=True)
    
    with col2:
        trips = df_travel_filtered.groupby('Community')['Trips'].sum().reset_index()
        trips = trips.sort_values('Trips', ascending=False)
        
        fig5 = go.Figure(data=[go.Bar(
            x=trips['Community'], y=trips['Trips'],
            marker_color='#43A047',
            text=trips['Trips'], textposition='outside'
        )])
        fig5.update_layout(title='Total Trips by Community', height=300, xaxis_title='', yaxis_title='Trips')
        st.plotly_chart(fig5, use_container_width=True)

# =============================================================================
# TABLES
# =============================================================================

st.markdown('<div class="section-header"><strong>Data Tables</strong></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Communities", "Hospitals", "Midwifery", "Travel Costs"])

with tab1:
    st.dataframe(df_communities_filtered[['Name', 'Traditional_Name', 'Affiliation']], use_container_width=True, hide_index=True, height=300)

with tab2:
    st.dataframe(df_hospitals[['Name', 'City', 'Level', 'Region']], use_container_width=True, hide_index=True, height=300)

with tab3:
    st.dataframe(df_midwifery[['Name', 'City', 'Region']], use_container_width=True, hide_index=True, height=300)

with tab4:
    if len(df_travel_filtered) > 0:
        df_display = df_travel_filtered.copy()
        df_display['Cost'] = df_display['Cost'].apply(lambda x: f"${x:,.0f}")
        st.dataframe(df_display[['Community', 'Year', 'Clients', 'Trips', 'Cost', 'Distance_KM', 'Road_Access', 'Fly_In']], use_container_width=True, hide_index=True, height=300)
    else:
        st.info("No data for selected filters")

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.caption("Data: Manitoba First Nations Education Resource Centre, Manitoba Health, NIHB MTRS | Project: IDEA - University of Calgary")
