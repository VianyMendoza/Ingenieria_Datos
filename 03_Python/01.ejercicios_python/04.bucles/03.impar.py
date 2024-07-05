def serie (numero):
    i = 1
    lista = [i]
    while i < (numero-1):
        i += 2
        lista.append(i)
        
    print (lista)

def serie2 (numero):
    for i in range(1,numero+1, 2):
        print(i, end=", ")


serie(int(input("Define un número entero y positivo: \n")))    
serie2(int(input("Define un número entero y positivo: \n")))    