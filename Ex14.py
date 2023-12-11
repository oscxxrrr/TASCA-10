def gran(a, b, c):
    if (a >= b):
        if (a >= c):
            return a
        else:
            return c
    else:
        if (b >= c):
            return b
        else:
            return c

# Uso de la función
x = int(input("Introduce el primer número a comparar: "))
y = int(input("Introduce el segundo número a comparar: "))
z = int(input("Introduce el tercer número a comparar: "))
c = gran(x, y, z)
print("El más grande es:", c)