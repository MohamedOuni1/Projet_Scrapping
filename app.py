import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Charger le modèle et le scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Mapper les prédictions en noms de médailles
medal_mapping = {2: 'Gold', 1: 'Silver', 0: 'Bronze', -1: 'Nothing'}

# Titre de l'application
st.title("Prédiction des Médailles pour 2028")

# Formulaire d'entrée pour ajouter les détails du joueur
st.header("Ajouter les détails du joueur")
nom_athlete = st.text_input("Nom de l'athlète",value="Mohamed Ouni")
agejo = st.number_input("Âge pendant les jeux olympiques 2028", min_value=10, max_value=60, value=25, step=1)
height = st.number_input("Taille (en cm)", min_value=100, max_value=250, value=175, step=1)
weight = st.number_input("Poids (en kg)", min_value=30, max_value=200, value=70, step=1)

# Bouton de prédiction
if st.button("Prédire la Médaille"):
    if nom_athlete:
        # Préparer les données pour la prédiction
        input_data = np.array([[agejo, height, weight]])
        input_data_scaled = scaler.transform(input_data)

        # Faire la prédiction
        prediction = model.predict(input_data_scaled)[0]
        prediction_proba = model.predict_proba(input_data_scaled)[0]

        # Résultats
        st.subheader(f"Résultats de la Prédiction pour {nom_athlete}")
        st.write(f"**Médaille Prédite :** {medal_mapping[prediction]}")

        # Afficher les probabilités pour chaque classe
        st.subheader("Probabilités pour chaque catégorie")
        for medal, prob in zip(['Nothing', 'Bronze', 'Silver', 'Gold'], prediction_proba):
            st.write(f"{medal}: {prob * 100:.2f}%")
    else:
        st.warning("Veuillez entrer le nom de l'athlète.")

# Note finale
st.info("Ce modèle est basé sur les données historiques des JO.")
