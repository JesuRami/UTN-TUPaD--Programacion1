# Actividad 5.
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0
# y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios
# para acertar el número.

# Importamos la librería random.
import random

# Creamos una variable que contenga el número a adivinar, luego permitimos que
# el usuario trate de adivinar el número.
numeroCorrecto = random.randrange(10)
intento = int(input("Intenta adivinar un número entero del cero al nueve. "))

# Sea el número correcto o no, imprimimos el resultado por pantalla.
if intento == numeroCorrecto:
    print(f"Qué suerte: {intento} era el número correcto.")
else:
    print(f"Mala suerte: {intento} no era el número correcto, sino {numeroCorrecto}.")
