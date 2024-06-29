def calcular_impuesto (renta): 
    if renta >= 60000:
        tipo = 45
    elif renta >= 35000 and renta < 60000:
        tipo = 30
    elif renta >= 20000 and renta < 35000:
        tipo = 20
    elif renta >= 10000 and renta < 20000:
        tipo = 15
    else:
        tipo = 5
    
    print(f"Impuesto a pagar €{renta * tipo /100} ")
    

calcular_impuesto(float(input("Monto de la renta anual: \n €")))