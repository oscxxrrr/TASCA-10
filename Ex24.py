def leer_lista():
    a = '1'
    l=[]
    while a!='a':
        a=input("Introduze un numero diferente a 'a': ")
        if a !='a':
            l.append(int(a))
        else:
            return l

def gran_llista(l):
    max = l[0]
    for e in l:
        if e > max:
            max = e 
    print("El numero mas grande de la lista {} és {}".format(l, max)) 

#Programa principal
l = leer_lista()
gran_llista(l)