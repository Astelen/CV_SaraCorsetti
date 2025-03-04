##GradientBoost sul database titanic. Bisogna prima pulire i dati (nulli ecc).
# Ci sono valori stringa che e' sempre meglio convertire in numeri.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

df_train = pd.read_csv("/Users/tap/Documents/GitHub/CV_SaraCorsetti/Corso Python - Formatemp/21_lunedi3mar/train.csv") #Dividere questo in train e test

# df_combined = pd.concat([df_train, df_test], ignore_index=True)
# print(df_combined.head())
# print(df_combined.tail())
# print(df_train.head())
# print(df_test.tail())

print(df_train.describe())
print(df_train.head())
print(df_train.info())
print(df_train.isnull().sum())

df_train_cleaned = df_train.dropna()

print(df_train_cleaned.info())
dummies = pd.get_dummies(df_train_cleaned)
print(dummies.head())
print(dummies.describe())
print(dummies.info())
print(dummies.tail())

X = dummies.drop('Survived', axis=1)
y = dummies['Survived']

scalar_data = StandardScaler()
X_scaled = scalar_data.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=8)

#gbc = GradientBoostingClassifier()
gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=8)
gbc.fit(X_train, y_train)
predictions = gbc.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)   

# Definisci la griglia di parametri (stampata da Copilot)
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Esegui GridSearchCV
# grid_search = GridSearchCV(estimator=gbc, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
# grid_search.fit(X_train, y_train)

# # Stampa i migliori parametri trovati
# print("Best parameters found: ", grid_search.best_params_)

# # Usa il miglior modello trovato per fare predizioni
# best_gbc = grid_search.best_estimator_
# predictions2 = best_gbc.predict(X_test)

# # Calcola l'accuratezza
# accuracy = accuracy_score(y_test, predictions2)
# print("Accuracy: ", accuracy)