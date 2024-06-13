def costo_envio (producto, cantidad):
    if str(producto) == "muñeca" or str(producto) == "MUÑECA" or str(producto) == "Muñeca" or str(producto) == "a" or str(producto) == "a.":
        envio_muñeca = 75*int(cantidad)*1
        return f"El costo de este envío para {int(cantidad)} Muñeca(s) será de ${envio_muñeca}"
    elif str(producto) == "payaso" or str(producto) == "PAYASO" or  str(producto) == "Payaso" or str(producto) == "b" or str(producto) == "b.":
        envio_payaso = 112*int(cantidad)*1
        return f"El costo de este envío para {int(cantidad)} Payaso(s) será de ${envio_payaso}"
    else :
        return "Producto no válido"
    
print(costo_envio(input("¿Cuál es el producto a enviar? \n a. Muñeca \n b. Payaso \n "), input(f"Cantidad de productos: ")))

#Falta afinar el proceso para que no acepte opciones no válidas de producto antes de pedir cantidad
