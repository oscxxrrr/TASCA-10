from datetime import date  # Importa la clase 'date' desde el módulo 'datetime'

# Define una función para obtener los nombres y fechas de nacimiento de 4 personas
def GetNames(aactual):
    a = []  # Inicializa una lista vacía para almacenar la información de las personas
    print("Introdueixi els nom i la data de naixament de les 4 persones:")
    for i in range(0, 4):  # Realiza un bucle para pedir los nombres y fechas de nacimiento de las 4 personas
        v = [0, 0, 0]  # Inicializa una lista temporal para almacenar los datos de cada persona
        v[0] = input("Escriu el nom de la {}a persona: ".format(i+1))  # Solicita el nombre de la persona
        v[1] = int(input("Escriu l'any de naixament de {}: ".format(v[0])))  # Solicita el año de nacimiento
        v[2] = aactual - v[1]  # Calcula la edad restando el año actual del año de nacimiento
        a.append(v)  # Agrega los datos de la persona a la lista principal
    return a  # Devuelve la lista con la información de las personas

# Programa Principal
avui = date.today()  # Obtiene la fecha actual
aactual = avui.year  # Obtiene el año actual
x = GetNames(aactual)  # Llama a la función 'GetNames' para obtener la información de las personas
print("L'any actual és: ", aactual)  # Imprime el año actual
# Imprime los encabezados y la información de las personas (nombre, fecha de nacimiento, edad)
print("{:<20} {:<20} {:<20}".format('Nom', 'Data naixament', 'Edat'))
for e in x:
    print("{:<20} {:<20} {:<20}".format(e[0], e[1], e[2]))  # Imprime los datos de cada persona formateados
