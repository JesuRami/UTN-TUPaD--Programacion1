# Actividad 10.
# Escribe un programa que invierta el orden de los dígitos de un número
# ingresado por el usuario.

numero = int(input("Ingrese un número a invertir en orden. "))
revertido = 0

while numero > 0:
    digito = numero % 10
    revertido = revertido * 10 + digito
    numero //= 10

print(revertido)
