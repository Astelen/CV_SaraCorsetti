#Creare Menu' di selezione che attivi gli script delle funzioni
#Generazione di dati
#Analisi descrittiva dei dati (scegliere dataset o usare i dati generati)
#Grafico riguardante i dati (possibilmente generati)
#Attivare i risultati del Classification report del Machine learning
import numpy as np
import pandas as pd
import plotly.express as px

df = None
X = None
y = None

def generazione_dati():
    global df, X, y
    media = int(input("Inserisci la media: "))
    dev_st = int(input("Inserisci la deviazione standard: "))
    dimens_campionaria = int(input("Inserisci la dimensione campionaria: "))
    numero_reati = np.random.normal(loc=media, scale=dev_st, size=dimens_campionaria)
    data_inizio = input("Inserisci la data di inizio (YYYY-MM-DD): ")
    date_range = pd.date_range(start=data_inizio, periods=dimens_campionaria, freq='D')
    reato = ["omicidio", "furto", "droga", "truffa", "rapina"]
    tipo_reato = np.random.choice(reato, dimens_campionaria)
    df = pd.DataFrame ({
    'Data': date_range,
    'Numero di reati': numero_reati,
    'Tipo reato': tipo_reato
    })
    X = df[['Numero di reati']]
    y = df['Tipo reato']
    return df

def analisi_descrittiva():
    global df, X, y
    scelta_df = input("Vuoi utilizzare il dataset generato? (s/n): ")
    if scelta_df == "s":
        if df is None:
            print("Il dataset e' vuoto. Genera prima i dati.")
        else:
            print("Ecco le informazioni del tuo dataframe: ", df.info())
            print("Ecco le prime 5 righe del tuo dataframe: ", df.head())
            print("Ecco una descrizione del tuo dataframe: ", df.describe())
            print("Ecco le ultime 5 righe del tuo dataframe: ", df.tail())
    elif scelta_df == "n":
        nome_dataset = input("Inserisci quale database vuoi utilizzare (1: iris, 2: wine, 3: diabetes): ")
        if nome_dataset == "1":
            from sklearn.datasets import load_iris
            data = load_iris()
        elif nome_dataset == "2":
            from sklearn.datasets import load_wine
            data = load_wine()
        elif nome_dataset == "3":
            from sklearn.datasets import load_diabetes
            data = load_diabetes()
        else:
            print("Scelta non valida")
        X = data.data
        y = data.target
        print("Ecco le informazioni del tuo dataframe: ", generazione_dati.df.info())
        print("Ecco le prime 5 righe del tuo dataframe: ", generazione_dati.df.head())
        print("Ecco una descrizione del tuo dataframe: ", generazione_dati.df.describe())
        print("Ecco le ultime 5 righe del tuo dataframe: ", generazione_dati.df.tail())
    else:
        print("Scelta non valida. Riprova.")

def grafico_dati():
    global df
    if df is None:
        print("Il dataset e' vuoto. Genera prima i dati.")
    else:
        fig = px.box(df, x="Tipo reato", y="Numero di reati", title="Distribuzione del Numero di Reati per tipo di reato")
        fig.show()

def classification_report():
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import classification_report
    global df, X, y
    scalar_data = StandardScaler()
    X_scaled = scalar_data.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=8)
    clf = DecisionTreeClassifier(random_state = 8)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuratezza = accuracy_score(y_test, y_pred)
    print(f"Accuratezza di: {accuratezza}")
    report_iris = classification_report(y_test, y_pred)
    print("Classification report: ", report_iris)

#Menu' di selezione per attivare gli script delle funzioni
while True:
    print("\n--- Gestione delle funzioni del software ---")
    print("1. Generazione di un set di dati per il numero di reati in un anno ")
    print("2. Analisi descrittiva dei dati")
    print("3. Grafico dei dati")
    print("4. Classification report")
    print("5. Esci")
    scelta = input("Seleziona un'opzione: ")
    if scelta == "1":
        generazione_dati()
    elif scelta == "2":
        analisi_descrittiva()
    elif scelta == "3":
        grafico_dati()
    elif scelta == "4":
        classification_report()
    elif scelta == "5":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")