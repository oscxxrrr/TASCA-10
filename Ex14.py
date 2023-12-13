def gran(a, b, c):
    if (a >= b): #Si "a" es major o igual a "b". 
        if (a >= c): #Si "a" es major o igual a "c" ens retornara "a"
            return a
        else: #Si no se cumple nada anterior retornara "c".
            return c
    else:
        if (b >= c): #Si "b" es major o igual que "c" retortana "b".
            return b
        else: #Si no cumpleix el anterior retornara "c".
            return c

# Uso de la función
x = int(input("Introduce el primer número a comparar: ")) #Inserir un numero amb un int devant del input per a que sea un nombre enter.
y = int(input("Introduce el segundo número a comparar: ")) #Inserir un numero amb un int devant del input per a que sea un nombre enter.
z = int(input("Introduce el tercer número a comparar: ")) #Inserir un numero amb un int devant del input per a que sea un nombre enter.
c = gran(x, y, z) #"c" es el nombre mes gran dels 3 nombres inserits.
print("El más grande es:", c) #Print del nombre mes gran