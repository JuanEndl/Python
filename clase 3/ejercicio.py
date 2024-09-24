'''
comentar el pyton comenta el parrafo
'''
# comenta la linea

mes1 = 5800
mes2 = 6922
mes3 = 8555

#sacar el promedio

promedio = (mes1 + mes2 + mes3) / 6

auxiliar = type(promedio)

# print(auxiliar) --> en modo de ejemplo, se usa el otro
# el type sirve para debugear y ver que tipo de dato es 
print(type (promedio))

#Python es dinamicamente tipado
promedio = str(promedio)  # 3546.1666666666665 --> se convierte en string "3546.1666666666665"
print("El ingreso promedio es " + str(promedio))



# SRT se usa para cambiar el tipo de dato de flotante pasa a string 