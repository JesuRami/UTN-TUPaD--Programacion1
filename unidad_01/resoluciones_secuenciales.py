print("Actividad (act) 1.")
print("Hola, mundo.")
print()


print("Actividad (act) 2.")
act2_name = input("¿Cuál es tu nombre? ")
print(f"Buenos días, {act2_name}.")
print()


print("Actividad (act) 3.")
act3_name = input("Ingrese su nombre. ")
act3_last_name = input("Ingrese su apellido. ")
act3_age = input("Ingrese su edad. ")
act3_residence = input("Ingrese su lugar de residencia. ")
print(f"Mi nombre es {act3_name} {act3_last_name}, tengo {act3_age} años y vivo en {act3_residence}.")
print()


print("Actividad (act) 4.")
act4_radius = float(input("Inserte el radio de un círculo en centímetros. "))
act4_area = 3.141592653589793 * (act4_radius ** 2)
act4_perimeter = 2 * 3.141592653589793 * act4_radius
print(f"El área del círculo es {round(act4_area,2)}cm² y el perímetro es {round(act4_perimeter,2)}cm.")
print()


print("Actividad (act) 5.")
act5_seconds = int(input("Inserte una cantidad de segundos. "))
print(f"{act5_seconds} segundos son equivalentes a", round(act5_seconds/3600,2), "horas.")
print()


print("Actividad (act) 6.")
act6_num = int(input("Inserte un número entero. "))
for act6_i in range(1, 11):
    print(f"{act6_num} x {act6_i} =", act6_num * act6_i) # Pude haber copiado esta línea variando i, pero el bucle es más efectivo.
print()


print("Actividad (act) 7.")
act7_num1, act7_num2 = map(float, input("Ingrese dos números distintos a cero separándolos con un espacio. ").split())
print(f"{act7_num1} + {act7_num2} =", act7_num1 + act7_num2)
print(f"{act7_num1} - {act7_num2} =", act7_num1 - act7_num2)
print(f"{act7_num1} x {act7_num2} =", act7_num1 * act7_num2)
print(f"{act7_num1} / {act7_num2} =", round((act7_num1 / act7_num2), 2))
print()


print("Actividad (act) 8.")
act8_height = float(input("Inserte su altura en metros. "))
act8_weight = float(input("Inserte su peso en kilos. "))
print("Su IMC (índice de masa corporal) es de", round((act8_weight/(act8_height ** 2)), 2), "puntos.")
print()


print("Actividad (act) 9.")
act9_celcius = float(input("Ingrese una temperatura en Celcius. "))
print(f"{act9_celcius} grados Celcius son equivalentes a", round(((9/5) * act9_celcius + 32), 2), "grados Farenheit.")
print()


print("Actividad (act) 10.")
act10_num1, act10_num2, act10_num3  = map(float, input("Ingrese tres números separándolos con espacios. ").split())
print(f"El promedio de {act10_num1}, {act10_num2} y {act10_num3} es", round(((act10_num1 + act10_num2 + act10_num3)/3), 2))
