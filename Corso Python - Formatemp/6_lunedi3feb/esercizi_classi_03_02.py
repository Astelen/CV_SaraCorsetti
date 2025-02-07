class Contatore:
    numero_istanze = 0  # Attributo di classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
        
# Creazione di alcune istanze

c1 = Contatore()
c2 = Contatore()



##prova classe con vari metodi
class Pippo:
    aumento = 0
    
    #metodo di istanza. Il piu' facile
    def saluta():
        print("ciao Mirko")
       
    #metodo di classe. Operano sulla classe e non su un'istanza specifica. Se cambio qualcosa con questo metodo, lo cambio per le istanze create da ora in poi. 
    @classmethod
    def aumenta():
        Pippo.aumento += 1
        print(Pippo.aumento)
    
    #metodo statico. Non serve un oggetto!
    @staticmethod
    def somma(a,b):
        return a + b
    
p = Pippo()

p.saluta()

p.aumenta()
Pippo.aumenta()

x = Pippo.somma(2,4)



###esercizio 1 slide 119

class Punto:
    x = 0
    y = 0
    def muovi_punto(self, nuovo_x, nuovo_y):
        self.x = nuovo_x
        self.y = nuovo_y
        print("Il nuovo x e' ", nuovo_x, " ed il nuovo y e' ", nuovo_y)
    
    def distanza_da_orgiine(self):
        if self.x != 0 and self.y != 0:
            print("La distanza di X e Y da 0 e' ", self.x, ", ", self.y)
            

roma = Punto() ##NB devi sempre creare un'istanza!
roma.muovi_punto(5, 6)
roma.distanza_da_orgiine()



###Crea una classe chiamata Libro.
# Questa classe dovrebbe avere: Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
        
class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print("Il libro ", self.titolo, " e' stato scritto da ", self.autore, " ed ha ", self.pagine, " pagine.")
        
stargirl = Libro("Stargirl", "Jerry Spinelli", 230)
stargirl.descrizione()

##esercizio slide 120, Libro

class Libro:
    autore = ""
    numero_pag = 0
    titolo = ""
    
    def __init__(self, autore, numero_pag, titolo):
        self.autore = autore
        self.numero_pag = numero_pag
        self.titolo = titolo
        
    def stampa_dati(self):
        print(self.autore, self.numero_pag, self.titolo)

class Biblioteca:
    lista_libri = []
    
    def crea_libro(self):
        autore = input()
        numero_pag = input()
        titolo = input()
        aggiunta = Libro() ##prendo dalla classe di sopra, devo inserire gli argomenti!
        self.lista_libri.append(aggiunta)
        
    def stampa_libro(self):
        # print(self.lista_libri[0].autore, self.lista_libri[0].numero_pag, self.lista_libri[0].titolo)  ##Questo stampa sempre il primo!
        for x in self.lista_libri:  #per stampare ogni libro
            print(x.stampa_dati())
        
biblio = Biblioteca()
    
while True:
    biblio.crea_libro()
    biblio.stampa_libro()
    
    scelta = input("Vuoi continuare? S/N")
    if scelta == "n":
        break
    





##esercizio slide 121, Ristorante

class Ristorante:
    apertura = False
    menu = {}
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def descrivi_ristorante(self):
        print("Il ristorante si chiama ", self.nome, " e la cucina e' ", self.tipo_cucina)
    def stato_apertura(self, apertura):
        self.apertura = apertura
        if apertura == False:
            print("Il ristorante e' chiuso")
        else:
            print("Il ristorante e' aperto")
    def apri_ristorante(self, apertura):
        self.apertura = True
    def chiudi_ristorante(self, apertura):
        self.apertura = False
        print("Il ristorante e' chiuso!")
    #def aggiungi_menu(self, nuova_chiave, nuovo_valore):
    #    self.menu = self.menu{[nuova_chiave], nuovo_valore}
    def rimuovi_menu(self, chiave_rimuovi):
        del self.menu[chiave_rimuovi]
    def stampa_menu(self):
        print("Il menu' e' ", self.menu)
        
diavolo = Ristorante("Il diavolo", "romana")
diavolo.descrivi_ristorante()


##esercizio slide 121, Ristorante CON LISTE

