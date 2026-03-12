import streamlit as st

# 1. LA SÉCURITÉ : Vérifier le mot de passe
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    if st.text_input("Mot de passe", type="password") == st.secrets["PASSWORD"]:
        st.session_state["authenticated"] = True
        st.rerun()
    else:
        st.error("Accès réservé")

if not st.session_state["authenticated"]:
    login()
    st.stop() # Arrête l'app ici si pas de mot de passe

# 2. TON APPLICATION (Le code que tu avais déjà)
st.title("🏠 Système Expert Immobilier")
st.write("Bienvenue dans l'accès sécurisé !")
# ... remets ici la suite de ton code app.py original
