#ES. slide 70

# nome_utente = "admin"
# password = "1234"

#Menu
# while True:
#     print("Benvenuto nel sistema!")
#     utente_1 = input("Inserisci il nome utente: ")
#     password_1 = input("Inserisci la tua password: ")
#     if utente_1 == nome_utente and password_1 == password:
#         print("Credenziali corrette! Accesso consetntito")
#         break
#     else:
#         print("Credenziali errate! Riprova")

# Esercizio slide 80
# while True:
#     print("Benvenuto! L'assistente virtuale ti aiutera' a sapere se il numero e' pari o dispari")
#     numero_da_verificare = int(input("Inserisci un numero: "))
#     if numero_da_verificare % 2 ==0:
#         print("Il numero e' pari")
#     elif numero_da_verificare % 2 !=0:
#         print("Il numero e' dispari")
#     else:
#         print("Qualcosa e' andato storto")
#     scelta = input("Vuoi controllare un altro numero? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

# while True:
#     print("Benvenuto nell'assistente virtuale!")
#     numero_input = int(input("Inserisci un numero: "))
#     for i in range(numero_input, 0, -1):
#         print(i)
#     scelta = input("Vuoi controllare un altro numero? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

# while True:
#     print("Benvenuto nell'assistente virtuale!")
#     numero_input = int(input("Inserisci un numero: "))
#     lista_range = range(numero_input, 0, -1)
#     for i in lista_range:
#         print(i * i)
#     scelta = input("Vuoi controllare un altro numero? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

# while True:
#     print("Benvenuto nell'assistente virtuale!")
#     scelta_numeri = int(input("Quanti numeri vuoi inserire? "))
#     lista_range = []
#     while len(lista_range) < scelta_numeri:
#         numero_input = int(input("Inserisci un numero: "))
#         lista_range.append(numero_input)
#     numero_max = 0
#     for i in lista_range:
#         if i > numero_max:
#             numero_max = i
#     print("Il numero massimo e' ", numero_max)
#     scelta = input("Vuoi continuare con un'altra lista? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

#Es. slide 85 intermedio
# while True:
#     print("Benvenuto! Scrivi due valori positivi che creino un intervallo: ")
#     valore_1 = int(input("Inserisci il primo valore: "))
#     valore_2 = int(input("Inserisci il secondo valore: "))
#     for numero in range(valore_1, valore_2):
#         if numero < 2:
#             continue
#         is_primo = True
#         for i in range(2, numero):
#             if numero % i == 0:
#                 is_primo = False
#                 break
#         if is_primo:
#             print(numero)
#     for x in range (2, numero, 1):
#         if numero % x != 0:
#             print("Il numero e' primo")
#         else:
#             print("Il numero non e' primo")

#Es. slide 85 difficile
# while True:
#     print("Benvenuto!")
#     valore_1 = int(input("Inserisci il primo valore: "))
#     valore_2 = int(input("Inserisci il secondo valore: "))
#     divisori_comuni = []
#     for divisore in range(2, valore_1):
#         if valore_1 % divisore == 0 and valore_2 % divisore == 0:
#             divisori_comuni.append(divisore)
#     if divisori_comuni != []:
#         print("I divisori comuni sono:", divisori_comuni)
#     else:
#         print("Non ci sono divisori comuni")
#     scelta = input("Vuoi continuare? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

# while True:
#     print("Benvenuto!")
#     stringa_1 = input("Inserisci la prima parola: ")
#     stringa_2 = input("Inserisci la seconda parola: ")
#     if stringa_1 == stringa_2:
#         print("Le stringhe sono identiche")
#     else:
#         caratteri_stringa1 = stringa_1.split().sort()
#         caratteri_stringa2 = stringa_2.split().sort()
#         if caratteri_stringa1 == caratteri_stringa2:
#             print("Le stringhe sono anagrammi")
#         else:
#             print("Le stringhe non sono anagrammi")
#     scelta = input("Vuoi continuare? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue

# Es. slide 86
# lista_numeri = []
# while True:
#     numero = int(input("Inserisci un numero: "))
#     if numero != 0:
#         lista_numeri.append(numero)
#     else:
#         print("La somma di tutti i numeri inseriti e' ", sum(lista_numeri))
#         break



# import random
# guess_number = random.randint(1, 100)
# print(guess_number)

