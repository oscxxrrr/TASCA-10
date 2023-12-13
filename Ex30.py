# Define una función para mostrar los números mayores que un valor de referencia en una tupla
def mostrar_majors_que(t, nreferencia):
    print("Tots els números majors de {} són: ".format(nreferencia))  # Imprime el mensaje con el número de referencia
    for e in t:  # Itera sobre cada elemento en la tupla 't'
        if e > nreferencia:  # Comprueba si el elemento es mayor que el valor de referencia
            print("{} ".format(e))  # Imprime el número si es mayor que la referencia

# Define una función para leer una tupla de números ingresados por el usuario
def llegir_tupla():
    a = []  # Inicializa una lista vacía
    i = 0
    print("Introdueixi tots els números que vulguis. Per aturar posi -1: ")  # Solicita números al usuario
    while i > -1:
        a.append(input("Introdueixi un número: "))  # Agrega números a la lista
        if a[i] == "-1":  # Verifica si se ha ingresado el número de parada "-1"
            a.remove("-1")  # Elimina el número de parada de la lista
            i = -2  # Establece el valor de 'i' para detener el bucle
        i += 1  # Incrementa 'i'
    return a  # Devuelve la lista de números como una tupla

# Programa principal
i = input("Introdueixi el número que voleu comparar: ")  # Solicita al usuario ingresar un número de referencia
x = llegir_tupla()  # Llama a la función 'llegir_tupla' para obtener una tupla de números
a = tuple(x)  # Convierte la lista de números en una tupla
mostrar_majors_que(a, i)  # Llama a la función 'mostrar_majors_que' para mostrar los números mayores que 'i' en la tupla 'a'
