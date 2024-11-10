
# Entrega con listas de diccionarios

'''
diccionario sintaxis

{clave 1: valor 1,
 clave 2: valor 2,
 clave 4: valor 4}


var = {"nombre": "pepe" str, "cantidad": "Luis" int, "precio": 60 float } 
'''


'''
productos = [
{"nombre":"uva","cantidad":12,"precio":12,4},
{"nombre":"papa","cantidad":24,"precio":16.6},
{"nombre":"batata","cantidad":5,"precio":17},
{"nombre":"sandia","cantidad":2,"precio":3},
]

'''


# traer el color al proyecto
import color

# productos = [] #  ---> se comento para usar los "productos" pre definidos por mio descomentar para agregar todos los productos desde 0

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


while True:
    # Menú de opciones
    #**************************************************************************
    print("*"*60) # el *60 es un multiplicador, multiplica el * 60 veces
    print("Menú de Gestión de Productos\n")
    print("1. Ingresar nuevos Productos")
    print("2. Modificacion")
    print("3. Eliminar Productos")
    print("4. Lista completa de Productos")
    print("0. Salir\n")
    print("*"*60)
    #**************************************************************************

    # Solicitar al usuario que seleccione una opción
    # valida si el usuario coloca un numero o una letra
    while True:
        try:
            opcion = int(input(f"{color.LIGHT_BLUE}Por favor, selecciona una opción (0-4): {color.RESET} "))
            break
        except ValueError:
            print(f"{color.RED}Por favor, ingresa un valor correcto.{color.RESET}")
            continue
    
    # cierra el programa
    if opcion == 0:
        print("*"*60)
        print(f"\n{color.BOLD}Hasta Luego. \n{color.RESET}")
        print("*"*60)
        break

    # comienza a usar el programa
    elif opcion == 1:
        
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

        print(f"\n{color.GREEN}Producto {producto["nombre"]} agredado correctamente.\n {color.RESET}")
    
    # todavia nada
    elif opcion == 2:
        print() # Modificacion de Productos
    # todavia nada
    elif opcion == 3:
        print() # Eliminar  Productos

    # muestra el listado y valida si hay algo o no
    elif opcion == 4:
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
    else:
    # Mostramos el numero de la opción seleccionada
        print(f"{color.RED}Has seleccionado: '{opcion}', elije una opcion correcta en el rango del 0 al 4{color.RESET}")

# termina el programa
print(f"{color.LIGHT_CYAN}Termino el programa{color.RESET}")