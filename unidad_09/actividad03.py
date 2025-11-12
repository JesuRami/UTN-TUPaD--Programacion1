def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)


while True:
    try:
        base = int(input("Ingrese la base: "))
        if base < 0:
            print("Solo se permiten números positivos y cero.")
            print()
            continue
        print()
        break
    except ValueError:
        print("Sólo se permiten números enteros. Pruebe otra vez.")
        print()
        continue
    except Exception:
        print("Ocurrió un imprevisto.")
        print()
        continue

while True:
    try:
        exponente = int(input("Ingrese el exponente: "))
        if exponente < 0:
            print("Solo se permiten números positivos y cero.")
            print()
            continue
        print()
        break
    except ValueError:
        print("Sólo se permiten números enteros. Pruebe otra vez.")
        print()
        continue
    except Exception:
        print("Ocurrió un imprevisto.")
        print()
        continue

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")
print()
