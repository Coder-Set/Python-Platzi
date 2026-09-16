#For para letras de un string
palabra = "Python"
for letra in palabra:
    print(letra)

#For para listas
frutas = ["Manzana", "Naranja", "Kiwi"]
for fruta in frutas:
    print(fruta)

#Break en Bucle For
marcasGuitarra = ["Fender", "Gibson", "Ibanez", "PRS", "Martin"]
for marca in marcasGuitarra:
    if marca == "Martin":
        break
    print(marca)

#Continue en Bucle For
ampliicadores = ['Fender', 'Marshall', 'PRRS', 'Mesa Bogge',  'Orange', 'Hugh & Kettner']
for amplificador in ampliicadores:
    if amplificador == "Mesa Bogge":
        continue
    print(amplificador)



print("----------------------------------------------------------------------------")


#Para que imprima solo un trozo de la condicion (Rango)
#range comenza desde cero y termina en el numero que asignemos sin incluirlo
i = 0
for i in range(6):
    print(i) #Imprime del 0 al 5

print("----------------------------------------------------------------------------")
#Para un Rango mas especifico (3, 8)
i = 1
for i in range(3, 8):
    print(i) #Imprime del 3 al 7

print("----------------------------------------------------------------------------")
for i in range(2, 10, 2):
    print(i) #Imprime del 2 al 8 de 2 en 2


print("----------------------------------------------------------------------------")
#For anidado

adjetivos = ["Saludable", "Grasosa", "Salado", "Dulce"]
comidas = ["Ensalada", "Hamburguesa", "Burrito", "Pan Dulce"]

for adjetivo in adjetivos:
	for comida in comidas:
		print(comida, adjetivo)