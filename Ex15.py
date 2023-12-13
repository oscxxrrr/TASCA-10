def longitud(a):
    long = 0 #Indica la variable 0 para almacenar la longitud
    for i in a: #Recorre todos los elementos de "i" en "a".
        long += 1 #Es long = long + 1
    return long #Ens retorna "long"

# Uso de la función
x = "Cal Dimoni" #Llista
print("La longitud de la cadena dada es:", longitud(x)) #Fa un print de la cadena y crida a la funcio longitud per a medirla.

y = [3, 4, 5, "a", "hola"] #Llista
print("La longitud de la lista dada es:", longitud(y)) #Fa un print de la cadena y crida a la funcio longitud per a medirla.

z = (3, 5, 7, 9, 10) #Llista
print("La longitud de la tupla dada es:", longitud(z)) #Fa un print de la cadena y crida a la funcio longitud per a medirla.

w = {3, 5, 7, 9, 10} #Llista
print("La longitud del conjunto dado es:", longitud(w)) #Fa un print de la cadena y crida a la funcio longitud per a medirla.