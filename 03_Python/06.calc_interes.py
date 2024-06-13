def calculo_inversion (cantidad, interes, años):
    capital = float(cantidad) * (float(interes) / 100 + 1) ** float(años)
    return f"El capital obtenido de esta inversión será de ${round(capital,2)}"

print(calculo_inversion(input("Cuál es la cantidad que invertirás? "),input("Cuál es el interés de la inversión? "),input("Por cuántos años lo invertirás? ")))