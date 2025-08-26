'''
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''

actividad4_edad = int(input("Ingrese su edad. "))
if actividad4_edad > 0: # Pedimos la edad del usuario y pedimos la edad máxima de la categoría más baja, una por una.
    if actividad4_edad < 12:
        print("Niño: menores de 12 años.")
    elif actividad4_edad < 18:
        print("Adolescente: mayor de 11 años y menor de 18 años.")
    elif actividad4_edad < 30:
        print("Adulto joven: mayor de 17 años y menor de 30.")
    else:
        print("Adulto mayor: mayor de treinta años.")
else:
    print("Edad inválida.")
