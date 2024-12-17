
import color
import sqlite3 as sql
import os

# crea la DB y si existe no la crea
def createDB():
    db_path = os.path.join("ultimaClase", "productos.db")  # Definir la ruta de la base de datos

    # Verificar si la base de datos ya existe
    if os.path.exists(db_path):
        print(f"La base de datos ya existe en la ruta: {db_path}")
    else:
    
        # Crear la base de datos si no existe
        try:
            os.makedirs("ultimaClase", exist_ok=True)  # Asegura que la carpeta exista
            conn = sql.connect(db_path)  # Hace la conexión con la ruta de la DB

            print(f"{color.GREEN}Base de datos creada exitosamente en la ruta: {db_path}{color.RESET}") # muestra el mensaje de creacion de la  DB exitoso

            conn.commit()
            conn.close()  # Cierra la conexión

        except Exception as i:
            print(f"{color.RED}Error al crear la base de datos: {i}{color.RESET}")

'''def createTable():

    db_path = os.path.join("ultimaClase", "productos.db") # Definir la ruta de la base de datos 
    
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """ Create table productos(
            id integer primary key autoincrement,
            nombre text not null,
            cantidad intager not null,
            precio real not null
        )"""
    )
    conn.commit()
    conn.close()
'''

# insertar fila (opcion 1)
def insertRow(nombre, cantidad, precio):

    db_path = os.path.join("ultimaClase", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agrega lo que ya le defino por query
    query = f"""insert into productos (nombre, cantidad, precio) 
                      values ('{nombre}', {cantidad}, {precio})""" # instruccion guardada para ejecutarla con el cursor.execute
                                                        # agrega los valores colocados a la db

    cursor.execute(query) # ejecuta la instraccion declarada arriba 

    conn.commit()
    conn.close()

# insertar fila (opcion 2)
def updateRow(cantidad, id):
    db_path = os.path.join("ultimaClase", "productos.db")

    try:
        # Conectar a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Actualiza la cantidad en la base de datos
        query = "UPDATE productos SET cantidad = ? WHERE id = ?"
        cursor.execute(query, (cantidad, id))

        # Verificar si realmente se actualizó la fila
        if cursor.rowcount == 0:
            print(f"{color.RED}No se encontró un producto con el ID {id}.{color.RESET}")
        else:
            print(f"{color.GREEN}Producto con ID {id} modificado correctamente.{color.RESET}")

        # Guardar cambios y cerrar conexión
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"{color.RED}Error al modificar la cantidad: {e}{color.RESET}")

# borrar fila por ID (opcion 3)
def deleteRow(id):
    db_path = os.path.join("ultimaClase", "productos.db")  # Ruta de la base de datos

    try:
        conn = sql.connect(db_path)  # Conexión a la base de datos
        cursor = conn.cursor()

        # Ejecuta el DELETE con un parámetro para evitar SQL Injection
        query = "DELETE FROM productos WHERE id = ?"
        cursor.execute(query, (id,))

        # Verifica si se eliminó alguna fila
        if cursor.rowcount == 0:
            print(f"No se encontró un producto con el ID {id}.")
        else:
            print(f"Producto con ID {id} eliminado correctamente.")

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

# mostrar toda la tabla (opcion 4)
def readRows():

    db_path = os.path.join("ultimaClase", "productos.db")

    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        instruccion = "SELECT * FROM productos"  # Trae todos los datos de la tabla productos
        cursor.execute(instruccion)
        datos = cursor.fetchall()  # Obtén todos los datos seleccionados

        conn.close()  # Cierra la conexión
        return datos
    except Exception as e:
        print(f"Error al leer los datos de la base de datos: {e}")
        return None
    
# muestra solo lo bajo en stock (opcion 5)
def readRowslow():

    db_path = os.path.join("ultimaClase", "productos.db")

    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        instruccion = "SELECT * FROM productos where cantidad < 5"  # Trae todos los datos que tengan bajo stock en este caso es menor a 5
        cursor.execute(instruccion)
        datos = cursor.fetchall()  # Obtén todos los datos seleccionados

        conn.close()  # Cierra la conexión
        return datos
    except Exception as i:
        print(f"Error al leer los datos de la base de datos: {i}")
        return None