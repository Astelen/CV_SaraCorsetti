# Crea un gestionale scolastico, l'utente
# può visualizzare il nome degli studenti presenti o inserire nuovi studenti

import mysql.connector

def init():
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
        query = "CREATE TABLE GestionaleScuola.Studenti (ID INT auto_increment PRIMARY KEY, Nome VARCHAR(20), Cognome VARCHAR(30), Voto1 INT, Voto2 INT, Voto3 INT, VotoItaliano INT)"
        mycursor.execute(query)
        mydb, mycursor = init() #Sewrve a salvare i valori e riportarli nel Try.
    return mydb, mycursor

mydb, mycursor = init()

# query = "ALTER TABLE Studenti ADD VotoItaliano INT"
# mycursor.execute(query)

# query = "show databases"
# mycursor.execute(query)
# for db in mycursor:
#     print(db)

# query = "CREATE database GestionaleScuola"

# mycursor.execute(query)

# query = "CREATE TABLE GestionaleScuola.Studenti (ID INT auto_increment PRIMARY KEY, Nome VARCHAR(20), Cognome VARCHAR(30))"

# mycursor.execute(query)

def visualizzastudenti():
    query = "Select * FROM Studenti"
    mycursor.execute(query)
    results = mycursor.fetchall()
    for riga in results:
        print(f"ID studente: {riga[0]}, Nome studente: {riga[1]}, Cognome studente: {riga[2]}")
        
def visualizzastudenti2():
    query = "Select * FROM Studenti"
    mycursor.execute(query)
    results = mycursor.fetchall()
    print("ID Studente, Nome studente, Cognome studente: ")
    for riga in results:
        print(f"{riga[0]} {riga[1]} {riga[2]}")

# def aggiungistudente(studente):
#     query = "INSERT INTO Studenti(Nome, Cognome) VALUES (%s, %s)"
#     mycursor.execute(query, studente)
#     mydb.commit()  #Serve a comunicare con la connessione
#     print(mycursor.rowcount, "studenti aggiunti!")

# aggiungistudente(("Mario", "Del Re"))
# visualizzastudenti()

def aggiungistudente2(nome, cognome, voto1, voto2, voto3, votoitaliano):   ##Versione diversa con tupla sull'execute perche' dopo la query va sempre una tupla! Ma se io nella funzone passo due parametri poi nel richiamarla devo scrivere due parametri.
    query = "INSERT INTO Studenti(Nome, Cognome, voto1, voto2, voto3, votoitaliano) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (nome, cognome, voto1, voto2, voto3, votoitaliano)) #
    mydb.commit()  #Serve a comunicare con la connessione
    print(mycursor.rowcount, "studente aggiunto!")
    
def rimuovistudente(ID_Studente):
    query = "DELETE FROM Studenti WHERE ID = %s"
    mycursor.execute(query, ID_Studente)
    mydb.commit()
    print(mycursor.rowcount, "studente rimosso!")
    
# aggiungistudente("Mario", "Del Re")
# visualizzastudenti()

# aggiungistudente2("Gesu'", "Di Nazaret", 8,7,6,9)
# aggiungistudente2("Valerio", "Dio", 8,7,6,9)
# aggiungistudente2("Regina", "Universo", 8,7,6,9)
# rimuovistudente((3,))

def menu():
        print("Benvenuto nel Gestionale degli Studenti.")
        while True: 
            scelta = input("Scegli 1 per visualizzare gli studenti, 2 per aggiungere uno studente, 3 per rimuovere uno studente, 9 per uscire: ")
            if scelta == "1":
                visualizzastudenti()
            elif scelta == "2":
                nome = input("Inserisci il nome dello studente: ")
                cognome = input("Inserisci il cognome dello studente: ")
                voto1 = input("Inserisci il voto: ")
                voto2 = input("Inserisci il voto: ")
                voto3 = input("Inserisci il voto: ")
                votoitaliano = input("Inserisci il voto: ")
                aggiungistudente2(nome, cognome, voto1, voto2, voto3, votoitaliano)
            elif scelta == "3":
                ID_studente = input("Inserisci l'ID dello studente: ")
                rimuovistudente((ID_studente, ))  ##In questo modo comunichiamo che e' una tupla
            elif scelta == "9":
                print("Ciao!")
                break
            else:
                print("Scelta non valida")
            
menu()

#rimuovistudente((3),)