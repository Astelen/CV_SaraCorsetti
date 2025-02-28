
#Es. funzioni
# Programma che indovina le funzioni
# Funzione che genera numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare il numero generato.

def gioco_numero (numero_primo):
    numero_casuale = numero_primo*2
    if numero_casuale > 100:
        numero_casuale == 100
    #devo controllare che sia diverso da 0
    while numero_casuale != numero_primo: #ciclo while per permettere all'utente di continuare a giocare
        numero_prova = int(input("Inserisci il numero da indovinare tra 1 e 100 "))
        if numero_prova > numero_casuale:
            print("Il numero da indovinare e' piu' basso! Prova ancora: ")
        elif numero_prova < numero_casuale:
            print("Il numero da indovinare e' piu' alto! Prova ancora: ")
        elif numero_prova == numero_casuale:
            scelta_giocatore = input("Hai indovinato! Vuoi continuare a giocare? Scegli S o N: ")
            if scelta_giocatore.lower() == "s":
                print("Continua a giocare!")
            else:
                print("Ok, alla prossima!")
                break
        else:
            print("Il numero scelto non e' un numero, devi inserire un numero per giocare. ")

print("Benvenuto in questo gioco! Il gioco consiste nell'indovinare un numero. Sei pronto?")
print("Ricorda che puoi sempre uscire dal gioco digitando Esc")
scelta_numero = int(input("Scrivi il tuo numero: "))
gioco_numero(scelta_numero)

##Altra possibilita' e' creare la funzione con ciclo For e poi fare un ciclo While esterno solo per entrare nel gioco e continuare a giocare




#es. slide 104
#menu per chiedere numero - ciclo while
#prima funzione per scoprire se e' primo o no, se non e' primo salva in una lista
#seconda funzione per trovare il divisore piu' piccolo

#prima funzione per scoprire se e' primo o no, se non e' primo salva in una lista
def primo(numero_primo):
    for numero in range(2, numero_primo):
        lista_numeri_utente = [] #creo lista
        lista_numeri_utente.append(numero_primo) #aggiungo tutti i valori alla lista
        if numero_primo % numero == 0: #numero non e' primo
            print(False)
            break
        else:
            print(True)
            break

#seconda funzione per trovare il divisore piu' piccolo
divisore_minimo = 1
def divisore(numero_dividendo):
    if numero_dividendo/2 % 0:
        print("Il divisore piu' piccolo e' 2. ")
    else:
        lista_divisori = [*range(3, numero_dividendo)] #creo lista di tutti i divisori da 1 a n
        lista_resti = []
        for numerodadividere in lista_divisori: #ciclo for per provare a dividere n per tutti i numeri della lista_divisori 
            lista_resti.append(numero_dividendo/numerodadividere)
            for resto in lista_resti: ### devo usare un primo If per creare una lista di numeridadividere / divisori, poi un altro if per verificare se sono diversi da 0
                if resto == 0:
                    divisore_minimo = numerodadividere/lista_divisori
                    print("Il divisore piu' piccolo e': ", divisore_minimo)
                    break
                else:
                    ("C'e' stato un errore.")
                
#creazione Menu'
decisione_utente = ""
numero_gioco = 0
def menu(scelta_utente):
    while True:
        decisione_utente = input("Ciao! Sono il tuo assistente virtuale. Vuoi entrare nel programma? Scegli S o N: ")
        if decisione_utente.lower() == "s":
            numero_gioco = int(input("Inserisci un numero: "))
            primo(numero_gioco)
            divisore(numero_gioco)
        else:
            print("Ok ciao!")
        
menu()