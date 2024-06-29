def mayor_edad (nombre, edad):
    print(f"Hola {nombre.capitalize()},")
    if int(edad) >= 18:
        print("eres mayor de edad")
    else:
        print("no eres mayor de edad")

print(mayor_edad(input("Cuál es tu nombre? \n"), input("Cuál es tu edad? \n")))