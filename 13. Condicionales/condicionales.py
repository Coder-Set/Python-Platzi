
x = 5
y = 3
z = 10
#Codicional if y and
if x > y and x > z:
    print("X es mayor que Y, y mayor que Z")
elif x < y:
    print("X es siempre mayor que Y")
elif x == y:
    print("X es igual que Y")
else:
    print("Ninguna de las condiciones se cumple")


#Condicional if y or
if x > y or x > z:
    print("X es mayor que Y, o mayor que Z")



#Otro ejemplo
a = "Python"
b = "JavaScript"
c = "Python"

if a == b:
    if a != b:
        print("a es igual a c, pero distinto a b")
    else:
        print("Estoy saliendo por el else del if interno...")
else:
    if a == c:
        print("a es igual que c, pero distinto a b")
    else:
        print("a no es igual que b")
