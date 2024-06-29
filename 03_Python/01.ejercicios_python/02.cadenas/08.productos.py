#def lista(productos):
    #for producto in productos:
        #print(producto)

#print(list(lista(input("Proporciona la lista de productos: "))))

def lista(productos):
    new_string = productos.replace(",", "\n")
    print(f"Lista de compras: \n {new_string}")


print(lista(input("Proporciona la lista de productos: ")))
