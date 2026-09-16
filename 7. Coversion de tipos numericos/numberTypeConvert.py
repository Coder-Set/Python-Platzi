x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))


positivo = 5
negativo = -5
decNeg = -5.5

imagine = 5 + 1j
imagine2 = -5.5 + 2j

# la primer variable x = 1 se necesita convertir a flotante
# El resultado se guarda en una nueva variable "xf"

xf = float(x)
print(type(xf))

print(xf) # Haciendo print a la nueva variable modificada 
# Nos dara un resultado de 1.0, antes la variable era 1 pero lo convertimos a flotante



# Ahora vamos a castear (pasar la segunda variable y = 2.5) a entero, para eso utilizamos la funcion int()

yi = int(y)
print(type(yi))
print(yi)


entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))

# Generar numero aleario en python
import random
print(random.randrange(1, 900))
import  math