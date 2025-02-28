
#Classe Prodotto:
# Attributi: nome, costo_produzione, prezzo_vendita
# Metodi: calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.

class Prodotto:
    nome = ""
    costo_produzione = 0
    prezzo_vendita = 0
    def __init__(self, nome, costo_produzione, prezzo_vendita): #funzione creazione istanza
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def descrizione(self):
        print(self.nome, self.costo_produzione, self.prezzo_vendita)
            
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
        
# Classi parallele:
# Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
# Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.

class Elettronica:
    nome = ""
    costo_produzione = 0
    prezzo_vendita = 0
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia): #funzione creazione istanza
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
        
    def descrizione(self):
        print(self.nome, self.costo_produzione, self.prezzo_vendita)

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Abbigliamento:
    nome = ""
    costo_produzione = 0
    prezzo_vendita = 0
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale): #funzione creazione istanza
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def descrizione(self):
        print(self.nome, self.costo_produzione, self.prezzo_vendita)
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

# Classe Fabbrica:
# Attributi:
# inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
# Metodi:
# aggiungi_prodotto: aggiunge prodotti all'inventario.
# vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
# resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.

class Fabbrica:
    dict_inventario = {}
    lista_prodotto_generico = []
    def aggiungi_prodotto(self):
        nome = input("Inserisci il nome del prodotto: ")
        costo_produzione = int(input("Inserisci il costo di produzione del prodotto: "))
        costo_vendita = int(input("Inserisci il costo di vendita del prodotto: "))
        aggiunta = Prodotto(nome, costo_produzione, costo_vendita) #crea istanza di tipo Prodotto, a cui devo dare gli argomenti
        self.lista_prodotto_generico.append(aggiunta) #metto il self per dire che aggiungo l'istanza alla lista propria dell'oggetto di tipo Fabbrica
        self.dict_inventario["prodotto_generico"] = self.lista_prodotto_generico # Serve ad aggiungere alla fine del dizionario una coppia con chiave
        # "prodotto_generico_" e con valore loggetto (che ha compe argomenti Nome, costo prod e costo vend.)
        aggiunta.descrizione() # Serve a stampare l'aggiunta appena aggiunta
    
    def aggiungi_elettronica(self):
        nome = input("Inserisci il nome del prodotto: ")
        costo_produzione = int(input("Inserisci il costo di produzione del prodotto: "))
        costo_vendita = int(input("Inserisci il costo di vendita del prodotto: "))
        garanzia = input("Inserisci i giorni di garanzia: ")
        aggiunta = Prodotto(nome, costo_produzione, costo_vendita, garanzia)
        self.lista_prodotto_generico.append(aggiunta)
        self.dict_inventario["prodotto_elettronica"] = self.lista_prodotto_generico
        
    def aggiungi_abbigliamento(self):
        nome = input("Inserisci il nome del prodotto: ")
        costo_produzione = int(input("Inserisci il costo di produzione del prodotto: "))
        costo_vendita = int(input("Inserisci il costo di vendita del prodotto: "))
        materiale = input("Inserisci il materiale del prodotto: ")
        aggiunta = Prodotto(nome, costo_produzione, costo_vendita, materiale)
        self.lista_prodotto_generico.append(aggiunta)
        self.dict_inventario["prodotto_abbigliamento"] = self.lista_prodotto_generico
    
    #def vendi prodotto
    def vendita_prodotto(self):
        prodotto_da_vendere = input("Scrivi il prodotto da vendere: ")
        if prodotto_da_vendere in self.lista_prodotto_generico:
            self.lista_prodotto_generico.remove(prodotto_da_vendere)
            print("Il guadagno e' ", self.prezzo_vendita - self.costo_produzione).
        else:
            print("Il prodotto non e' nell'inventario.")
            
    # resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.     
    def reso_prodotto(self, nome):
        if self.nome in self.dict_inventario:
            print("Puoi rendere questo articolo.")
        else:
            print("L'articolo non e' presente e quindi il reso non e' permesso.")
       
    def stampa_inventario(self):
        for prodotto in self.lista_prodotto_generico:
            print(prodotto.descrizione()) #lo segna grigetto solo perche' potrebbero non esserci dei prodotti, e si sfascia

        
while True:
    scelta = int(input("Per inserire un prodotto generico, premi 1, per un prodotto di elettronica, premi 2, per un prodotto di abbigliamento, premi 3: "))
    if scelta == 1:
        oggetto1 = Fabbrica()
        oggetto1.aggiungi_prodotto()
    elif scelta ==2:
        oggetto1 = Fabbrica()
        oggetto1.aggiungi_elettronica()
    elif scelta ==2:
        oggetto1 = Fabbrica()
        oggetto1.aggiungi_abbigliamento()
    else:
        print("Scelta non valida.")
    continuare = input("Vuoi inserire un altro prodotto? Digita S o N: ")
    if continuare.lower == "n":
        stampa_inventario = input("Vuoi stampare la lista dei prodotti? Digita S o N: ")
        if stampa_inventario == "s":
            oggetto1.stampa_inventario() #Dovrei fare 3 scelte per capire quale inventario stampare
        elif stampa_inventario == "n":
            print("Ciao!")
        else:
            print("Scelta non valida.")
    elif continuare.lower() == "s":
        pass
    else:
        print("Scelta non valida.")

 

## Creazione libreria

class Libro:
    isbn = 0 #Isbn parte da 0
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn + 1 #assegno al primo libro isbn = 0 + 1
        isbn += 1 #aumento di 1 tutti gli Isbn cosi' vado avanti col contatore
    
    def descrizione(self): #funzione descrizione libro con tutti e 3 gli attributi
        print("Il titolo del libro e': ", self.titolo, ":, il suo autore e': ", self.autore, " ed il suo isbn e': ", self.isbn)
        
class Libreria:
    diz_libri = {} # attributo catalogo
    lista_libri = []
    # metodo aggiungi_libro
    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        aggiunta = Libro(titolo, autore)
        self.lista_libri.append(aggiunta)
        self.diz_libri[self.isbn] = self.lista_libri  ##In questo modo utilizzo il valore di Isbn come chiave, si puo' fare?
    # metodo rimuovi_libro
    # cerca per titolo
    # mostra_catalogo
    


