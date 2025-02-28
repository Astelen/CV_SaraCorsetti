from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score, homogeneity_score
from sklearn.decomposition import PCA

# Esercizio:
# Utilizzando il dataset "Iris" disponibile in scikit-learn, applica l'algoritmo K-
# Means per raggruppare i campioni e confronta i cluster ottenuti con le etichette
# originali delle specie di iris.

# Istruzioni:
# Carica il dataset "Iris" utilizzando sklearn.datasets.load_iris().
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
print(df.head())
print(df.info())
print(df.describe())

# Considera tutte le quattro caratteristiche (lunghezza e larghezza di sepali e
# petali) per il clustering.
# Applica l'algoritmo K-Means con un numero di cluster pari a 3.
km = KMeans(
    n_clusters=3,
    random_state=42
)
km.fit(X)
y_km = km.predict(X)

# Visualizza i cluster ottenuti utilizzando tecniche di visualizzazione adeguate
#(ad esempio, plot 2D delle prime due componenti principali).
pca_iris = PCA(n_components=2)
X_pca = pca_iris.fit_transform(X)
plt.figure(figsize=(12, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, s=50, cmap='viridis')
plt.title('Componenti della PCA')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.colorbar(label="Classi Iris")
plt.show()

# Confronta i cluster assegnati dall'algoritmo con le etichette reali delle
# specie di iris.
# Visualizza i cluster ottenuti utilizzando tecniche di visualizzazione adeguate
# Grafico delle etichette reali delle specie di iris
plt.figure(figsize=(12, 6))
#Subplot 1 (stesso grafico di prima per i cluster)
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_km, s=50, cmap='viridis')
centri = km.cluster_centers_
plt.scatter(centri[:, 0], centri[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clustering con K-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
#Subplot 2
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], s=50, cmap='viridis')
plt.title('Etichette Reali delle Specie di Iris')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

# Calcola metriche di valutazione come l'Indice di Rand Adjusted o l'Homogeneity
# Score per quantificare la qualità del clustering.
rand_adj = adjusted_rand_score(y, y_km)
homo_score = homogeneity_score(y, y_km)
print("Adjusted Rand Index: ", rand_adj)  #Serve a capire se il mio clustering e' sensato,
#quanto differesce da un altro sistema di clustering. In questo caso serve a capire quando i clusters
#si allontano dalla divisione per tipi di iris. Varia tra -0,5 e 1. ARI vicino lo 0 -> clusters casuali.
#Ari vicino 1 -> clusters adeguati.
print("Homogeneity score: ", homo_score) #Riporta quanto i punti all'interno dei clusters siano omogenei
#(ovvero se tutti quei punti appartengono davvero a quel cluster). Riporta valore tra 0 e 1 -> verso 1 e' meglio

# Discuta i risultati e l'eventuale corrispondenza tra i cluster e le specie
# reali.
##Grafico, ARI e HS riportano tutti la stessa informazione: la divisione per clusters rispecchia in maniera adeguata la
#divisione per classi.