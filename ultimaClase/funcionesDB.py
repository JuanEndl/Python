import sqlite3 as sql
import os
import FuncionesAparte


'''def createDB():
                
    db_path = os.path.join("ultimaClase", "productos.db") # Definir la ruta de la base de datos 

    # crear la base de datos 
    conn = sql.connect(db_path) # hace la conexion con la ruta donde se entra la DB
    conn.commit()
    conn.close() # cierra conexion
'''

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