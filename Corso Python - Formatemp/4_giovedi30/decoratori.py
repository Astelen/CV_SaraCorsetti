
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della f")
        funzione()
        print("Dopo l'esecuzione della f")
    return wrapper
@decoratore
def saluta():
    print("Ciao")
    
saluta()

@decoratore
def pippo():
    print(21)
    
pippo()



#nuova prova decoratore
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma (a, b):
    return a + b

x = somma(3,4)

print(x)

print(somma(3,4))




#decoratore per modificare la funzione moltiplica
def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b
# Chiamata alla funzione decorata
moltiplica(3, 4)




##Decoratore che calcola il tempo di esecuzione della funzione
import time

def calcola_tempo(funzione):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2) #questo aggiunge 2 secondo, ho una partenza in differita di due secondi
    print("Calcolo completato")

# Chiamata alla funzione decorata
calcolo_lento()


