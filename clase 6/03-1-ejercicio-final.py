numero1 = 5
numero2 = 7


while True:

    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 dividir")
    print("0 salir")

    opcion = input("Opcion ?: ")
    opcion = int (opcion)

    if opcion == 1:
            resultado = numero1 + numero2
            print(f"el resultado de la Suma {resultado}")
    elif opcion == 2:
            resultado = numero1 - numero2
            print(f"el resultado de la Resta {resultado}")
    elif opcion == 3:
            resultado = numero1 * numero2
            print(f"el resultado de la Multiplicacion {resultado}")
    elif opcion == 4:
            resultado = numero1 / numero2
            print(f"el resultado de la Divicion {resultado}")
    elif opcion == 0:
            print("Adios")
            break
    else:
           print("error colocar un numero del 0 al 4")
# end while


#####################

