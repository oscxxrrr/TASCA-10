def llegir_llista():
    a = '1'  # Inicialitza 'a' amb '1'
    l = []   # Inicialitza una llista buida 'l'
    while a != 'a':  # Mentre 'a' no sigui igual a 'a':
        a = input("Introdueix un número diferent a 'a': ")  # Demana a l'usuari introduir un número diferent a 'a'
        if a != 'a':  # Si 'a' no és igual a 'a':
            l.append(int(a))  # Converteix 'a' a enter i l'afegeix a la llista 'l'
        else:
            return l  # Retorna la llista 'l' si 'a' és igual a 'a'

def sumar_llista(l):
    s = 0  # Inicialitza 's' a 0
    for e in l:  # Per a cada element 'e' a la llista 'l':
        s += e  # Suma el valor de 'e' a 's'
    print("La suma dels elements {} de la llista és {}".format(l, s))  # Mostra la suma dels elements de 'l'

def multiplicar_llista(l):
    m = 1  # Inicialitza 'm' a 1
    for e in l:  # Per a cada element 'e' a la llista 'l':
        m *= e  # Multiplica 'm' pel valor de 'e'
    print("La multiplicació dels elements {} de la llista és {}".format(l, m))  # Mostra la multiplicació dels elements de 'l'

# Programa principal
l = llegir_llista()  # Crida a la funció 'llegir_llista' per obtenir una llista
sumar_llista(l)  # Crida a la funció 'sumar_llista' per sumar els elements de la llista 'l'
multiplicar_llista(l)  # Crida a la funció 'multiplicar_llista' per multiplicar els elements de la llista 'l'
