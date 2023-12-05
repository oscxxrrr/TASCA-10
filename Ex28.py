def bin_to_dec(binari_num):
    decimal_num = int(binari_num, 2)
    return decimal_num

# Programa Principal
b = input("Ingrese el número binario: ")
decimal = bin_to_dec(b)
print("El número en binario {} en decimal es {}".format(b, decimal))
