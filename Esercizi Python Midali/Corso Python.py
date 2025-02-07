Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
3 + 3
6
x = 69
type(x)
<class 'int'>
y = 6.7
type(y)
<class 'float'>
<class 'float'>
SyntaxError: invalid syntax
r = 4.0
type (r)
<class 'float'>
x / y
10.298507462686567
4**4
256
3**3
27
30 / 7
4.285714285714286
30 //7
4
30 % 7
2
10 % 3
1
<class 'float'>
SyntaxError: invalid syntax
y
6.7
x
69
r
4.0
r - 2
2.0
>>> r
4.0
>>> pi_greco = 3.14
>>> pi_greco
3.14
>>> r - 6
-2.0
>>> r
4.0
>>> r = 6
>>> r
6
>>> type(r)
<class 'int'>
>>> v = 8*2
>>> v
16
>>> s = r+v
>>> s
22
>>> amici = "Marco" "Luca" "Sara"
>>> amici
'MarcoLucaSara'
>>> type (amici)
<class 'str'>
>>> amici 'Marco, Luca, Sara'
SyntaxError: invalid syntax
>>> amici = "Marco, Luca, Sara"
>>> amici
'Marco, Luca, Sara'
>>> c = "Ha detto \"no!\""
>>> c
'Ha detto "no!"'
>>> amici + c
'Marco, Luca, SaraHa detto "no!"'
>>> b ="Le ho chieso di venire"
>>> b + c
'Le ho chieso di venireHa detto "no!"'
>>> b + " " + c
'Le ho chieso di venire Ha detto "no!"'

cancello = True

counter = 0
while counter <= 10:
    print(counter)
    counter += 1 # counter = counter + 1


while 33 == 33:
    print("Sei dentro al tunnel!")

counter = 0
run = True
stop = 1000
while run == True:
    print(counter)
    counter += 1 # counter = counter + 1
    if counter > stop:
        print("Siamo quasi fuori dal tunnel")
        break


counter = 0
skip = 3
while counter <10:
    counter += 1 # counter = counter + 1
    if counter == skip:
        print("Sto saltando " + str(skip))
        continue
    print(counter)


counter = 0
skip = 3
while counter <10:
    counter += 1 # counter = counter + 1
    if counter == skip:
        print("Sto saltando " + str(skip))
    print(counter)



for numero in range (38, 5, -2):  # ciclo for dove parto da 38, mi fermo a 5 e scendo di 2 step ogni volta
    print(numero)


import random

for numero in range(10):    # seleziona 10 numeri
    val = random.randint(1, 50)  # random. serve ad indicare il modulo, dopo il punto inserisco il nome della fuznione
    print(val)

from math import sqrt

sqrt (25)

from random import *

for numero in range(10):    # seleziona 10 numeri
    val = randint(1, 50)  # random. serve ad indicare il modulo, dopo il punto inserisco il nome della fuznione
    print(val)



def addizione(a, b):
    print("Questa e' la funzione addizione")
    print("Il risultato dell'addizione e' ", str(a + b))

addizione (5, 7)


def nuovo_lavoro (orario, paga, vicinanza):
    print("Il tuo nuovo lavoro avra' le seguenti caratteristiche: ")
    print("Orario: ", orario)
    print("Salario: ", paga)
    print("Distanza da casa: ", vicinanza)

nuovo_lavoro("8-14", 1200, "12 km")


def addizione(a, b):
    risultato = a + b
    return risultato

addizione (5, 7)



def addizione(a, b):
    risultato = a + b
    return risultato

risultato = addizione (5, 7)
print(risultato)



g = 5

def funzione_esempio ():
    h = g
    h += 2
    return h

print(funzione_esempio())


g = 5

def funzione_esempio ():
    global g
    g += 2
    return g

print(funzione_esempio())


def val ():
    s = 2
    return s

new_val = val() + 2
print(new_val)


my_list = [14, 3.0, "bianco"]
type(my_list)

new_list = [my_list, 5, 6, "nero"]
new_list




my_list = [ 14, 13, "io"]
my_list
[14, 13, 'io']
type(my_list)
<class 'list'>
new_list = [3.4, 6, "no", my_list]
new_list
[3.4, 6, 'no', [14, 13, 'io']]
new_list [3]
[14, 13, 'io']
new_list[1]
6
my_list [-1]
'io'
my_list [-3]
14
my_list [-4]


lista_numeri = [1, 2, 3, 4, 7, 11, 12, 13, 14]
lista_numeri [4:6]
lista_primi = lista_numeri [4:6]
lista_primi


lista_numeri [4:]


nome = "Mario"
anni = 12
print(f"Ciao {nome}, tu hai {anni} anni")
f"Il quadrato di {anni} e' {anni * anni}"


messaggio = "Fate il vostro gioco"
messaggio.isalpha()
messaggio.isalnum()
messaggio.isdecimal()

asd = "Fateilvostrogioco"
asd.isalpha()
numeggs = "10"
numeggs.isalpha()
numeggs.isdecimal()
numeggs.isalnum()


to_do = ["Mangiare", "Bere", "Giocare"]
"   ".join(to_do)
da_fare = "   ".join(to_do)
da_fare

citazione = "Nel mezzo del cammin di nostra vita..."
citazione.split(" ")
citazione = citazione.split(" ")
citazione
len(citazione)
" ".join(citazione)
citazione = " ".join(citazione)
len(citazione)

"Nel" in citazione
"e" in citazione
"f" in citazione
"Nel" not in citazione
"e" not in citazione

