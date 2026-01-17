import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Travel Costs", layout="wide")

# Data
travel_data = {
    'Community': ['Garden Hill', 'St. Theresa Point', 'Cross Lake', 'Mathias Colomb', 'Bunibonibee'],
    'Total_Cost': [4861843, 4625426, 3265187, 3687653, 3143694],
    'Affiliation': ['Oji-Cree', 'Oji-Cree', 'Cree', 'Cree', 'Cree']
}

df = pd.DataFrame(travel_data)
df = df.sort_values('Total_Cost', ascending=True)

# Sidebar filter
affiliations = ['All'] + sorted(df['Affiliation'].unique().tolist())
selected = st.sidebar.selectbox("Filter by Affiliation", affiliations)

if selected != 'All':
    df = df[df['Affiliation'] == selected]

# Chart
fig = go.Figure(data=[go.Bar(
    x=df['Total_Cost'],
    y=df['Community'],
    orientation='h',
    marker_color='#E53935',
    text=[f"${x:,.0f}" for x in df['Total_Cost']],
    textposition='outside'
)])

fig.update_layout(
    title='Total Travel Costs by Community (2018-2025)',
    height=400,
    xaxis_title='Cost ($)',
    yaxis_title='',
    margin=dict(l=10, r=120, t=50, b=50)
)

st.plotly_chart(fig, use_container_width=True)
