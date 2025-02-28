from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Si vuole realizzare un’analisi del famoso dataset Iris utilizzando Pandas e NumPy. Il lavoro deve
# essere suddiviso in Tre branch consecutivi, ognuno dedicato a una parte specifica del progetto.

# Branch 1 – Esplorazione iniziale: Caricamento del dataset, verifica delle informazioni di base
# (dimensioni, tipi di dato, eventuali valori mancanti), statistica descrittiva iniziale (media,
# deviazione standard, minimo, massimo) e semplice visualizzazione di base (ad esempio
# conteggio di quante specie ci sono).
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target_names'] = iris.target
print(df.info())
#Non ci sono valori mancanti. Ogni colonna ha 150 valori.
print(df.describe())
#Media, deviazione standard, minimo, massimo per ogni variabile del dataset
#(4 variabili: lunghezza e larghezza sepalo, lunghezza e larghezza petalo)
print("Max della lunghezza sepalo: ", max(df['sepal length (cm)'])) #Prova per stampare max di una colonna
print("Min della lunghezza sepalo: ", min(df['sepal length (cm)'])) #Prova per stampare min di una colonna
print("Media della lunghezza sepalo: ", df['sepal length (cm)'].mean()) #Prova per stampare media di una colonna
print("Dev. st. della lunghezza sepalo: ",df['sepal length (cm)'].std()) #Prova per stampare deviazione standard di una colonna
print(df.head())
#Stampare quante specie ci sono
print("Specie di iris: ", iris.target_names)

# Branch 2 – Analisi approfondita: Utilizzo delle funzionalità di Pandas per analisi più
# dettagliate (correlazioni tra le variabili, raggruppamenti per specie, confronto dei valori
# medi e massimi delle diverse caratteristiche) 
#Matrice di correlazione 
correlation_matrix = df.select_dtypes(include=["number","bool"]).corr()
correlation_matrix
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()
#La matrice mostra correlazione tra lunghezza sepalo e petalo, tra lunghezza sepalo e larghezza petalo,
#tra lunghezza petalo e larghezza petalo.

#Box plot tra lunghezza del sepalo e categoria di specie
fig = px.box(df, x="target_names", y="sepal length (cm)").update_layout(xaxis_title="Specie di Iris", yaxis_title="Lunghezza sepalo")
fig.show()

# Aggiungi una colonna con i nomi delle specie (copiato da Copilot)
df['species'] = df['target_names'].map({i: name for i, name in enumerate(iris.target_names)})
# Raggruppa per specie e calcola il valore minimo e massimo per ogni caratteristica
grouped = df.groupby('species').agg(['min', 'max'])
# Stampa i risultati
print(grouped)
# Le specie Versicolor e Virginica differiscono significativamente dalla Setosa per lunghezza del sepalo rispetto alla prima specie.

# Branch 3 - Aggiungi almeno due grafici a scelta (boxplot, scatter plot) per comprendere
# meglio la distribuzione dei dati e descrivi con un print cosa dimsotrano questi grafici.
plt.figure(figsize=(10, 6))
sns.pairplot(df.select_dtypes(include=['number']), hue='target_names', palette='coolwarm', corner=True)
plt.show()
#Il pairplot conferma la distribuzione che vedevamo nel boxplot. Date le correlazioni tra le variabili,
#era facilmente prevedibile che anche la distribuzione delle altre variabili fosse clusterizzata.
# La specie Setosa e' significativamente diversa dalle altre due.