# Solicita al usuario una frase e imprime:
#   -Las palabras únicas (usando un set).
#   -Un diccionario con la cantidad de veces que aparece cada palabra.

# Determina la frase (convertida en minúsculas) con la que se va a empezar.
frase = input("Ingrese una cadena de caractéres. ").lower()

# Ahora vamos, carácter por carácter, verificando si es alfanumérico (o un
# espacio): si no, lo ignoramos.
fraseLimpia = ""
for i in range(0, len(frase)):
    if frase[i].isalnum() or frase[i].isspace():
        fraseLimpia += frase[i]
listPalabras = list(fraseLimpia.split())

dicPalabras = {}

# Pasamos las palabras, una por una, a un diccionario.
for i in range(0, len(listPalabras)):
    palabra = listPalabras[i]
    if palabra in dicPalabras:
        dicPalabras[palabra] += 1
    else:
        dicPalabras[palabra] = 1

# Copiamos el contenido del diccionario en un set.
setPalabras = set(dicPalabras)

print(dicPalabras)
print(setPalabras)
