x, y, z = "Manzana", "Banana", "Cereza"
print(x, y, z)

a = b = c = d = "Fruta"

# Vamos ahora a concatenar una variable con un string desde print
e = "Zapote"
print(a, b, c, d)
print("Mi fruta favorita es " + e)

# Concatenando variables, dejando un espacio entre ellas, desde print
print(x + " " + z) 

# Reasignamos los valores de las variables d y e
d = 5
e = 6

print(d + e)
"""
Al tratarse esta vez de dos numeros, entonces  el operador + ya no concatenará sino 
que sumará los valores de las variables d y e, dando como resultado 11.
"""
