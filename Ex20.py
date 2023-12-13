def superposicio(a,b): #Definim superposicio
    for element in a: #Recorregut des elements de dins "a".
        if element in b: #Si element esta en "b"...
            return True #Retornara "true"
    return False #Sino retornara "false"

a = input("Introduce una lista de caracteres: ") #Introdueix una cadena caracteres
b = input("Introduce una lista de caracteres: ") #Introdueix unaltra cadena de caracteres

if superposicio(a,b): #Si es superposicio (crida la funcio)
    print("Las listas {} y {} tienen elementos en comun.".format(a,b)) #Imprimira el seguent
else: #Sino
    print("Las listas {} y {} no tienen elementos en comun.".format(a,b)) #Imprimira aquest