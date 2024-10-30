'''dejar link de  github'''

'''
    producuto
    [nombre(str),cantidad(int),precio(float)]
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

    # valida si el usuario coloca un numero o una letra
    while True:
        try:
            opcion = int(input("Por favor, selecciona una opción (0-4): "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
    
    # cierra el programa
    if opcion == 0:
        print("Nos vemos !!")
        break

    # comienza a usar el programa
    elif opcion == 1:
        print("Ingresar Producto: ")
        nombre = input("Ingresar nombre: ")

        # Validad cantidad
        while True:
            try:
                cantidad = int(input("Ingresar cantidad: "))
                break
            except ValueError:
                print("Por Favor, Ingresar un numero correcto")
            

        # Validad precio
        while True:
            try:
                precio = float(input("Ingresar precio: "))
                break
            except ValueError:
                print("Por Favor, ingresar un valir correcto")
            
                

        # crear un producto y añadirlo a la Lista
        producto = [nombre,cantidad,precio]
        productos.append(producto)

        print(f"Producto {producto[0]} agredado correctamente.\n")

    # todavia nada
    elif opcion == 2:
        print()
    # todavia nada
    elif opcion == 3:
        print()

    # muestra el listado y valida si hay algo o no
    elif opcion == 4:
        print("Listado")
        if len(productos) == 0:
            print("no hay nada")

        # si encuentra algo trae el producto y ademas valida si tiene el stock bajo o no
        else:
            print("nombre".ljust(30) + "cantidad".ljust(15) + "precio".ljust(10) + "comentario".just(20)) # -> acomoda los titulos
            for elemento in productos:
                comentario = ""
                if elemento[1] < 5: #-> revisa si tiene bajo el stock
                    comentario = "Stock Bajo" 
                print(f"{elemento[0].ljust(30)}{str(elemento[1]).ljust(15)}{str(elemento[2]).ljust(10)}{comentario.rjust(20)}")
    else:
    # Mostramos el nro de la opción seleccionada
        print(f"Has seleccionado: , {opcion}")

print("Salio del Programa")