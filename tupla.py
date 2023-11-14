from math import e


def segona_ocurrencia(l, e):
    a = l.count(e)
    if a==0:
        print("No hi ha ocurrències d'aquest element")
    elif a==1:
        print("la primera ocurréncia esta en la posicio {}: ".format(l.index(e)))
    elif a>2:
        print("Hi ha més de dues ocurrència de {}: ".format(e))
        p= l.index(e)
        print(p)
        so=l.index(e,(p+1))
        print(so)  
        to=l.index(e,(so+1))
        print(to)
    else:
        print("Nomes hi ha una o ninguna ocurrència")

#Programa principal
l= (1, 4, 2, (1, 3, 3), 3, 4, 2, 1, 2, 1)
x = int(input("Eligeix l'element que vols cercar en la tupla: "))
segona_ocurrencia(l,x)