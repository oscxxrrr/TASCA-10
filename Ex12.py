def menu_principal():
    print("""
        1. Operaciones con Números Enteros
        2. Operaciones con Números Reales
        3. Salir
    """)
    return int(input("Elige una opción: "))

def calculadora_enteros():
    print("Calculadora Enteros")
    numero1 = int(input("Ingresa el primer número entero: "))
    numero2 = int(input("Ingresa el segundo número entero: "))
    operacion = int(input("""
        Menu Enteros:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Cambiar números
        6. Cambiar tipo de números
        7. Salir
        Elige una opción: 
    """))
    
    if operacion == 1:
        resultado = numero1 + numero2
        print(f"Resultado: {numero1} + {numero2} = {resultado}")
    elif operacion == 2:
        resultado = numero1 - numero2
        print(f"Resultado: {numero1} - {numero2} = {resultado}")
    elif operacion == 3:
        resultado = numero1 * numero2
        print(f"Resultado: {numero1} * {numero2} = {resultado}")
    elif operacion == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {numero1} / {numero2} = {resultado}")
        else:
            print("No se puede dividir por cero.")
    elif operacion == 5:
        numero1 = int(input("Ingresa un nuevo primer número entero: "))
        numero2 = int(input("Ingresa un nuevo segundo número entero: "))
    elif operacion == 6:
        return
    elif operacion == 7:
        print ("Has salido de la calculadora de numeros enteros")
        print("Elige otra opcion: ")

def calculadora_reales():
    print("Calculadora Reales")
    numero1 = float(input("Ingresa el primer número real: "))
    numero2 = float(input("Ingresa el segundo número real: "))
    operacion = int(input("""
        Menu Reales:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Cambiar números
        6. Cambiar tipo de números
        7. Salir
        Elige una opción: 
    """))
    
    if operacion == 1:
        resultado = numero1 + numero2
        print(f"Resultado: {numero1} + {numero2} = {resultado}")
    elif operacion == 2:
        resultado = numero1 - numero2
        print(f"Resultado: {numero1} - {numero2} = {resultado}")
    elif operacion == 3:
        resultado = numero1 * numero2
        print(f"Resultado: {numero1} * {numero2} = {resultado}")
    elif operacion == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {numero1} / {numero2} = {resultado}")
        else:
            print("No se puede dividir por cero.")
    elif operacion == 5:
        numero1 = float(input("Ingresa un nuevo primer número real: "))
        numero2 = float(input("Ingresa un nuevo segundo número real: "))
    elif operacion == 6:
        return
    elif operacion == 7:
        print("Has salido de la caluladora de numeros reales")
        print("Elige otra opcion: ")

# Programa principal
while True:
    opcion = menu_principal()
    
    if opcion == 1:
        calculadora_enteros()
    elif opcion == 2:
        calculadora_reales()
    elif opcion == 3:
        print("Has salido de la calculadora creada por Óscar Martínez")
        break
    else:
        print("Opción no válida. Intente de nuevo.")