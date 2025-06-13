import mysql.connector

def inizio():
    try:
        mydb = mysql.connector.connect(    ##si connette solo al database
            host ="localhost",
            user = "root",
            password = "root",
            port = 8889,
            database = "Gestionale_Mus"
            )
        mycursor = mydb.cursor()
        print("Connection established")
    except:
        mydb = mysql.connector.connect(    ##si connette solo al database
            host ="localhost",
            user = "root",
            password = "root",
            port = 8889,
            )
        print("Connection established")
        mycursor = mydb.cursor()
        query = "CREATE database Gestionale_Mus"
        mycursor.execute(query)
        print("Database creato")
        query = "CREATE table Gestionale_Mus.Inventario_Musicale (ID_canzone INT auto_increment PRIMARY KEY, Artista VARCHAR(30), ID_artista INT UNIQUE, Genere_Musicale VARCHAR(30), Lunghezza_Traccia INT, Band BOOL)"
        mycursor.execute(query)
        print("Tabelle create")
    return mydb, mycursor

mydb, mycursor = inizio()

def aggiungi_tabella():
    try:
        query = "CREATE table Gestionale_Mus.Musicisti (ID_artista INT auto_increment PRIMARY KEY, Artista VARCHAR(30), Eta INT, Genere VARCHAR(1), Genere_Musicale VARCHAR(30), Esibizioni_live INT, Iscrizione BOOL, FOREIGN KEY (ID_artista) REFERENCES Inventario_musicale(ID_artista))"
        mycursor.execute(query)
        mydb.commit()
        print("Tabella Musicisti aggiunta!")
    except:
        print("Tabella gia' presente!")

def aggiungi_chiavi():
    query = "ALTER table Inventario_Musicale ADD FOREIGN KEY (ID_artista) REFERENCES Musicisti(ID_artista)"
    mycursor.execute(query)
    query = "ALTER table Musicisti ADD FOREIGN KEY (ID_artista) REFERENCES Inventario_Musicale(ID_artista)"
    mycursor.execute(query)
    mydb.commit()
    print("Chiave relazionale aggiunta")

aggiungi_tabella()

def aggiungi_canzone(Artista, ID_artista, Genere_Musicale, Lunghezza_traccia, Band):
    query = "INSERT INTO Inventario_Musicale (Artista, ID_artista, Genere_Musicale, Lunghezza_traccia, Band) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(query, (Artista, ID_artista, Genere_Musicale, Lunghezza_traccia, Band))
    mydb.commit()
    print("Canzone aggiunta all'inventario!")

def aggiungi_artista(Artista, ID_artista, Eta, Genere, Genere_Musicale, Esibizioni_live, Iscrizione):
    query = "INSERT INTO Musicisti (Artista, ID_artista, Eta, Genere, Genere_Musicale, Esibizioni_live, Iscrizione) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (Artista, ID_artista, Eta, Genere, Genere_Musicale, Esibizioni_live, Iscrizione))
    mydb.commit()
    print("Artista aggiunto all'inventario!")

def menu():
        print("Benvenuto nel Gestionale degli Studenti.")
        while True: 
            scelta = input("Scegli 1 per visualizzare gli studenti, 2 per aggiungere uno studente, 3 per rimuovere uno studente, 9 per uscire: ")
            if scelta == "1":
                pass
            elif scelta == "2":
                ID_artista = input("Scrivi l'ID dell'artista: ")
                query2 = "SELECT ID_artista FROM Gestionale_Mus.Artisti WHERE EXISTS (ID_artista FROM Gestionale_Mus.Artisti WHERE ID_artista = %s)"
                if mycursor.execute(query2) == False:
                    print("Devi prima inserire l'artista per poter aggiungere un suon brano all'inventario!")
                else: pass
                Artista = input("Scrivi il nome dell'artista: ")
                Genere_Musicale = input("Scrivi il nome dell'artista: ")
                Lunghezza_traccia = int("Scrivi la lunghezza della traccia (sec): ")
                Band = bool("Digita 1 se il pezzo e' registrato da una band, 0 se e' registrato da un solista: ")
                aggiungi_canzone(Artista, ID_artista, Genere_Musicale, Lunghezza_traccia, Band)

menu()