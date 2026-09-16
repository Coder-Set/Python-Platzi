# Texto Strings

comillasSimples = 'Esto es un texto'
comillasDobles = "Esto es un texto"
comillasTriples = '''Esto es un texto'''

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)



# Numeros

a = 1
b = 3.14 # Python utiliza el punto, para separar los decimales
c = 5 + 2j # Numeros complejos
print(a)
print(b)
print(c)



# Lista o List 

lista = [0, 1, 2, 3, 4, 5]
print(lista)


# Tuplas o Tuple

tupla = ("a", "b", "c") # NO se puede modificar
tupla = ("a", "b", "c", "d") # Se puede modificar, pero no se puede cambiar el valor de los elementos
print(tupla)


# Conjuntos o Set
conjunto = {1, 1, 2, 2, 3, 4, 5} #Los elementos repetidos se eliminan automaticamente en el print
print(conjunto) # No se pueden repetir elementos, no tiene orden, no se puede modificar



# Booleanos o Boolean

booleanoVerdadero = True
booleanoFalso = False
print(booleanoVerdadero + booleanoFalso)
 # True = 1, False = 0, por lo que el resultado es 1