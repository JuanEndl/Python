import sqlite3 as sql
import os # importa la DB. Para trabajar con rutas

# para abrir la base de sebe apretar shift + ctrl + P. Colocar SQLite 3 y apretar en la opcion "Open DataBase" y eleguir nuestra DB

'''Funcion que crea la DB y la ruta donde se va a encontrar'''
def createDB():
                
    db_path = os.path.join("EntregaConDB", "productos.db") # Definir la ruta de la base de datos 

    # crear la base de datos 
    conn = sql.connect(db_path) # hace la conexion con la ruta donde se entra la DB
    conn.commit()
    conn.close() # cierra conexion

'''Funcion que crea la tabla de la DB'''
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

'''Funcion que agrega una columna'''
def insertColum():

    db_path = os.path.join("EntregaConDB", "productos.db") # Definir la ruta de la base de datos 
    
    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agregar una comlumna a la tabla ya creada con "alter table"
    cursor.execute(
        """ alter table productos 
            add column descripcion text not null"""
    )
    conn.commit()
    conn.close()

'''Funcion que agrega una fila'''
def insertRow():

    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # agrega lo que ya le defino por query
    instruccion = f"""insert into productos (nombre, cantidad, precio, descripcion) 
                      values ('roro', 12, 64, 'lalalal')""" # instruccion guardada para ejecutarla con el cursor.execute
                                                        # agrega los valores colocados a la db

    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba 

    conn.commit()
    conn.close()

'''Funcion que lee todos los datos de la tabla'''
def readRows():

    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    instruccion = f"select * from productos" # trae todos los datos de la tabla productos
    
    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba
    datos = cursor.fetchall() # este metodo devuelve todos los datos seleccionados

    conn.commit()
    conn.close()

    print(datos) # hacemos un print para mostrar en la consola

'''Funcion de filtro, en este caso trae del campo cantidad lo que tiene menor o igual a 5'''
def readOrder():

    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    instruccion = f"select * from productos 
                    where cantidad <= 5" # trae todos los datos de la tabla productos
    
    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba
    datos = cursor.fetchall() # este metodo devuelve todos los datos seleccionados

    conn.commit()
    conn.close()

    print(datos) # hacemos un print para mostrar en la consola

'''Funcion que hace un update y modifica la fila. En este caso modifica la cantidad que se encuentra en el ID 2 a 500'''
def UpdateRow():

    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    instruccion = f"update productos
                    set cantidad = 500 
                    where id = 2" # modifica la cantidad a 500 de la fila que contiene el id 2 
    
    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba
    
    conn.commit()
    conn.close()

'''Funcion que borra una fila. En este coso borra la fila con el ID 2'''
def deleteRow():
    db_path = os.path.join("entregaConDB", "productos.db")

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    instruccion = f"delete from productos 
                    where id = 2" # modifica la cantidad a 500 de la fila que contiene el id 2 
    
    cursor.execute(instruccion) # ejecuta la instraccion declarada arriba
    
    conn.commit()
    conn.close()


# aca se ejecuta la funcion sin ejecutarse algun otro codigo que se entre afuera de la misma
if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow()
    #readRows()
    #readOrder()
    #UpdateRow()
    deleteRow()
    
