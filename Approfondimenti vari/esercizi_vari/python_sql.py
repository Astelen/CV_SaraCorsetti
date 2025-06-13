import mysql.connector

def inizio():
    try:
        mydb = mysql.connector.connect(    ##si connette solo al database
            host ="localhost",
            user = "root",
            password = "root",
            port = 8889,
            database = "GestionaleScuola"
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
        mycursor = mydb.cursor()
        query = "CREATE database GestionaleScuola"
        mycursor.execute(query)
        print("Database creato")
        query = "CREATE TABLE GestionaleScuola.Studenti (ID INT auto_increment PRIMARY KEY, Nome VARCHAR(20), Cognome VARCHAR(30), Classe VARCHAR(30), Inglese INT, Italiano INT, Matematica INT)"
        mycursor.execute(query)
        print("Tabella Studenti creata")
        mydb, mycursor = inizio() #Sewrve a salvare i valori e riportarli nel Try.
    return mydb, mycursor

mydb, mycursor = inizio()

def visualizza_studenti():
    query = "SELECT * FROM Studenti"
    print("Ecco la lista degli studenti:")
    mycursor.execute(query)
    results = mycursor.fetchall()
    for riga in results:
        print("Nome: ", riga[1], "Cognome: ", riga[2], "Classe: ", riga[3], "Voto Inglese: ", riga[4], "Voto Italiano: ", riga[5], "Voto Matematica: ", riga[6])

def aggiungi_studente(Nome, Cognome, Classe, Inglese, Italiano, Matematica):
    query = "INSERT INTO Studenti(Nome, Cognome, Classe, Inglese, Italiano, Matematica) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (Nome, Cognome, Classe, Inglese, Matematica, Italiano))
    mydb.commit()
    print(mycursor.rowcount, "studente aggiunto!")

def rimuovi_studente(Nome, Cognome, Classe):
    query = "DELETE FROM Studenti WHERE Nome = %s AND Cognome = %s AND Classe = %s"
    mycursor.execute(query, (Nome, Cognome, Classe))
    mydb.commit()
    print("Studente rimosso!")

def modifica_tabella(Nome_Colonna):
    query = "ALTER TABLE Studenti ADD %s"
    mycursor.execute(query, (Nome_Colonna))
    mydb.commit()
    print("Colonna aggiunta!")

def modifica_studente(Nome_Colonna, Valore, Nome, Cognome, Classe):
    query = "UPDATE Studenti SET %s = %s WHERE Nome = %s, Cognome = %s, Classe = %s"
    mycursor.execute(query, (Nome_Colonna, Valore, Nome, Cognome, Classe))
    mydb.commit()
    print("Studente modificato!")

def menu():
        print("Benvenuto nel Gestionale degli Studenti.")
        while True: 
            scelta = input("Scegli 1 per visualizzare gli studenti, 2 per aggiungere uno studente, 3 per rimuovere uno studente, 4 per modificare la tabella, 5 per modificare uno studente, 9 per uscire: ")
            if scelta == "1":
                visualizza_studenti()
            elif scelta == "2":
                nome = input("Inserisci il nome dello studente: ")
                cognome = input("Inserisci il cognome dello studente: ")
                classe = input("Inserisci la classe dello studente: ")
                Inglese = input("Inserisci il voto: ")
                Italiano = input("Inserisci il voto: ")
                Matematica = input("Inserisci il voto: ")
                aggiungi_studente(nome, cognome, classe, Inglese, Italiano, Matematica)
            elif scelta == "3":
                Nome = input("Inserisci il nome dello studente: ")
                Cognome = input("Inserisci il cognome dello studente: ")
                Classe = input("Inserisci la classe dello studente: ")
                rimuovi_studente(Nome, Cognome, Classe)
            elif scelta == "4":
                Nome_Colonna = input("Inserisci il nome della colonna da aggiungere: ")
                modifica_tabella(Nome_Colonna,)
            elif scelta == "5":
                Nome = input("Inserisci il nome dello studente: ")
                Cognome = input("Inserisci il cognome dello studente: ")
                Classe = input("Inserisci la classe dello studente: ")
                Nome_Colonna = input("Quale colonna vuoi modificare? ")
                Valore = input("Inserisci il valore da inserire: ")
                modifica_studente(Nome_Colonna, Valore, Nome, Cognome, Classe)
            elif scelta == "9":
                print("Ciao!")
                break
            else:
                print("Scelta non valida")

menu()