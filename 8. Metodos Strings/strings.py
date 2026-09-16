
#Usando comillas simples y dobles para print
print("hola 'mundo'")
print('hola "mundo"')


#Uso en Ingles
ingles = "I'm Marco"
print(ingles)

#Valor de una variable en multiples lineas 
multiples = """Hola
Mundo
Desdez
Comillas
Triples"""

print(multiples)


#Metodo Length
palabra = "murcielago"
print(len(palabra))


#Metodo Include
texto = "Este curso es de Fundamentos de Python"
isIncluded = "Python" in texto
print(isIncluded)

oracion = "Aqui se encuentra Stratocaster"
print("Stratocaster" in oracion)


# Verificando si no esta incluida la palabra 
text1 = "La oracion no incluida"
isNotIncluded = "Python" not in text1
print(isNotIncluded)


#Convirtiendo texto a mayusculas
phrase = "Probando textos en Python"
mayusculas = phrase.upper()
minusculas = phrase.lower()
print(mayusculas)
print(minusculas)


#Eliminando espacios 
prueba = "       Hola     Mundo       "
sinEspacios = prueba.strip()
print(sinEspacios)
print(prueba)