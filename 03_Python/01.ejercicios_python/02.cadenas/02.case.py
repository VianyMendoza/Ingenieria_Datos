def saludar(nombre):
    print(nombre.upper())
    print(nombre.lower())
    print(nombre.capitalize())
    print(f"Tu nombre tiene {len(nombre)} letras")

print(saludar(input("Cuál es tu nombre? \n")))