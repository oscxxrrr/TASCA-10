def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de números enters
          2. Calculadora de números reals
          3. Sortir
          """)
    a = int(input("Elegeixi una opcio: "))
    return a
def calculadora_enters():
    op = 1
    while op>0:
        print("""
              Menú enters
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = int(input("Elixeixi una opció: "))
        match op:
            case 1: #Sumar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adéu, ja tornaras a la calculadora inicial \n\n")
                op=-1


def calculadora_reals():
    op = 1
    while op>0:
        print("""
              Menú reals
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = float(input("Elixeixi una opció: "))
        match op:
            case 1: #Sumar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adéu, ja tornaras a la calculadora inicial \n\n")
                op=-1

#programa principal
a = 1
while a>0 :
    a = menu_principal()
    match a :
        case 1: #Si elijes el 1 del programa principal entraras a la calculadora de enteros.
            calculadora_enters()
        case 2: #Si elijes el 2 del programa principal entraras a la calculadora de reales.
            calculadora_reals()
        case 3: #Si elijes el 3 del programa principal saldras de la calculadora.
            a = -1
        case other: #Si elijes un numero que no este en el programa principal se hara un print de opcion no valdia
            print("Opció no vàlida ") 