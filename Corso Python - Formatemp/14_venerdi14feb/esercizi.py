import mysql.connector

# mydb = mysql.connector.connect(    ##si connette solo al server
#     host ="localhost",
#     user = "root",
#     password = "root",
#     port = 8889
# )

# print(mydb)

# mycursor = mydb.cursor() #creo cursore

#query = "create database mydatabase" #creo Query che va in un'unica stringa

#mycursor.execute(query) #il cursore esegue la query

# query = "show database" 


# for db in mycursor:
#     print(db)


mydb = mysql.connector.connect(    ##si connette solo al database
    host ="localhost",
    user = "root",
    password = "root",
    port = 8889,
    database = "mydatabase"
)

mycursor = mydb.cursor() #creo cursore

#query = "create table Customers(ID INT auto_increment PRIMARY KEY, Nome varchar(100), indirizzo varchar(100))"

#mycursor.execute(query)

# query = "show database"

# mycursor.execute(query)

# for db in mycursor:
#     print(db)


# query = "insert into Customers(Nome, indirizzo) values('Tommaso', 'via Roma')" #inserisco questa riga
# mycursor.execute(query)
# mydb.commit()   #Quando mi occupo dei dati mando il Commit per confermare l'inserimento dei dati
# print(mycursor.rowcount, "righe inserite!")

# query = "insert into Customers(Nome, indirizzo) values(%s, %s)" #Metto %s come placeholder, poi verra' sostituito dalla tupla
# tupla_valori = ("Giovanni", "Via Milano 5")
# mycursor.execute(query, tupla_valori)
# mydb.commit()   #Quando mi occupo dei dati mando il Commit per confermare l'inserimento dei dati
# print(mycursor.rowcount, "righe inserite!")


# query = "insert into Customers(Nome, indirizzo) values(%s, %s)"
# lista_di_tuple = [("Carlo", "Via Adda"), ("Enea", "Via Celano"), ("Ludovico", "Via Gubbio")]
# mycursor.executemany(query, lista_di_tuple)
# mydb.commit()   #Quando mi occupo dei dati mando il Commit per confermare l'inserimento dei dati
# print(mycursor.rowcount, "righe inserite!")

def aggiungi_customer():  #la rendo funzione
    query = "insert into Customers(Nome, indirizzo) values(%s, %s)"
    lista_di_tuple = [("Carlo", "Via Adda"), ("Enea", "Via Celano"), ("Ludovico", "Via Gubbio")]
    mycursor.executemany(query, lista_di_tuple)
    mydb.commit()   #Quando mi occupo dei dati mando il Commit per confermare l'inserimento dei dati
    print(mycursor.rowcount, "righe inserite!")

def leggivalori ():
    query = "SELECT * FROM Customers"
    mycursor.execute(query)
    results = mycursor.fetchall()  #cattura tutti i valori dal cursore
    for riga in results:
        print(riga)
        
        
def leggivalore ():
    query = "SELECT * FROM Customers"
    mycursor.execute(query)
    results = mycursor.fetchone()  #cattura il valore dal cursone
    print(results)
    
    
# leggivalori()
# leggivalore()


def eliminavalore (val):
    query = "DELETE FROM Customers WHERE ID = %s"
    mycursor.execute(query, val)
    mydb.commit()
    print(mycursor.rowcount, "righe eliminate")
    
# eliminavalore ((2,))   #Siccome ho Val come parametro della funzione, quanto la richiamo devo passare il valore della tupla.
# # Va con la virgola o non lo prendo

def aggiornavalore (val):
    query = "UPDATE Customers SET Nome = %s WHERE ID = %s"
    mycursor.execute(query, val)
    mydb.commit()
    print(mycursor.rowcount, "righe modificate")
    
# aggiornavalore(("Tommaso", 3))

def aggiornavalori (val):
    query = "UPDATE Customers SET Nome = %s WHERE ID = %s"
    mycursor.executemany(query, val)
    mydb.commit()
    print(mycursor.rowcount, "righe modificate")
    
# aggiornavalori([("Valerio", 3), ("Chiara", 5)])

leggivalori()