# 🏠 Immo Predict Pro - Application Multi-Pages

Cette application de Machine Learning permet d'explorer les données immobilières et d'estimer le prix de vente des logements en fonction de leurs caractéristiques.

## 🏗️ Architecture du Projet
Le projet respecte une structure professionnelle pour garantir la modularité :
- **`app.py`** : Point d'entrée avec authentification et menu de navigation.
- **`pages/1_Data.py`** : Exploration interactive avec 4 graphiques dynamiques et filtres.
- **`pages/2_Training.py`** : Entraînement d'un modèle Gradient Boosting avec interprétation du score $R^2$.
- **`pages/3_Prediction.py`** : Interface de saisie utilisateur pour l'estimation de prix.
- **`utils/model_utils.py`** : Logique métier (nettoyage et entraînement du modèle).

## 🔒 Sécurisation et Déploiement
- **Authentification** : Accès restreint par mot de passe via `st.secrets`.
- **Validation** : Contrôle des entrées utilisateurs (min/max) pour éviter les erreurs de prédiction.
- **Sécurité réseau** : Déploiement via Streamlit Cloud avec protocole HTTPS activé 🔒.
- **Gestion des logs** : Monitoring des événements d'entraînement et de prédiction.

## 🚀 Installation locale
1. Cloner le dépôt.
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt