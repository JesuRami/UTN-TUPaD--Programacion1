# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3
# notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}
promedio = []
for i in range(0,3):
    nombre = input("\nIngrese el nombre del alumno. ")
    nota1, nota2, nota3 = map(int, input("Inserte sus tres notas separándolas con espacios. ").split())
    promedio.append((nota1 + nota2 + nota3)/3)
    tupla = (nota1, nota2, nota3)
    alumnos[nombre] = tupla

print()
for i in range(0,3):
    print(f"El promedio del alumno {i+1}: {promedio[i]}")
