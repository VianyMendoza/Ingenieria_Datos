def mostrar_nombre (nombre, repeticiones):
    inicio = 0
    while inicio < int(repeticiones):
        print(nombre)
        inicio += 1

mostrar_nombre(input("¿Cuál es tu nombre? \n"),input("¿Cuántas veces lo imprimo? \n")) 