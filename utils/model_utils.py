import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.impute import SimpleImputer
import joblib

def clean_data(df):
    # On garde les colonnes numériques principales pour simplifier la prédiction
    cols = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt', 'SalePrice']
    df = df[cols].dropna()
    # Feature engineering rapide
    df['SurfaceTotale'] = df['GrLivArea'] + df['TotalBsmtSF']
    df['AgeLogement'] = 2026 - df['YearBuilt']
    return df.drop(['YearBuilt', 'GrLivArea', 'TotalBsmtSF'], axis=1)

@st.cache_resource
def train_and_save_model(df):
    X = df.drop('SalePrice', axis=1)
    y = df['SalePrice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = GradientBoostingRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    # On sauvegarde les noms des colonnes pour la page prédiction
    return model, X_train.columns, model.score(X_test, y_test)
