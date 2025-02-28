
#esercizio verifica 1
# Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata.
# Deve poter stampare una lista singola o tutte. 
# Si deve ripetere X volte definite all'inizio dall'utente

#creazione liste, poi da inserire nella funzione
valore_stringa = ""
valore_intero = 0
valore_booleano = True
lista_stringa = []
lista_numeri = []
lista_booleano = []
scelta_stampa = ""

#prima funzione di aggiunta alla lista
def aggiunta_lista(valore_da_aggiungere):
    scelta_tipo_valore = int(input("Scegli 1 per aggiungere una stringa, 2 per un numero inero, 3 per un valore booleano: "))
    if scelta_tipo_valore == 1:
        valore_stringa = input("Inserisci la parola da aggiungere: ")
        lista_stringa.append(valore_stringa)
        return lista_stringa
    elif scelta_tipo_valore == 2:
        valore_intero = int(input("Inserisci il numero da aggiungere: "))
        lista_numeri.append(valore_intero)
        return lista_numeri
    elif scelta_tipo_valore == 3:
        valore_booleano = bool(input("Inserisci True o False: "))
        lista_booleano.append(valore_booleano)
        return lista_booleano
    else:
        print("Errore nella digitazione")
    
# seconda funzione di stampa
def stampa_liste(lista_da_stampare):
    elenco_stampa = int(input("Seleziona 1 per stampare la lista delle stringhe, 2 per la lista dei numeri, 3 per la lista dei booleani, 4 per stampare tutte le liste"))
    if elenco_stampa == 1:
        print("Ecco la lista selezionata: ", lista_stringa)
    elif elenco_stampa == 2:
        print("Ecco la lista selezionata: ", lista_numeri)
    elif elenco_stampa == 3:
        print("Ecco la lista selezionata: ", lista_booleano)
    elif elenco_stampa == 4:
        print("Ecco tutte le liste: ")
        print(lista_stringa)
        print(lista_numeri)
        print(lista_booleano)
    else:
        print("Selezione non valida.")

# Def per menu' con ciclo while
def menu():
    while True:
        scelta_utente = input("Vuoi aggiungere un numero ad una lista? Scegli S o N: ")
        if scelta_utente.lower() == "s":
            aggiunta_lista()
            scelta_stampa = input("Vuoi stampare una lista? Scegli S o N: ")
            if scelta_stampa.lower() == "s":
                stampa_liste()
            elif scelta_stampa.lower() == "n":
                print("Ok! Puoi sempre aggiungere un altro dato, se vuoi.")
            else:
                print("Scelta non valida")
        elif scelta_utente.lower() == "n":
            print("Arrivederci")
            break
        else: 
            print("Selezione non valida")




#### Es 2:  Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle
# l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente
# alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito

#funzione di inserimento stringhe SE sono piu' lunghe della precedente

stringa_es2 = ""
lista_stringhe_es2 = []

def aggiunta_stringhe():
    stringa_es2 = input("Scrivi la parola da aggiungere: ")
    while True:
        if len(stringa_es2) > len(lista_stringhe_es2[-1]):
            return lista_stringhe_es2.append(stringa_es2)
        else:
            print("La parola aggiunta e' piu' breve della precedente, quindi non verra' aggiunta.")
            break

def stampa_stringhe():
    print("Ecco la lista delle stringhe: ", lista_stringhe_es2)
    print("Ecco il numero delle stringhe inserite: ", len(lista_stringhe_es2))
    
#Menu' per aggiunere stringhe
aggiunta_stringhe()
stampa_stringhe()




###esercizio 13
# Andare a creare una funzioni che si occupi di salvare i dati dell'utente,
# andare a creare una funzione che si occupi di fare il login dell'utente,
# Andare a creare un funzioni che modifichi i dati dell'utente solo se questi sono già stati creati  / salvati e solo dopo il login.
# Andare a creare un menu che concateni le tre funzioni precedenti e permetta di ripetere il ciclo a più utenti diversi

#funzione salvataggio dati utente

login_utente = ""
nome_utente = "" #le creo fuori per usarle in tutte le def?
password_utente = ""
login_password = ""
id_utente = 0
#funzione dati utente
def registrazione_utente(nome_utente, password_utente):
    nome_utente = input("Scegli un nome utente: ")
    password_utente = input("Scegli una password: ")
    utente_1 = [] #meglio usare un dizionario
    utente_1.append(nome_utente, password_utente)
    id += 1

#funzione login
def login(nome_utente, password_utente):
    login_utente = input("Inserisci il nome utente: ")
    login_password = input("Inserisci la tua password: ")
    if login_utente == nome_utente and login_password == password_utente:
        print("Benvenuto!")
    else:
        print("Utente non registrato.")
        
#funzione modifica dati utenti
def modifica_registrazione(nuovo_nome_utente, nuova_password):
    scelta1_utente = input("Vuoi modificare il nome utente? Scegli S o N: ")
    if scelta1_utente.lower() == "s":
        nome_utente = input("Digita il nuovo nome utente: ")
    elif scelta1_utente.lower() == "n":
        print("Perfetto.")
    else:
        print("C'e' stato un errore.")
    scelta2_utente = input("Vuoi modificare la password? Scegli S o N: ")
    if scelta2_utente.lower() == "s":
        password_utente = input("Digita la nuova password: ")
    elif scelta2_utente.lower() == "n":
        print("Perfetto.")
    else:
        print("C'e' stato un errore.")
        
def menu():
    while True:
        domanda1 = input("Benvenuto! Devi registrarti? Scegli S o N, premi 9 per uscire: ")
        if domanda1.lower() == "s":
            registrazione_utente()
        elif domanda1 == "9":
            break
        elif domanda1 == "n":
            login()
            if login_utente == nome_utente and login_password == password_utente:
                modifica_registrazione() #cosi' la legge SOLO se ho fatto il Login o sbaglio?
        else:
            print("C'e' stato un errore.")
            
menu()
