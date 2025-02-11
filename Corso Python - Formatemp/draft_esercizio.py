
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
            
            
