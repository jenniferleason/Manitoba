import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Distance vs Cost", layout="wide")

# Data
data = {
    'Community': ['Garden Hill', 'St. Theresa Point', 'Cross Lake', 'Mathias Colomb', 'Bunibonibee'],
    'Distance_KM': [485, 510, 525, 680, 450],
    'Total_Cost': [4861843, 4625426, 3265187, 3687653, 3143694],
    'Total_Trips': [1647, 1739, 5094, 2082, 2544],
    'Fly_In': ['Yes', 'Yes', 'No', 'Partial', 'No']
}

df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x='Distance_KM',
    y='Total_Cost',
    size='Total_Trips',
    color='Fly_In',
    hover_name='Community',
    color_discrete_map={'Yes': '#E53935', 'No': '#1E88E5', 'Partial': '#FB8C00'},
    labels={
        'Distance_KM': 'Distance to Winnipeg (km)',
        'Total_Cost': 'Total Cost ($)',
        'Fly_In': 'Fly-In Only'
    }
)

fig.update_traces(marker=dict(line=dict(width=2, color='white')))

fig.update_layout(
    title='Distance vs Travel Costs',
    height=500,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)
