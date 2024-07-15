def validacion(numero):
    i = 2
    while numero % i != 0:
        i += 1    
    if i == numero :
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")


validacion(int(input("Define el número: \n")))