
patente = "no"

eta = 21

bevuto = "si"

if eta < 18:
    print("Sei minorenne, non puoi guidare")
elif patente != "si":
    print("Non hai la patente, non puoi guidare")
elif bevuto != "no":
    print("Non puoi guidare perche' hai bevuto")
else:
    print("Puoi guidare")
    
    
    
##Esercizio per riportare vocale e indice
def trova_parole():
    vocali = "aeiou"
    frase = input("Scrivi una frase: ")
    indice = 0
    for elemento in frase.lower():
        indice += 1
        if elemento in vocali:
            print(f"Vocale: {elemento}, indice: {indice}")
            
        
trova_parole()


##Varie su Dizionari

mio_diz = { "Nome" : "Sara", "Cognome" : "Corsetti" }

## mio_diz["via"] # non mi stampa perche' non c'e', mi da' errore!
print(mio_diz.get("via", "Via non presente"))  ##Questo metodo cerca una chiave e riporta un testo in caso in cui non venga trovata
print(mio_diz)


lista1 = ["uno", "due"]

for indice, valore in enumerate(lista1):
    print(list(enumerate(lista1)))
    #oppure print(f:Indice {indice}, valore {valore})
    
    

##Esercizio traccia
# # Scrivete un programma che chiede una stringa all’utente e
# restituisce un dizionario rappresentante la "frequenza di
# comparsa" di ciascun carattere componente la stringa.
# Esempio:
# Stringa "ababcc",
# Risultato
# {"a": 2, "b": 2, "c": 2}

def es_diz():
    stringa1 = input("Scrivi una frase: ")
    for lettera in stringa1:
        indice =+ 1
        for indice in len(stringa1):
            return lettera, indice
        # aggiungere a dizionario
        
es_diz()



## Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti,
# quando l’utente scrive media il programma andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10


diz_alunni = {"Nome" : "Marco", "Nome" : "Marco"}
print(diz_alunni)

def stampa_dati_alunni():
    diz_alunni = {}
    nome = input("Scrivi il nome: ")
    media = input("Scrivi media: ")
    diz_alunni[-1]
    pass




## Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti,
# quando l’utente scrive media il programma andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

diz_alunni = {}
def stampa_dati_alunni(nome, voto, diz_alunni):
    diz_alunni[nome] = voto
    
    somma = 0
    
    
    for numero in voto:
        somma += numero
        media = somma/ len(voto)
    diz_alunni[nome] = media
    return diz_alunni
    
    # stampa_media = input("Cosa vuoi stampare? ")
    # if stampa_media.lower() == "media":
    #     for chiave, valore in diz_alunni:
    #         print(f"Nome alunno: {chiave}, media voti: {valore}")
    # else:
    #     print("Ciao!")


#### Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti,
# quando l’utente scrive media il programma andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

dizionario2 = {}
def calcolo_media(lista_voti):
    return sum(lista_voti)/ len(lista_voti)

while True:
    nome = input("Scrivi il nome: ")
    numero_voti = int(input("Quanti voti vuoi inserire? "))
    lista_voti = []
    for x in range(numero_voti):
        voto = int(input("Inserisci il voto: "))
        lista_voti.append(voto)
    dizionario2[nome] = lista_voti
    scelta_aggiunta = input("Vuoi continuare ad aggiungere? S/N: ")
    if scelta_aggiunta.lower() == "s":
        print("Aggiungi")
    else:
        for elemento in dizionario2:
            print(elemento, calcolo_media(dizionario2[elemento]))
        break
            
            


lista = ["1", "2", "3", "4"]
lista2 = []
for x in lista: #come convertire valori in interi.
    lista2.append(int(x))

lista3 = [int(num) for num in lista] #prima scrivo cosa faccio all'elemento, poi dico dove li trovo
lista4 = [int(num) for num in lista if int(num)%2==0] #escludo i dispari

print(lista)
print(lista2)
print(lista3)
print(lista4)