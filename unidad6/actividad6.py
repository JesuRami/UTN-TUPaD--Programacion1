# Crear una función llamada tabla_multiplicar(numero) que reciba un número como
# parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.

def tablaDeMultiplicar(numero):
    for i in range(1,10):
        print(f"{numero}x{i}={numero*i}.")

tablaDeMultiplicar(int(input("Ingrese un número. ")))
