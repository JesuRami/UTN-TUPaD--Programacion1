# 2: Crear una función llamada saludar_usuario(nombre) que reciba como
# parámetro un nombre y devuelva un saludo personalizado. Llamar a esta función
# desde el programa principal solicitando el nombre al usuario.

def saludador(nombre):
    print(f"Buenos días, {nombre}.")

saludador(nombre = input("¿Cuál es tu nombre? "))
