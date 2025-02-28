from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import mean_squared_error

# Caricamento del dataset
X, y = load_wine(return_X_y=True)

# Suddivisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione del modello di regressione lineare
model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione sui dati di test
y_pred = model.predict(X_test)

# Calcolo dell'errore quadratico medio
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Stampa dei coefficienti
print("Coefficienti:", model.coef_)
print("Intercetta:", model.intercept_)




#Prova Regressione lostistica e lineare
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import classification_report

# Caricamento del dataset
data = load_wine()
X = data.data
y = data.target

# Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Creazione del modello
model = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='auto')

# Addestramento del modello
model.fit(X_train, y_train)

# Predizione
y_pred = model.predict(X_test)

# Valutazione
print(classification_report(y_test, y_pred))






# Utilizzando il dataset "Diabetes" disponibile in scikit-learn, sviluppa un modello
# di regressione lineare per predire la progressione della malattia del diabete
# basandoti sulle dieci misurazioni cliniche fornite.

from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Istruzioni:
# Carica il dataset "Diabetes" utilizzando sklearn.datasets.load_diabetes().
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Esplora i dati per comprendere le caratteristiche disponibili e la variabile
# target.
df = pd.DataFrame(X, columns=diabetes.feature_names)
print(df.head())
print(df.info())
print(df.describe())

# Suddividi il dataset in set di training e test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un modello di regressione lineare utilizzando LinearRegression di scikit-learn.
lr = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)
# Addestra il modello sui dati di training.
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# Valuta le prestazioni del modello sui dati di test utilizzando metriche
# appropriate come l'Errore Quadratico Medio (MSE) e il Coefficiente di
# Determinazione (R²).
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(y_test, y_pred) #Spiega quanta varianza e' spiegata dal modello
print("R^2 Score:", r2)
print("Coefficienti:", lr.coef_)
print("Intercetta:", lr.intercept_)

# Analizza i risultati e discuti l'efficacia del modello.
# Crea uno scatter plot con la linea di regressione
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, label='Valori Predetti')
sns.regplot(x=y_test, y=y_pred, scatter=False, color='red', label='Linea di Regressione')
plt.xlabel('Valori Reali')
plt.ylabel('Valori Predetti')
plt.title('Scatter Plot dei Valori Reali vs Valori Predetti con Linea di Regressione')
plt.legend()
plt.show()

#Il modello e' abbastanza efficace per analizzare questi dati. 
# Infatti, l'errore quadratico medio e il coefficiente di determinazione indicano che il modello
# è in grado di spiegare una buona parte della variazione nei dati.
# Inoltre, dal grafico a dispersione con la linea di regressione, 
# possiamo osservare che i valori predetti sono abbastanza vicini ai valori reali, 
# suggerendo che il modello ha una buona capacità predittiva. 
# Tuttavia, potrebbero essere necessarie ulteriori analisi per valutare meglio le prestazioni del modello
# e identificare eventuali aree di miglioramento.













from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score, homogeneity_score
from sklearn.decomposition import PCA

# Esercizio slide 421
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