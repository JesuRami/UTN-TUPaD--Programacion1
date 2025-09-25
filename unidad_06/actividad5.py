# 5: Crear una función llamada segundos_a_horas(segundos) que reciba una
# cantidad de segundos como parámetro y devuelva la cantidad de horas
# correspondientes.

def horasASegundos(segundos):
    print(f"{segundos} segundos son {round(segundos/3600,2)} horas.")

horasASegundos(int(input("Inserte una cantidad de segundos. ")))