class Ristorante:
    apertura = False #In generale meglio mettere queste categorie nell'Init in modo da essere sicuri che vengano creati gli oggetti con le caratteristiche come le scelgo io
    lista_piatti = []
    lista_prezzi = []
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def descrivi_ristorante(self):
        print("Il ristorante si chiama ", self.nome, " e la cucina e' ", self.tipo_cucina)
    def stato_apertura(self, apertura):
        self.apertura = apertura
        if apertura == False:
            print("Il ristorante e' chiuso")
        else:
            print("Il ristorante e' aperto")
    def apri_ristorante(self, apertura):
        if self.apertura == True:
            print("Il ristorante e' gia' aperto!")
        else:
            self.apertura = True
            print("Il ristorante e' aperto!")
    def chiudi_ristorante(self, apertura):
        if self.apertura == False:
            print("Il ristorante e' gia' chiuso!")
        else:
            self.apertura = False
            print("Il ristorante e' chiuso!")
    #Fare lista prezzi e piatti
    def aggiungi_menu(self, nome_piatto, prezzo_piatto):
        self.nome_piatto = nome_piatto
        self.prezzo_piatto = prezzo_piatto
        self.lista_piatti.append(nome_piatto)
        self.lista_prezzi.append(prezzo_piatto)
    def rimuovi_menu(self, nome_piatto): #togliere tramite chiave ma metti che non si pou' togliere qualcosa al di sopra dell'elenco liste
        if self.nome_piatto in self.lista_piatti:
            indice = self.lista_piatti.index(nome_piatto)
            self.lista_piatti.pop(indice)
            self.lista_prezzi.pop(indice)
        else:
            print("Questo piatto non e' presente nella lista.")
        ##Col ciclo for?
        # for nome_piatto in self.lista_piatti:
        #     x = 0
        #     if self.sestesso.menupiatti # prendo l'indice
        #     ##quando trovi nome del piatto
        #     x += 1
        #     self.lista_piatti.remove([])
    def stampa_menu1(self): ## menu 1 con ciclo For unico, ma stampa i piatti tutti insieme ed i prezzi tutti insieme
        print("Il menu' e': ")
        for x, y in self.lista_piatti, self.lista_prezzi:
            print(x, y)
        #for x in self.lista_piatti:
            #print(self.lista_piatti, self.lista_prezzi)
    def stampa_menu2(self): ## menu 2 con due cicli For concatenati
        print("Il menu' e': ")
        for x in self.lista_piatti:
            print(x)
            for x in self.lista_prezzi:
                print(x)
                break
    def stampa_menu3(self): ##Menu' 3, l'unica possibilita' funzionante bene
        print("Il menu' e': ")
        for piatto, prezzo in zip(self.lista_piatti, self.lista_prezzi):
            print(piatto, prezzo)
    def stampa_menu4(self): ## Stampa tutti piatti e tutti prezzi insieme
        print("Il menu' e': ")
        for x, y in self.lista_piatti, self.lista_prezzi:
            print(x, y)
                
diavolo = Ristorante("Il diavolo", "romana")
diavolo.descrivi_ristorante()

diavolo.aggiungi_menu("Carbonara", 10)
diavolo.aggiungi_menu("Amatriciana", 9)
diavolo.aggiungi_menu("Gricia", 9)

print(diavolo.lista_piatti)
print(diavolo.lista_prezzi)

diavolo.rimuovi_menu("Gricia")
print(diavolo.lista_piatti)
print(diavolo.lista_prezzi)

diavolo.stampa_menu1()
diavolo.stampa_menu2()
diavolo.stampa_menu3()
diavolo.stampa_menu4()




##Dizionari
studente = {
    "nome": "Alice", 
    "eta": 20, 
    "sesso": "Femmina", 
    4: "Mario"}
print(studente)
print(studente["nome"])
print(studente[4])
studente["nome"] = "Carlo"
print(studente)


#esercizio dizionari
valore1 = int(input("Inserisci un numero"))
valore2 = bool(input("So la piu' simpatica Vero o Falso?"))
valore3 = input("Scrivi il tuo nome")
lista_provadict = []
lista_provadict.append(valore1) #oppure con un ciclo For
lista_provadict.append(valore2)
lista_provadict.append(valore3)

dizionario_prova = {"tipididato": lista_provadict}

print(dizionario_prova)



##Prova unione lista chiavi e lista valori
nuovo_diz = {}
lista_chiavi = ["io", "tu"]
lista_valori = [34, 67]
for x, y in lista_chiavi, lista_valori: ##Come fondere due liste come chiavi e valori
    nuovo_diz[x] = y
    
print(nuovo_diz)