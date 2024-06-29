def impuesto (edad, ingreso):
    if edad > 16 and ingreso >= 1000.0:
        print("Debe tributar")
    else:
        print("No debe pagar impuesto")

edad = int(input("Edad de la persona: \n"))
ingreso = float(input("Ingreso mensual \n €"))
print(impuesto(edad, ingreso))