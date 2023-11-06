numero1=int(input("Ingresa un número: "))
numero2=int(input("Ingresa otro número: "))

eleccion = 0

while eleccion != 6:
    print("""
          Menu Principal: 
          1. Suma
          2. Resta
          3. Multiplicacion
          4. Division
          5. Cambiar numeros
          6. Salir
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
