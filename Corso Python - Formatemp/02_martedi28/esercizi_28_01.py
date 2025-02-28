# 28 gennaio 2025
nome = ""
eta = 0
cap = 0
boolRif = False

if nome == "" and eta == 0 and cap == 0 and  boolRif == False:
    nome = input("Inserisci il nome")
    if nome != "" and eta == 0 and cap == 0 and boolRif == False:
        eta = int(input("Inserisci l'eta'"))
        if nome != "" and eta > 0 and cap == 0 and boolRif == False:
            cap = int(input("Inserisci il tuo cap"))
            if nome != "" and eta > 0 and cap != 0 and boolRif == False:
                if (riferimento > 0):
                    boolRif = False
                    print (nome, eta, cap, boolRif)
                elif(riferimento <=0):
                    boolRif = True
                    print(nome, eta, cap, boolRif)
                else:
                    print("Pippo hai sbagliato a digitare")
                

# esercizio verde

nome_utente_registrazione = ""
password_registrazione = ""
login_bool = False
scelta = ""
modifica = ""

if nome_utente_registrazione == "":
    nome_utente_registrazione = input("Registrati! Scegli un nome utente: ")
    if nome_utente_registrazione != "":
        print("Benvenuto ", nome_utente_registrazione, "!")
        password_registrazione = input("Ora scegli la tua password: ")
    else: 
        pass  #evita errore perche' vuoto
 
# richiedo il login per evitare furto di dati da parte di Pippo
nome_utente_login = input("Inserisci il nome per il login: ")
password_login = input("Inserisci la password: ")

if nome_utente_login.lower() == nome_utente_registrazione.lower() and password_login == password_registrazione:
    login_bool = True
    print("Benvenuto ", nome_utente_registrazione, "! Vuoi modificare qualcosa?")
    modifica = input("Premi: 1 per modificare il nome utente, 2 per modificare la password, qualsiasi altro tasto se non vuoi modificare nulla")
    if modifica == "1":
        nome_utente_registrazione = input("Scegli il nuovo nome utente: ")
        nome_utente_login = nome_utente_registrazione
    elif modifica == "2":
        password_registrazione_registrazione = input("Scegli la nuova password: ")
        password_login = password_registrazione
    else:
        print("Hai scelto di non modificare nulla! Proseguiamo")
else:
    print("Non sei registrato! Torna alla pagina di registrazione cliccando sull'icona della penna")
    
if login_bool:
    scelta = input("Quale domanda segreta vuoi? A) Nome dell'animale domestico; B) Nome del supereroe preferito")
else:
    pass

if scelta.upper() == "A" or "B":
    scelta_segreta = input("Inserisci la risposta segreta: ")
else:
    print("La scelta non e' valida")
    
    
    
#esercizio if - else - elif
lista_valori = []
valore1 = int(input("Aggiungi valore numerico "))
valore2 = int(input("Aggiungi valore numerico "))
valore3 = int(input("Aggiungi valore numerico "))

if valore1 > 0 and valore2 > 0 and valore3 > 0:
    lista_valori.append(valore1)
    lista_valori.append(valore2)
    lista_valori.append(valore3)
    
    if len(lista_valori) > 0:
        lista_valori.sort()
else:
    pass

print(lista_valori)

numero_valori = int(input("Quanti valori puoi aggiungere?" ))
lista_valori2 = []       
   
   
#rivedere ciclo while                 
while len(lista_valori2) < numero_valori:
    valore = int(input("Quale valore puoi aggiungere?"))
    lista_valori2.append(valore)
    print(lista_valori2)
    
lista_valori2.sort()
lista_valori2.reverse()


#esercizio eta

eta = int(input("Quanti anni hai?"))
lista = ["1: Il silenzio degli innocenti", "2: The Mask", "3: Piovono Polpette"]

if eta >= 18:
    print("Sei maggiorenne! Puoi vedere uno dei nostri film. Ecco la lista: \n", lista)
    scelta = int(input("Scegli il film selezionando il numero relativo: "))
    if scelta == 1:
        print("Hai scelto ", lista[0])
    if scelta == 2:
        print("Hai scelto ", lista[1])
    if scelta == 3:
        print("Hai scelto ", lista[2])i
else:
    print("Mi dispiace, nsei troppo giovane, questi film sono vietati ai minori di 18 anni!")
    
    
#esercizio 2 if-else-elif

print("Benvenuto nella calcolatrice virtuale!")
operazione_da_eseguire = int(input("Premi: 1 per Addizione, 2 per Sottrazione, 3 per Moltiplicazione, 4 per Divisione. "))
valore1 = ""
valore2 = ""
                        
if operazione_da_eseguire == 1:
    valore1 = int(input("Inserisci il primo numero "))
    valore2 = int(input("Inserisci il secondo numero "))
    print("Ecco il risultato dell'addizione: ", valore1 + valore2)
elif operazione_da_eseguire == 2:
    valore1 = int(input("Inserisci il primo numero "))
    valore2 = int(input("Inserisci il secondo numero "))
    print("Ecco il risultato dell'addizione: ", valore1 - valore2)
