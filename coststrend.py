import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Costs Over Time", layout="wide")

# Data
yearly_data = {
    'Year': ['2018/2019', '2019/2020', '2020/2021', '2021/2022', '2022/2023', '2023/2024', '2024/2025'],
    'Cost': [2537758, 3105949, 3026468, 2727894, 2832575, 2473186, 2879973],
    'Clients': [993, 1024, 830, 747, 790, 763, 631],
    'Trips': [2832, 2954, 1839, 1592, 1444, 1309, 1136]
}

df = pd.DataFrame(yearly_data)

# Metric selector
metric = st.sidebar.selectbox("Select Metric", ['Cost', 'Clients', 'Trips'])

colors = {'Cost': '#E53935', 'Clients': '#1E88E5', 'Trips': '#43A047'}

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df[metric],
    mode='lines+markers',
    line=dict(color=colors[metric], width=3),
    marker=dict(size=12),
    fill='tozeroy',
    fillcolor=f'rgba{tuple(list(int(colors[metric].lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.1])}'
))

title_map = {'Cost': 'Travel Costs Over Time', 'Clients': 'Clients Over Time', 'Trips': 'Trips Over Time'}
yaxis_map = {'Cost': 'Cost ($)', 'Clients': 'Number of Clients', 'Trips': 'Number of Trips'}

fig.update_layout(
    title=title_map[metric],
    height=400,
    xaxis_title='Fiscal Year',
    yaxis_title=yaxis_map[metric],
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)
