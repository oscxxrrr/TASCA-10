# Define una función para filtrar palabras de una lista según su longitud
def filtrar_palabras(l, t):
    for e in l:
        if len(e) > t:  # Comprueba si la longitud de la palabra actual es mayor que 't'
            print(e)  # Imprime la palabra si su longitud es mayor que 't'

# Define una función para leer una lista de palabras desde la entrada del usuario
def leer_lista():
    a = '1'
    l = []  # Inicializa una lista vacía
    while a != 'a':
        a = input("Introduze un numero diferente a 'a': ")  # Solicita al usuario ingresar una palabra
        if a != 'a':  # Si la entrada no es 'a'
            l.append(a)  # Agrega la palabra a la lista 'l'
        else:
            return l  # Si se ingresa 'a', devuelve la lista 'l' y termina la función

# Programa principal
l = leer_lista()  # Llama a la función 'leer_lista' para obtener una lista de palabras del usuario
n = int(input("Introduce el tamaño para filtrar: "))  # Solicita al usuario ingresar un tamaño para filtrar
filtrar_palabras(l, n)  # Llama a la función 'filtrar_palabras' para imprimir las palabras de 'l' con longitud mayor que 'n'
