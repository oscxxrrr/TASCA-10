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
                print("Has sortit de la calculadora \n\n")
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
                print("Has sortit de la calculadora \n\n")
                op=-1

def canvis_base():
    op = 1
    while op>0:
        print("""
            Menu canvis de base:
              1.Donat un binari ho passarem a tota la resta
              2.Donat un octal el passem a tota la resta
              3.Donat un decimal ho passem a tota la resta 
              4.Donat un hexadecimal ho passem a tota la resta
              5.Sortit
              """)
        op = int(input("Eligeix una opció: "))
        match op:
            case 1: #Binari to
                b = input("Introdueixi el numero binari: ")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El numero binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: #Octal to
                o = input("Introdueix el numero octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 3: #Decimal to
                o = input("Introdueix el numero octal: ")
                b = dectobin(o)
                d = dectooct(o)
                h = dectohex(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 4: #hexadecimal to
                o = input("Introdueix el numero octal: ")
                b = hextobin(o)
                d = hextooct(o)
                h = hextodec(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
#programa principal
a = 1
while a>0 :
    a = menu_principal()
    match a :
        case 1:
            calculadora_enters()
        case 2: 
            calculadora_reals()
        case 3:
            print("Has salido de la calculadora")
            a = -1
        case other:
            print("Opció no vàlida ") 