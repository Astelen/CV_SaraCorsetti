from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# Branch 3 - Aggiungi almeno due grafici a scelta (boxplot, scatter plot) per comprendere
# meglio la distribuzione dei dati e descrivi con un print cosa dimsotrano questi grafici.
