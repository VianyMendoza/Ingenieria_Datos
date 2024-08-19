def capturar_lista():
    lista_num = []
    
    while True:
        numero = input(f"Ingresa el numero (deje vacío para terminar la captura):  ")
        if numero == "":
            break
        lista_num.append(float(numero))
        
    return lista_num

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

def calcular_desvest(lista, media):
    sumsq = 0
    for i in lista:
        sumsq += i**2
    stdev = (sumsq/len(lista)-media**2)**(1/2)
    return stdev

def calcular_moda(lista):
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    frecuencia_maxima = max(frecuencia.values())
    moda = [num for num, freq in frecuencia.items() if freq == frecuencia_maxima]
    return moda

lista_numeros = capturar_lista()
media = calcular_media(lista_numeros)
print(f"La media es: \n {round(media,2)}")
desvest = calcular_desvest(lista_numeros, media)
print(f"La desviaci+on estandar es: \n {round(desvest,2)}")
moda = calcular_moda(lista_numeros)
print(f"La moda es : \n {moda}")