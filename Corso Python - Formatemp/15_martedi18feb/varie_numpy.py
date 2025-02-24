import numpy as np

arr1 = np.arange(0,50, dtype = float)

#print(arr1)
print(arr1.shape)

arr2 = np.arange(6)
print(arr2)
reshaped_arr2 = arr2.reshape((2, 3))
print(reshaped_arr2)


arr_rand = np.random.randint(10, 50, 20) #Primo valore min, secondo valore max, terzo valore quanti valori vuoi nel range
print(arr_rand)

print(arr_rand[0:10])
print(arr_rand[45:])
print(arr_rand[5:15])
print(arr_rand[::3])

arr_rand[range(5,10)]  = 99
print(arr_rand)

##2D

matrice1 = np.random.randint(1, 101, size=(6, 6))    #Funzione che genera numeri casuali, 1 come primo num, 101 come secondo
# size ci dice la dimensione della matrice


matrice1 = np.random.randint(1, 101, size=(6, 6))    #Funzione che genera numeri casuali, 1 come primo num, 101 come secondo
# size ci dice la dimensione della matrice

print(matrice1)
matrice2 = matrice1[np.ix_([1,5],[1,5])] #How to extract a submatrix NON RISOLTO
matric2mod = matrice1 [1:5, 1:5]  #SOLUZIONE a come estrarre sottomatrice da matrice 
print(matric2mod)


matrice3 = np.arange(0, 16).reshape((4, 4)) #Altro modo per creare matrice
print(matrice3)


##Esercizi: Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
# Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.


random_arr = np.random.rand(3, 3) #Rand crea valori casuali tra 0 e 1, #random valori casuali
print(random_arr)

###Esercizio slide 244
# Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.

# Esercizio:

# Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# Cambia la forma dell'array a una matrice 3x4.
# Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# Calcola e stampa la somma degli elementi di entrambe le matrici.



####ESERcizio Slide 245
# Consegna:
# Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
# Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
# Somma i due array elemento per elemento per ottenere un nuovo array.
# Calcola la somma totale degli elementi del nuovo array.
# Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
# Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.

# Obiettivo:
# Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni per la somma parziale.



###ESERCIZI SLIDE 255
# Esercizio 1: Somma e Media di Elementi Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100. Calcolare e stampare la somma di tutti gli elementi dell'array.
# Calcolare e stampare la media di tutti gli elementi dell'array. 

# Esercizio 2: Manipolazione di Array Multidimensionali 
# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
# Estrarre e stampare la seconda colonna della matrice. 
# Estrarre e stampare la terza riga della matrice. Calcolare e stampare la somma degli elementi della diagonale principale della matrice. 

# Esercizio 3: Operazioni con Fancy Indexing Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50. Utilizzare fancy indexing per selezionare e
# stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0). 
# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).
# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.

##Vedi altri esercizi slide 256-257