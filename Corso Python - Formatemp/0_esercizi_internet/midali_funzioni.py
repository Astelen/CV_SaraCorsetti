def sommare():
    somma = 0
    for x in somma:
        return x + x
    
    
def stampa_informazioni(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

stampa_informazioni(nome="Anna", eta=25, professione="Ingegnere")


def funzione1(funzione, a, b):
    return funzione(a, b)

def moltiplica(a, b):
    return a * b

f1 = funzione1(moltiplica(5, 6))

