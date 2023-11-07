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
    eleccion = int(input())
    if eleccion == 1:
        print("Resultado: ", numero1, "+", numero2, "=", numero1+numero2)
    
    if eleccion == 2:
        print("Resultado: ", numero1, "-", numero2, "=", numero1-numero2)

    if eleccion == 3:
        print("Resultado: ", numero1, "*", numero2, "=", numero1*numero2)
    
    if eleccion == 4:
        print("Resultado: ", numero1, "/", numero2, "=", numero1/numero2)
    
    if eleccion == 5:
       numero1=int(input("Ingresa un número: "))
       numero2=int(input("Ingresa otro número: "))

    if eleccion == 6:
        print("Has salido de la calculadora creada por: Óscar Martínez")