

def op_division (dividendo, divisor):
    c = int(dividendo) / int(divisor)
    r = int(dividendo) % int(divisor)
    return(f"El resultado de dividir {dividendo} entre {divisor} es {int(c)}. Con residual de {int(r)}")

print(op_division(input("Indica el número entero a dividir: "), input("Indica el numero divisor entero: ")))


def op_division (dividendo, divisor):
    return(f"El resultado de dividir {dividendo} entre {divisor} es {int(int(dividendo) / int(divisor))}. Con residual de {int(int(dividendo) % int(divisor))}")

print(op_division(input("Indica el número entero a dividir: "), input("Indica el numero divisor entero: ")))