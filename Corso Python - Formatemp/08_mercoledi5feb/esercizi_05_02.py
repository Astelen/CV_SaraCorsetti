
# classe padre MembroSquadra
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def descrizione_membro(self):
        print("Il nome del membro e' :", self.nome,
              "l'eta' del membro e' :", self.eta)

# classe figlio Giocatore
class Giocatore(MembroSquadra):
    def __init__ (self, nome, eta, ruolo):
        MembroSquadra.__init__(self, nome, eta)
        self.ruolo = ruolo
        
    def __str__ (self):
        return f"Nome: {self.nome}, eta: {self.eta}, ruolo: {self.ruolo}."
    #descrizione_giocatore(self):
        # MembroSquadra.descrizione_membro(self)
        # print("Il ruolo del giocatore e' :", self.ruolo)
        
    def gioca_partita(self):
        print("Sta per entrare in campo!")

# classe figlio Allenatore
class Allenatore(MembroSquadra):
    def __init__ (self, nome, eta, anni_esperienza):
        MembroSquadra.__init__(self, nome, eta)
        self.anni_esperienza = anni_esperienza
        
    def __str__ (self):
        return f"Nome: {self.nome}, eta: {self.eta}, ruolo: {self.anni_esperienza}."
    
    # def descrizione_allenatore(self):
    #     MembroSquadra.descrizione_membro(self)
    #     print("Ha accumulato questi anni di esperienza come allenatore :", self.anni_esperienza)
        
    def dirige_allenamento(self):
        print("Allenamenti in corso, non disturbare.")
        
# classe figlio Assistente
class Assistente(MembroSquadra):
    def __init__ (self, nome, eta, specializzazione):
        MembroSquadra.__init__(self, nome, eta)
        self.specializzazione = specializzazione

    def __str__ (self):
        return f"Nome: {self.nome}, eta: {self.eta}, specializzazione: {self.specializzazione}."
        
    # def descrizione_assistente(self):
    #     MembroSquadra.descrizione_membro(self)
    #     print("E' specializzato come :", self.specializzazione)
        
    def supporto_allenamento(self):
        print("Supporta l'allenamento come ", self.specializzazione)
        
# classe Squadra, composto da MembroSquadra
class Squadra:
    lista_squadra = []
    lista_giocatori = []
    lista_allenatori = []
    lista_assistenti = []
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra

    def aggiungi_giocatore(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        ruolo = input("Digita il ruolo: ")
        aggiunta_giocatore = Giocatore(nome, eta, ruolo) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_giocatori.append(aggiunta_giocatore)
        
    def aggiungi_allenatore(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        anni_esperienza = input("Digita gli anni di esperienza: ")
        aggiunta_allenatore = Giocatore(nome, eta, anni_esperienza) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_allenatori.append(aggiunta_allenatore)
        
    def aggiungi_assistente(self):
        nome = input("Digita il nome: ")
        eta = int(input("Digita l'eta': "))
        specializzazione = input("Digita la specializzazione: ")
        aggiunta_assistente = Giocatore(nome, eta, specializzazione) #creo giocatore dentro il metodo prima di aggiungerlo alla lista
        self.lista_assistenti.append(aggiunta_assistente)
    
    def __str__(self): #stampa oggetto
        print("Squadra: ", self.nome_squadra)
        for x in self.lista_giocatori:
            print("Lista giocatori ", x)
        for y in self.lista_allenatori:
            print("Lista allenatori ", y)
        for z in self.lista_assistenti:
            print("Lista assistenti ", z)
        return ""
    
squadra1 = Squadra("Roma")

while True:
    scelta_inserimento = int(input("Scegli 1 per inserire un giocatore, 2 per un allenatore, 3 per un assistente, 4 per uscire."))
    if scelta_inserimento == 1:
        squadra1.aggiungi_giocatore()
    elif scelta_inserimento == 2:
        squadra1.aggiungi_allenatore()
    elif scelta_inserimento == 3:
        squadra1.aggiungi_assistente()
    elif scelta_inserimento == 4:
        scelta_stampa = input("Vuoi stampare la lista della squadra? Scegli S o N: ")
        if scelta_stampa.lower() == "s":
            print(squadra1)
        elif scelta_stampa.lower() == "n":
            print("Ok!")
            break
    else:
        print("Scelta non valida")

print(squadra1)



## Esercizio Personale cucina

class PersonaleCucina:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def lavora(self):
        print("Lavoro specifico")

class Chef(PersonaleCucina):
    def __init__(self, nome, eta, tipo_chef):
        super().__init__(self, nome, eta)
        self.tipo_chef = tipo_chef
    def lavora(self):
        print("Lavoro chef")

class SousChef(PersonaleCucina):
    def __init__(self, nome, eta, tipo_souschef):
        super().__init__(self, nome, eta)
        self.tipo_souschef = tipo_souschef
    def lavora(self):
        print("Lavoro linea")

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta, tipo_linea):
        super().__init__(self, nome, eta)
        self.tipo_linea = tipo_linea
    def lavora(self):
        print("Lavoro linea")

        
cuoco1 = CuocoLinea("Mario", 32, "xd")



# es. Conto Bancario slide 153
class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        
        if titolare != "":
            self.__titolare = titolare
        else:
            self.__titolare = "Sconosciuto"
        
        if saldo_iniziale > 0:
            self.__saldo = saldo_iniziale
        else:
            self.__saldo = 0
    
    #metodo per prelievi e depositi        
    def rinnovo_saldo(self, importo):
        nuovo_saldo = self.__saldo + importo
        if nuovo_saldo >=0:
            self.__saldo = nuovo_saldo
        else:
            print("Prelievo non disponibile")
    
    #stampa saldo
    # def get_saldo(self):
    #     return self.__saldo
    
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, nuovo_titolare):
        if nuovo_titolare != "":
            self.__titolare = nuovo_titolare
    
contobancario1 = ContoBancario("Antonio", 1000)  
contobancario1.visualizza_saldo()
contobancario1.rinnovo_saldo(2000)
print("Saldo dopo deposito: ", contobancario1.get_saldo())
print(contobancario1.get_titolare())
contobancario1.set_titolare("Valerio")
print(contobancario1.get_titolare())
            