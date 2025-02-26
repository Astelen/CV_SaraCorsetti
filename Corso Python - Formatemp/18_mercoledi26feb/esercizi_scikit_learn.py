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