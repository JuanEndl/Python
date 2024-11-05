# diccionario sintaxis
'''
{clave 1: valor 1,
 clave 2: valor 2,
 clave 4: valor 4}
 '''

# var = {"titulo": "pepe", "actor": "Luis", "duracion": 60 } 



####################################################################

peliculas = {"titulo" : "el señor de los anillos",
             "duracion": 60,
             "actor": "cintia"
}

print("mostrar pelicula:", peliculas)

# acceder a los elementos del dirreccionados
print("titulo de la peli:", peliculas["titulo"])
print("duracion de la peli:", peliculas["duracion"], "minutos")
print("actores:", peliculas["actor"])

# modificar elemento
peliculas["actores"] = "pepe"
print("actor modificado", peliculas["actor"])