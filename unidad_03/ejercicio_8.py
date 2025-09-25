# Ejercicio 8
# Solicito el nombre.
nombreUsuario = input("Hola!, Ingresa tu nombre: \n")

# Menú de opciones.
menuUsuario = input("Ingresa el numero correspondiente a como lo quieres ver: \n1.Mayúsculas \n2.Minusculas \n3.Primera mayuscula, resto minuscula\n")

# Imprime segun la eleccion del usuario.
if menuUsuario == "1": print(nombreUsuario.upper())
if menuUsuario == "2": print(nombreUsuario.lower())
if menuUsuario == "3": print(nombreUsuario.title()
