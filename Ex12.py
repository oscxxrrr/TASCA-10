def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de números enters
          2. Calculadora de números reals
          3. Canvis de base
          4. Sortir
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
        print("Eligeixi una opcio: ")
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

# Funciones de cambios de base
def dectobin(numero):
    return bin(numero)
def dectooct(numero):
    return oct (numero)
def dectohex(numero):
    return hex (numero)


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

def menu_canvis_base():
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
#De binari a octal:
def binario_a_octal(binario):
    decimal = int(binario, 2)
    octal = oct(decimal)
    return octal

#De binari a decimal:
def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal

#De binari a hexadecimal:
def binario_a_hexadecimal(binario):
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)
    return hexadecimal

#De octal a decimal:
def octal_a_decimal(octal):
    decimal = int(octal, 8)
    return decimal

#De octal a binario:
def octal_a_binario(octal):
    decimal = int(octal, 8)
    binario = bin(decimal)[2:]
    return binario

#De octal a hexadecimal:
def octal_a_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)
    return hexadecimal

#De decimal a binario:
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

#De decinal a octal:
def decimal_a_octal(decimal):
    octal = oct(decimal)[2:]
    return octal

#De decimal a hexadecimal:
def decimal_a_hexadecimal(decimal):
    hexadecimal = hex(decimal)[2:]
    return hexadecimal

#De hexadecimal a decimal:
def hexadecimal_a_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

#De hexadecimal a binario:
def hexadecimal_a_binario(hexadecimal):
    decimal = int(hexadecimal, 16)
    binario = bin(decimal)[2:]
    return binario

#De hexadecimal a octal:
def hexadecimal_a_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)
    return octal

def canvis_base():
    op = int(input("Eligeix una opció: "))
    match op:
        case 1: #Binari to decimal
            b = input("Introdueixi el numero binari: ")
            o = binario_a_octal(b)
            d = binario_a_decimal(b)
            h = binario_a_hexadecimal(b)
            print("El numero binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))        
        case 2: #Octal to
            o = input("Introdueix el numero octal: ")
            b = octal_a_binario(o)
            d = octal_a_decimal(o)
            h = octal_a_hexadecimal(o)
            print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
        case 3: #Decimal to
            o = input("Introdueix el numero octal: ")
            b = decimal_a_binario(o)
            d = decimal_a_octal(o)
            h = decimal_a_octal(o)
            print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
        case 4: #hexadecimal to
            o = input("Introdueix el numero octal: ")
            b = hexadecimal_a_binario(o)
            d = hexadecimal_a_octal(o)
            h = hexadecimal_a_decimal(o)
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
            canvis_base()
        case 4:
            print("Has salido de la calculadora")
            a = -1 
        case other:
            print("Opció no vàlida ") 