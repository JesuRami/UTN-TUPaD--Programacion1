# Actividad 9.
#  Elabora un programa que permita al usuario ingresar 100 números enteros y
#  luego calcule la media de esos valores.

limite = int(input("Inserte la cantidad límite de iteraciones; ambos sabemos que acá no se van a colocar cien números distintos. "))

# Preguntamos un número por iteración y vamos sumando los resultados en la
# variable promedio.
for i in range(0,limite):
    numero = int(input(f"Inserte un número entero. {i+1}/{limite}. "))

    if i != 0:
        promedio += numero
    else:
        promedio = numero

# Completamos el promedio dividiendo por el número de iteraciones.
promedio /= limite

# Imprimimos el resultado.
print(f"El promedio es {promedio}.")

