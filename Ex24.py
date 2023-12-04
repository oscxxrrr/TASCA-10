def gran_llista(lista):
    if len(lista) == 0:
        return None
    
    maximo = lista[0]
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
    
    return maximo

def ingresar_lista():
    entrada = input("Ingrese una lista de números separados por espacios: ")
    lista_numeros = [int(num) for num in entrada.split()]  
    return lista_numeros

lista_del_usuario = ingresar_lista()
resultado = gran_llista(lista_del_usuario)
if resultado is not None:
    print("El número más grande de la lista es:", resultado)
else:
    print("No hay nada en la lista.")