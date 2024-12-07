import sqlite3 as sql
import os # importa la DB. Para trabajar con rutas


'''Funcion que crea la DB y la ruta donde se va a encontrar'''
def createDB():
                
    db_path = os.path.join("EntregaConDB", "productos.db") # Definir la ruta de la base de datos 

    # crear la base de datos 
    conn = sql.connect(db_path) # hace la conexion con la ruta donde se entra la DB
    conn.commit()
    conn.close() # cierra conexion

def createTable():

    db_path = os.path.join("EntregaConDB", "productos.db") # Definir la ruta de la base de datos 
    
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """ Create table productos(
            id integer primary key autoincrement,
            nombre text not null,
            descripcion tex not null,
            cantidad intager not null,
            precio real not null
        )"""
    )
    conn.commit()
    conn.close()

def insertColum():

    db_path = os.path.join("EntregaConDB", "productos.db") # Definir la ruta de la base de datos 
    
    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agregar una comlumna a la tabla ya creada con "alter table"
    cursor.execute(
        """ alter table productos add column descripcion text not null"""
    )
    conn.commit()
    conn.close()

def insertRow():

    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agrega lo que ya le defino por query
    instruccion = f"insert into productos (nombre, cantidad, precio, descripcion) values ('roro', 12, 64, 'lalalal')" # instruccion guardada para ejecutarla con el cursor.execute
                                                                                                                      # agrega los valores colocados a la db

    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba 

    conn.commit()
    conn.close()


# aca se ejecuta la funcion sin ejecutarse algun otro codigo que se entre afuera de la misma
if __name__ == "__main__":
    #createDB()
    #createTable()
    insertRow()
