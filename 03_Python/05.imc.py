def calculadora_imc (peso, estatura):
    imc = float(peso) / ((float(estatura)/100) ** 2)
    if imc < 18.5:
        return f"Tu IMC es: {round(float(imc),2)}, es inferior al normal."
    elif imc >= 18.5 and imc <= 24.9:
        return f"Tu IMC es: {round(float(imc),2)}, es normal."
    elif imc >= 25 and imc <= 29.9:
        return f"Tu IMC es: {round(float(imc),2)}, es superior al normal."
    else:
        return f"Tu IMC es: {round(float(imc),2)}, es señal de obesidad."
        

print(calculadora_imc(input("¿Cuál es tu peso en Kg? "),input("¿Cuál es tu estatura en cm? ")))