def pagar_entrada (edad):
    if edad > 18:
        print("Mayor de edad, entrada 10€")
    elif edad >= 4:
        print("Menor de edad, entrada 5€")
    else:
        print("Menor de edad, entrada gratuita")

pagar_entrada(int(input("¿Cuál es tu edad? \n")))