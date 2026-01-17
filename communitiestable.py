import streamlit as st
import pandas as pd

st.set_page_config(page_title="Communities Table", layout="wide")

# Data
communities_data = """Name,Traditional_Name,Affiliation
Northlands Denesuline,Dahlu T'ua,Dene
Sayisi Dene,Tes-He-Olie Twe,Dene
Barren Lands,Kisipakamak,Cree
Marcel Colomb,Marcel Colomb,Cree
O-Pipon-Na-Piwin,O-Pipon-Na-Piwin,Cree
Mathias Colomb,Mathias Colomb,Cree
Nisichawayasihk,Nisichawayasihk,Cree
Tataskweyak,Tataskweyak,Cree
York Factory,Kischewaskahegan,Cree
War Lake,Mooseocoot,Cree
Fox Lake,Makaso Sakahigan,Cree
Shamattawa,Kisematawa,Cree
Manto Sipi,Manto Sipi,Cree
Bunibonibee,Bunibonibee,Cree
God's Lake,Manto Sakahigan,Cree
Cross Lake,Pimicikamak,Cree
Norway House,Kinosao Sipi,Cree
Opaskwayak,Opaskwayak,Cree
Mosakahiken,Mosakahiken,Cree
Misipawistik,Misipawistik,Cree
Chemawawin,Chemawawin,Cree
Sapotaweyak,Sapotaweyak,Cree
Wuskwi Sipihk,Wuskwi Sipihk,Cree
Fisher River,Ochekiwi Sipi,Cree
Red Sucker Lake,Mithkwamepin,Oji-Cree
Garden Hill,Kistiganwacheeng,Oji-Cree
Wasagamack,Wasagamack,Oji-Cree
St. Theresa Point,Minithayinikam,Oji-Cree
Poplar River,Azaadiwi-ziibiing,Ojibway
Berens River,Mememwi-ziibiing,Ojibway
Pauingassi,Pauingassi,Ojibway
Little Grand Rapids,Mishi-baawitigong,Ojibway
Bloodvein,Miskoseepi,Ojibway
Hollow Water,Wanipigow,Ojibway
Black River,Makadewaagamijiwanoonsing,Ojibway
Fort Alexander,Sagkeeng,Ojibway
Brokenhead,Baaskaandibewi-ziibiing,Ojibway
Peguis,Peguis,Ojibway
Lake St. Martin,Obashkodeyaang,Ojibway
Sandy Bay,Gaa-wiikwedaawangaag,Ojibway
Long Plain,Gaa-ginooshkodeyaag,Ojibway
Swan Lake,Gaa-biskigamaag,Ojibway
Roseau River,Bigwan Shkoo Ziibi,Ojibway
Dakota Tipi,Dakota Tipi,Dakota
Sioux Valley,Wipazoka Wakpa,Dakota"""

df = pd.read_csv(pd.io.common.StringIO(communities_data))

# Filter
affiliations = ['All'] + sorted(df['Affiliation'].unique().tolist())
selected = st.sidebar.selectbox("Filter by Affiliation", affiliations)

if selected != 'All':
    df = df[df['Affiliation'] == selected]

st.subheader(f"First Nations Communities ({len(df)})")
st.dataframe(df, use_container_width=True, hide_index=True, height=500)
