x = float(input("Introduzca el primer elemento: "))
y = float(input("Introduzca el segundo elemento: "))
z = float(input("Introduzca el tercer elemento: "))

if x > y and x > z:
	print(x, " > ", y , " > ", z)
elif x == y and y == z:
	print(x, " = ", y, " = ", z)
elif y > x and y > z:
	print(y, " > ", x, " > ", z)
elif y == z:
	print(y, " = ", z, " = ", x)
elif z > x and z > y:
	print(z, " > ", x, " > ", y)
elif z == y:
	print(z, " = ", y, " = ", x)
else:
	print("Los tres elementos son distintos. Ninguno es mayor que los otros dos.")