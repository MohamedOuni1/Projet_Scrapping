# Projet de Scraping, Analyse et Prédiction des Performances Olympiques
![LOGO JO](https://upload.wikimedia.org/wikipedia/commons/a/a7/Olympic_flag.svg)



Ce projet vise à extraire, analyser et prédire les performances des athlètes aux Jeux Olympiques. Il repose sur l'utilisation de techniques de **web scraping**, l'analyse de données historiques et l'application de modèles de prédiction pour fournir des insights sur les performances des athlètes dans différents sports.

---

## Description du projet

Ce projet se concentre sur l'analyse des performances des athlètes aux Jeux Olympiques, en explorant les tendances des médailles 🥇🥈🥉 en fonction du sexe, de l'âge, du sport, et en identifiant les athlètes les plus performants à travers les éditions des Jeux. L'objectif est également de prédire les résultats pour les Jeux Olympiques de 2028 en utilisant les données des éditions précédentes.

---

## Fonctionnalités principales

- **Scraping des données** : Extraction des résultats des Jeux Olympiques depuis le site **Olympedia**.
- **Analyse des tendances** : Exploration des performances par sexe, âge, sport, et pays.
- **Prédiction des résultats pour 2028** : Utilisation de modèles de machine learning pour prédire les performances des athlètes en 2028.
---

## Outils utilisés 🛠️

- **Pandas** 🐼 : 
    - Utilisé pour la manipulation et l'analyse des données, permettant de gérer facilement les DataFrames.
  
- **NumPy** 🔢 : 
    - Bibliothèque pour les calculs numériques et les tableaux multidimensionnels.

- **Plotly** 📊 : 
    - Utilisé pour créer des visualisations interactives, tant avec `plotly.graph_objects` que `plotly.express`.

- **Matplotlib** 📈 : 
    - Bibliothèque pour créer des visualisations statiques, telles que des graphiques et des histogrammes.

- **Seaborn** 🌈 : 
    - Utilisé pour la visualisation statistique des données avec des graphismes de haute qualité.

- **Scikit-learn** 🔍 : 
    - Utilisé pour les tâches de machine learning, notamment pour la classification et l'évaluation des modèles.

- **BeautifulSoup** 🍲 : 
    - Outil pour le scraping des données des pages web, ici utilisé pour extraire les résultats des Jeux Olympiques.

- **Requests** 🌐 : 
    - Utilisé pour faire des requêtes HTTP pour récupérer les pages web à scraper.

- **CSV** 📜 : 
    - Utilisé pour lire et écrire des fichiers CSV, permettant une manipulation facile des données tabulaires.

- **Google Colab** ☁️ : 
    - Un environnement de développement interactif permettant d'exécuter du code Python dans un navigateur.



## Étapes du projet

### Étape 1 : Scraping des données
- **Description** : Extraction des données historiques des Jeux Olympiques (médaille, sport, sexe, âge, etc.) à l'aide de techniques de scraping.
- **Technologies utilisées** : Python, `BeautifulSoup`, `requests`.

### Étape 2 : Compréhension du dataset
- **Description** : Exploration initiale des données collectées pour comprendre leur structure et les relations entre les variables.
- **Outils** : Pandas, Matplotlib, Seaborn.

### Étape 3 : Nettoyage du dataset
- **Description** : Nettoyage des données pour gérer les valeurs manquantes, les erreurs typographiques, et la transformation des données catégorielles en variables numériques.
- **Outils** : Pandas, NumPy.

### Étape 4 : Comparaison des datasets
- **Description** : Comparaison des datasets collectés pour vérifier la qualité et la cohérence des données.
- **Outils** : Pandas, Python.

### Étape 5 : Analyse des données
- **Description** : Exploration des tendances et des relations entre les performances des athlètes et les facteurs tels que le sexe, l'âge et le sport.
- **Outils** : Pandas, Matplotlib, Seaborn, Scipy.

### Étape 6 : Prédiction des performances pour 2028
- **Description** : Application de modèles de machine learning pour prédire les résultats des athlètes en 2028.
- **Outils** : Scikit-learn, XGBoost.

---
![Les données des athlétes](https://i.ibb.co/Cb58G9y/11.jpg)
![Resultat](https://i.ibb.co/pP4WgnM/22.jpg)

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/MohamedOuni1/Projet_Scrapping

## Contributeurs
- Développeur : **Mohamed Ouni**

