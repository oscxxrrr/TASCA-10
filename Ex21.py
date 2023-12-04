def crear_repetidos():
    return caracter * numero

numero = int(input("Introduce un numero: "))
caracter = input("Introduce una letra: ")

resultado = crear_repetidos()
print("El resultado és {}".format(resultado))