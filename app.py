import streamlit as st

st.set_page_config(page_title="Immo Predict Pro", page_icon="🏠", layout="wide")

# CSS pour personnaliser les boutons et le titre
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #7030A0; color: white; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Système Expert Immobilier")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### 🧭 Workflow de l'application :
    1. **Exploration** : Chargez votre CSV et analysez les tendances du marché.
    2. **Entraînement** : Configurez et lancez l'apprentissage du modèle.
    3. **Prédiction** : Utilisez l'interface interactive pour estimer un prix.
    """)
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/609/609036.png", width=200)