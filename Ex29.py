from datetime import date

def GetNames(aactual):
    a = []
    print("Introdueixi els nom i la data de naixament de les 4 persones:")
    for i in range(0, 4):
        v = [0, 0, 0]
        v[0] = input("Escriu el nom de la {}a persona: ".format(i+1))
        v[1] = int(input("Escriu l'any de naixament de {}: ".format(v[0])))
        v[2] = aactual - v[1]
        a.append(v)
    return a

# Programa Principal
avui = date.today()
aactual = avui.year
x = GetNames(aactual)
print("L'any actual és: ", aactual)
print("{:<20} {:<20} {:<20}".format('Nom', 'Data naixament', 'Edat'))
for e in x:
    print("{:<20} {:<20} {:<20}".format(e[0], e[1], e[2]))