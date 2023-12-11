def esta_ordenada(a):
    b = sorted(a)  # Copia profunda de la lista ordenada
    return a == b

def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

# Programa principal
a = llegir_llista()
ordenada = esta_ordenada(a.copy())  # Se realiza una copia de la lista para evitar modificaciones

if ordenada:
    print("La llista {} està ordenada".format(a))
else:
    print("La llista {} no està ordenada".format(a))