# def indovina_numero():
#     import random
#     guess_number = random.randint(1, 100)
#     while True:
#         numero_utente = int(input("Inserisci un numero tra 1 e 100: "))
#         if numero_utente == guess_number:
#             print("Hai indovinato il numero!")
#         elif numero_utente > guess_number:
#             scelta = input("Il numero misterioso e' piu' basso. Scegli si per continuare a giocare, altrimenti scegli no: ")
#             if scelta.lower() == "si":
#                 continue
#             elif scelta.lower() == "no":
#                 print("Va bene, ciao!")
#                 break
#             else:
#                 print("Scelta non valida!")
#                 continue
#         elif numero_utente < guess_number:
#             scelta = input("Il numero misterioso e' piu' alto. Scegli si per continuare a giocare, altrimenti scegli no: ")
#             if scelta.lower() == "si":
#                 continue
#             elif scelta.lower() == "no":
#                 print("Va bene, ciao!")
#                 break
#             else:
#                 print("Scelta non valida!")
#                 continue
#         else:
#             print("Qualcosa e' andato storto")

# while True:
#     print("Benvenuto nel gioco del numero misterioso!")
#     indovina_numero()


# class Automobile:
#     def __init__(self, marca, modello, colore):
#         self.marca = marca
#         self.modello = modello
#         self.colore = colore
        
#     def stampa_info(self):
#         print("L'automobile ha queste caratteristiche: marca: ", self.marca, ",modello: ", self.modello, ", colore: ", self.colore)

# auto1 = Automobile("BMW", "X5", "rosso")
# auto1.stampa_info()

# print(auto1.marca)


#Es. slide 117
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def muovi_punto(self, nuova_x, nuova_y):
#         self.x = self.x + nuova_x
#         self.y = self.y + nuova_y
#         print("Il nuovo punto e' ", self.x, self.y)
        
#     def distanza(self):
#         print("La distanza dall'origine e': ", self.x, " sull'asse delle x e ", self.y, " sull'asse delle y")

# class Libro:
#     def __init__ (self, titolo, autore, pagine):
#         self.titolo = titolo
#         self.autore = autore
#         self.pagine = pagine
        
#     def descrizione(self):
#         print("Il titolo del libro e': ", self.titolo, ", l'autore e': ", self.autore, " e il numero di pagine e': ", self.pagine)

# libro1 = Libro("Hannibal", "Thomas Harris", "500")

# libro1.descrizione()

# class Biblioteca:
#     def __init__(self, nome):
#         self.nome = nome

#     lista_libri = []
    
#     def crea_libro(self):
#         titolo = input("Inserisci il titolo del libro: ")
#         autore = input("Inserisci il nome dell'autore: ")
#         pagine = int(input("Inserisci il numero di pagine: "))
#         aggiunta = Libro(titolo, autore, pagine)
#         self.lista_libri.append(aggiunta)
#         print("Il libro e' stato aggiunto alla biblioteca")
        
#     def stampa_libri(self):
#         for libro in self.lista_libri:
#             print("Il titolo del libro e': ", libro.titolo, ", l'autore e': ", libro.autore, " e il numero di pagine e': ", libro.pagine)
    

# biblio = Biblioteca("Biblioteca Comunale")

# while True:
#     biblio.crea_libro()
#     biblio.stampa_libri()
#     scelta = input("Vuoi continuare? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue


#Es. ristorante slide 119
# class Ristorante:
#     def __init__(self, nome, tipo_cucina):
#         self.nome = nome
#         self.tipo_cucina = tipo_cucina
    
#     aperto = False
    
#     menu = {}

#     def descrivi_ristorante(self):
#         print("Il ristorante si chiama ", self.nome, " e la cucina e' ", self.tipo_cucina)
    
#     def stato_apertura(self, aperto):
#         if self.aperto == True:
#             print("Il ristorante e' aperto")
#         else:
#             print("Il ristorante e' chiuso")
    
#     def apri_ristorante(self):
#         self.aperto = True
#         print("Il ristorante e' aperto")
    
#     def chiudi_ristorante(self):
#         self.aperto = False
#         print("Il ristorante e' chiuso")
    
#     def aggiungi_piatto(self, piatto, prezzo):
#         self.menu[piatto] = prezzo
#         print("Il piatto e' stato aggiunto al menu")
    
#     def rimuovi_piatto(self, piatto):
#         if piatto in self.menu:
#             del self.menu[piatto]
#             print("Il piatto e' stato rimosso dal menu")
#         else:
#             print("Il piatto non e' presente nel menu")
    
#     def stampa_menu(self):
#         print("Il menu del ristorante e': ")
#         for piatto, prezzo in self.menu.items():
#             print(piatto, " - ", prezzo)
    
# risto1 = Ristorante("Da Mimmo", "cucina italiana")

# while True:
#     risto1.descrivi_ristorante()
#     risto1.stato_apertura(risto1.aperto)
#     risto1.apri_ristorante()
#     risto1.aggiungi_piatto("Pizza", 10)
#     risto1.aggiungi_piatto("Pasta", 8)
#     risto1.stampa_menu()
#     risto1.rimuovi_piatto("Pizza")
#     risto1.stampa_menu()
    
