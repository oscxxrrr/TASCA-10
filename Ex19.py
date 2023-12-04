def es_palindron():
    a = a.lower()
    return a == a[a::-1]

b = input("Introduce una palabra: ")

if es_palindron:
    print("La palabra {} és palindron".format(b))

else:    
    print("La palabra {} no palindron".format(b))