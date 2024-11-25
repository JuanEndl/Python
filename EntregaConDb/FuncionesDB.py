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
            cantidad intager not null,
            precio real not null
        )"""
    )
    conn.commit()
    conn.close()

    

# aca se ejecuta la funcion sin ejecutarse algun otro codigo que se entre afuera de la misma
if __name__ == "__main__":
    #createDB()
    createTable()
