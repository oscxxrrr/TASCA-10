def detectar_vocals(a):
    l = ('a','e','i','o','u')
    d = a.lower() #Pasa les lletres inserides a minusculas.
    if d in l: #Si algun element de "d" esta dins la llista "l"...
        print("Es vocal") #Sera vocal
    else: #No es vocal
        print("No es vocal")

#Programa principal
a = input("Introduce un caracter: ") #Introdueix un caracter 
b = detectar_vocals(a) #Crida a la funcio de dalt
