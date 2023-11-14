a = 1 
while a>0:
    print("""   
    Menu Principal:
    1.Comprobacion par/impar
    2.Salir
    """)
    a = int(input("Introdueix una opcio: "))
    match a:
        case 1: #Si volem veure si es par i impar
            x = int(input("Introdueix un nombre: "))
            if x % 2 == 0:
                print("Es parell")
            else:
                print("Es imparell")
        case 2:
            a=0
