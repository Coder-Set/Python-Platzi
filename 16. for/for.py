#Fr para letras de un string
palabra = "Python"
for letra in palabra:
    print(letra)

#FFor para listas
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
