import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Immo Predict Pro", page_icon="🏠")

# --- 1. SYSTÈME DE SÉCURITÉ ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    # On crée le champ de saisie
    pwd = st.text_input("Veuillez entrer le mot de passe pour accéder à l'application", type="password")
    if st.button("Se connecter"):
        if pwd == st.secrets["PASSWORD"]:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("❌ Mot de passe incorrect")

# --- 2. VÉRIFICATION ---
if not st.session_state["authenticated"]:
    st.title("🔐 Accès Restreint")
    login()
    st.stop()  # On bloque tout ici si pas de mot de passe

# --- 3. CONTENU DE L'APPLICATION (Une fois connecté) ---
st.title("🏠 Système Expert Immobilier")
st.success("✅ Connexion réussie. Bienvenue dans l'interface sécurisée.")

st.markdown("""
### Bienvenue sur Immo Predict Pro !
Cette application est un outil d'aide à la décision pour le marché immobilier. 
Elle utilise le **Machine Learning** pour analyser les données et prédire les prix.

**Utilisez le menu à gauche pour naviguer :**
* 📊 **Data** : Explorez les données de ventes passées.
* ⚙️ **Training** : Entraînez le modèle d'intelligence artificielle.
* 🔮 **Prediction** : Estimez le prix d'un bien en temps réel.

---
*Développé dans le cadre du projet IA M2 DS - Sécurisation HTTPS & Authentification active.*
""")
