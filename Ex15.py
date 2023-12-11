def longitud(a):
    long = 0
    for i in a:
        long += 1
    return long

# Uso de la función
x = "Cal Dimoni"
print("La longitud de la cadena dada es:", longitud(x))

y = [3, 4, 5, "a", "hola"]
print("La longitud de la lista dada es:", longitud(y))

z = (3, 5, 7, 9, 10)
print("La longitud de la tupla dada es:", longitud(z))

w = {3, 5, 7, 9, 10} 
print("La longitud del conjunto dado es:", longitud(w))