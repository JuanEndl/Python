acumulador = 0
contador = 0

while True:
    nota = int (input("nota: "))
    if nota > 10:
           continue # --> lo que hace el continue es si no cumple la condicione vuelve arriba del while anterior
    acumulador = acumulador + nota
    respuesta = input("Deseas continuar? (s/n)")
    if respuesta.lower() == "n":
        print("saliendo")
        break

promedio = acumulador / contador