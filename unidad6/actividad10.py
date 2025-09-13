# 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres
# números como parámetros y devuelva el promedio de ellos. Solicitar los
# números al usuario y mostrar el resultado usando esta función.

def promediar(a,b,c):
    return round((a+b+c)/3, 2)

a, b, c = map(float, input("Inserte tres números a promediar, separándolos con espacios. ").split())
promedio = promediar(a,b,c)
print(f"El promedio es {promedio}.")
