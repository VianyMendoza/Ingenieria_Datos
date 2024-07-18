def loteria():
    lista_loteria =[]

    while True:
        numeros = input("Escribe los números ganadores: \n")
        if numeros == "":
            break
        lista_loteria.append(int(numeros))
    
    lista_loteria.sort()

    print("Estos son los números ganadores:")
    for num in lista_loteria:
        print(num)

loteria()