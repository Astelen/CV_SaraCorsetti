
#esercizio Teatro slide 165, simulazione TEATRO

## Classe Base: Posto
# Attributi privati:
# _numero (intero): il numero del posto.
# _fila (stringa): la fila in cui si trova il posto.
# _occupato (booleano): stato del posto, se è occupato (True) o libero (False).

class Posto:
    def __init__(self, numero_posto, fila_posto, occupato_bool = False): #costruttore con parametri
        self.__numero_posto = numero_posto
        self.__fila_posto = fila_posto
        self.occupato_bool = occupato_bool
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato.")
        else:
            print("Posto gia' occupato, scegline un altro.")
            
    def libera_posto(self): #Disdetta prenotazione che imposta booleano su False
        if self.occupato_bool == True:
            self.occupato_bool = False
            print("Prenotazione disdetta. Il posto ora e' di nuovo libero.")
        else:
            print("Il posto e' gia' libero.")
            
    def get_attributi(self): #recupero attributi dell'ogggetto
        return f"Numero posto: {self.__numero_posto}, fila: {self.__fila_posto}, stato: {self.occupato_bool}."
    
    def get_numero_posto(self):
        return self.numero_posto
    
    def get_numero_posto(self):
        return self.numero_posto
            
posto_mario = Posto(10, "G", True)    
print(posto_mario.get_attributi())   
posto_mario.libera_posto()
            
class PostoVIP(Posto):
    def __init__(self, numero_posto, fila_posto, occupato_bool, servizi_extra): #costruttore con parametri
        super().__init__(numero_posto, fila_posto, occupato_bool)
        self.__servizi_extra = servizi_extra
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato. Ora puoi scegliere i tuoi servizi extra. Abbiamo disponibile: accesso alla lounge, aperitivo vip.")
            num_scelta_vip = int(input("Quanti servizi vuoi prenotare? Digita 1 o 2: "))
            if num_scelta_vip == 1:
                tipo_scelta_vip = int(input("Digta 1 per l'accesso alla lounge, 2 per l'aperitivo Vip: "))
                if tipo_scelta_vip == 1:
                    print("Hai selezionato l'accesso alla lounge.")
                elif tipo_scelta_vip == 2:
                    print("Hai selezionato l'aperitivo VIP.")
                else:
                    print("Scelta non valida.")
            elif num_scelta_vip == 2:
                print("Ottima scelta!")
            else:
                print("Scelta non valida.")
        else:
            print("Posto gia' occupato, scegline un altro.")

    def get_attributi_vip(self): #recupero attributi dell'ogggetto. 
        #Se riscrivo la get come nel padre mi dice che non abbiamo attributo PostoVIP_numero_posto
        # quindi ho pensato a questa soluzione, chiedere a Mirko se e' giusta
        print(self.get_attributi(), "Servizi aggiuntivi: ", self.__servizi_extra)

posto_mario = PostoVIP(10, "G", True, "accesso lounge")    
posto_mario.get_attributi_vip()
posto_mario.libera_posto()

class PostoStandard(Posto):
    def __init__(self, numero_posto, fila_posto, occupato_bool, costo = 20): #costruttore con parametri
        super().__init__(numero_posto, fila_posto, occupato_bool)
        self.costo = costo
        
    def prenota_posto(self): #Prenotazione del posto che imposta booleano su True
        if self.occupato_bool == False:
            self.occupato_bool = True
            print("Posto prenotato. Il costo e' di ", self.costo, " euro.")
            scelta_acquisto = input("Per continuare con l'acquisto, digirare si: ")
            if scelta_acquisto.lower() == "si":
                print("Ti stiamo indirizzando al sito del pagamento.")
            elif scelta_acquisto.lower() == "no":
                print("Torna alla scelta dei posti")
            else:
                print("Scelta non valida.")

    def get_attributi_standard(self):
        print(self.get_attributi(), "Costo: ", self.costo)


posto_mario = PostoStandard(10, "G", True)    
posto_mario.get_attributi_standard()
posto_mario.libera_posto()


