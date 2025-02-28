y = "boh"
nome = "Sara"
eta = 23
print("Il mio nome e' ", nome, "ed ho ", eta, " anni")

nome = input("Inserisci il tuo nome")
eta = int(input("Inserisci la tua eta'"))
print(1+2)
print("1" + "2")

s = "Python"
print(s[0])
print(s[2])

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio)

prova = "Evviva tutti"
print(prova)
print(len(prova))
print(prova.upper())
print(prova.lower())
print(prova.split(" "))
print(prova.replace("tutti", "io"))
print(4==4)

numero_intero = 2
print(float(numero_intero))
stringa_prova = "Ciao sono Sara"
print(2>2) # booleano false
print(5>2) # booleano true

print(input()) #bisogna usare l'input per l'esercizio


print(int(input("Scrivi un numero decimale!")))
print(float(input("Scrivi un numero intero!")))
print(input("Scrivi l'iniziale del tuo nome "))


nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))
altezza = float(input("Quanto sei alto?"))
classe = str(input("In che classe eri? "))
sport = bool(input(("Fai sport? ")))
print(sport)

print("Ciao ", nome, ", hai ", eta, " anni, sei alto ", altezza, " cm e ti piace lo sport", sport)


# Esercizi IF

numero = input("Scrivi un numero ")
if  numero == 0:
    print("Il numero e' 0!")
elif numero > 0:
    print("Il numero e' positivo")
else:
    print("Il numero e' negativo")
    
    
    # esercizio 2 27 gennaio
nome = input("Scrivi il tuo nome")
variazione = input("Vuoi modificare i tuoi dati? Seleziona tra: aggiungi, sostituisci o elimina")
variazione = variazione.lower()

if variazione == "aggiungi":
    nome = nome + input("Scrivi cosa vuoi aggiungere")
    print("Il tuo nuovo nome e' ", nome)
elif variazione == "sostituisci":
    nuovo_nome = input("Scrivi il nuovo nome") #idea stupida, basta inserire come input una nuova variabile chiamata nome che si sovrascrive
    nome = nome.replace (nome, nuovo_nome)
    print("Il nuovo nome utente e' ", nome)
elif variazione == "elimina":
    nome = " "
    print("Hai eliminato il tuo nuovo nome")
else: 
    nome == " " 
    print("Questo comando non e' valido!")
    
    
# esercizio 3, If, 27 gennaio, seconda prova

nome_utente = "utente_anonimo" 
id = 0 

if nome_utente == "utente_anonimo" and id ==0: # primo If per creazione primo utente
    nome_utente = input("Inserisci il tuo nome utente ") # creazione nome_utente e sovrascrizione variabile precedente
    password = input("Inserisci la tua password ")
    id =+ 1 # aumento ID di 1 ogni volta che viene creato un utente
    
    if nome_utente == "utente_anonimo" and id ==0: # verifico creazione nome utente
        print("Qualcosa e' andato storto")
    else:
        print("Benvenuto ", nome_utente, "! Hai creato il tuo account")
else: 
    print("C'e' stato un errore")
    
    
# Fine esercizi If

