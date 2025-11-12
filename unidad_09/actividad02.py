def calcular_posicion_fibonacci(posicion):
        if posicion <= 0:
            return 0
        elif posicion == 1:
            return 1
        else:
            return calcular_posicion_fibonacci(posicion-1) + calcular_posicion_fibonacci(posicion-2)

while True:
    try:
        posicion = int(input("Ingrese un número natural. "))
        if posicion < 0:
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

    print(f"#{posicion} = {calcular_posicion_fibonacci(posicion)}")
    print()

    if input("¿Quiere hacer otro cálculo? [S]í/[N]o. ").lower() == "n":
        print("Saliendo...")
        print()
        break
    print()
