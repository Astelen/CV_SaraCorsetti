from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Neighbors =3, test_size = 0.2
#Loading data
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=3)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)

print(accuracy)
#Accuracy 0.9



# Riduciamo il test_size per verificare l'accuratezza, neighbors =3, test_size = 0.1
#Loading data
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=10)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=3)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
#Accuracy 0.93




#Aumentiamo il test_size per verificare l'accuratezza: neighbors =3, test_size = 0.8
#Loading data
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=10)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=3)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
#Accuracy 0.96



#Provo a cambiare anche n. neighbors =5, test_size = 0.2
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=5)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
#Accuracy 0.96




#Provo a cambiare anche neighbors =10, test_size = 0.2
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=10)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
#Accuracy 1





#Provo a cambiare anche n. neighbors =10, test_size = 0.4
data = load_iris()
X = data.data
y = data.target

#Splitting test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=10)

#KNN model
#Creo istanza modello
knn = KNeighborsClassifier(n_neighbors=10)
#Addestro il modello con fit sui dati di training
knn.fit(X_train, y_train)
#Effettuo predizioni sui nuovi dati
predictions = knn.predict(X_test)

#Accuracy per valutare le prestazioni
accuracy = accuracy_score(y_test, predictions)
print(accuracy)
#Accuracy 0.96




###Esercizio slide 374
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset Iris.
data = load_iris()
X = data.data
y = data.target

# Standardizza le caratteristiche utilizzando StandardScaler.
#Ricorda la sintassi: richiamo la funzione dentro StandardScaler 
scalar_data = StandardScaler()
X_scaled = scalar_data.fit_transform(X)

# Suddividi i dati in training e test set # (70% training, 30% test).
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=8)

# Applica l'algoritmo DecisionTreeClassifier.
clf = DecisionTreeClassifier(random_state = 8)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Valuta la performance del modello
accuratezza = accuracy_score(y_test, y_pred)
print(f"Accuratezza di: {accuratezza}")

# utilizzando il classification_report (precisione, recall, F1-score).
report_iris = classification_report(y_test, y_pred)
print(report_iris)

# Visualizza la matrice di confusione.
cm = confusion_matrix(y_test, y_pred)
#Rappresentazione grafica
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()