def leer_lista():
    a = '1'
    l=[]
    while a!='a':
        a=input("Introduze un numero diferente a 'a': ")
        if a !='a':
            l.append(int(a))
        else:
            return l
    
def sumar_lista(l):
    s = 0
    for e in l:
        s += e
    print("La suma de los elementos {} de la llista és {}".format(l,s))

def multiplicar_lista(l):
    m = 1
    for e in l:
        m *= e
    print("La multiplicacion de los elementos {} de la llista és {}".format(l,m))

# Programa principal
l = leer_lista()
sumar_lista(l)
multiplicar_lista(l)

