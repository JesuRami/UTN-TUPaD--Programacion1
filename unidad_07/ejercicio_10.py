capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasíl": "Río de Janeiro", "Nicaragua": "Managua"}
print(capitales)

valores = capitales.values()
claves = capitales.keys()
capitalesInvertidas = {}


capitalesInvertidas = {valor: clave for clave, valor in capitales.items()}
print("Diccionario invertido:", capitalesInvertidas)
