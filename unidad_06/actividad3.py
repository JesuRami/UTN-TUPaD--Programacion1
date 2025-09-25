# 3: Crear una función llamada informacion_personal(nombre, apellido, edad,
# residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido],
# tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y
# llamar a esta función con los valores ingresados.

def presentacion(nombre, apellido, edad, residencia):
    print(f"Mi nombre es {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("Ingrese su nombre, apellido, años de edad y residencia.")
nombre, apellido, edad, residencia = map(str, input("Separa cada uno con espacios, sin caractéres que no sean alfanuméricos. ").split(" "))

presentacion(nombre, apellido, edad, residencia)
