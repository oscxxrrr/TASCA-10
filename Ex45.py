def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

def eliminar_capicua(a):
    b = a[1:-1] if len(a) > 1 else []
    return b

# Programa principal
x = llegir_llista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x, y))