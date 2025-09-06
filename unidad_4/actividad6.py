# Actividad 6.
# Desarrolla un programa que imprima en pantalla todos los números pares
# comprendidos entre 0 y 100, en orden decreciente.

# Realizamos un bucle for que pase, número por número, verificando si el resto
# del número divido por dos es 0. Lo imprime en caso de que sí; lo ignora en
# caso de que no.
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
