def medir_rendimiento (puntuacion):
    niveles = {
        'a':'Inaceptable',
        'b': 'Aceptable',
        'c':'Meritorio'
    }
    bono = puntuacion * 2400 
    if  puntuacion == 0.0:
        print(f"El desempeño se evaluó como: {niveles.get('a')}")
        print(f"La bonificación es de €{bono}")
    elif puntuacion == 0.4:
        print(f"El desempeño se evaluó como: {niveles.get('b')}")
        print(f"La bonificación es de €{bono}")
    elif puntuacion >= 0.6:
        print(f"El desempeño se evaluó como: {niveles.get('c')}")
        print(f"La bonificación es de €{bono}")
    else:
        print("Puntuación no válida, vuelve a intentarlo")

medir_rendimiento(round(float(input("Puntuación del empleado: \n")),1))   
    
    