#     scelta = input("Vuoi continuare? Scegli si o no: ")
#     if scelta.lower() == "si":
#         continue
#     elif scelta.lower() == "no":
#         print("Va bene, ciao!")
#         break
#     else:
#         print("Scelta non valida!")
#         continue


#Es slide 120, fabbrica
# class Prodotto:
#     def __init__(self, nome, costo_produzione, prezzo_vendita):
#         self.nome = nome
#         self.costo_produzione = costo_produzione
#         self.prezzo_vendita = prezzo_vendita
    
#     def calcola_profitto(self):
#         print("Il profitto e': ", self.prezzo_vendita - self.costo_produzione)

# class Elettronica:
#     def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
#         self.nome = nome
#         self.costo_produzione = costo_produzione
#         self.prezzo_vendita = prezzo_vendita
#         self.garanzia = garanzia
    
#     def calcola_profitto(self):
#         print("Il profitto e': ", self.prezzo_vendita - self.costo_produzione)

# class Abbigliamento:
#     def __init__(self, nome, costo_produzione, prezzo_vendita, tessuto):
#         self.nome = nome
#         self.costo_produzione = costo_produzione
#         self.prezzo_vendita = prezzo_vendita
#         self.tessuto = tessuto
    
#     def calcola_profitto(self):
#         print("Il profitto e': ", self.prezzo_vendita - self.costo_produzione)

# class Fabbrica:
#     def __init__(self, nome):
#         self.nome = nome
    
#     inventario = {}
    
#     def aggiungi_prodotto(self):
#         tipo_prodotto = input("Scegli 1 per Prodotto generico, 2 per Abbigliamento, 3 per Elettronica")
#         nome = input("Scrivi il nome del prodotto: ")
#         costo_produzione = int(input("Scrivi il costo di produzione del prodotto: "))
#         prezzo_vendita = int(input("Scrivi il prezzo di vendita del prodotto: "))
#         if tipo_prodotto == "1":
#             Prodotto(nome, costo_produzione, prezzo_vendita)
#             self.inventario[nome] = costo_produzione, prezzo_vendita
    
#     def stampa_inventario(self):
#         for elemento in self.inventario.items():
#             print(elemento)

# fabbrica1 = Fabbrica("Bolzano")
# fabbrica1.aggiungi_prodotto()
# fabbrica1.stampa_inventario()



#Es. slide 137
# class Animale:
#     def __init__(self, nome, eta):
#         self.nome = nome
#         self.eta = eta
#     def fai_suono(self):
#         print(self.nome, " fa un suono generico!")

# class Giraffa(Animale):
#     def __init__(self, nome, eta, altezza):
#         Animale.__init__(self, nome, eta)
#         self.altezza = altezza
#     def fai_suono(self):
#         print(self.nome, " e' una giraffa e fa una specie di muggito!")

# class Leone(Animale):
#     def __init__(self, nome, eta, criniera):
#         Animale.__init__(self, nome, eta)
#         self.criniera = criniera
#     def fai_suono(self):
#         print(self.nome, " e' un leone, i leoni ruggiscono!")
#     def caccia(self):
#         print(self.nome, " caccia in branco con gli altri leoni")

# giraffa1 = Giraffa("Marta", 24, 2.58)
# giraffa1.fai_suono()
# leone1 = Leone("Lambert", 3, "nera")
# leone1.caccia()


#es. slide 138 squadre
# class MembroSquadra():
#     def __init__(self, nome, eta):
#         self.nome = nome
#         self.eta = eta
#     def descrivi(self):
#         print("Questo membro si chiama ", self.nome, " ed ha ", self.eta, " anni")

# class Giocatore(MembroSquadra):
#     def __init__(self, nome, eta, ruolo, numero_maglia):
#         super().__init__(nome, eta)
#         self.ruolo = ruolo
#         self.numero_maglia = numero_maglia
    
#     def gioca_partita(self):
#         print("Il giocatore ", self.nome, " gioca solo il secondo tempo")

# class Allenatore(MembroSquadra):
#     def __init__(self, nome, eta, esperienza):
#         MembroSquadra.__init__(self, nome, eta)
#         self.esperienza = esperienza
    
#     def dirige_allenamento(self):
#         print("L'allenatore ", self.nome, " fa fare un breve riscaldamento e poi tutta partita")

# giocatore1 = Giocatore("Paolo", 25, "attaccante", 10)
# giocatore1.gioca_partita()
# allenatore1 = Allenatore("Sara", 37, 12)
# allenatore1.dirige_allenamento()

#Esercizi attributi privati__/protetti_
# class Computer():
#     def __init__(self, processore):
#         self.__processore = processore
    
