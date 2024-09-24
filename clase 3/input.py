nombre = input("ingresa tu nombre: ")

edad = input("ingresa tu edad: ") # el imput simpre devuelve string (str)

# edad = int(input("ingresa tu edad: ")) --> es lo mismo pero todo anidado
edadSRT = int(edad) # pasa a hacer un int numero entero

edadEnDiezAños = edadSRT + 10

print(f"hola {nombre}, tu edad en 10 años es {edadEnDiezAños} años")