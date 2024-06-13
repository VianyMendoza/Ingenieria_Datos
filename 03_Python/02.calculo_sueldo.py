def sueldo (horas, valor_hora, dias):
    calculo_sueldo = float(horas) * float(valor_hora) * float(dias)
    return f"El sueldo semanal que te corresponde es de ${calculo_sueldo}"

print(sueldo(input("¿Cuántas horas diarias trabajaste? "), input("¿Cuánto te pagan por hora? "), input("¿Cuántos días de la semana trabajaste? ")))   
 


