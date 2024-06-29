def calc_cuenta (tipo, cantidad):
    if int(tipo) == 1:
        de_hoy = int(cantidad) * 3.49
        return f"Piezas del día: {cantidad} \n €{round(float(de_hoy),2)} "
    elif int(tipo) == 2:
        de_ayer = (int(cantidad) * 3.49) * 0.40
        return f"Piezas de ayer día: {cantidad} \n Precio regular: €{round(3.49*float(cantidad),2)} \n Precio final: €{round(float(de_ayer),2)} "
    elif int(tipo) != 1 or int(tipo) != 2: 
        return "Selección no válida"
    
print(calc_cuenta(input("Teclea el número del producto \n 1 Pan de hoy \n 2 Pan de ayer \n "), input(f"Número de piezas: ")))


#Falta afinar el proceso para que no acepte opciones no válidas de producto antes de pedir cantidad
