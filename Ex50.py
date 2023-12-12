def crear_llista_fitxer(fitxer):
    with open(fitxer, 'r') as f:
        llista = f.readlines()
    lparaules = [linea.rstrip('\n') for linea in llista] 
    for a in lparaules:
        print(a)
    f.close()

# Programa principal
crear_llista_fitxer('/home/cicles/AO/TASCA-10/prova.txt')
