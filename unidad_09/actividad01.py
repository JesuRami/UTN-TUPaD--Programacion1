def calcular_factorial(num):
        if num == 0:
            return 1
        else:
            return num * calcular_factorial(num-1)

while True:
    try:
        num = int(input("Ingrese un número natural. "))
        if num < 0:
            print("Solo se permiten números positivos y cero.")
            print()
            continue

    except ValueError:
        print("Sólo se permiten números enteros. Pruebe otra vez.")
        print()
        continue
    except Exception:
        print("Ocurrió un imprevisto. Interrumpiendo el programa...")
        print()
        break

    for i in range(0,num+1):
        print(f"{i}!: {calcular_factorial(i)}.")
    print()

    if input("¿Quiere hacer otro cálculo? [S]í/[N]o. ").lower() == "n":
        print("Saliendo...")
        print()
        break
    print()
