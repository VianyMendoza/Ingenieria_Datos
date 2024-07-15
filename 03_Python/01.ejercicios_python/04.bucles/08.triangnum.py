def dibujar_figura (numero):
    for i in range(1, numero+1, 2):
        for j in range(i,0,-2):
            print (f"{j} ", end= "")
        print("")
        
dibujar_figura (int(input("Proporciona un npumero entero: \n")))