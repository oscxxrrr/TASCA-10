# Define una función para convertir un número binario a decimal
def bin_to_dec(binari_num):
    decimal_num = int(binari_num, 2)  # Convierte el número binario a decimal usando int() con base 2
    return decimal_num  # Devuelve el número decimal convertido desde binario

# Programa Principal
b = input("Ingrese el número binario: ")  # Solicita al usuario ingresar un número binario
decimal = bin_to_dec(b)  # Llama a la función para convertir el número binario a decimal
# Imprime el número binario original y su equivalente en decimal
print("El número en binario {} en decimal es {}".format(b, decimal))
