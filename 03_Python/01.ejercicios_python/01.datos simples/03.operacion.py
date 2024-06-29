def operacion (n):
    calculo = ((int(n) + 1) * int(n)) / 2 
    if calculo % 2 == 0:
        return f"El resultado es par: {int(calculo)}"
    else:
        return f"El resultado es impar: {int(calculo)}"
    
print(operacion(input("Define el número a calcular: ")))

    