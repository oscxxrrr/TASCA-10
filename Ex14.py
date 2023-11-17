x = int(input("Introduze el primer numero: "))
y = int(input("Introduze el segundo numero: "))
z = int(input("introduze el tercer numero: "))
if x>y>z:
    print("El numero más grande és {}".format(x)) 
elif x>z>y: 
    print("El numero más grande és {}".format(x))   
elif x>y==z: 
    print("El numero más grande és {}".format(x)) 
elif z>x>y:
    print("El numero más grande és {}".format(z)) 
elif y>x>z:
    print("El numero más grande és {}".format(y)) 
elif y>z>x:
    print("El numero más grande és {}".format(y)) 
elif y>x==z:
    print("El numero más grande és {}".format(y))   
elif z>y>x:
    print("El numero más grande és {}".format(z))  
elif y==z>x:
    print("El numero más grande és {}".format(y))  
elif x==y==z:
    print("Los tres numeros son iguales")
elif x==y>z:
    print("El numero más grande és {}".format(x))  
elif x==z>y:
    print("El numero más grande és {}".format(x)) 