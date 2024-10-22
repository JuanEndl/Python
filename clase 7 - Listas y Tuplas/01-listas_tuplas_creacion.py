
'''
Las listas son una collecccion de elementos son ordenadas, 0,,,,,99999 tienen metodos asociados
'''

cadena = "asdasdsadasdadasd"


##lista 1
miPrimeraLista = list()

print("hola", miPrimeraLista)

##lista 2
miSegundaLista = []
print("hola dos", miSegundaLista)

##lista 3
miTerserLista = [5, 6.8, 7]
print("hola", miTerserLista[1]) # --> estoy llamando el caracter de la posicion 1
print(len(miTerserLista)) ## --> muestra la cantidad de lo que se encuentra en la lista

#### cambio el dato a gato 
miTerserLista[1] = "gato"
print(miTerserLista)


######################################

#metodo 1 --> agarrar la cadena y pasar todo a mayusculas
print(cadena.upper())


######### metodos de las listas
#append
miTerserLista.append("agrega el elemento al final") # --> append agrega un elemento al final de la lista
print(miTerserLista)

#remove
miTerserLista.remove(1) # --> elemina el primer elemento que coincida