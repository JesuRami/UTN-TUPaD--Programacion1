# Actividad 2.
# Desarrolla un programa que solicite al usuario un número entero y determine
# la cantidad de dígitos que contiene.
num = int(input("Ingrese un número entero. "))

#
contador = 0
while num>=1:
    num = num / 10
    contador += 1

print(f"El número contiene {contador} dígitos.")
