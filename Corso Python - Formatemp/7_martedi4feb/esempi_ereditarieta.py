
#classe padre
class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        print(self.nome, " fa suono generico")
        
#classe figlio
class Cane(Animale):
    
    def parla(self):
        print(self.nome, " abbaia!")
        
animale_generico = Animale("Animale generico")
cane = Cane("Fido")

animale_generico.parla()
cane.parla()



class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def mostra_informationi(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) #richiama questi parametri dalla classe padre Veicolo
        DotazioniSpeciali.__init__(self, dotazioni) #richiama questi parametri dalla classe padre DotazioniSpeciali
        self.cavalli = cavalli #aggiunge questo parametro
    
    def mostra_informazioni(self):
        super().mostra_informazioni()  ##prende da prima classe padre ovvero Veicolo
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        
autosportiva1 = AutomobileSportiva("BMW", "5", "Cruise control", "1500")
autosportiva1.mostra_informazioni()



##esercizio Animali
#classe padre Animale
class Animali:
    def __init__(self, nome_animale, eta):
        self.nome_animale = nome_animale
        self.eta = eta
    def verso_animale(self):
        print(self.nome_animale, " ha un verso generico")
#classe figlio gibbone
class Gibbone(Animale):
    def __init__(self, nome_animale, eta, fidanzato):
        Animale.__init__(self, nome_animale, eta)
        self.fidanzato = fidanzato
    def verso_animale(self):
        print(self.nome_animale, " fa U-U-U-U-AHHHH!")
    def grooming(self):
        if self.fidanzato == "si":
            print("Il compagno di grooming preferito e' il partner.")
        else:
            print("Il compagno preferito di grooming puo' essere chiunque.")
class Suricato(Animale):
    def __init__(self, nome_animale, eta, numero_fratelli):
        Animale.__init__(self, nome_animale, eta)
        self.numero_fratelli = numero_fratelli
    def verso_animale(self):
        print(self.nome_animale, " come fa?? Boh! Ma quello non era il coccodrillo?")
    def allarme(self):
        if self.allarme == "si":
            print("Il suricato mette in allarme tutto il gruppo.")
        else:
            print("Il suricato sta tranquillo a prendere il sole!")

class Struzzo(Animale):
    def __init__(self, nome_animale, eta, buchi_testa):
        Animale.__init__(self, nome_animale, eta)
        self.buchi_testa = buchi_testa
    def verso_animale(self):
        print(self.nome_animale, " fa AHHHHHH AHHHHH!")
    def buchi_testa(self):
        if self.buchi_testa > "0":
            print("Lo struzzo ha dei buchi dove nascondere la testa!")
        else:
            print("Che struzzo coraggioso, non si nasconde mai.")


#classe computer che ha come padre processore (velocita') e RAM (memoria)
class Processore:
    def __init__(self, tipo_processore, velocita):
        self.tipo_processore = tipo_processore
        self.velocita = velocita
    
    def sistema_supportato():
        print("I nuovi processori supportano solo sistemi operativi rilasciati dal 2020 in poi.")
        
    def stampa_info_processore(self):
        print("Le informazioni del processore sono: ", self.tipo_processore, self.velocita)
    
class Ram:
    def __init__(self, memoria):
        self.memoria = int(memoria)
    
    def aumento_ram(self):
        if self.memoria < 100:
            print("Questa RAM puo' essere estesa, devi acquistare un'estensione!")
            
    def stampa_info_ram(self):
        print("Le informazioni della ram sono: ", self.memoria)
    
class Computer(Processore, Ram):
    def __init__(self, tipo_processore, velocita, memoria, linguaggio_computer):
        Processore.__init__(self, tipo_processore, velocita)
        Ram.__init__(self, memoria)
        self.linguaggio_computer = linguaggio_computer
       
    def tipo_tastiera(self):
        if self.linguaggio_computer == "eng":
            print("La tastiera ha la formattazione inglese")
        elif self.linguaggio_computer == "it":
            print("La tastiera ha la formattazione italiana")
        else:
            print("Formattazione non riconosciuta o inserimento non valido.")
            
    def stampa_informazioni(self):
        Processore.stampa_info_processore(self)
        Ram.stampa_info_ram(self)
        
    def __str__(self): ##Questo metodo va solo con f
        return f"Caratteristiche: {self.velocita}, {self.tipo_processore}, {self.linguaggio_computer}" 
        
            
computer1 = Computer("Intel", "Super", "100", "eng")
computer1.stampa_informazioni()
computer1.tipo_tastiera()
print(computer1)
