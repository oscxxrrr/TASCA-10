def gran(a, b):
		if (a>b): #Nos devolvera A si es mas grande que B
			return a
		else:#Sino, devolvera B, es decir, B es mas grande
			return b

# Programa principal
x = input("Introdueixi el primer número a comparar: ")
y = input("Introdueixi el segon número a comparar: ")
c = gran(x, y)
print("El més gran és: ", c) 