def desglosar_prod (nombre, precio, unidades):
    costo_total = float(precio) * float(unidades)
    print(f"Producto: {nombre}")
    print(f"Precio: ${round(float(precio),2)}")
    print(f"Cantidad: {unidades}")
    print(f"Total: ${round(float(costo_total),2)}")

nombre = input("Nombre producto: \n")
precio = float(input("Costo al público: \n"))
unidades = float(input("Cantidad: \n"))
print(desglosar_prod(nombre, precio, unidades))
    