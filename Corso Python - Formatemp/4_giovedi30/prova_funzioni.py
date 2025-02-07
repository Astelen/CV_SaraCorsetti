def saluta(nome):
    print("Ciao,", nome)
    
saluta("Sara")

def somma (a, b):
    risultato = a + b
    print("Il risultato della somma e' ", risultato)
    
somma(5, 6)

def moltiplica (a, b=2):
    return a * b

moltx = moltiplica(2,3)
print(moltx)

risultato2 = moltiplica(moltiplica(3))
print("Il risultato e' ", risultato2)



def quadrato_iterno(n):
    risultato = n*n
    print(risultato)


def quadrato(n):
    return n*n
x = quadrato(5)

print(x)

x = quadrato(quadrato(3))

