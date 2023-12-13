def invertir(a):#Definim com a invertir
	b = list(a)   # Converteix 'a' en una llista 'b'
	c = b[::-1]   # Inverteix la llista 'b' i guarda el resultat a 'c'
	r = "".join(c)  # Uneix els elements de 'c' com a cadena i guarda el resultat a 'r'
	return r  # Retorna la cadena invertida 'r'

# Programa principal
s = "Això és una cadena que s’ha de girar"  # Defineix una cadena 's'
print("La cadena girada és: ",invertir(s))  # Imprimeix la cadena 's' invertida
