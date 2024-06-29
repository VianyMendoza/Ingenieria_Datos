def saludar(nombre, numero):
    i = 1
    while i <= int(numero):
        print(nombre)
        i += 1


print(saludar(input("Cuál es tu nombre? \n"), input("Cuántas veces quieres imprimirlo? \n")))