#     def get_processore(self):
#         print(self.__processore)
    
#     def set_processore(self, processore):
#         self.__processore = processore

# computer1 = Computer("Intel 5")
# computer1.get_processore()
# computer1.set_processore("Silicon")
# computer1.get_processore()

#Es banca slide 151
# class ContoBancario:
#     def __init__(self, titolare, saldo):
#         self.__titolare = titolare
#         self.__saldo = saldo
    
#     def deposito(self, aggiunta):
#         if aggiunta > 0:
#             self.__saldo = self.__saldo + aggiunta
#         else:
#             print("Non puoi versare un valore negativo")
    
#     def get_saldo(self):
#         print("Il saldo ammonta a ", self.__saldo)

# conto1 = ContoBancario("Io", 200)
# conto1.get_saldo()
# conto1.deposito(150)
# conto1.get_saldo()


# import numpy as np
# arr1 = np.arange(0, 50)
# print(arr1)
# print(arr1.dtype)
# arr2 = np.arange(0, 50, dtype = "float64")
# print(arr2.dtype)
# print(arr2.shape)


# arr = np.array([10, 20, 30, 40, 50])
# # Utilizzo di un array di indici
# indices = np.array([1, 3])
# print(arr[indices])  # Output: [20 40]
# # Utilizzo di una lista di indici
# indices = [0, 2, 4]
# print(arr[indices])  # Output: [10 30 50]

# import numpy as np
# import random
# arr1 = np.random.randint(10, 51, size = (40,))
# print(arr1)
# print(arr1[-5:])
# print(arr1[5:15])
# print(arr1[2::3])
# arr1[5:10] = 99
# print(arr1)

# import numpy as np
# import random
# # arr1 = np.random.randint(1, 100, size = (6, 6))
# # print(arr1)
# # print(arr1[1:5])
# # indices = [5, 4, 3, 2, 1, 0]
# # print(arr1[1:5].diagonal())

# arr2 = np.linspace(1,20, 5)
# print(arr2)

# random_arr = np.random.rand(3, 3) 
# print(random_arr)
# random_arr_int = np.random.randint(3, 10, size=6) 
# print(random_arr_int)


# import pandas as pd
# # Dataset di esempio:
# # Vendite: Prodotto, Quantità, Città, Data
# # Costi: Prodotto, Costo per unità
# date = date_range = pd.date_range(start='2021-01-01',periods=4, freq='D')
# vendite = {"Prodotto": ["computer", "mouse", "telefono", "tavolo"],
#         "Quantita": [1, 4, 3, 2], 
#         "Citta": ["Roma", "Roma", "Napoli", "Milano"], 
#         "Data": date}
# costi = {"Prodotto": ["computer", "mouse", "telefono", "tavolo"],
#         "Costo per unita": [1000, 10, 500, 300]}
# df_vendite = pd.DataFrame(vendite)
# print(df_vendite)

# df_costi = pd.DataFrame(costi)
# print(df_costi)

# df_merged = pd.merge(df_vendite, df_costi, on='Prodotto')
# print(df_merged)

# df_merged['Vendite totali'] = df_merged['Quantita'] * df_merged['Costo per unita']
# print(df_merged)
# pivot_fd_merged = df_merged.pivot_table(values='Vendite totali', index='Citta', columns='Prodotto', aggfunc='mean')

# print(pivot_fd_merged)




# Algoritmi sort
# Metodi
lista1 = [3, 7, 4, 3, -1, 4]
lista1.sort()
print(lista1)

lista1 = [3, 7, 4, 3, -1, 4]
lista2 = sorted(lista1)
print(lista2)

# Def Bubblesort: confronta i numeri uno ad uno e li inverte se il secondo e' piu' piccolo del primo
def bubblesort(lista):
    for j in range(0, len(lista)):
        for i in range(0, len(lista) -1):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

lista_bubble = [4, 7, 3, 2, -1, -7, 6, 6, 0, 9]
bubblesort(lista_bubble)
print(lista_bubble)

# Algoritmo Selection sort: trova il piu' piccolo e lo mette in prima posizione e cosi' via
def selectionsort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

lista_selection = [4, 7, 3, 2, 55, -7, 6, 6, 0, 109]
selectionsort(lista_selection)
print(lista_selection)

# Algoritmo Insertion sort: crea lista ordinata di valori aggiungendo un valore mano mano
def insertion_sort(lista):
    for i in range(1,len(lista)):       
        chiave = lista[i]
        j = i-1
        while j >= 0 and chiave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chiave

lista_insertion = [4, 40, 16, 2, -1, -7, 6, 6, -29, 9]
insertion_sort(lista_insertion)
print(lista_insertion)
