'''dejar link de  github'''

'''
    producuto
    [nombre(str),precio(float),cantidad(int)]
'''

productos = []


while True:
    # Menú de opciones
    #**************************************************************************
    print("*"*60) # el *60 es un multiplicador, multiplica el * 60 veces
    print("Menú de Gestión de Productos\n")
    print("1. Ingresar nuevos Productos")
    print("2. Modificacion")
    print("3. Eliminar Productos")
    print("4. Lista completa de Productos")
    print("0. Salir")
    print("*"*60)
    # Solicitar al usuario que seleccione una opción
    #**************************************************************************

    opcion = int(input("Por favor, selecciona una opción (1-0): "))

    if opcion == 0:
        print("Nos vemos !!")
        break
    elif opcion == 1:
        print("Ingresar Producto: ")
        nombre = input("Ingresar nombre: ")
        cantidad = int(input("Ingresar cantidad: "))
        precio = float(input("Ingresar precio: "))


            # se arma el producto

        producto = [nombre,cantidad,precio]
        productos.append(producto)

    elif opcion == 2:
        print()
    elif opcion == 3:
        print()
    elif opcion == 4:
        print("Listado")
        if len(productos) == 0:
            print("no hay nada")
        else:
            print("nombre".ljust(30) + "precio".ljust(15) + "cantidad".ljust(10) + "comentario".ljust(10)) # -> acomoda los titulos 
            for elemento in productos:
                comentario = ""
                if producto[2] < 5: #-> revisa si tiene bajo el stock
                    comentario = "Bajo" 
                print(f"{elemento[0].ljust(30)}{str(elemento[1].ljust(15))}{elemento[2].ljust(10)}{comentario.ljust(10)}")
    else:
    # Mostramos el nro de la opción seleccionada
        print(f"Has seleccionado: , {opcion}")

print("Salio del Programa")