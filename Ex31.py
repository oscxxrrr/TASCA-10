def noms_que_comencen_per(llista, lletra):
    comptador = 0
    llnom = []
    for e in llista:
        if e[0] == lletra:
            llnom.append(e)
            comptador += 1
    print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

def llegir_noms():
    llista_noms = []
    print("Introdueixi els noms (per acabar, introdueixi 'fi'): ")
    nom = input("Introdueixi un nom: ")
    while nom.lower() != 'fi':
        llista_noms.append(nom)
        nom = input("Introdueixi un nom: ")
    return llista_noms

# Uso de las funciones
nombres = llegir_noms()
lletra = input("Introdueixi la lletra per a la cerca: ")
noms_que_comencen_per(nombres, lletra)
