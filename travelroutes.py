import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Travel Routes", layout="wide")

# Community data with costs
communities = {
    'Garden Hill': {'lat': 53.873498, 'lon': -94.650573, 'cost': 4861843, 'distance': 485},
    'Cross Lake': {'lat': 54.620881, 'lon': -97.753973, 'cost': 3265187, 'distance': 525},
    'St. Theresa Point': {'lat': 53.815883, 'lon': -94.851849, 'cost': 4625426, 'distance': 510},
    'Bunibonibee': {'lat': 54.949964, 'lon': -95.265839, 'cost': 3143694, 'distance': 450},
    'Mathias Colomb': {'lat': 55.741918, 'lon': -101.316876, 'cost': 3687653, 'distance': 680}
}

winnipeg = [49.9030, -97.1574]

# Map
m = folium.Map(location=[53.5, -97.0], zoom_start=5, tiles='CartoDB positron')
m.fit_bounds([[49.0, -102.0], [57.0, -89.0]])

# Add Winnipeg hospital
folium.Marker(
    location=winnipeg,
    tooltip="Health Sciences Centre - Winnipeg",
    icon=folium.Icon(color='red', icon='plus', prefix='fa')
).add_to(m)

# Add communities and travel lines
max_cost = max(c['cost'] for c in communities.values())

for name, data in communities.items():
    # Circle for community
    folium.CircleMarker(
        location=[data['lat'], data['lon']],
        radius=10,
        color='#1E88E5',
        weight=2,
        fill=True,
        fill_color='#1E88E5',
        fill_opacity=0.7,
        tooltip=f"{name}: ${data['cost']:,} ({data['distance']} km)"
    ).add_to(m)
    
    # Line to Winnipeg
    weight = 2 + (data['cost'] / max_cost) * 5
    folium.PolyLine(
        locations=[[data['lat'], data['lon']], winnipeg],
        color='#D32F2F',
        weight=weight,
        opacity=0.6,
        tooltip=f"{name} → Winnipeg: {data['distance']} km"
    ).add_to(m)

# Winnipeg label
folium.map.Marker(
    location=[49.6, -97.15],
    icon=folium.DivIcon(html='<div style="font-size:12px;font-weight:bold;color:#C62828;">WINNIPEG</div>')
).add_to(m)

st_folium(m, width=1000, height=550, returned_objects=[])
