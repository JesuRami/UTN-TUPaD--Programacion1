# Ejercicio 6.
# Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su
# media y las compare para determinar si hay sesgo
# positivo, negativo o no hay sesgo. Imprimir el
# resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print(numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if(media > mediana and mediana > moda):
    print("[Sesgo positivo o a la derecha]")
elif(media < mediana and mediana < moda):
    print("[Sesgo negativo o a la izquierda]")
elif(mediana == media and media == moda):
    print("[Sin sesgo]")
else:
    print("[Ninguna de las anteriores]")