alpha = "abddfgehiurhnik..."
dots = alpha[-3:]
dots
alpha = alpha[0 : -3]
alpha

alpha = "abddfgehiurhnik"
match = "d"
counter = 0

for char in alpha:
    if char == match:
        counter += 1

output = f"Ho trovato {counter} caratteri {match}!"
print(output)


my_tuple = (4, 5, 6, 7)
my_tuple
type(my_tuple)

tuple_2 = (4, 6, "io", 5)
type(tuple_2)

my_set = {3, 5, 6, 7, "bad"}
type(my_set)
my_set.add("io", 90) # non posso aggiungere due elementi insieme
my_set.add(90)



#lez16

my_dict = {"chiave1": "prova", "chiave2": "successo", "chiave3": 3, 14: "numero serie" }
my_dict
my_dict["chiave1"]
my_dict.items()
my_dict.keys()
my_dict.values()

items = my_dict.items()
items
list(items)
lista_chiavi = list(my_dict.keys())
lista_chiavi

for chiave in my_dict:
    print(chiave)

for keys in my_dict:
    print(keys)


my_dict2 = {"chiave1": "prova", "chiave2": "successo", "chiave3": 3, 14: "numero serie" }
my_dict2.keys()

if "birra" in my_dict2.keys():
    print("La chiave e' presente nell'elenco")
else:
    print ("La chiave non e' presente") #stampa "la chiave non e' presente


if "chiave1" in my_dict2.keys():
    print(my_dict2["chiave1"]) #la chiave e' presente quindi stampa il valore corrispondente alla chiave
else:
    print ("La chiave non e' presente")


if "chiave1" in my_dict2.keys():
    print(my_dict2[14])
else:
    print ("La chiave non e' presente")

my_dict2.get("chiave1", "chiave non trovata")

my_dict2.setdefault("birra", "nuova chiave") # aggiunge coppia chiave + valore

my_dict2.setdefault("birra", "Prova su birra")


class Studente:
	def __init__ (self, nome, cognome, corso_di_studi):
		self.nome = nome
		self.cognome = cognome
		self.corso_di_studi = corso_di_studi

studente_uno = Studente ("Valeria", "Corsetti", "Biologia")

studente_due = Studente ("Marco", "Del Re", "Biologia")

print(studente_uno)

class Studente:
	def __init__ (self, nome, cognome, corso_di_studi):
		self.nome = nome
		self.cognome = cognome
		self.corso_di_studi = corso_di_studi

studente_uno = Studente ("Valeria", "Corsetti", "Biologia")

studente_due = Studente ("Marco", "Del Re", "Biologia")







class Studente:
    def __init__ (self, nome, cognome, corso_di_studi):
		self.nome = nome
		self.cognome = cognome
		self.corso_di_studi = corso_di_studi
          
    def scheda_personale (self):
        return f” Scheda studente: Nome: {self.nome} cognome: {self.cognome}, Corso di studi {self.corso_di_studi}"

studente_uno = Studente ("Valeria", "Corsetti", "Biologia")

studente_due = Studente ("Marco", "Del Re", "Biologia")

print(studente_uno.scheda_personale())



class Studente:
    def __init__ (self, nome, cognome, corso):
        self.nome = nome
        self.cognome = cognome
        self.corso = corso

    def scheda_personale (self):
        return f"Scheda personale: Nome {self.nome}, Cognome {self.cognome}, Corso {self.corso}"
     
studente_tre = Studente("Io", "Tu", "Ok")

print(studente_tre.scheda_personale())




def moltiplicatore():
    try: 
        a = int(input('Inserisci il valore di a: '))
        b = int(input('Inserisci il valore di b: '))
        risultato = a * b
        print(risultato)
    except ValueError as e:
        print(f"C'e' stato un errore: {e}")
        print("Ehi tu! Solo caratteri numerici")
    finally:
        print("Sto chiudendo l'applicazione!")

moltiplicatore()



def toLowerCase(self, s: str) -> str: #Codice preso da Leetcode
        return s.lower()

parola_minuscola = toLowerCase (s: "CIAONE") #non funziona



class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    s = "CIAONE"
    print(s.lower())

c = "BUUUUU"
print(c.lower())


class Solution:
    def toLowerCase(self, s: str) -> str:

        return s.lower()
    messaggio = "CIAONE"
    print(toLowerCase(messaggio, s))



lettera = input("Scrivi una lettera \n").lower()
vocali = "aeiou"

if lettera in vocali:
    print("La lettera e' una vocale")
else:
    print("La lettera e' una consonante")



class Studente:
    def __init__ (self, nome, cognome, corso):
        self.nome = nome
        self.cognome = cognome
        self.corso = corso

    def scheda_personale (self):
        return f"Scheda personale: Nome {self.nome}, Cognome {self.cognome}, Corso {self.corso}"
     
studente_tre = Studente("Io", "Tu", "Ok")

print(studente_tre.scheda_personale())


#Lezioni di Edoardo Midali
class Persona:
     nome = "Luca"
     cognome = "Rossi"

persona1 = Persona()
persona2 = Persona()
print(persona1.cognome)



class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
         print("Ciao sono " + self.nome)


persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Marco", "Verdi")

persona2.saluta()




class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
         print("Ciao sono " + self.nome)

        
class Insegnante(Persona):
     pass #serve se non voglio ad ora inserire nulla nella classe

persona1 = Persona("Maria", "Del Re")
insegnate1 = Persona("Lorenza", "Fontana")

persona1.nome
insegnate1.cognome

insegnate1.saluta()


