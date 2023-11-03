#Lista
a = [3,2,4,'a',[1,'b'],"Hola"]

#Sublista 
print (a [-2:])
print (a[2:4])
print (a [1:-2])
print (a[:-4])
print (a[4:5])
print (a[1:7])
print (a[0:1])
print (a[3:-1])
print (a[1:-4])

a.insert(1,3)
print(a)

#Añade mas de un elemento a la lista
a.extend(["Hola","Adeu"])

#Añade 1 elemento a la lista
a.append["BUENAS"]

#Suma dos listas
a = [1,2]
b = [3,4]
c = a + b 
print(c)

#Elimina por posicion
d = [1,2,3,"OSCAR"]
del d[1]
print(d)

#Elimina por nombre o elemento
d = [1,2,3,"OSCAR"]
d.remove("OSCAR")
print(d)

#Elimina por posicion "() és el ultimo"
d = [1,2,3,"OSCAR"]
d.pop(2)
d.pop()
print(d)

#Muestra el nº de caracteres
d = [1,2,3,"OSCAR"]
print(len(d))
