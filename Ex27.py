# Define una función para contar letras mayúsculas en una cadena
def contar_mayusculas(s):
    num_maj = 0  # Inicializa el contador de letras mayúsculas
    num_men = 0  # Inicializa el contador de letras minúsculas
    for e in s:  # Itera sobre cada carácter en la cadena
        if e.isupper():  # Verifica si el carácter es mayúscula
            num_maj += 1  # Incrementa el contador de letras mayúsculas en uno
        elif e.islower():  # Verifica si el carácter es minúscula
            num_men += 1  # Incrementa el contador de letras minúsculas en uno
    return num_maj  # Devuelve el número total de letras mayúsculas encontradas

# Programa Principal
x = input("Introduce una cadena de caracteres: ")  # Solicita al usuario ingresar una cadena
resultado = contar_mayusculas(x)  # Llama a la función para contar las letras mayúsculas
print("El numero de letras mayusculas en la cadena es {}".format(resultado))  # Imprime el número de letras mayúsculas encontradas
