
from abc import ABC, abstractmethod ##Obbligatorio, serve ad importare la funzione

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro)")

class Pesce(Animale):
    def muovi(self):
        print("Nuoto")




###Azienda per gestire gli impiegati

from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
        
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
#classe derivata ImpiegatoFisso
class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base
    
    def __str__(self):
        return f"Ecco i dati dell'impiegato: {self.nome}, {self.cognome}, {self.calcola_stipendio()}"

#classe derivata ImpiegatoProvvigione:
class ImpiegatoProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base + (self.stipendio_base*4)/100
    
    def __str__(self):
        return f"Ecco i dati dell'impiegato: {self.nome}, {self.cognome}, {self.calcola_stipendio()}"
    
    #Funzione suggerita da Mirko, non so perche'.
    #def paga_soldi(umano): #metto un parametro
    #    umano.calcola_stipendio() #devo riportare l'umano per far partire la funzione
    
imp1 = ImpiegatoFisso("Andrea", "De Santis", 100)
print(imp1.calcola_stipendio())
print(imp1.calcola_stipendio())

imp3 = ImpiegatoProvvigione("Valerio", "Leo", 200)
print(imp3.calcola_stipendio())

print(imp1)
print(imp3)
