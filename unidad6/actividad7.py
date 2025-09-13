# 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números
# como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos,
# multiplicarlos y dividirlos.

def operacionesBasicas(a, b):
    tupla = (f"{a}+{b}={a+b}.",
             f"{a}-{b}={a-b}.",
             f"{a}*{b}={a*b}.",
             f"{a}/{b}={a/b}.")
    return tupla


tupla = operacionesBasicas(int(input("Inserte un número. ")), int(input("Inserte otro número. ")))
for i in range(0,len(tupla)):
    print(tupla[i])
