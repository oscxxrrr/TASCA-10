x = float(input("Introdueixi la quantitat sol·licitada (entre 50000 i 80000) euros: "))
y = float(input("Introdueixi l'interés (entre 0.5 i 13) percentatge: "))
z = int(input("Introdueixi el número d'anys: "))

if not (50000 <= x <= 80000) or not (0.5 <= y <= 13):
    print("Si us plau, introdueixi valors dins dels rangs especificats.")
else:
    # Calcular el cfinal
    cfinal = x * (1 + y / 100) ** z
    # Imprimir el resultado con dos decimales
    print("El capital {:.2f}€ a un interés del {}% a {} anys resulta que pagarem {:.2f}€".format(x, y, z, cfinal))