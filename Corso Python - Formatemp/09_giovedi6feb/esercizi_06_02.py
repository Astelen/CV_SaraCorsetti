
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
        
        def __metodo_privato(self):
            return "Questo e' un metodo privato"
        
        def __pippo_privato(self):
            print("Ciao")
            
        def __pippo_privato(self):
            print(__metodo_privato)
        
obj = MiaClasse()
# se stampo print(obj.__variabile_privata) ottengo un errore!! AttributeError
print(obj._MiaClasse__variabile_privata) # questo funziona MA NON SI FA.



#####

##esercizio scuola slide 154

class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta
    
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    def set_nome(self, nuovo_nome):
        if self.__nome != "":
            self.__nome = nuovo_nome
    
    def set_eta(self, nuova_eta):
        if self.__eta != 0:
            self.__eta = nuova_eta
    
    def presentazione(self):
        print("Il nome e': ", self.__nome, ", l'eta' e': ", self.__eta)

class Studente(Persona):     #NB con get posso evitare di fare l'init! Basta che faccio def get.nome e def get.eta INVECE del costruttore.
        #In questo caso devo mettere per forza il setter per modificarlo. In questo caso posso mettere privati
        # i dati anche nel padre
    __voti = []
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        if len(voti) != 0:
            self.__voti = voti #posso inserire un ciclo e mettere tipo quanti voti hai? poi li inserisco in una lista e lo passo come parametro. Da fare nel menu'
        else:
            self.__voti = []
        
    def calcola_media(self):
        somma = 0
        if len(self.__voti) > 0: #sto ciclo If non serve davvero
            for x in self.__voti:
                somma += x
            print(somma/len(self.__voti))
        else:
            return "La media e' 0"
        
    def get_voti(self):
        return self.__voti
     
    def presentazione(self):
        print("Il nome e': ", self.get_nome(), ", l'eta' e': ", self.get_eta(), ", i voti sono: ", self.get_voti())
        
        
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
        
    def presentazione(self):
        print("Il nome e': ", self.get_nome(), ", l'eta' e': ", self.get_eta(), ", la materia di ineagnamento e': ", self.get_materia())

while True: #creazione Menu' per inserimento persone
    scelta_aggiunta = input("Benvenuto nel database di studenti e insegnanti. Vuoi aggiungere un contatto? Digita S o N: ")
    if scelta_aggiunta.lower() == "s":
        pass
    elif scelta_aggiunta.lower() == "n":
        scelta_stampa = input("Vuoi stampare la lista di studenti e insegnanti? Scegli S o N: ")
        break
    else:
        print("Scelta non valida.")

    
     
persona1 = Persona("Marco", 34)
print(persona1.get_nome())
print(persona1.get_eta())
persona1.set_nome("Antonio")
persona1.set_eta(56)
print(persona1.get_nome())
print(persona1.get_eta())
persona1.presentazione()

studente1 = Studente("Sara", 37, [28, 30, 19])
studente2 = Studente("Luca", 28, [28, 30, 30])
print(studente1.get_nome())
print(studente1.get_eta())
print(studente2.get_nome())
print(studente2.get_eta())
studente2.calcola_media()




## esercizio 164 Metodi Pagamenti

class MetodoPagamento: #classe padre
    def __init__(self, importo):
        self.__importo = importo
    
    def effettua_pagamento(self, importo):
        return self.__importo

class CartaDiCredito(MetodoPagamento):
    def __init__(self, importo, numero_carta):
        super().__init__(importo)
        self.__numero_carta = numero_carta
    
    def effettua_pagamento(self, importo, numero_carta):
        return self.__importo, self.__numero_carta
    
class Paypal(MetodoPagamento):
    def effettua_pagamento(self, importo, conto_paypal):
        super().effettua_pagamento(importo)
        self.__conto_paypal = conto_paypal
        print("Hai effettuato un pagamento tramite il conto Paypal n. ", self.__conto_paypal)
        
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo, conto_bancario):
        super().effettua_pagamento(importo)
        self.__conto_bancario = conto_bancario
        print("Hai effettuato un pagamento tramite il conto bancario n. ", self.__conto_bancario)
              
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def effettua_pagamento_gen(self, pagamento):
        #input   # o If con Input o init nelle classi sovrastanti, oppure Init
        print(pagamento.effettua_pagamento())
        
pagamento1 = CartaDiCredito(200, 202020)
#pagamento2 = Paypal()
#pagamento3 = BonificoBancario()

gestore = GestorePagamenti()
gestore.effettua_pagamento_gen()





## esercizio 164 Metodi Pagamenti PROVA N. 2

class MetodoPagamento:
    def effettua_pagamento(self, importo):
        self.__importo = importo
    
class CartaDiCredito(MetodoPagamento):
    def __init__(self, importo):
        self.__importo = importo

    def effettua_pagamento(self, importo):
        print("Pagamento con carta di credito")
        
class GestionePagamento:
    def __init__(self, metodo_pagamento):
        self.__metodo_pagamento = metodo_pagamento
    
    def effettua_pagamento_gen(self, importo):
        self.__importo = importo
        return self.__importo, self.__metodo_pagamento

pagamento1 = CartaDiCredito(200)
gestore1 = GestionePagamento(CartaDiCredito)




## esercizio 164 Metodi Pagamenti PROVA N. 3

class CartaDiCredito:
    def effettua_pagamento(importo):
        print(importo, "pagato con carta di credito.")

class GestionePagamento:
    def __init__(self, metodo_di_pagamento):
        self.__metodo_di_pagamento = metodo_di_pagamento
    
    def esegui_pagamento(self, importo):
        self.__metodo_di_pagamento.effettua_pagamento(importo)
        
carta1 = CartaDiCredito()
gestione1 = GestionePagamento(carta1)  #creo istanza GestionePagamento chiamata gestione1, il parametro assegno carta1 oggetto di metodo_di_pagamento
gestione1.esegui_pagamento(200)



    
        