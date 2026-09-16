# Slicing (Cortar una cadena de texto)
texto = "Este es un texto"
print(texto[3])
print(texto[3:10])

print(texto[0]) #Demostrando que el primer caracter es el 0




# Replace (Reemplazar una cadena de texto)
curso = "Este es un curso de JavaScript"
cursoCorrecto = (curso.replace("JavaScript", "Python")) #Reemplaza JavaScript por Python
print(cursoCorrecto)
# En este ejemplO, Almacenamos la nueva cadena en una variable aparte

incorrect = "El curso es de Backend"
print(incorrect.replace("Backend", "Base de Datos")) #Reemplaza Backend por Python
# En este ejempolo, No almacenamos la nueva cadena en una variable aparte, sino que la imprimimos directamente.





# Split (Separar una cadena de texto)
parrafo = "Este texto nos sirve para la prueba de .slice()"
parrafoDividido = parrafo.split(" ")
print(parrafoDividido)

