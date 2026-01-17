import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Communities by Affiliation", layout="wide")

# Data
data = {
    'Affiliation': ['Cree', 'Ojibway', 'Oji-Cree', 'Dene', 'Dakota'],
    'Count': [21, 17, 4, 2, 2]
}

colors = {
    'Cree': '#1E88E5',
    'Oji-Cree': '#8E24AA',
    'Ojibway': '#43A047',
    'Dene': '#FB8C00',
    'Dakota': '#E53935'
}

fig = go.Figure(data=[go.Pie(
    labels=data['Affiliation'],
    values=data['Count'],
    hole=0.5,
    marker_colors=[colors[a] for a in data['Affiliation']],
    textinfo='label+value',
    textposition='outside'
)])

fig.update_layout(
    title='First Nations Communities by Affiliation',
    height=450,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)
