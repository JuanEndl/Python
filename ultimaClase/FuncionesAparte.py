# importar el color a la Funciones
import color
import funcionesDB

############################ conexion de la base de datos

funcionesDB.createDB()

#funcionesDB.createTable()
########################################################


# Funcion asteriscos que separan  el menu
def asterisco():
    print(f"{color.LIGHT_GREEN}{'*' * 60}{color.RESET}")

# Funcion Muestra el menu
def menu():
    print("Menú de Gestión de Productos\n")
    print("1. Ingresar nuevos Productos")
    print("2. Modificar Precio del Producto")
    print("3. Eliminar Productos")
    print("4. Lista completa de Productos")
    print("5. Mostrar todo el Stock bajo")
    print("0. Salir\n")

# Funcion que elije del 0 al 4, Solicitar al usuario que seleccione una opción y valida si el usuario coloca un numero o una letra
def opcioninicial():
    while True:
        global opcion # ---> se declara variable global para usar fuera del la funcion
        try:
            opcion = int(input(f"{color.LIGHT_BLUE}Por favor, selecciona una opción (0-5): {color.RESET} ")) # ingresa el numero

            # si elije del 0 al 4 entra en algunas de opciones disponibles
            if 0 <= opcion <= 5:

                # si elije 0 cierra todo y sale del bucle
                if opcion == 0:
                    asterisco()

                    # mensajes de saludos
                    print(f"\n{color.BOLD}Hasta Luego. \n{color.RESET}")
                    print(f"{color.LIGHT_CYAN}Termino el programa{color.RESET}")
                
                    asterisco()
                    return opcion
                return opcion
            
            # si ingresamos un numero mayor a 4 nos dice el siguiente error
            else:
                print(f"{color.RED}Por favor, ingresa un Numero correcto.{color.RESET}")

        # si no es un numero nos dice el error
        except ValueError:
            print(f"{color.RED}No se Permiten letras elija una opcion correcta del 0 al 5{color.RESET}")

'''DB'''
# Funcion opcion 1 agregar productos
def opcioniUno():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 1:
        
        print("\nIngresar el Producto: \n")
       
        #Ingresar nombre
        while True:
                nombre = input("Ingresar nombre: ")
                 # valida si es un string o no
                if nombre.isalpha(): #----> metodo "isalpha" devuelve True si todos los caracteres son alfabéticos, False de lo contrario
                    break
                else:
                    print(f"{color.RED}Por Favor, Ingresar un nombre correcto {color.RESET}")


        # Ingresar descripcion
        while True:
                descripcion = input("Ingrese el Color del Producto: ")
                 # valida si es un string o no
                if descripcion.isalpha(): #----> metodo "isalpha" devuelve True si todos los caracteres son alfabéticos, False de lo contrario
                    break
                else:
                    print(f"{color.RED}Por Favor, Ingresar una descripcion correcta {color.RESET}")

        # Ingresa Cantidad y la validad
        while True:
            try:
                cantidad = int(input("Ingresar cantidad: "))
                if cantidad > 0: # Valida si el id es mayor a 0 o no, si es correcto entra en el break y sale
                    break
                else:
                    print(f"{color.RED}Ingrese un número mayor a 0.{color.RESET}")
            except ValueError:
                print(f"{color.RED}Por Favor, Ingresar un valor correcto{color.RESET}")
            
       # Ingresa Precio y la validad
        while True:
            try:
                precio = float(input("Ingresar precio: "))
                if precio > 0: # Valida si el id es mayor a 0 o no, si es correcto entra en el break y sale
                    break
                else:
                    print(f"{color.RED}Por Favor, Ingresar un valor correcto{color.RESET}")
            except ValueError:
                print(f"{color.RED}Por Favor, ingresar un valor correcto {color.RESET}")
            
        # crear un producto y lo añade a la lista en forma de diccionario
        try:
            funcionesDB.insertRow(nombre, descripcion, cantidad, precio)  # Llama a la función para insertar en la base de datos
            print(f"\n{color.GREEN}Producto {nombre} agregado correctamente a la base de datos.{color.RESET}")
        except Exception as e:
            print(f"{color.RED}Error al agregar el producto a la base de datos: {e}{color.RESET}")

