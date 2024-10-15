
numero = int(input("coloca un numero "))

if numero % 2 == 0:
        print(f"{numero} es un numero par.")
else:
        print(f"{numero} es un numero impar.")

#########################################


## --> elif 

edad = int(input("ingresa tu edad "))

if edad < 18:
        print(f"{numero} sos menor de edad.")
elif edad < 30:
        print(f"{numero} sos adulto joven.")
elif edad < 50:
        print(f"{numero} sos viejo adulto.")
elif edad < 70:
        print(f"{numero} sos viejo.")
