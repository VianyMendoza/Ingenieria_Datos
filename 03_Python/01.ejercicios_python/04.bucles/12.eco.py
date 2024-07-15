print("Esta es una cueva donde todo lo que escribas se repetirá, hasta que escribas salir")
while True:
    frase = input("Escribe tu frase:\n")
    if frase == 'salir':
        break
#BREAK se utiliza para salir de la estructura de control de bucle más cercana en la que se encuentra. Es comúnmente utilizada en bucles for y while para detener la ejecución del bucle antes de que se haya completado completamente la iteración normal.
#solo afecta al bucle más cercano 
    print(frase) 