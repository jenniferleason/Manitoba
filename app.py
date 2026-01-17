import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Map", layout="wide")

# Data
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

hospitals_data = """Name,City,Latitude,Longitude,Level
Health Sciences Centre,Winnipeg,49.9030,-97.1574,Level 3
St. Boniface Hospital,Winnipeg,49.8833,-97.0975,Level 3
Thompson General Hospital,Thompson,55.7439,-97.8328,Level 2
Flin Flon General Hospital,Flin Flon,54.7671,-101.8761,Level 1
The Pas Hospital,The Pas,53.8253,-101.2522,Level 1
Brandon Regional Health Centre,Brandon,49.8486,-99.9508,Level 2"""

df_hospitals = pd.read_csv(pd.io.common.StringIO(hospitals_data))

midwifery_data = """Name,City,Latitude,Longitude
Thompson Midwifery Services,Thompson,55.7439,-97.8328
Access Downtown Midwifery,Winnipeg,49.9000,-97.1380
Women's Health Clinic Birth Centre,Winnipeg,49.8683,-97.1183"""

df_midwifery = pd.read_csv(pd.io.common.StringIO(midwifery_data))

affiliation_colors = {
    'Cree': '#1E88E5',
    'Oji-Cree': '#8E24AA',
    'Ojibway': '#43A047',
    'Dene': '#FB8C00',
    'Dakota': '#E53935'
}

# Sidebar
st.sidebar.markdown("**Layers**")
show_communities = st.sidebar.checkbox("Communities", value=True)
show_hospitals = st.sidebar.checkbox("Hospitals", value=True)
show_midwifery = st.sidebar.checkbox("Midwifery", value=True)

affiliations = ['All'] + sorted(df_communities['Affiliation'].unique().tolist())
selected_affiliation = st.sidebar.selectbox("Affiliation", affiliations)

if selected_affiliation != 'All':
    df_communities = df_communities[df_communities['Affiliation'] == selected_affiliation]

# Map
m = folium.Map(location=[54.0, -98.0], zoom_start=5, tiles='CartoDB positron')
m.fit_bounds([[49.0, -102.0], [60.0, -89.0]])

if show_communities:
    for idx, row in df_communities.iterrows():
        color = affiliation_colors.get(row['Affiliation'], '#666')
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=8, color=color, weight=2,
            fill=True, fill_color=color, fill_opacity=0.7,
            tooltip=f"{row['Name']} ({row['Affiliation']})"
        ).add_to(m)

if show_hospitals:
    for idx, row in df_hospitals.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=f"{row['Name']} - {row['Level']}",
            icon=folium.Icon(color='red', icon='plus', prefix='fa')
        ).add_to(m)

if show_midwifery:
    for idx, row in df_midwifery.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            tooltip=row['Name'],
            icon=folium.Icon(color='green', icon='user', prefix='fa')
        ).add_to(m)

st_folium(m, width=1000, height=600, returned_objects=[])
