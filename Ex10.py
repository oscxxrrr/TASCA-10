#Definició de la funció 
def major(a):  
    if a>18: #Si el nombre inserit es mayor a 18 es mayor d'edat
        print("És major d'edat")
    elif a<18:#Si el nombre inserit es menos a 18 es menos d'edat
        print("És menor d'edat")
    else:#Si el nombre inserit es 18
        print("Té 18 anys")    

#Programa principal
x= int(input("introdueixi la seva edat: ")) 
major(x) 