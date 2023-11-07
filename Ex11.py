def menu_principal():
    print("""
        Menú Principal:
          1.Calculadora de numeros enteros
          2.Calculadora de numeros reales
          3.Salir
          """)
    a = int(input("Elige una opcion: "))
    return a
def calculadora_enteros():
    op = 1 
    while op>0:
        print("""
        Menu Enteros:
        1.Sumar
        2.Restar
        3.Multiplicar 
        4.Dividir
        5.Salir
          """)
        op = int(input("Elige una opcion: "))
        match op:
            case 1: #Sumar
                x = int(input("Introduze el primer numero: "))
                y = int(input("Introduze el segundo numero: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introduze el primer numero: "))
                y = int(input("Introduze el segundo numero: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introduze el primer numero: "))
                y = int(input("Introduze el segundo numero: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introduze el primer numero: "))
                y = int(input("Introduze el segundo numero: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Salir
                print("Has salido de la calculadora de numeros enteros")
                op = -1

def calculadora_reales():
    op = 1 
    while op>0:
        print("""
        Menu Reales:
        1.Sumar
        2.Restar
        3.Multiplicar 
        4.Dividir
        5.Salir
          """)
        op = int(input("Elige una opcion: "))
        match op:
            case 1: #Sumar
                x = float(input("Introduze el primer numero: "))
                y = float(input("Introduze el segundo numero: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introduze el primer numero: "))
                y = float(input("Introduze el segundo numero: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introduze el primer numero: "))
                y = float(input("Introduze el segundo numero: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introduze el primer numero: "))
                y = float(input("Introduze el segundo numero: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Salir
                print("Has salido de la calculadora de numeros reales")
                op = -1
       
#Programa principal
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enteros()
        case 2:
            calculadora_reales()
        case 3:
            a = -1
        case other:
            print("Opcion no valida")