class Teatro: #2 liste, posti occupati e non occupati. 
    def __init__(self, nome_teatro, numero_posti): #costruttore con parametri
        self.nome_teatro = nome_teatro
        self.numero_posti = numero_posti #posti = Lista
    #aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
        
    lista_posti_tot = []
    lista_posti_prenotati = []
    def prenota_posto_teatro(self, numero_posto, fila_posto): #cerca nella lista il posto corrispondente al numero e
        #alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
        #Devo fare 2For.
        for x in self.lista_posti_tot:
            #print(x)
            if numero_posto == x.get.numero() and fila_posto == x.get.fila():
                for self.numero_posto in self.lista_posti_prenotati:
                    if self.numero_posto in self.lista_posti_tot:
                        for self.fila_posto in self.lista_posti_tot:
                            if self.fila_posto in self.lista_posti_tot:
                                print("Posto gia' occupato")
                            else:
                                print("Posto prenotabile.")
                                scelta_pren = input("Posto standard o vip? 1/2: ")
                                if scelta_pren == 1:
                                    PostoStandard.prenota_posto(numero_posto, fila_posto)
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 1A")
                                elif scelta_pren == 2:
                                    PostoVIP.prenota_posto(numero_posto, fila_posto)
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 2A")
                                else:
                                    print("Scelta non valida")
                    else:
                        print("Il posto e' libero!")
                        scelta_pren = int(input("Posto standard o vip? 1/2: "))
                        if scelta_pren == 1:
                            PostoStandard.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 1")
                        elif scelta_pren == 2:
                            PostoVIP.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 2")
                        else:
                            print("Scelta non valida")
            else:
                print("Scelta non valida.")
                
    def prenota_posto_teatro2(self, numero_posto, fila_posto): ##Prova n. 2
        for self.numero_posto in self.lista_posti_prenotati:
                    if self.numero_posto in self.lista_posti_tot:
                        for self.fila_posto in self.lista_posti_tot:
                            if self.fila_posto in self.lista_posti_tot:
                                print("Posto gia' occupato")
                            else:
                                print("Posto prenotabile.")
                                scelta_pren = input("Posto standard o vip? 1/2: ")
                                if scelta_pren == 1:
                                    PostoStandard.prenota_posto(numero_posto, fila_posto)
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 1A")
                                elif scelta_pren == 2:
                                    PostoVIP.prenota_posto(numero_posto, fila_posto)
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 2A")
                                else:
                                    print("Scelta non valida")
                    else:
                        print("Il posto e' libero!")
                        scelta_pren = input("Posto standard o vip? 1/2: ")
                        if scelta_pren == 1:
                            PostoStandard.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 1")
                        elif scelta_pren == 2:
                            PostoVIP.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 2")
                        else:
                            print("Scelta non valida")
                
    def prenota_posto_teatro3(self, numero_posto, fila_posto): #cerca nella lista il posto corrispondente al numero e
        #alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
        #Devo fare 2For.
        for x in self.lista_posti_tot:
            if get.numero_posto() == numero_posto and fila_posto == x.get.fila():
                for self.numero_posto in self.lista_posti_prenotati:
                    if self.numero_posto in self.lista_posti_tot:
                        for self.fila_posto in self.lista_posti_tot:
                            if self.fila_posto in self.lista_posti_tot:
                                print("Posto gia' occupato")
                            else:
                                print("Posto prenotabile.")
                                scelta_pren = input("Posto standard o vip? 1/2: ")
                                if scelta_pren == 1:
                                    x.prenota_posto()
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 1A")
                                elif scelta_pren == 2:
                                    x.prenota_posto()
                                    self.aggiunta_posto()
                                    print("Sei arrivo qui 2A")
                                else:
                                    print("Scelta non valida")
                    else:
                        print("Il posto e' libero!")
                        scelta_pren = int(input("Posto standard o vip? 1/2: "))
                        if scelta_pren == 1:
                            PostoStandard.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 1")
                        elif scelta_pren == 2:
                            PostoVIP.prenota_posto()
                            self.aggiunta_posto()
                            print("Sei arrivo qui 2")
                        else:
                            print("Scelta non valida")
            else:
                print("Scelta non valida.")
        
    def prenota_posto_teatro4(self, numero_posto, fila_posto): #prova metodo Costanza
        self.numero_posto = numero_posto
        self.fila_posto = fila_posto
        #numero_posto = int(input("Inserisci il numero del posto: "))
        #fila_posto = input("Inserisci la fila del posto")
        if numero_posto in self.posti and fila_posto in self.posti:
            if numero_posto in self.posti_occupati and fila_posto in self.posti_occupati:
                print("Posto gia' occupato.")
            else:
                posto_prenotato = PostoVIP(numero_posto, fila_posto, True)
                self.posti_occupati.append(posto_prenotato) 
        else:
            print("Posto non presente")
        
    def stampa_posti_occupati(self):
        for x in self.posti:
            return x
    
    # def aggiunta_posto(self, posto):
    # self.lista_posti_prenotati.append(posto) #ogni posto e' num+lettera
    def aggiunta_posto(self, numero_posto, fila_posto):
        posto_da_aggiungere = "".join([str(numero_posto), fila_posto])
        self.lista_posti_prenotati.append(posto_da_aggiungere) #ogni posto e' num+lettera  
        ##Possibilita' aggiungere posto VIP o st  
        
    def stampa_posti_occupati(self):
        for x in self.lista_posti_prenotati:
            return x
        
    @classmethod
    def stampa_posti_occupati2(cls): ##
        #print(f"I posti occupati sono {cls.lista_posti_prenotati}")
        for x in cls.lista_posti_prenotati:
            return x
    
teatro1 = Teatro("Brancaccio", ["1a", "1B", "1C"])
print(teatro1.numero_posti)

print(teatro1.lista_posti_prenotati)

teatro1.prenota_posto_teatro(1, "D")
teatro1.prenota_posto_teatro2(1, "D")
teatro1.prenota_posto_teatro3(1, "D")

teatro1.aggiunta_posto(1, "D")
print(teatro1.stampa_posti_occupati()) #mi funzionano entrambe
print(teatro1.stampa_posti_occupati2())