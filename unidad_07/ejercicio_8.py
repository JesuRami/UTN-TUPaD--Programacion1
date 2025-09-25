# Armá un diccionario donde las claves sean nombres de productos y los valores
# su stock. Permití al usuario:
#    -Consultar el stock de un producto ingresado.
#    -Agregar unidades al stock si el producto ya existe.
#    -Agregar un nuevo producto si no existe.

inventario = {"Relój": 5,
              "Par de anillos": 4,
              "Bufanda": 3,
              "Corbata": 2,
              "Paragüas": 1}

productoBuscado = input("¿Qué objeto busca? ")
if productoBuscado in inventario:
    print(f"Stock: {inventario.get(productoBuscado)}.\n")

    if input("¿Quiere añadir más unidades a este producto? (S)í. ").lower() == "s":
        inventario[productoBuscado] += int(input(f"¿Cuántas? "))
        print(f"Añadidas {inventario[productoBuscado]} unidades.\n")
    else:
        print("No se añadirá ninguna.")

else:
    if input("No sé encontró el producto. ¿Quiere añadirlo? (S)í. "):
        inventario[productoBuscado] = int(input(f"\n¿Cuántas unidades piensa ingresar? "))
        print()

print(f"{inventario}")
