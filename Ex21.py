def crear_repetidos(): #Definim crear_repetidos
    return caracter * numero #Ens retornara el "caracter" multiplicat per "numero".

numero = int(input("Introduce un numero: ")) #Numero es introdueix un nombre.
caracter = input("Introduce una letra: ") #Caracter es introdueix una lletra.

resultado = crear_repetidos() #Resultado crida la funcio
print("El resultado és {}".format(resultado)) #Imprimeix el resultado és (el resultat de la multiplicació)