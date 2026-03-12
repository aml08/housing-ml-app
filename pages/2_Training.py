import streamlit as st
import plotly.graph_objects as go
from utils.model_utils import clean_data, train_and_save_model
import time

st.title("⚙️ Engine Room : Entraînement")

if 'df_raw' in st.session_state:
    if st.button("🚀 Lancer l'apprentissage du Gradient Boosting"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Optimisation des hyperparamètres... {percent_complete+1}%")
            
        df_clean = clean_data(st.session_state['df_raw'])
        model, cols, score = train_and_save_model(df_clean)
        
        st.session_state['model'] = model
        st.session_state['features'] = cols
        
        st.success("Entraînement terminé !")
        
        # Jauge de performance
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score * 100,
            title = {'text': "Précision du Modèle (R² %)"},
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#7030A0"}}
        ))
        st.plotly_chart(fig_gauge)
else:
    st.error("Données manquantes. Retournez à la page Data.")

#bloc de sécurité
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("Veuillez vous connecter sur la page d'accueil (app) pour accéder à cette page.")
    st.stop()

