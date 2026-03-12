import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("💾 Exploration des Données")

# Chemin vers le fichier local
DATA_PATH = "data/train.csv"
@st.cache_data
def get_local_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        # Petit nettoyage pour l'affichage
        df['SurfaceTotale'] = df['GrLivArea'] + df['TotalBsmtSF']
        return df
    else:
        st.error(f"Fichier {DATA_PATH} introuvable. Vérifiez votre dossier 'data/'.")
        return None

# Chargement automatique
df = get_local_data()

if df is not None:
    # On stocke dans la session pour les autres pages
    st.session_state['df_raw'] = df
    
    # --- FILTRES SIDEBAR --- (On garde les filtres pour l'interactivité)
    st.sidebar.header("🔍 Filtres")
    selected_nb = st.sidebar.multiselect("Quartiers", options=df['Neighborhood'].unique(), default=df['Neighborhood'].unique()[:5])
    
    df_filtered = df[df['Neighborhood'].isin(selected_nb)]

    min_p, max_p = int(df['SalePrice'].min()), int(df['SalePrice'].max())
    price_range = st.sidebar.slider("Plage de prix ($)", min_p, max_p, (min_p, max_p))

    # --- AFFICHAGE DES 4 GRAPHIQUES ---
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(df_filtered, x="SalePrice", title="Distribution Prix"), use_container_width=True)
    with col2:
        st.plotly_chart(px.scatter(df_filtered, x="SurfaceTotale", y="SalePrice", color="OverallQual", title="Surface vs Prix"), use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(px.box(df_filtered, x="Neighborhood", y="SalePrice", title="Prix par Quartier"), use_container_width=True)
    with col4:
        avg_p = df_filtered.groupby("OverallQual")["SalePrice"].mean().reset_index()

        st.plotly_chart(px.bar(avg_p, x="OverallQual", y="SalePrice", title="Prix Moyen / Qualité"), use_container_width=True)

