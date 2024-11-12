# funcion

'''
sintaxis

Se define despues el nombre ():
y lo que quiero hacer

def pepe():
    print("hola")

pepe() --> invocar la funcion
'''

def pepe():
    print("hola")

pepe()


################ funcion con return ################


def esMayorDeEdad(edad): # funcion que determina si una persona es mayor o no
    if edad >= 18:
        return True
    else:
        return False
    
resultado = esMayorDeEdad(19)

resultado


print(resultado)

# ================================

def lentCasero(secuencia):
    contador = 0
    for elemento in secuencia:
        contador = contador + 1
        #print(elemento)

respuesta = lentCasero("hola")

print(respuesta)

print(lentCasero("sasasasas"))
