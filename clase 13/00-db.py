conn = sqlite3.connect('nombre.db') 

cursor = conn.cursor() 

 

cursor.execute(""" 

 

""") 

conn.commit() 

conn.close()