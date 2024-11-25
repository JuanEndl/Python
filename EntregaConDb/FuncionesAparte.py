# importar el color a la Funciones
import color

# productos = [] # --> se comento para usar los "productos" pre definidos por mio descomentar para agregar todos los productos desde 0

# productos pre definidos por mi, "comentados"
'''productos = [
    {
        "id": 1,
        "nombre":"uva",
        "cantidad":12,
        "precio":12.4
    },
    {
        "id": 2,
        "nombre":"papa",
        "cantidad":24,
        "precio":16.6
    },
    {
        "id": 3,
        "nombre":"batata",
        "cantidad":5,
        "precio":17
    },
    {
        "id": 4,
        "nombre":"sandia",
        "cantidad":2,
        "precio":3
    },
]
'''



# Funcion asteriscos que separan  el menu
def asterisco():
    print(f"{color.LIGHT_GREEN}{'*' * 60}{color.RESET}")

# Funcion Muestra el menu
def menu():
    print("Menú de Gestión de Productos\n")
    print("1. Ingresar nuevos Productos")
    print("2. Modificacion")
    print("3. Eliminar Productos")
    print("4. Lista completa de Productos")
    print("0. Salir\n")

# Funcion que elije del 0 al 4, Solicitar al usuario que seleccione una opción y valida si el usuario coloca un numero o una letra
def opcioninicial():
    while True:
        global opcion # ---> se declara variable global para usar fuera del la funcion
        try:
            opcion = int(input(f"{color.LIGHT_BLUE}Por favor, selecciona una opción (0-4): {color.RESET} ")) # ingresa el numero

            # si elije del 0 al 4 entra en algunas de opciones disponibles
            if 0 <= opcion <= 4:

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
            print(f"{color.RED}No se Permiten letras elija una opcion correcta del 0 al 4{color.RESET}")

# Funcion opcion 1 agregar productos
def opcioniUno():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 1:
        
        print("\nIngresar el Producto: \n")
       
        while True:
            # Ingresa el ID y lo valida 
            try:
                id = int(input("Ingresar id: ")) # si es un id correcto sale, si no va al error
                if id > 0: # Valida si el id es mayor a 0 o no, si es correcto entra en el break y sale
                    break
                else:
                    print(f"{color.RED}Coloca un Id que sea mayor a 0{color.RESET}")
            except ValueError:
                print(f"{color.RED}Por Favor, ingresar un valor correcto{color.RESET}")

        while True:
                nombre = input("Ingresar nombre: ")
                 # valida si es un string o no
                if nombre.isalpha(): #----> metodo "isalpha" devuelve True si todos los caracteres son alfabéticos, False de lo contrario
                    break
                else:
                    print(f"{color.RED}Por Favor, Ingresar un nombre correcto {color.RESET}")

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
        producto = {
            "id" : id,
            "nombre" : nombre,
            "cantidad" : cantidad,
            "precio" : precio
        }

        print(producto)  # ---> muestro en consola lo que se agrego para saber como lo agrego al diccionario

        productos.append(producto) #---> el metodo "append" añade un elemento al final del diccionario.

        print(f"\n{color.GREEN}Producto {producto['nombre']} agregado correctamente.\n {color.RESET}")

# Funcion opcion 2 modicar Productos
def opcioniDos():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 2:
        while True: # ---> valida si el id es ingresado correctamente
            try:
                idProducto = int(input("\nIngresa el id del producto a modificar: ")) # ---> guardo el dato ingresado en la variable idProductos
                break
            except ValueError:
                print(f"{color.RED}ingresa un nuemero{color.RESET}")

        idEncontrado = False # --->  Variable para verificar si se encontró el producto   "Bandera" (siempre se utiliza con un false)

        for  elemento in productos: # ---> recorre cada elemento de lista, cada elemento es un diccionario dentro de la variable Productos

            if idProducto == elemento["id"]: # ---> consulto si la variable agregada por el usuario se encuentra en los elementos del diccionario y valida

                # muestra el precio viejo y si se comple la condicion se modifica el precio 
                nuevoPrecio = float(input(f"\nPrecio Actual: {color.RED}{elemento['precio']}{color.RESET} ingresa el nuevo precio: ")) # --> se ingresa el precio

                elemento["precio"] = nuevoPrecio # --> se modifica el precio y se guarda en la variable nuevoPrecio

                print(f"\n{color.GREEN}Precio actualizado a: {nuevoPrecio}{color.RESET}") # --> se imprime en la pantalla la variable nueva con el precio

                # Si el producto fue encontrado sale 
                idEncontrado = True  # "Bandera" 
                break
        
        # Si no se encontró el producto, muestra un mensaje
        if not idEncontrado:
            print(f"{color.LIGHT_RED}ID no encontrado. Si no te acuerdas el ID, presiona 4 para ver la lista de productos.{color.RESET}")

# Funcion opcion 2 eliminar Productos
def opcionTres():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 3:
        while True: # ---> valida si el id es ingresado correctamente
            try:
                idProducto = int(input("\nIngresa el id del producto a Borrar: ")) # ---> guardo el dato ingresado en la variable idProductos
                break
            except ValueError:
                print(f"{color.RED}ingresa un nuemero{color.RESET}")

        idEncontrado = False # --->  Variable para verificar si se encontró el producto   "Bandera" (siempre se utiliza con un false)

        for  elemento in productos: # ---> recorre cada elemento de lista, cada elemento es un diccionario dentro de la variable Productos

            if idProducto == elemento["id"]: # ---> consulto si la variable agregada por el usuario se encuentra en los elementos del diccionario y valida
                
                productos.remove(elemento) # ---> elimina el producto completo de la Lista

                print(f"\n{color.GREEN}Se borro el producto con el id: {idProducto}{color.RESET}") # --> se imprime en la pantalla la variable nueva con el precio

                # Si el producto fue encontrado sale 
                idEncontrado = True  # "Bandera" 
                break
        
        # Si no se encontró el producto, muestra un mensaje
        if not idEncontrado:
            print(f"{color.LIGHT_RED}ID no encontrado. Si no te acuerdas el ID, presiona 4 para ver la lista de productos.{color.RESET}")

# Funcion opcion 4 muestra el listado de los Productos
def opcioncuatro():
    if opcion == 4:
        print(f"{color.LIGHT_WHITE}\nListado de Productos\n{color.RESET}")
    if len(productos) == 0:
            print("no hay nada")

        # si encuentra algo trae el producto y ademas valida si tiene el stock bajo o no
    else:
            print(
                f"{color.LIGHT_PURPLE}id{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}nombre{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}cantidad{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}precio{color.RESET}".ljust(25) +
                f"{color.LIGHT_PURPLE}comentario{color.RESET}"
                ) #----> el titulo del ticket acomodado
            for elemento in productos: # se utiliza el bucle for
                comentario = ""
                if elemento["cantidad"] < 5: #-> revisa si tiene bajo el stock
                    comentario = "Stock Bajo" 
                print(f"{str(elemento["id"]).ljust(19)}"
                      f"{elemento["nombre"].ljust(22)}"
                      f"{str(elemento["cantidad"]).ljust(17)}"
                      f"{str(elemento["precio"]).ljust(13)}{comentario}") #----> muestra la lista de productos
