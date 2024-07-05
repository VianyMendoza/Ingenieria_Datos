def serie (numero):
    for i in range(numero, -1, -1):
        print(i, end=", ")

def serie2 (numero):
    i = numero
    lista = [i]
    while i > 0:
        i -= 1
        lista.append(i)
        
    print (lista)

serie(int(input("Define un número entero y positivo: \n")))  
serie2(int(input("Define un número entero y positivo: \n")))      
  