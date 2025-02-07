# Es. 1 if
# prendi imput, capire se e' pari o dispari, stampare

numero_pari = int(input("Ciao! Scrivi un numero e ti diro' se e' pari o dispari: "))

if numero_pari%2 == 0:
     print("Il numero che hai digitato e' pari!")
elif numero_pari%2 != 0:
     print("Il numero che hai digitato e' pari!")
else: print("Questo non e' un numero!")



# Es. 2 while + range
# prende input numero N positivo 

lista_es2 = []
max_lista_es2 = 0
controllore = True

while controllore:
    numero_es2 = int(input("Scrivi un numero intero positivo: "))
    for numero in range(numero_es2):
        lista_es2.append(numero)

    max_lista_es2 = max(lista_es2)

    lista_es2range = range(max_lista_es2, 0, -1)

    for numeri in lista_es2range:
        print(numeri)
    
    decisione = input("Vuoi continuare? Scegli S o N ")
    if decisione.lower() == "s":
        pass
    elif decisione.lower() == "n":
        print: ("Allora ciao!")
        controllore = False
    else:
        print("Scelta non valida")




# Es. 3 for
# Ciclo per aggiungere alla lista, poi esci. 
# Uso ciclo for i in lista, stampa(i**2)

lista_es3 = []
controllore = True

#Ciclo while per inserire numeri nella lista
while controllore:
     numero_da_aggiungere = int(input("Scrivi un numero da aggiungere alla lista: "))
     lista_es3.append(numero_da_aggiungere)
     decisione = input("Vuoi aggiungere un altro numero? Scegli S o N: ")
     if decisione.lower() == "s":
          pass
     elif decisione.lower() == "n":
          print("Fermiamoci qui! Ecco la tua lista: ", lista_es3, ".")
          controllore = False
     else:
          print("Scelta non valida")
          pass     
          
#ciclo for per stampare il quadrato dei numeri
for numero in lista_es3:
     print(numero**2)
 
     


# Es. 4 if + while + for
# Lista input di numeri interi. For per trovare il Max, while per contare i numeri, if per lista vuota oppure num max e num min.
    
###### Inserisco tutti i valori insieme, codice molto piu' snello


lista_es4 = []
valore_es4 = 0
controllore = True
max_lista_es4 = 0
counter_numeri = 0

numeri_da_aggiungere = int(input("Quanti valori vuoi aggiungere? "))

# Ciclo while per inserire numeri nella lista
while numeri_da_aggiungere >0 :
     valore_es4 = int(input("Aggiungi un valore per la lista: "))
     lista_es4.append(valore_es4)
     numeri_da_aggiungere -= 1
     
for numeri in lista_es4:
     max_lista_es4 = max(lista_es4)


# while per contare i numeri,     
while counter_numeri < len(lista_es4):
     counter_numeri += 1

print("La lista e' compsota da ", counter_numeri, " numeri.")

# if per lista vuota oppure num max e num min.
if len(lista_es4) == 0:
     print("La lista e' vuota.")
elif len(lista_es4) != 0:
     print("Il numero massimo e' ", max(lista_es4), " ed il numero minimo e' ", min(lista_es4))
else:
     print("C'e' un errore!")
     
 
     

###### Esercizio completo slide 89

# Entro in applicazione creando il primo ciclo While true vuoi entrare nel menu'? Si o no, e metto break. Se si, entro nel menu.

risposta = ""
lista_es89 = []
somma_pari = 0

while True:
     risposta = input("Vuoi entrare nel menu'? Premi S o N: ")
     if risposta.lower() == "n":
          break
     elif risposta.lower() == "s":
     ## ciclo While per inserire un numero. Controllo se il numero e' corretto ed entro nel menu' che ha 5 opzioni (if con 5 casi e un else)
          while True:
                numero_es89 = int(input("Inserisci un numero positivo, o scrivi 9 per uscire dal programma: "))
                if numero_es89 <= 0:
                    print("Il numero non e' positivo.")
                elif numero_es89 == 9:
                   print("Oh no! Addio!")
                   break
                else:
                    risposta2 = input("Hai inserito il numero positivo. Vuoi cambiarlo? Scegli S o N: ")
                    if risposta2.lower() == "n":
                        # inserire le opzioni: calcolo numeri pari
                        opzione_menu = int(input("Premi: 1 per sommare tutti i numeri pari compresi tra 0 ed il numero scelto, 2 per stampare tutti i numeri dispari compresi tra 0 ed il numero scelto, 3 per verificare se il numero scelto e' un numero primo, 4 per uscire dal programma. "))
                        if opzione_menu == 1:
                            for n in range(0, numero_es89+1, 2):
                                somma_pari += n
                                print(somma_pari) #in questa riga stampa tutte le somme passo dopo passo
                            print(somma_pari) #mettendo il print fuori il ciclo for, stampa direttamente la somma finale
                        # stampare numeri dispari,
                        elif opzione_menu == 2:
                            for n in range(1, numero_es89, 2):
                                print(n)
                        # verificare se numero_es89 e' primo
                        elif opzione_menu == 3:
                            if numero_es89 < 2:
                                print("1 e 0 non sono considerati numeri primi.")
                            else:
                                num_primo = True
                                for numero in range(2, numero_es89):
                                    if numero_es89 % numero == 0:
                                        num_primo = False
                                        break
                                if num_primo:
                                    print(numero_es89, " e' un numero primo.")
                                else:
                                    print(numero_es89, " non e' un numero primo.")
                                                #Altra possibilita' per i numeri primi e' creare un for che verifica se dividendo il numero per tutti i valori del range da sopra 2 al numero meno il numero target, e verifico il resto
                        ### for x in range (2, numero_89_1, 1):
                                #if numero_89 % x != 0:
                                #   print("Il numero e' primo")
                                #else:
                                    #print("Il numero non e' primo")
                                    #break
                        #inserire uscita dal programma
                        #
                        #inserire uscita dal programma
                        elif opzione_menu == 4:
                            print("Ciao!")
                            break
                        else:
                            print("Scelta non valida")
                            continue
                    else:
                         print("Hai scelto di cambiare il numero")
     else:
          print("Scelta non valida.")
          