'''DB'''
# Función opción 2 modificar Productos
def opcionDos():
    global productos  # ---> Se declara variable global para usar fuera de la función
    if opcion == 2:

        # Solicita el ID del producto a modificar y Valida si el ID es ingresado correctamente
        while True:
            try:
                id = int(input("\nIngresa el id del producto a modificar: "))

                # Verifica si el ID existe en la base de datos
                datos_db = funcionesDB.readRows()
                producto_existente = any(row[0] == id for row in datos_db)

                if not producto_existente:
                    print(f"{color.RED}No se encontró un producto con el ID {id}. Elegir la opción 4 para encontrar el ID.{color.RESET}")
                    return  # Finaliza la función si no encuentra el ID
                else:
                    print(f"{color.GREEN}Producto con ID {id} encontrado.{color.RESET}\n")
                    break  # Sale del bucle si encuentra el ID válido
            except ValueError:
                print(f"{color.RED}Ingresa un número válido.{color.RESET}")

        # Solicita la nueva cantidad del producto
        while True:
            try:
                cantidad = int(input("Ingresa la nueva cantidad: "))
                if cantidad >= 0:  # Valida que la cantidad sea positiva
                    break
                else:
                    print(f"{color.RED}La cantidad no puede ser negativa.{color.RESET}")
            except ValueError:
                print(f"{color.RED}Por favor, ingresa un número válido para la cantidad.{color.RESET}")

        # Llama a la función que actualiza la base de datos
        if funcionesDB.updateRow(cantidad, id):
            print(f"{color.GREEN}Producto con ID {id} modificado correctamente.{color.RESET}")

        # Actualiza la lista de productos en memoria después de la modificación
        datos_db = funcionesDB.readRows()
        productos = [
            {"id": row[0], "nombre": row[1], "cantidad": row[2], "precio": row[3]}
            for row in datos_db
        ]

'''DB'''
# Funcion opcion 3 eliminar Productos
def opcionTres():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 3:
        while True: # ---> valida si el id es ingresado correctamente
            try:
                id = int(input("\nIngresa el id del producto a Borrar: ")) # ---> guardo el dato ingresado en la variable idProductos
                break
            except ValueError:
                print(f"{color.RED}ingresa un nuemero{color.RESET}")


        funcionesDB.deleteRow(id)

        # Actualiza la lista de productos después de la eliminación
        datos_db = funcionesDB.readRows()
        productos = [
            {"id": row[0], "nombre": row[1], "cantidad": row[2], "precio": row[3]}
            for row in datos_db
        ]

'''DB'''
# Funcion opcion 4 muestra el listado de los Productos
def opcioncuatro():
    global productos  # Accede a la lista global de productos

    print(f"{color.LIGHT_WHITE}\nListado de Productos\n{color.RESET}")

    # Actualiza la lista de productos desde la base de datos
    datos_db = funcionesDB.readRows() 


    productos = [ # recorre cada fila de la DB (datos_db) 
        {"id": row[0], "nombre": row[1], "descripcion": row[2],"cantidad": row[3], "precio": row[4]}
        for row in datos_db 
    ]

    if len(productos) == 0:
        print(f"{color.LIGHT_RED}No hay productos en la base de datos.{color.RESET}")
    else:
        print(
            f"{color.LIGHT_PURPLE}id{color.RESET}".ljust(30) +
            f"{color.LIGHT_PURPLE}Nombre{color.RESET}".ljust(30) +
            f"{color.LIGHT_PURPLE}Descripcion{color.RESET}".ljust(30) +
            f"{color.LIGHT_PURPLE}Cantidad{color.RESET}".ljust(30) +
            f"{color.LIGHT_PURPLE}Precio{color.RESET}".ljust(27) +
            f"{color.LIGHT_PURPLE}Comentario{color.RESET}"
        )  # Títulos de la tabla
        for elemento in productos:
            comentario = ""
            if elemento["cantidad"] < 5:  # Revisa si tiene bajo stock
                comentario = "Stock Bajo"
            print(
                f"{str(elemento['id']).ljust(19)}"
                f"{elemento['nombre'].ljust(21)}"
                f"{elemento['descripcion'].ljust(21)}"
                f"{str(elemento['cantidad']).ljust(17)}"
                f"{str(elemento['precio']).ljust(14)}{comentario}"
            )

# Funcion opcion 5 muestra el listado de los Productos que tienen bajo stock
def opcioncinco():
    if opcion == 5:
        global productos  # Accede a la lista global de productos

        print (f"{color.LIGHT_WHITE}\nListado de Productos Bajo Stock\n{color.RESET}")
    
        datos_db = funcionesDB.readRowslow()

        productos = [ # recorre cada fila de la DB (datos_db) 
        {"id": row[0], "nombre": row[1], "descripcion": row[2], "cantidad": row[3], "precio": row[4]}
        for row in datos_db 
    ]
        if len(productos) == 0:
            print(f"{color.LIGHT_RED}No hay productos con bajo stock.{color.RESET}")
            return
        
        else:
            print(
                f"{color.LIGHT_PURPLE}id{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}Nombre{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}Descripcion{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}Cantidad{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}Precio{color.RESET}".ljust(25) +
                f"{color.LIGHT_PURPLE}Comentario{color.RESET}"
                ) #----> el titulo del ticket acomodado


        for elemento in productos:
            if elemento["cantidad"] < 5:  # Solo imprime si tiene bajo stock

                comentario = "Stock bajo"
                print(
                    f"{str(elemento['id']).ljust(19)}"
                    f"{elemento['nombre'].ljust(21)}"
                    f"{elemento['descripcion'].ljust(21)}"
                    f"{str(elemento['cantidad']).ljust(17)}"
                    f"{str(elemento['precio']).ljust(12)}{comentario}"
                )
