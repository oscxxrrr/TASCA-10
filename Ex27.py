def contar_mayusculas(s):
    num_maj = 0
    num_men = 0
    for e in s:
        if e.isupper():  
            num_maj += 1

        elif e.islower():
            num_men +=1
    
    return num_maj

#Programa Principal
x = input("Introduce una cadena de caracteres: ")
resultado = contar_mayusculas(x)
print("El numero de letras ayusculas en la cadena es {}".format(resultado))
