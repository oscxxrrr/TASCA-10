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

# Define una función para encontrar la palabra más larga en una lista de palabras
def palabra_larga(x):
    max = x[0]  # Inicializa la variable 'max' con la primera palabra de la lista
    for e in x:  # Itera sobre cada palabra en la lista 'x'
        if len(e) > len(max):  # Comprueba si la longitud de la palabra actual es mayor que la longitud de 'max'
            max = e  # Actualiza 'max' con la palabra actual si es más larga
    return max  # Devuelve la palabra más larga encontrada en la lista

# Programa principal
llista_paraules = leer_lista()  # Llama a la función 'leer_lista' para obtener una lista de palabras del usuario
# Imprime la palabra más larga encontrada en la lista 'llista_paraules' utilizando la función 'palabra_larga'
print("La palabra mas grande de la lista {} és {}".format(llista_paraules, palabra_larga(llista_paraules)))
l = leer_lista()  # Vuelve a llamar a la función 'leer_lista' para obtener otra lista de palabras
