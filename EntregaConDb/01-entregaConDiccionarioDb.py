# importaciones de archivos
import FuncionesAparte # traer el funciones al proyecto

while True:
    # Muestra el menu de opciones
 
    FuncionesAparte.asterisco() # esta Funcion trae del modulo FuncionesAparte la funcion asterisco que es un multiplicador de *
    FuncionesAparte.menu() #esta Funcion trae del modulo FuncionesAparte la Funcion que muestra el menu
    FuncionesAparte.asterisco()


    # Esta Funcion trae del modulo FuncionesAparte la funcion inicial que elije del 0 al 4
    # Solicitar al usuario que seleccione una opción
    # valida si el usuario coloca un numero o una letra
    opcion = FuncionesAparte.opcioninicial()


    # comienza a usar el programa de acuerdo a la opcion elegida

    # cierra el programa
    if opcion == 0:
        break

    # si elije la opcion 1 accede a la funcion "opcionUno" que se encuentra en FuncionesAparte
    elif opcion == 1:
        FuncionesAparte.opcioniUno()
    
    # Modificacion del producto
    elif opcion == 2:
        FuncionesAparte.opcioniDos()
    
    # Elimina un producto entero de la Lista (diccionario)
    elif opcion == 3:
        FuncionesAparte.opcionTres()

    # muestra el listado y valida si hay algo o no
    elif opcion == 4:
        FuncionesAparte.opcioncuatro()
    
    # Mostrar todo los productos bajos en stock
    elif opcion == 5:
        FuncionesAparte.opcioncinco()

# termina el programa
