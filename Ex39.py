x = int(input("Introdueixi un número natural (<100): "))
suma = 0

# Asegúrate de que el valor ingresado esté dentro del rango permitido
if x >= 100:
    print("Si us plau, introdueixi un número menor que 100.")
else:
    for i in range(1, x, 4):
        suma += i ** 2

    print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(x, suma))