def crear_repetits(a, b):
    # Multiplica 'b' por 'a' convertido a entero
    c = b * int(a)
    return c

def crear_punts(a):
    for e in a:
        # Para cada elemento en 'a', crea puntos repetidos según el valor del elemento
        c = crear_repetits(int(e), '.')
        print(c)

# Solicita al usuario ingresar una lista numérica de elementos
a = input("Escriu una llista numèrica d'elements: ")
crear_punts(a)  # Llama a la función 'crear_punts' con la lista ingresada