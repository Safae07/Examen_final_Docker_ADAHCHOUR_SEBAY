
# Comparaison des méthodes de réduction de dimension
# Avec Trustworthiness


import pandas as pd
import numpy as np
from sklearn.manifold import trustworthiness
from sklearn.preprocessing import StandardScaler

# Charger les données

data = pd.read_csv("data/city_lifestyle_dataset.csv")

# que numériques
X_original = data.select_dtypes(include=np.number)

# Standardiser
scaler = StandardScaler()
X_original_scaled = scaler.fit_transform(X_original)

# charger les exports des résultats

pca_2d = pd.read_csv("outputs/pca_export.csv")[["PC1", "PC2"]].values

tsne_2d = pd.read_csv("outputs/tsne_export.csv")[["Dim1", "Dim2"]].values


# calcul du trustworthiness

## afficher les résultats
print("===== Trustworthiness Scores =====\n")

score_pca = trustworthiness(X_original_scaled, pca_2d, n_neighbors=10)
print("PCA :", round(score_pca, 4))

score_tsne = trustworthiness(X_original_scaled, tsne_2d, n_neighbors=10)
print("t-SNE :", round(score_tsne, 4))

print("\n===== Interpretation =====")

print("La PCA obtient un score de trustworthiness de", round(score_pca,4),
      "qui montre une bonne préservation de la structure locale des données.")

print("La méthode t-SNE obtient un score de", round(score_tsne,4),
      "ce qui montre une meilleure préservation des voisinages locaux.")

if score_tsne > score_pca:
    print("Conclusion : t-SNE préserve mieux la structure locale que la PCA sur ce dataset.")
else:
    print("Conclusion : La PCA préserve mieux la structure locale sur ce dataset.")
