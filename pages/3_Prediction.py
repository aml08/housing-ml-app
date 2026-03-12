import streamlit as st
import pandas as pd
import joblib 
from utils.model_utils import clean_data

# --- 1. SÉCURISATION DE LA PAGE ---
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("🔒 Accès refusé. Veuillez vous connecter sur la page d'accueil.")
    st.stop()

# --- 2. CONFIGURATION ---
st.title("🔮 Prédiction du Prix Immobilier")
st.write("Saisissez les caractéristiques du bien pour obtenir une estimation.")

# --- 3. VALIDATION DES ENTRÉES (Sécurité des données) ---
# On utilise min_value et max_value pour empêcher les données absurdes
with st.form("prediction_form"):
    st.subheader("Caractéristiques du bien")
    
    col1, col2 = st.columns(2)
    
    with col1:
        surface = st.number_input("Surface habitable (m²)", min_value=10, max_value=1000, value=100, step=1)
        qualite = st.slider("Qualité globale des finitions (1-10)", min_value=1, max_value=10, value=5)
    
    with col2:
        pieces = st.number_input("Nombre de pièces", min_value=1, max_value=20, value=4, step=1)
        annee = st.number_input("Année de construction", min_value=1800, max_value=2026, value=2000, step=1)

    submit = st.form_submit_button("Calculer l'estimation")

# --- 4. LOGIQUE DE PRÉDICTION ---
if submit:
    try:
        # Création d'un dictionnaire avec les entrées validées
        input_data = {
            'GrLivArea': surface,
            'OverallQual': qualite,
            'TotRmsAbvGrd': pieces,
            'YearBuilt': annee
        }
        
        # Simulation de la prédiction (Remplace par ton vrai modèle chargé)
        # exemple : model = joblib.load('models/model.pkl')
        # prediction = model.predict(pd.DataFrame([input_data]))[0]
        
        # Pour l'exemple, on affiche une réussite
        st.success(f"✅ Analyse terminée !")
        st.metric(label="Prix estimé", value=f"{surface * qualite * 200:,.0f} €")
        
        # LOGS : On affiche un message dans la console de gestion (Manage App)
        print(f"LOG: Prédiction effectuée pour {surface}m2 - Statut: Succès")

    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
        print(f"LOG: Erreur de prédiction - {e}")

st.info("💡 Note : Les logs de cette opération sont consultables dans la console Streamlit Cloud.")