elif operazione_da_eseguire == 3:
    valore1 = int(input("Inserisci il primo numero "))
    valore2 = int(input("Inserisci il secondo numero "))
    print("Ecco il risultato della moltiplicazione: ", valore1 * valore2)
elif operazione_da_eseguire == 4:
    valore1 = int(input("Inserisci il primo numero "))
    valore2 = int(input("Inserisci il secondo numero "))
    if valore2 == 0:
        print("Burlone! Non si puo' dividere un numero per 0")
    else:
        print("Ecco il risultato della divisione: ", valore1 / valore2)
else:
    print("La scelta dell'operazione non e' disponibile, o hai selezionato un numero sbagliato")
    
    

#esercizio 2 con cicli

print("Benvenuto nella calcolatrice virtuale!")
numero_operazioni = int(input("Quante operazioni vuoi eseguire?"))

if numero_operazioni == 0:
    print("D'accordo, allora ciao!")
else:
    pass #mettere il resto delle operazioni sotto Else?

operazione_da_eseguire = 0
operazioni_eseguite = 0

while operazioni_eseguite <= operazione_da_eseguire:
    operazione_da_eseguire = int(input("Perfetto! Che tipo di operazione? Premi: 1 per Addizione, 2 per Sottrazione, 3 per Moltiplicazione, 4 per Divisione. "))
    if operazione_da_eseguire <4 and operazione_da_eseguire >0:
        valore1 = int(input("Inserisci il primo numero "))
        valore2 = int(input("Inserisci il secondo numero "))
        if operazione_da_eseguire == 1:
            print("Ecco il risultato! ", valore1 + valore2)
            operazioni_eseguite += 1
        elif operazione_da_eseguire == 2:
            print("Ecco il risultato! ", valore1 - valore2)
            operazioni_eseguite += 1
        elif operazione_da_eseguire == 3:
            print("Ecco il risultato! ", valore1 * valore2)
            operazioni_eseguite += 1
        elif operazione_da_eseguire == 4:
            if valore2 == 0:
                print("Non si puo' dividere per 0, lo sanno tutti!")
            else:
                print("Ecco il risultato! ", valore1 / valore2)
                operazioni_eseguite += 1
    else:
        print("selezione errata!")
        

numeri = [1, 2, 3, 4, 5]

for x in numeri:
    print(x)



#primo esercizio ciclo While, modo di Costanza

numero_range = int(input("Inserisci un numero per iniziare il conto alla rovescia"))
lista_range = range(numero_range) 
for x in lista_range:
    if x == 0: #questo e' il primo passaggio perche' x parte da 0 e quindi serve a selezionare il max!!
       max = len(lista_range)
    print(lista_range[max-1])
    max -= 1
        
        
#primo esercizio ciclo While,
#modo di Carmen (forse?)
controllore = True
lista_carmen = []
while controllore:
    numero_carmen = int(input("Inserisci un numero"))
    lista_carmen.append(numero_carmen)
    decisione = input("Vuoi continuare? Scegli si o no ")
    if decisione == "no":
        controllore = False
    else:
        pass
#questo l'ho copiato dalla soluzione di Costanza
for valori in range(len(lista_carmen), -1, -1):
    print(valori)
    
    
    
    
    
## Nuova prova esercizio 1 ##   
controllore = True
prova_lista2 = []

while controllore: #aggiungo elementi inseriti dall'utente alla lista
    valore_prova2 = int(input("Inserisci un numero: "))
    prova_lista2.append(valore_prova2)
    decisione2 = input("Vuoi continuare? Scrivi Y per yes o N per no")
    if decisione2.lower() == "n": #serve a chiudere il ciclo se l'utente non vuole piu' aggiungere numeri
        break
    else: #continua il ciclo (anche se andrebbe messo elif per Y e un else per dire che la scelta non e' corretta)
        pass

max = max(prova_lista2) #seleziona valore massimo

for valore in range(max, -1, -1): #fa il range e stampa ogni valore! Parte dal massimo che ho definito alla riga precedente, poi mi fermo a 0 (perche' ho scritto -1) e ho un passo di -1 perche' vado all'indietro 
    print(valore)
    
    
    
    
    
#####Compito di Carmen
controllore = True
numeri = []

while (controllore):
    numero = int(input("Inserisci un numero: "))

#Inserisce i valori nella lista da 0 a numero
for num in range(0, numero):
    numeri.append(num)

#Dispone i valori in ordine decrescente
numeri.reverse()
print(numeri)

#Controllo per condizione di rottura
risposta = input("Vuoi continuare? (y/n) : ")
if (risposta == "y"):
    controllore = True
elif (risposta == "n") :
    print("Ciao")
    controllore = False
else :
    print("Carattere non valido")

####Fine compito di Carmen






        
#secondo esercizio, creo lista numeri primi vuota, poi ciclo while con lista < 5, poi input con numero e controllo se e' primo e lo aggiungo alla lista se e' primo
lista_pari = []
while len(lista_pari) <5:
    numero_da_verificare = int(input("Inserisci un numero: "))
    if numero_da_verificare%2 == 0:
        print("Il numero e' pari")
        lista_pari.append(numero_da_verificare)
    else:
        print("Il numero e' dispari")
print(lista_pari)

    