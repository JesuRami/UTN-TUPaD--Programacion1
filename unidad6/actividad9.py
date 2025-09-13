# 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una
# temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.

def convertirCelciusAFarenheit(celcius):
    return round((celcius*1.8)+32, 2)

celcius = float(input("Inserte una temperatura en grados Celcius. "))
temperatura_convertida = convertirCelciusAFarenheit(celcius)
print(f"{celcius}°C = {temperatura_convertida}°F.")
