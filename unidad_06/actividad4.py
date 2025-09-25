# 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como
# parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio)
# que reciba el radio como parámetro y devuelva el perímetro del círculo.

# Importamos una librería de matemática para poder operar con pi.
import math

def calcularAreaDelCirculo(radio):
    return math.pi * radio**2

def calcularPerimetroDelCirculo(radio):
    return 2 * math.pi * radio

radio = int(input("¿Cuál es el radio del círculo? "))
print(f"El área del círculo es: {round(calcularAreaDelCirculo(radio),2)}m².")
print(f"El perímetro del círculo es: {round(calcularPerimetroDelCirculo(radio),2)}cm.")
