# Actividad 3.
# Escribe un programa que sume todos los números enteros comprendidos entre dos
# valores dados por el usuario, excluyendo esos dos valores.

# Pedimos ambos números.
num1, num2 = map(int, input("Inserte dos números enteros separándolos con un espacio. ").split())

# Verificamos cuál es el mayor.
if num2 > num1:
    i = num1
    f = num2
else:
    i = num2
    f = num1

# Usamos un for para mostrar, uno por uno, los números entre los dos.
for i in range(i+1, f):
    print(i)
    i += 1
