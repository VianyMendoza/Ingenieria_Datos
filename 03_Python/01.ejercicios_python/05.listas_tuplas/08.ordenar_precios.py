def ordenar_precios():
    precios_list = []
       
    while True:
        cap_precio = input("Ingresa los precios (deje vacío para terminar): ")
        if cap_precio == "":
            break
        try:
            precio = float(cap_precio)
            precios_list.append(precio)
        except ValueError:
            print("Ingresa un valor válido")

    lista_ordenada = sorted(precios_list)

    print(lista_ordenada)    

ordenar_precios()