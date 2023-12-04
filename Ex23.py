def crear_punts(llista):
    for num in llista:
        print("." * num)

def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)

imatge_dibuixar = [
    [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
    
]
dibuixar_imatge(imatge_dibuixar)