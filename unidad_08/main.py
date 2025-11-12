def crear_lista(direccion_archivo):
    sublista = []
    diccionario = {}
    lista_productos = []

    with open(direccion_archivo, "r", encoding="UTF-8") as f:
        for linea in f:
            limpio = linea.strip()
            sublista = limpio.split(",")
            diccionario = {"Nombre": sublista[0], "Precio": float(sublista[1]), "Cantidad": int(sublista[2])}
            lista_productos.append(diccionario)

    return lista_productos


def mostrar_productos(direccion_archivo, lista_productos):
    print()
    for i in lista_productos:
        print(f"Producto: {i['Nombre']} | Precio: {i['Precio']} pesos | Cantidad: {i['Cantidad']}")


def agregar_producto(direccion_archivo, lista_productos):
    print()
    producto = ""
    precio = 0.0
    cantidad = 0

    while True:
        continuar = True
        try:
            producto = input("¿Qué producto quiere añadir? ")

            if producto == "" or producto == " ":
                print("El valor ingresado está vacío. Ingrese un valor válido.")
                continue

            for i in lista_productos:
                if producto in {i['Nombre']}:
                    if input("El producto coincide (al menos parcialmente) con otro.\n¿Continuar de todas formas? ¿(s)/(n)?. ") == "s":
                        continuar = True
                    break

            if continuar == True:
                break
        except ValueError:
            print("Valor inválido. Use otro.")
        except Exception:
            print("Ha ocurrido un imprevisto. Saliendo...")
            return

    while True:
        try:
            print()
            precio = float(input("Precio individual: "))
            if precio > 0:
                break
            print("No se puede tener valores núlos o negativos. ")
        except ValueError:
            print("Valor inválido. Sólo se permiten números.")
        except Exception:
            print("Ha ocurrido un imprevisto. Saliendo...")
            return

    while True:
        try:
            print()
            cantidad = int(input("¿Cuántas unidades tiene? "))
            if cantidad > 0:
                break
            print("No tiene sentido tener cero o menos unidades.")

        except ValueError:
            print("Valor inválido. Sólo se permiten números.")
        except Exception:
            print("Ha ocurrido un imprevisto. Saliendo...")
            return

    lista_productos.append({"Nombre": producto, "Precio": precio, "Cantidad": cantidad})

    with open(direccion_archivo, "w", encoding="UTF-8") as f:
        for i in lista_productos:
            f.write(f"{i['Nombre']},{i['Precio']},{i['Cantidad']}\n")



def buscar_producto(direccion_archivo, lista_productos):
    print()
    encontrado = False
    busqueda = input("Nombre buscado: ").lower()

    with open(direccion_archivo, "r", encoding="UTF-8") as f:
        for linea in f:
            if busqueda in linea:
                print(linea.strip().split(","))
                if encontrado == False:
                    encontrado = True

    if encontrado == False:
        print(f"No se encontró {busqueda} entre los productos.")


direccion_archivo = "productos.txt"
while True:
    lista_productos = crear_lista(direccion_archivo)

    print()
    print("¿Qué quiere hacer?")
    print(" [M]ostrar productos.")
    print(" [A]ñadir producto.")
    print(" [B]uscar producto.")
    print(" [Ingrese otro para salir].")
    operacion = input("  ").lower()

    if operacion == "m":
        mostrar_productos(direccion_archivo, lista_productos)
    elif operacion == "a":
        agregar_producto(direccion_archivo, lista_productos)
        lista_productos = crear_lista(direccion_archivo)
        mostrar_productos(direccion_archivo, lista_productos)
    elif operacion == "b":
        buscar_producto(direccion_archivo, lista_productos)
    else:
        break

print()
