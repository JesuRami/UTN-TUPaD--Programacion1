# Pasar los valores clave de precios_frutas a una lista.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Inventario de frutas: \n{precios_frutas}\n")

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas["Banana"] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Inventario de frutas actualizado: \n{precios_frutas}\n")

lista = list(precios_frutas)
print(f"Únicamente las frutas: \n{lista} \n")
