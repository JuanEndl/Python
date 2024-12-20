
import color
import sqlite3 as sql
import os

# crea la DB y si existe no la crea
def createDB():
    db_path = os.path.join("db", "productos.db")  # Definir la ruta de la base de datos y guardarla a una variable

    # Verificar si la base de datos ya existe
    if os.path.exists(db_path):
        print(f"La base de datos ya existe en la ruta: {db_path}")
    else:
    
        # Crear la base de datos si no existe
        try:
            os.makedirs("db", exist_ok=True)  # Asegura que la carpeta exista
            conn = sql.connect(db_path)  # Hace la conexión con la ruta de la DB

            print(f"{color.GREEN}Base de datos creada exitosamente en la ruta: {db_path}{color.RESET}") # muestra el mensaje de creacion de la  DB exitoso

           
            conn.close()  # Cierra la conexión

        except Exception as i:
            print(f"{color.RED}Error al crear la base de datos: {i}{color.RESET}")


    # Crear la tabla "productos" si no existe
    try:
        conn = sql.connect(db_path)
        cursor = conn.cursor()


    # Crear la tabla
        cursor.execute("""
            create table if not exists productos(
                id integer primary key autoincrement,
                nombre text not null,
                descripcion text not null,
                cantidad integer not null,
                precio real not null
            )
        """)
        conn.commit()
        print(f"{color.GREEN}Tabla 'productos' creada.{color.RESET}")
    except Exception as i:
        print(f"{color.RED}Error al crear la tabla: {i}{color.RESET}")
    finally:


        conn.close()  #  Cierra la conexion

# insertar fila (opcion 1)
def insertRow(nombre, descripcion, cantidad, precio):

    db_path = os.path.join("db", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agrega lo que ya le defino por query
    query = f"""insert into productos (nombre, descripcion, cantidad, precio) 
                      values ('{nombre}', '{descripcion}', {cantidad}, {precio})""" # Query para ingresar productos a la DB

    cursor.execute(query) # ejecuta la instraccion declarada arriba 

    conn.commit()
    conn.close()

# insertar fila (opcion 2)
def updateRow(cantidad, id):
    db_path = os.path.join("db", "productos.db")

    try:
        # Conectar a la base de datos
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Actualiza la cantidad en la base de datos
        query = "UPDATE productos SET cantidad = ? WHERE id = ?"
        cursor.execute(query, (cantidad, id))

        # Verificar si realmente se actualizó la fila
        if cursor.rowcount == 0:
            conn.commit()
            conn.close()
            return False  # Indica que no se encontró el ID
        else:
            conn.commit()
            conn.close()
            return True  # Indica éxito

    except Exception as e:
        print(f"{color.RED}Error al modificar la cantidad: {e}{color.RESET}")
        return False

# borrar fila por ID (opcion 3)
def deleteRow(id):
    db_path = os.path.join("db", "productos.db")  # Ruta de la base de datos

    try:
        conn = sql.connect(db_path)  # Conexión a la base de datos
        cursor = conn.cursor()

        # Ejecuta el DELETE con un parámetro para evitar SQL Injection
        query = "DELETE FROM productos WHERE id = ?"
        cursor.execute(query, (id,))

        # Verifica si se eliminó alguna fila
        if cursor.rowcount == 0:
            print(f"\n{color.RED}No se encontró un producto con el ID {id}. Elegir la opcion 4 para encontrar el ID\n{color.RESET}")
        else:
            print(f"{color.GREEN}Producto con ID {id} eliminado correctamente.\n{color.RESET}")

        conn.commit()
        conn.close()
    except Exception as i:
        print(f"{color.RED}Error al eliminar el producto: {i}{color.RESET}")

# mostrar toda la tabla (opcion 4)
def readRows():

    db_path = os.path.join("db", "productos.db")

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

    db_path = os.path.join("db", "productos.db")

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