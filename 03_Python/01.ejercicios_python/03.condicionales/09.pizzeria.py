def elegir_pizza (tipo):
    
    vegetariana = {
        'a':'Pimientos', 
        'b':'Tofu', 
        'c':'Seitan'
    }
    no_vegetariana = {
        'a':'Peperoni', 
        'b':'Jamón', 
        'c':'Salmón'
    } 
    
    if tipo == 'a':
        print("Elige tu ingrediente:")
        for x, y in vegetariana.items():
           print(x, y)
        x = input()
        orden= print((f"Pizza vegetaria, con {vegetariana.get(x)}."))
        return orden

    elif tipo == 'b':
        print("Elige tu ingrediente:")
        for x, y in no_vegetariana.items():
           print(x, y)
        x = input()
        orden= print((f"Pizza vegetaria, con {no_vegetariana.get(x)}."))
        return orden
    
    print("¡Gracias por su compra!")
 
print("¡Bienvenido a Bella Napoli!")
print("Todas nuestras pizzas incluyen queso mozzarella y salsa de tomate")
elegir_pizza(input("Elige la pizza que se te antoja: \n a. Vegetariana \n b. No vegetariana \n"))


