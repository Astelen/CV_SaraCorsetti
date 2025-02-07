

class Automobile:                         # dichiaro la classe
    numero_di_ruote = 4                    # attributo di classe
    def __init__(self, marca, modello):   # metodo costruttore
        self.marca = marca                  # attributo di istanza
        self.modello = modello              # attributo di istanza
    def stampa_info(self):               # metodo di istanza
        print("L'automobile è una", self.marca, self.modello)
        
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")
auto3 = Automobile("500")
auto1.numero_di_ruote = 6 #posso modificare il numero di ruote! 
print(auto1.numero_di_ruote)

auto1.stampa_info()
auto2.stampa_info()
auto3.stampa_info()




class Automobile:                         # dichiaro la classe
    numero_di_ruote = 4                    # attributo di classe
    def __init__(pippo, marca, modello):   # metodo costruttore
        pippo.marca = marca                  # attributo di istanza
        pippo.modello = modello              # attributo di istanza
    def stampa_info(self):               # metodo di istanza
        print("L'automobile è una", self.marca, self.modello)
        
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()