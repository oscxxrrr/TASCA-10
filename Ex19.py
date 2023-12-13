def es_palindron(): #Definim es_palindron
    a = a.lower() #Pasa les lletres a lower (minuscula)
    return a == a[a::-1] #Ens retorna la llista si "a" es igual que el contingut de "a" al reves.

b = input("Introduce una palabra: ") #Introdueix una palanra

if es_palindron: #Si es palindron...
    print("La palabra {} és palindron".format(b)) #Imprimira aquesta opcio

else:    
    print("La palabra {} no palindron".format(b)) #Si no ho es imprimira aquesta