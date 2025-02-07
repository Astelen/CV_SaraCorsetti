##Hai 60 min per creare un esercizio che rappresenti tutto quello che hai imparato nella settimana precedente,
# riprendi la tabella delle conoscenze per maggiori info.

#Software Bignami: aiuto per la scuola

#esercizio if per numero pari/dispari ed esercizio For ##INSERITO
numero_inserito = 0
if numero_inserito%2 == 0:
    print("Il numero e' pari")
elif numero_inserito%2 != 0:
    print("Il numero e' dispari")
    scelta2 = input("Vuoi sapere se e' dispari? Scegli S o N: ")
    if scelta2.lower() == "s":
        for numero in range(3, numero_inserito):
            if numero_inserito % numero != 0:
                print("Il numero e' anche primo, farai un figurone!")
            else: 
                print("Il numero non e' primo.")
    elif scelta2.lower() == "n":
        print("Rimani nell'ignoranza!")
    else:
        print("Scelta non valida.")
else:
    print("C'e' stato un errore.")
    
#esercizio while ##INSERITO
while True:
    scelta = input("Se hai bisogno del Bignami per barare al compito di matematica, digita 21, che e' la risposta universale! Altrimenti digita Esc. Puoi digitare il numero 666 quante volte vuoi, senza causare nulla. ")
    if scelta == "21":
        print("Ci pensa il tuo Bignami informatico!")
    elif scelta.lower() == "esc":
        print("Bugiardo, tutti ne hanno bisogno!")
        break
    elif scelta == "666":
        continue
    else:
        print("Se non sai neanche digitare 21 o Esc, decisamente ti serve il nostro aiuto. Torna al menu' principale.")    

#operatore splat ##INSERITO
numero_divisore = input("Inserisci il numero dei divisori" )
lista_divosir_splat = [*range(1, numero_divisore)]

#lista
lista_jukebox = []

if len(lista_jukebox) == 0:
    print("Il Juke-box e' vuoto! Inserisci una canzone")
    canzone1 = input("Inserisci il titolo della canzone da aggiungere: ")
    lista_jukebox.append(canzone1)
elif len(lista_jukebox) < 10:
    canzone1 = input("Inserisci il titolo della canzone da aggiungere: ")
    lista_jukebox.append(canzone1)
if len(lista_jukebox) >= 10:
    print("Il Juke-box e' pieno")
    
#castare lista in Tupla perche' le canzoni nel Juke-box non sono modificabili
lista_jukebox = tuple(lista_jukebox)



#creazione funzione programma Bignami mascherato da Juke-boxe per barare ai compiti in classe.
                    
def numero_pariodispari():
    numero_inserito = 0
    if numero_inserito%2 == 0:
        print("Il numero e' pari")
    elif numero_inserito%2 != 0:
        print("Il numero e' dispari")
        scelta2 = input("Vuoi sapere se e' dispari? Scegli S o N: ")
        if scelta2.lower() == "s":
            for numero in range(3, numero_inserito):
                if numero_inserito % numero != 0:
                    print("Il numero e' anche primo, farai un figurone!")
                    lista_divisori_splat = [*range(1, numero_inserito)]
                    print("So che non ti interessa, ma ecco la lista dei possibili divisori fino al numero scelto: ", lista_divisori_splat)
                else: 
                    print("Il numero non e' primo.")
        elif scelta2.lower() == "n":
            print("Rimani nell'ignoranza!")
        else:
            print("Scelta non valida.")
    else:
        print("C'e' stato un errore.")

def juke_box():
    print("Benvenuto nel juke-box!")
    lista_jukebox = []
    if len(lista_jukebox) == 0:
        print("Il Juke-box e' ancora vuoto! Inserisci una canzone")
        canzone1 = input("Inserisci il titolo della canzone da aggiungere: ")
        lista_jukebox.append(canzone1)
    elif len(lista_jukebox) < 10:
        canzone1 = input("Inserisci il titolo della canzone da aggiungere: ")
        lista_jukebox.append(canzone1)
    if len(lista_jukebox) >= 10:
        print("Il Juke-box e' pieno")
        lista_jukebox = tuple(lista_jukebox)

def menu_bignami():
    while True:
        scelta = input("Se hai bisogno del Bignami per barare al compito di matematica digita 21, che e' la risposta universale! Se devi nasconderti nel juke_buke, digita J. Altrimenti digita Esc. Puoi digitare il numero 666 quante volte vuoi, senza causare nulla. ")
        if scelta == "21":
            print("Ci pensa il tuo Bignami musicale!")
            return numero_pariodispari()
        elif scelta.lower() == "j":
            return juke_box()
        elif scelta.lower() == "esc":
            print("Bugiardo, tutti ne hanno bisogno!")
            break
        elif scelta == "666":
            continue
        else:
            print("Se non sai neanche digitare 21 o Esc, decisamente ti serve il nostro aiuto. Torna al menu' principale.")    
            
def decoratore():
    def wrapper():
        print("Benvenuto nel Bignami elettronico trasformato da Juke-boxe, ti fa i calcoli e ascoltare la musica, cosi' il professore non scoprira' che hai barato.")
        menu_bignami()
    return wrapper
        
@decoratore #richiama decoratore
#richiamare funzione





## Andiamo ora a creare un sistema di funzioni che richiami tutte le singole parti che abbiamo creato nel precedente esercizio,
# devono essere usate SOLO funzioni e almeno da 2 decoratori ed essere ripetibile