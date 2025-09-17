# Actividad 8.
# Escribe un programa que permita al usuario ingresar 100 números enteros.
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos
# son impares, cuántos son negativos y cuántos son positivos.

# Inicializamos variables claves.
contadorPar = 0
contadorImpar = 0
contadorPositivo = 0
contadorNegativo = 0
limite = int(input("Inserte la cantidad límite de iteraciones; ambos sabemos que acá no se van a colocar cien números distintos. "))

# Preguntamos un número cada iteración y revisamos su positividad e imparidad.
for i in range(0,limite):
    numero = int(input(f"Inserte un número. {i+1}/{limite}. "))
    if numero < 0:
        contadorNegativo += 1
    else:
        contadorPositivo += 1
    if numero % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1

# Mostramos los resultados por pantalla.
print(f"Positivos: {contadorPositivo}.")
print(f"Negativos: {contadorNegativo}.")
print(f"Pares: {contadorPar}.")
print(f"Impares: {contadorImpar}.")
