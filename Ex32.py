def noms_que_comencen_per(llista, lletra):
    comptador = 0
    llnom = []
    for e in llista:
        if e[0] == lletra:
            llnom.append(e)
            comptador += 1
    print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

def llegir_noms():
    l = []
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while True:
        nom = input("Posi el següent nom: ")
        if nom == "-1":
            break
        l.append(nom)
    return l

# Programa principal
noms = llegir_noms()
caracter = input("Introdueixi el caràcter que vols que comencin les paraules a cercar: ")
noms_que_comencen_per(noms, caracter)