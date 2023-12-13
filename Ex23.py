# Define crear_punts
def crear_punts(llista):
    for num in llista:
        print("." * num)  # Imprime una cadena de puntos (".") de longitud 'num'

# Define una función para dibujar una imagen utilizando la función 'crear_punts'
def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)  # Llama a la función 'crear_punts' para cada línea en la imagen

# Lista que contiene una única fila con una secuencia de valores de longitud de puntos
imatge_dibuixar = [
    [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
]

# Dibuja la imagen utilizando la función 'dibuixar_imatge'
dibuixar_imatge(imatge_dibuixar)
