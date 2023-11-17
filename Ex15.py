def contar_caracteres(elemento):
    return len(str(elemento))

a = input("Introduze una lista o una cadena de caracteres: ")
b = contar_caracteres(a)

print("La lista o cadena de caracteres {} tiene {} caracteres.".format(a,b))
