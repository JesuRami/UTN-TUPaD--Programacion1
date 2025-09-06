# Ejercicio 7.
palabraUsuario = input("Ingresa una palabra: \n")

#verificacion si cumple alguna condicion
if palabraUsuario[-1].lower() in "aeiou":
    print(palabraUsuario + "!")
#Si no.
else:
    print(palabraUsuario)
