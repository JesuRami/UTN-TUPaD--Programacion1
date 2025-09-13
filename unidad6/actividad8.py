# 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en
# kilogramos y la altura en metros, y devuelva el índice de masa corporal.

def calcularIMC(peso, altura):
    imc = round(peso/altura**2,2)
    if imc <= 18.5:
        print(f"IMC = {imc}: Bajo.")
    elif imc <= 24.9:
        print(f"IMC = {imc}: Normal.")
    elif imc <= 29.9:
        print(f"IMC = {imc}: Sobrepeso.")
    else:
        print(f"IMC = {imc}: Obeso.")

calcularIMC(float(input("¿Cuál es su peso en kilos? ")), float(input("¿Cuál es su altura en metros? ")))
print()
