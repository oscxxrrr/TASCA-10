def  menu_principal():
    print("""
        Menú principal:
          1. Calculadora de números enteros
          2. Calculadora de números reales
          3. Cambios de base
          4. Salir
          """)
    a = int(input("Elija una opción: "))
    return a

def calculadora_enteros():
    op = 1
    while op > 0:
        print("""
              Menú enteros
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Salir
        """)
        op = int(input("Elija una opción: "))
        if op == 1:  # Sumar
            x = int(input("Ingrese el primer número: "))
            y = int(input("Ingrese el segundo número: "))
            print("{} + {} = {}".format(x, y, x + y))
        elif op == 2:  # Restar
            x = int(input("Ingrese el primer número: "))
            y = int(input("Ingrese el segundo número: "))
            print("{} - {} = {}".format(x, y, x - y))
        elif op == 3:  # Multiplicar
            x = int(input("Ingrese el primer número: "))
            y = int(input("Ingrese el segundo número: "))
            print("{} * {} = {}".format(x, y, x * y))
        elif op == 4:  # Dividir
            x = int(input("Ingrese el primer número: "))
            y = int(input("Ingrese el segundo número: "))
            print("{} / {} = {}".format(x, y, x / y))
        elif op == 5:  # Salir
            print("Ha salido de la calculadora de enteros.\n")
            break

def calculadora_reales():
    op = 1
    while op > 0:
        print("""
              Menú reales
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Salir
        """)
        op = int(input("Elija una opción: "))
        if op == 1:  # Sumar
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            print("{} + {} = {}".format(x, y, x + y))
        elif op == 2:  # Restar
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            print("{} - {} = {}".format(x, y, x - y))
        elif op == 3:  # Multiplicar
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            print("{} * {} = {}".format(x, y, x * y))
        elif op == 4:  # Dividir
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            print("{} / {} = {}".format(x, y, x / y))
        elif op == 5:  # Salir
            print("Ha salido de la calculadora de reales.\n")

# Definicions Binari to

def bin_to_oct(binary_num):
    decimal_num = int(binary_num, 2)
    octal_num = oct(decimal_num)
    return octal_num[2:]

def bin_to_dec(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num[2:]

def bin_to_hex(binary_num):
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num)
    return hex_num[2:]

# Definicions Octal to

def oct_to_bin(octal_num):
    decimal_num = int(octal_num, 8)
    binary_num = bin(decimal_num)
    return binary_num[2:]

def oct_to_dec(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_num[2:]

def oct_to_hex(octal_num):
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num)
    return hex_num[2:]

# Definicions Decimal to

def dec_to_bin(decimal_num):
    binary_num = bin(int(decimal_num))
    return binary_num[2:]

def dec_to_oct(decimal_num):
    octal_num = oct(int(decimal_num))
    return octal_num[2:]

def dec_to_hex(decimal_num):
    hex_num = hex(int(decimal_num))
    return hex_num[2:]

# Definicions Hexadecimal to

def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16)
    binary_num = bin(decimal_num)
    return binary_num[2:]

def hex_to_oct(hex_num):
    decimal_num = int(hex_num, 16)
    octal_num = oct(decimal_num)
    return octal_num[2:]

def hex_to_dec(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num[2:]            

def menu_cambios_base():
    while True:
        print("""
            Menú cambios de base:
              1. De binario a otras bases
              2. De octal a otras bases
              3. De decimal a otras bases
              4. De hexadecimal a otras bases
              5. Salir
        """)
        op = int(input("Elija una opción: "))
        if op == 1:  # De binario
            b = input("Ingrese el número binario: ")
            o = oct(int(b, 2))[2:]
            d = int(b, 2)
            h = hex(int(b, 2))[2:]
            print("El número binario {} es:\nOctal -> {}\nDecimal -> {}\nHexadecimal -> {}".format(b, o, d, h))
        elif op == 2:  # De octal
            o = input("Ingrese el número octal: ")
            b = bin(int(o, 8))[2:]
            d = int(o, 8)
            h = hex(int(o, 8))[2:]
            print("El número octal {} es:\nBinario -> {}\nDecimal -> {}\nHexadecimal -> {}".format(o, b, d, h))
        elif op == 3:  # De decimal
            d = int(input("Ingrese el número decimal: "))
            b = bin(d)[2:]
            o = oct(d)[2:]
            h = hex(d)[2:]
            print("El número decimal {} es:\nBinario -> {}\nOctal -> {}\nHexadecimal -> {}".format(d, b, o, h))
        elif op == 4:  # De hexadecimal
            h = input("Ingrese el número hexadecimal: ")
            b = bin(int(h, 16))[2:]
            o = oct(int(h, 16))[2:]
            d = int(h, 16)
            print("El número hexadecimal {} es:\nBinario -> {}\nOctal -> {}\nDecimal -> {}".format(h, b, o, d))
        elif op == 5:  # Salir
            print("Ha salido del menú de cambios de base.\n")
            break

# Programa principal
while True:
    a = menu_principal()
    if a == 1:
        calculadora_enteros()
    elif a == 2:
        calculadora_reales()
    elif a == 3:
        menu_cambios_base()
    elif a == 4:
        print("Ha salido de la calculadora creada por Óscar Martínez.")
        break
    else:
        print("Opción no válida.")