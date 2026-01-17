import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Distance vs Travel Costs", layout="wide")

# Data (same as yours)
data = {
    'Community': ['Garden Hill', 'St. Theresa Point', 'Cross Lake', 'Mathias Colomb', 'Bunibonibee'],
    'Distance_KM': [485, 510, 525, 680, 450],
    'Total_Cost': [4861843, 4625426, 3265187, 3687653, 3143694],
    'Total_Trips': [1647, 1739, 5094, 2082, 2544],
    'Fly_In': ['Yes', 'Yes', 'No', 'Partial', 'No']
}
df = pd.DataFrame(data)

df['Cost_pretty'] = df['Total_Cost'].apply(lambda x: f"${x:,.0f}")
df['Trips_pretty'] = df['Total_Trips'].apply(lambda x: f"{x:,}")

st.title("Distance vs Total Travel Costs")
st.caption("Bubble size = number of trips | Color = access type")

fig = px.scatter(
    df,
    x='Distance_KM',
    y='Total_Cost',
    size='Total_Trips',
    color='Fly_In',
    hover_name='Community',
    color_discrete_map={'Yes': '#dc2626', 'No': '#2563eb', 'Partial': '#d97706'},
    size_max=65,
    opacity=0.85
)

fig.update_traces(
    hovertemplate=(
        "<b>%{hovertext}</b><br>" +
        "Distance: %{x:,} km<br>" +
        "Cost: %{customdata[0]}<br>" +
        "Trips: %{customdata[1]}<extra></extra>"
    ),
    customdata=df[['Cost_pretty', 'Trips_pretty']].values,
    marker=dict(line=dict(width=1.5, color='white'))
)

# Add subtle trend line
fig.add_trace(
    go.Scatter(
        x=df['Distance_KM'], y=df['Total_Cost'],
        mode='lines', line=dict(color='gray', dash='dot', width=1.5),
        name='Trend', hoverinfo='skip', showlegend=False
    )
)

fig.update_layout(
    height=650,
    xaxis_title="Distance to Winnipeg (km)",
    yaxis_title="Total Estimated Travel Cost ($)",
    legend_title="Access Type",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    plot_bgcolor="#f9fafb",
    paper_bgcolor="white",
    font=dict(family="Segoe UI, Arial", size=14),
    margin=dict(l=60, r=40, t=80, b=60),
    hoverlabel=dict(bgcolor="white", font_size=14)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("**Insight**: Fly-in communities (red) tend to have higher costs even at similar distances due to air transport expenses.")
