# City Lifestyle – Réduction de Dimension

## Description du projet

Ce projet a pour objectif d’appliquer et de comparer différentes méthodes de réduction de dimension sur le dataset *City Lifestyle Segmentation*.

Le jeu de données contient 300 villes décrites par plusieurs indicateurs socio-économiques et environnementaux (revenu moyen, densité de population, qualité de l’air, score de bonheur, espaces verts, etc.).

Chaque méthode (PCA, t-SNE) a été développée dans une branche Git dédiée, puis fusionnée dans la branche `main`.  
Un script Python permet ensuite de comparer les résultats obtenus à l’aide de la métrique **trustworthiness**.

Le projet est conteneurisé avec Docker afin de permettre une exécution simple et reproductible.

---

## Dataset

Le dataset comprend :

- 300 villes
- 8 variables numériques
- 2 variables qualitatives (`city_name`, `country`)
- Aucune valeur manquante

Les variables couvrent plusieurs dimensions :

- Démographie (population_density)
- Économie (avg_income, avg_rent)
- Infrastructure (public_transport_score, internet_penetration)
- Environnement (air_quality_index, green_space_ratio)
- Bien-être (happiness_score)

---

## Méthodes implémentées

### PCA

- Standardisation des données
- Réduction en 2 dimensions
- Visualisation des individus
- Cercle de corrélation
- Export des coordonnées 2D dans `outputs/`

### t-SNE

- Méthode non linéaire
- Projection en 2 dimensions
- Préservation des voisinages locaux
- Export des coordonnées 2D dans `outputs/`

---

## Comparaison des méthodes

La comparaison est réalisée avec la métrique **trustworthiness**, qui mesure la capacité d’une méthode à préserver les relations de voisinage locales lors de la réduction de dimension.

Résultats obtenus :

- **PCA : 0.9363**
- **t-SNE : 0.9723**

La méthode t-SNE obtient un score plus élevé, indiquant une meilleure préservation de la structure locale des données par rapport à la PCA.

---

## Structure du projet

.
├── data/
│   └── city_lifestyle_dataset.csv  
├── notebooks/
│   └── PCA.ipynb  
│   └── t-SNE.ipynb  
├── outputs/
│   ├── pca_export.csv  
│   └── tsne_export.csv  
├── evaluate.py  
├── requirements.txt  
├── Dockerfile  
└── README.md  

---

## Script d’évaluation

Le script `evaluate.py` :

1. Charge les données originales  
2. Charge les projections 2D exportées  
3. Calcule la métrique de trustworthiness  
4. Affiche les scores obtenus  

---

## Dockerisation

Le projet peut être exécuté directement via Docker.

### Construction de l’image

docker build -t reduc_dim_city .

### Exécution du conteneur

docker run reduc_dim_city

Le conteneur exécute automatiquement le script `evaluate.py` et affiche les scores de comparaison.

---

## Image Docker Hub

L’image est disponible sur Docker Hub :

https://hub.docker.com/repository/docker/safae07/reduc_dim_city 

Téléchargement :

docker pull safae07/reduc_dim_city:latest  
docker run safae07/reduc_dim_city  

---

## Technologies utilisées

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Git / GitHub  
- Docker  

---

## Conclusion

Ce projet met en évidence :

- La différence entre une méthode linéaire et une méthode non linéaire (t-SNE)
- La mise en place d’un workflow Git collaboratif  
- La reproductibilité d’un projet via Docker  