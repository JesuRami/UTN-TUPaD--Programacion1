# Actividad 7.
# Crea un programa que calcule la suma de todos los números comprendidos entre
# 0 y un número entero positivo indicado por el usuario.

# Se pide el número más alto.
limite = int(input("Inserte un número entero; se sumarán todos los números enteros entre él y cero. "))

# Se suman todos los números entre los dos y se guarda el resultado en la
# variable resultado.
resultado = 0
for i in range(0, limite):
    resultado += i

print(f"El total es: {resultado}.")
