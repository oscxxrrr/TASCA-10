def gran(a, b):
		if (a>b):
			return a
		else:
			return b

# Ús de la funció 
x = input("Introdueixi el primer número a comparar: ")
y = input("Introdueixi el segon número a comparar: ")
c = gran(x, y)
print("El més gran és: ", c)