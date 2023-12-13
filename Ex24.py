# Define una función para leer una lista de números desde la entrada del usuario
def leer_lista():
    a = '1'
    l = []  # Inicializa una lista vacía
    while a != 'a':
        a = input("Introduze un numero diferente a 'a': ")  # Solicita al usuario ingresar un número
        if a != 'a':  # Si la entrada no es 'a'
            l.append(int(a))  # Convierte la entrada a entero y la agrega a la lista 'l'
        else:
            return l  # Si se ingresa 'a', devuelve la lista 'l' y termina la función

# Define una función para encontrar el número más grande en una lista
def gran_llista(l):
    max = l[0]  # Inicia la variable 'max' con el primer elemento de la lista
    for e in l:  # Recorre sobre cada elemento de la lista 'l'
        if e > max:  # Si el elemento actual es mayor que 'max'
            max = e  # Actualiza 'max' con el elemento actual
    # Imprime el número más grande encontrado en la lista
    print("El numero mas grande de la lista {} és {}".format(l, max)) 

# Programa principal
l = leer_lista()  # Llama a la función 'leer_lista' para obtener una lista del usuario
gran_llista(l)  # Llama a la función 'gran_llista' para encontrar el número más grande en la lista 'l'
