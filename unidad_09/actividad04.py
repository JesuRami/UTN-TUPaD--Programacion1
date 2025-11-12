def convertir_a_binario(decimal):
    if decimal < 2:
        return str(decimal)
    else:
        res = decimal%2
        resultado = str(res)
        decimal = int(decimal/2)
    return convertir_a_binario(decimal)+ resultado

while True:
    try:
        decimal = int(input("¿Qué decimal quiere convertir a binario? "))
        if decimal < 0:
            print("El número debe ser positivo. Pruebe de nuevo.")
            print()
            continue

        print(f"    {decimal} en binario es: {convertir_a_binario(decimal)}.")
        print()
        break
    except ValueError:
        print("Usted ha ingresado un valor incorrecto. Sólo se permiten números naturales. Pruebe otra vez.")
        continue
    except Exception:
        print("Ha ocurrido un imprevisto. Cancelando ejecución...")
        print()
        break
