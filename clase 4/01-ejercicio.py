"""
Nombre_del_producto1 = input("Nombre del Producto 1: ")
cantidad_del_producto1 = float(input("Cantidad del producto: "))
precio_del_producto1 = float(input("Precio del producto: "))

Nombre_del_producto2 = input("Nombre del Producto 2: ")
cantidad_del_producto2 = float(input("Cantidad del producto: "))
precio_del_producto2 = float(input("Precio del producto: "))

Nombre_del_producto3 = input("Nombre del Producto 3: ")
cantidad_del_producto3 = float(input("Cantidad del producto: "))
precio_del_producto3 = float(input("Precio del producto: "))"""

# ejemplo para hacer pruebas

Nombre_del_producto1 = "papa"
cantidad_del_producto1 = 2222.0
precio_del_producto1 = 5


Nombre_del_producto2 = "papa"
cantidad_del_producto2 = 2222.0
precio_del_producto2 = 5


Nombre_del_producto3 = "papa"
cantidad_del_producto3= 2222.0
precio_del_producto3 = 5


"""##### Calcular el importe de IVA (21%) para cada precio_del_product #####"""

iva_producto1 = precio_del_producto1 * 0.21
iva_producto2 = precio_del_producto2 * 0.21
iva_producto2 = precio_del_producto3 * 0.21

"""##### Calcular el costo total de cada producto sin IVA #####"""

costo_total1 = precio_del_producto1 * cantidad_del_producto1
costo_total2 = precio_del_producto2 * cantidad_del_producto2
costo_total3 = precio_del_producto3 * cantidad_del_producto3

"""##### Calcular el total neto y el IVA total #####"""

neto_total = costo_total1 + costo_total2 + costo_total3
iva_total = neto_total * 0.21

"""Mostrar ticket de compra """

print("*"*60)
print("ticket de compra\n")
print(f"Producto\t Cantidad\t Precio")
print(f"{Nombre_del_producto1:16} {cantidad_del_producto1:<17} {precio_del_producto1}")
print(f"{Nombre_del_producto2:16} {cantidad_del_producto2:<17} {precio_del_producto2}")
print(f"{Nombre_del_producto3:16} {cantidad_del_producto3:<17} {precio_del_producto3}")
print("*"*60)