def menu_principal():
    # Imprime el menú principal con varias opciones numeradas
    print("""
        Menú principal:
          1. Calculadora de números enteros
          2. Calculadora de números reales
          3. Cambios de base
          4. Salir
          """)
    # Solicita al usuario que ingrese un número que represente una opción del menú
    a = int(input("Elija una opción: "))
    # Retorna el número ingresado por el usuario
    return a

def calculadora_enteros():
    op = 1  # Inicialización de la variable de opción para ingresar al bucle while
    while op > 0:  # Mientras la opción ingresada sea mayor que cero, se ejecutará el bucle
        print("""
              Menú enteros
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Salir
        """)
        op = int(input("Elija una opción: "))  # Solicita al usuario que elija una opción del menú
        if op == 1:  # Si la opción es 1, realiza la suma
            x = int(input("Ingrese el primer número: "))  # Imprime el primer número
            y = int(input("Ingrese el segundo número: "))  # Imprime el segundo número
            print("{} + {} = {}".format(x, y, x + y))  # Muestra el resultado de la suma
        elif op == 2:  # Si la opción es 2, realiza la resta
            x = int(input("Ingrese el primer número: "))  # Imprime el primer número
            y = int(input("Ingrese el segundo número: "))  # Imprime el segundo número
            print("{} - {} = {}".format(x, y, x - y))  # Muestra el resultado de la resta
        elif op == 3:  # Si la opción es 3, realiza la multiplicación
            x = int(input("Ingrese el primer número: "))  # Imprime el primer número
            y = int(input("Ingrese el segundo número: "))  # Imprime el segundo número
            print("{} * {} = {}".format(x, y, x * y))  # Muestra el resultado de la multiplicación
        elif op == 4:  # Si la opción es 4, realiza la división
            x = int(input("Ingrese el primer número: "))  # Imprime el primer número
            y = int(input("Ingrese el segundo número: "))  # Imprime el segundo número
            print("{} / {} = {}".format(x, y, x / y))  # Muestra el resultado de la división
        elif op == 5:  # Si la opción es 5, sale del bucle
            print("Ha salido de la calculadora de enteros.\n")  # Muestra un mensaje de salida
            break  # Sale del bucle while

def calculadora_reales():
    op = 1  # Inicialización de la variable de opción para ingresar al bucle while
    while op > 0:  # Mientras la opción ingresada sea mayor que cero, se ejecutará el bucle
        print("""
              Menú reales
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Salir
        """)
        op = int(input("Elija una opción: "))  # Solicita al usuario que elija una opción del menú
        if op == 1:  # Si la opción es 1, realiza la suma
            x = float(input("Ingrese el primer número: "))  # Solicita el primer número
            y = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
            print("{} + {} = {}".format(x, y, x + y))  # Muestra el resultado de la suma
        elif op == 2:  # Si la opción es 2, realiza la resta
            x = float(input("Ingrese el primer número: "))  # Solicita el primer número
            y = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
            print("{} - {} = {}".format(x, y, x - y))  # Muestra el resultado de la resta
        elif op == 3:  # Si la opción es 3, realiza la multiplicación
            x = float(input("Ingrese el primer número: "))  # Solicita el primer número
            y = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
            print("{} * {} = {}".format(x, y, x * y))  # Muestra el resultado de la multiplicación
        elif op == 4:  # Si la opción es 4, realiza la división
            x = float(input("Ingrese el primer número: "))  # Solicita el primer número
            y = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
            print("{} / {} = {}".format(x, y, x / y))  # Muestra el resultado de la división
        elif op == 5:  # Si la opción es 5, muestra un mensaje de salida
            op = -1
            print("Ha salido de la calculadora de reales.\n")  # Muestra un mensaje de salida

# Definicions Binari to
def bin_to_oct(binary_num):
    # Convierte el número binario a decimal
    decimal_num = int(binary_num, 2)
    # Convierte el número decimal a octal y lo devuelve eliminando el prefijo '0o'
    octal_num = oct(decimal_num)
    return octal_num[2:]  # Retorna el número octal eliminando los dos primeros caracteres ('0o')

def bin_to_dec(binary_num):
    # Convierte el número binario a decimal y lo devuelve
    decimal_num = int(binary_num, 2)
    return decimal_num  # Retorna el número decimal

def bin_to_hex(binary_num):
    # Convierte el número binario a decimal
    decimal_num = int(binary_num, 2)
    # Convierte el número decimal a hexadecimal y lo devuelve eliminando el prefijo '0x'
    hex_num = hex(decimal_num)
    return hex_num[2:]  # Retorna el número hexadecimal eliminando los dos primeros caracteres ('0x')


# Definicions Octal to
def oct_to_bin(octal_num):
    # Convierte el número octal a decimal
    decimal_num = int(octal_num, 8)
    # Convierte el número decimal a binario y lo devuelve eliminando el prefijo '0b'
    binary_num = bin(decimal_num)
    return binary_num[2:]  # Retorna el número binario eliminando los dos primeros caracteres ('0b')

def oct_to_dec(octal_num):
    # Convierte el número octal a decimal y lo retorna
    decimal_num = int(octal_num, 8)
    return decimal_num  # Retorna el número decimal

def oct_to_hex(octal_num):
    # Convierte el número octal a decimal
    decimal_num = int(octal_num, 8)
    # Convierte el número decimal a hexadecimal y lo devuelve eliminando el prefijo '0x'
    hex_num = hex(decimal_num)
    return hex_num[2:]  # Retorna el número hexadecimal eliminando los dos primeros caracteres ('0x')


# Definicions Decimal to
def dec_to_bin(decimal_num):
    # Convierte el número decimal a binario y devuelve el resultado eliminando el prefijo '0b'
    binary_num = bin(int(decimal_num))
    return binary_num[2:]  # Retorna el número binario eliminando los dos primeros caracteres ('0b')

def dec_to_oct(decimal_num):
    # Convierte el número decimal a octal y devuelve el resultado eliminando el prefijo '0o'
    octal_num = oct(int(decimal_num))
    return octal_num[2:]  # Retorna el número octal eliminando los dos primeros caracteres ('0o')

def dec_to_hex(decimal_num):
    # Convierte el número decimal a hexadecimal y devuelve el resultado eliminando el prefijo '0x'
    hex_num = hex(int(decimal_num))
    return hex_num[2:]  # Retorna el número hexadecimal eliminando los dos primeros caracteres ('0x')


# Definicions Hexadecimal to
def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16)  # Convierte el número hexadecimal a decimal
    binary_num = bin(decimal_num)  # Convierte el número decimal a binario
    return binary_num[2:]  # Retorna el número binario eliminando los dos primeros caracteres ('0b')

def hex_to_oct(hex_num):
    decimal_num = int(hex_num, 16)  # Convierte el número hexadecimal a decimal
    octal_num = oct(decimal_num)  # Convierte el número decimal a octal
    return octal_num[2:]  # Retorna el número octal eliminando los dos primeros caracteres ('0o')

def hex_to_dec(hex_num):
    decimal_num = int(hex_num, 16)  # Convierte el número hexadecimal a decimal
    return decimal_num  # Retorna el número decimal
            

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