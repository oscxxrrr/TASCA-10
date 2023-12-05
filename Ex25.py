def leer_lista():
    a = '1'
    l=[]
    while a!='a':
        a=input("Introduze un numero diferente a 'a': ")
        if a !='a':
            l.append(a)
        else:
            return l

def palabra_larga(x):
    max = x[0]
    for e in x:
        if len(e) > len(max):
            max = e
    return max

#Programa principal
llista_paraules = leer_lista()
print("La palabra mas grande de la lista {} és {}".format(llista_paraules,palabra_larga(llista_paraules)))
l = leer_lista()
