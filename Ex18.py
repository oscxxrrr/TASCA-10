def invertir(cadena):
    cadena_invertida = ""
    for caracter in cadena: 
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida
cadena_principal = input("Introduce una cadena de caracteres: ")

cadena_invertida = invertir(cadena_principal)

print("La cadena invertida se ve asi: {}".format(cadena_invertida)) 