def serie (numero):
    i = 1
    lista = [i]
    while i < numero:
        i += 2
        lista.append(i)
        
    print (lista)


serie(int(input("Define un número entero y positivo: \n")))    