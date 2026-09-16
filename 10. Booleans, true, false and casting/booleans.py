#Algunas de las formas en las que podemos obtener valores booleanos son:

#Mediante declaracion e impresion de variables 
v = True
f = False
print(v)
print(f)

#Mediante comparaciones 
print(5 > 3) #True
print(8 < 10) #False
print(8 > 10) #False

print(type(v))


#Mediante el casteo de booleans a strings

print(bool("Hola Mundo")) #True
print(bool("")) #False )) #False


#Datos que nos van a dar true:

print(bool("Hola Mundo")) #True
print(bool(123)) #True
print(bool(["Manzana", "Pera", "Banana"])) #True
print(bool(" ")) #True, por el espacio del string


#Datos que nos van a dar false:
print(bool("")) #False, sin espacio, se toma como string vacio
print(bool(0)) #False
print(bool([])) #False
print(bool(None)) #False

