def superposicio(a,b):
    for element in a:
        if element in b:
            return True
    return False

a = input("Introduce una lista de caracteres: ")
b = input("Introduce una lista de caracteres: ")

if superposicio(a,b):
    print("Las listas {} y {} tienen elementos en comun".format(a,b))
else:
    print("Las listas {} y {} no tienen elementos en comun".format(a,b))