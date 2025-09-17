# Actividad 4.
# Elabora un programa que permita al usuario ingresar números enteros y los
# sume en secuencia. El programa debe detenerse y mostrar el total acumulado
# cuando el usuario ingrese un 0.

# Inicializamos las variables antes de entrar al bucle.
entrada = 1
resultado = 0

# Entramos a un bucle while que se ejecutará siempre en cuando no se ingrese un
# cero. Dentro, se sumarán repetidas veces los números ingresados, y el
# resultado será guardado en la variable resultado.
while entrada != 0:
    entrada = int(input("Inserte un número a sumar. O un 0, si quiere terminar el proceso."))

    # Condicional para evitar errores en la primera iteración del bucle.
    if resultado == 0:
        resultado = entrada
    else:
        resultado += entrada

# Mostramos el resultado una vez roto el bucle.
print(f"El total es de {resultado}.")
