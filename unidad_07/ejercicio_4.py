# Escribí un programa que permita almacenar y consultar números telefónicos.
#   -Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#   -Luego, pedí un nombre y mostrale el número asociado, si existe.

registroNumeros = {}

opcion = "s"
while opcion.lower() == "s":
    opcion = input("¿Añadir un contacto? ¿S/N? ")
    if opcion.lower() != "s":
        break

    nombre = input("Ingrese el nombre del contacto. ")
    numero = int(input("Ingrese el número del contacto. "))
    print()

    registroNumeros.update({nombre: numero})

print(f"\n {registroNumeros}\n")
if input("¿Quiere buscar el número de algún contacto? ¿S/N? ").lower() == "s":
    nombreBuscado = input("¿Cuál? ")

    if nombreBuscado not in registroNumeros:
        print(f"\n'{nombreBuscado}' no existe en la lista. Ésta es la lista:\n {registroNumeros}")
    else:
        print(f"\nEl número de {nombreBuscado} es {registroNumeros[nombreBuscado]}.")
