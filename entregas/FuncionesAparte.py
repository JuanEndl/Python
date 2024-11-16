# importar el color a la funciones
import color

# productos = [] # --> se comento para usar los "productos" pre definidos por mio descomentar para agregar todos los productos desde 0


# productos pre definidos por mi
productos = [
    {
        "nombre":"uva",
        "cantidad":12,
        "precio":12.4
    },
    {
        "nombre":"papa",
        "cantidad":24,
        "precio":16.6
    },
    {
        "nombre":"batata",
        "cantidad":5,
        "precio":17
    },
    {
        "nombre":"sandia",
        "cantidad":2,
        "precio":3
    },
]


# funcion asteriscos que separan  el menu
def asterisco():
    print(f"{color.LIGHT_GREEN}{'*' * 60}{color.RESET}")

# funcion Muestra el menu
def menu():
    print("Menú de Gestión de Productos\n")
    print("1. Ingresar nuevos Productos")
    print("2. Modificacion")
    print("3. Eliminar Productos")
    print("4. Lista completa de Productos")
    print("0. Salir\n")



# funcion que elije del 0 al 4, Solicitar al usuario que seleccione una opción y valida si el usuario coloca un numero o una letra
def opcioninicial():
    while True:
        global opcion # ---> se declara variable global para usar fuera del la funcion
        try:
            opcion = int(input(f"{color.LIGHT_BLUE}Por favor, selecciona una opción (0-4): {color.RESET} ")) # ingresa el numero

            # si elije del 0 al 4 entra en algunas de opciones
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
            print(f"{color.RED}No se Permiten letras elije una opcion correcta del 0 al 4{color.RESET}")


# opcion 1
def opcioniUno():
    global productos # ---> se declara variable global para usar fuera del la funcion
    if opcion == 1:
        
        print("\nIngresar Producto: ")
        # valida si es un string o no
        while True:    
                nombre = input("\nIngresar nombre: ")
                if nombre.isalpha(): #----> metodo "isalpha" devuelve True si todos los caracteres son alfabéticos, False de lo contrario
                    break
                else:
                    print(f"{color.RED}Por Favor, Ingresar un nombre correcto {color.RESET}")

        # Validad cantidad
        while True:
            try:
                cantidad = int(input("Ingresar cantidad: "))
                break
            except ValueError:
                print(f"{color.RED}Por Favor, Ingresar un valor correcto {color.RESET}")
            
        # Validad precio
        while True:
            try:
                precio = float(input("Ingresar precio: "))
                break
            except ValueError:
                print(f"{color.RED}Por Favor, ingresar un valor correcto {color.RESET}")
            
        # crear un producto y añadirlo a la Lista en forma de diccionario
        producto = {
            "nombre" : nombre,
            "cantidad" : cantidad,
            "precio" : precio
        }

        print(producto)  # ---> muestro en consola lo que se agrego para saber como lo agrego al diccionario

        productos.append(producto) #---> el metodo "append" añade un elemento al final del diccionario.

        print(f"\n{color.GREEN}Producto {producto['nombre']} agregado correctamente.\n {color.RESET}")

# opcion 4
def opcioniCuatro():
    if opcion == 4:
        print("Listado\n")
    if len(productos) == 0:
            print("no hay nada")

        # si encuentra algo trae el producto y ademas valida si tiene el stock bajo o no
    else:
            print(
                f"{color.LIGHT_PURPLE}nombre{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}cantidad{color.RESET}".ljust(30) +
                f"{color.LIGHT_PURPLE}precio{color.RESET}".ljust(25) +
                f"{color.LIGHT_PURPLE}comentario{color.RESET}"
                ) #----> el titulo del ticket acomodado
            for elemento in productos: # se utiliza el bucle for
                comentario = ""
                if elemento["cantidad"] < 5: #-> revisa si tiene bajo el stock
                    comentario = "Stock Bajo" 
                print(f"{elemento["nombre"].ljust(22)}{str(elemento["cantidad"]).ljust(17)}{str(elemento["precio"]).ljust(13)}{comentario}") #----> muestra la lista de productos
