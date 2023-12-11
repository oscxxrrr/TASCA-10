def comptar_vocals(a):
    b = ('a', 'e', 'i', 'o', 'u', 'altres')
    vocals = [0, 0, 0, 0, 0, 0]
    for i, e in enumerate(a):
        if e.lower() in ['a', 'à', 'á']:
            vocals[0] += 1
        elif e.lower() in ['e', 'è', 'é']:
            vocals[1] += 1
        elif e.lower() in ['i', 'í']:
            vocals[2] += 1
        elif e.lower() in ['o', 'ò', 'ó']:
            vocals[3] += 1
        elif e.lower() in ['u', 'ú']:
            vocals[4] += 1
        else:
            vocals[5] += 1
    for i, e in enumerate(vocals):
        print("La vocal {} apareix {} vegades".format(b[i], vocals[i]))

# Programa Principal
a = input("Introdueixi una paraula a analitzar: ")
comptar_vocals(a)
