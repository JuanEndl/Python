frutas = []
while True:
    nombreProducto = input("ingresar el nombre del producto (s para salir): ")
    if nombreProducto.lower() == "s":
        print("carga finalizada")
        break
    precio = float(input("agrega el precio: "))

    #lista Producto
    producto = []
    producto.append(nombreProducto)
    producto.append(precio)

    frutas.append(producto)

print(frutas)