
# Menú de opciones
#**************************************************************************
print("*"*60) # el *60 es un multiplicador, multiplica el * 60 veces
print("Menú de Gestión de Productos\n")
print("1. Ingresar nuevos Productos")
print("2. Consultar Productos")
print("3. Modificar la cantidad de un Producto")
print("4. Eliminar Productos")
print("5. Lista completa de Productos")
print("6. Lista de productos con cantidad bajo mínimo")
print("0. Salir")
print("*"*60)
# Solicitar al usuario que seleccione una opción
#**************************************************************************

opcion = int(input("Por favor, selecciona una opción (1-0): ")) #El imput retorna un string

# Mostramos el nro de la opción seleccionada

print(f"Has seleccionado: , {opcion}")