def detectar_vocals(a):
    l = ('a','e','i','o','u')
    d = a.lower()
    if d in l:
        print("Es vocal")
    else:
        print("No es vocal")

#Programa principal
a = input("Introduce un caracter: ")
b = detectar_vocals(a)
