# Dado un diccionario de frutas y precios, añadir más frutas y precios.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas, '\n')

precios_frutas['Naranja'] = 1200
precios_frutas.update({'Manzana': 1500})
precios_frutas.update({'Pera': 2300})

print(precios_frutas, '\n')
