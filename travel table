import streamlit as st
import pandas as pd

st.set_page_config(page_title="Travel Costs Table", layout="wide")

# Data
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

# Filters
col1, col2, col3 = st.sidebar.columns([1,1,1])

communities = ['All'] + sorted(df['Community'].unique().tolist())
selected_community = st.sidebar.selectbox("Community", communities)

years = ['All'] + sorted(df['Year'].unique().tolist())
selected_year = st.sidebar.selectbox("Year", years)

affiliations = ['All'] + sorted(df['Affiliation'].unique().tolist())
selected_affiliation = st.sidebar.selectbox("Affiliation", affiliations)

# Apply filters
if selected_community != 'All':
    df = df[df['Community'] == selected_community]
if selected_year != 'All':
    df = df[df['Year'] == selected_year]
if selected_affiliation != 'All':
    df = df[df['Affiliation'] == selected_affiliation]

# Format cost
df_display = df.copy()
df_display['Cost'] = df_display['Cost'].apply(lambda x: f"${x:,}")

st.subheader(f"Travel Cost Data ({len(df)} records)")
st.dataframe(df_display, use_container_width=True, hide_index=True, height=500)

# Summary
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("Total Cost", f"${df['Cost'].sum():,}")
col2.metric("Total Clients", f"{df['Clients'].sum():,}")
col3.metric("Total Trips", f"{df['Trips'].sum():,}")
