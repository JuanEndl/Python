mes1 = 5800
mes2 = 6922
mes3 = 8555

promedio = (mes1 + mes2 + mes3) / 6

auxiliar = type(promedio)

print(type (promedio))

promedio = str(promedio)   # 3546.1666666666665 --> se convierte en string "3546.1666666666665"
print("El ingreso promedio es " + str(promedio) + ".-\nMeses: \nmes1:" + str(mes1) + "\nmes2:" + str(mes2) )

# \n --> salto de linea en el print

print(f"{promedio}")

print(f"El ingreso promedio es {promedio} .\nMeses: \nmes1: {mes1} \nmes2: {mes2}") # el print(f) hace todo mas facil al cambiar el tipo de dato
                                                                                    # no es necesario usar el srt cada vez que quieras cambiar el dato

