def filtrar_palabras(l,t):
    for e in l:
        if len(e) > t:
            print(e)

def leer_lista():
    a = '1'
    l=[]
    while a!='a':
        a=input("Introduze un numero diferente a 'a': ")
        if a !='a':
            l.append(a)
        else:
            return l

#Prograna principal
l = leer_lista()
n = int(input("Introduce el tamaño para filtrar: "))
filtrar_palabras(l,n)
