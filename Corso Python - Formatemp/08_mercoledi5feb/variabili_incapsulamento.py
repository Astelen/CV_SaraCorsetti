# var globale
numero = 10

def funzione_esterna():
    #var locale nella funzione
    numero = 5
    print("Numero dentro funzione_esterna (locale): ", numero) #in questo caso stampa con numero = 5
    
    def funzione_interna():
        #utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal): ", numero) #qui stampa con numero = 3 e cambia anche il futuro!
    
    funzione_interna() #stampa con numero = 3 dopo che e' stato modificato dal nonlocal
    print("Numero dentro funzione_esterna (locale): ", numero)

print("Numero nel main (globale): ", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato): ", numero)