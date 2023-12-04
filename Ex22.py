def crear_punts(llista):
    for num in llista:
        print("." * num)

llista = input("Introduce una lista separados por espacios: ")
numeros = []

for valor in llista.split():
    numeros.append(int(valor))

crear_punts(numeros)