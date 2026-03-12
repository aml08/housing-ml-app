import streamlit as st
import pandas as pd

st.title("🔮 Estimateur de Valeur")

if 'model' in st.session_state:
    with st.expander("📝 Paramètres du bien", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            qual = st.select_slider("Qualité (Finition)", options=range(1, 11), value=6)
            age = st.number_input("Année de construction", 1850, 2025, 2000)
        with c2:
            surf = st.number_input("Surface Habitable (m²)", 20, 500, 120)
            garage = st.radio("Garage (Nb places)", [0, 1, 2, 3], horizontal=True)
        with c3:
            bath = st.selectbox("Salles de bain", [1, 2, 3, 4])
            basement = st.number_input("Surface Sous-sol (m²)", 0, 300, 50)

    # Conversion m² vers sqft (approximation pour le dataset US)
    surf_sqft = (surf + basement) * 10.76
    age_logement = 2026 - age

    if st.button("💎 Estimer la valeur marchande"):
        input_data = pd.DataFrame([[qual, garage, surf_sqft, age_logement, bath]], 
                                 columns=['OverallQual', 'GarageCars', 'SurfaceTotale', 'AgeLogement', 'FullBath'])
        
        # Aligner les colonnes avec le modèle
        input_data = input_data[st.session_state['features']]
        prediction = st.session_state['model'].predict(input_data)[0]
        
        st.markdown("---")
        st.metric(label="Estimation du prix", value=f"{prediction:,.0f} $", delta="Prix de marché")
        st.balloons()
else:
    st.warning("Veuillez d'abord entraîner le modèle sur la page Training.")