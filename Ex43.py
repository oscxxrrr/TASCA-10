suma = 0

# Solicitar un número al usuario
a = input("Introdueix un número: ")

# Verificar si la entrada es un número
if a.isdigit():
    print("{} té {} dígits".format(a, len(a)))

    # Calcular la suma de los dígitos
    for i in a:
        suma += int(i)

    print("La suma dels dígits del número {} és {}".format(a, suma))

    # Determinar si la suma es par o impar
    if suma % 2 == 0:
        print("La suma dels dígits del número {} és parell".format(a))
    else:
        print("La suma dels dígits del número {} és senar".format(a))
else:
    print("Si us plau, introdueixi un número vàlid.")