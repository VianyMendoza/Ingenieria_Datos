def calcular_inversion(capital: float, interes: float, anios: int):
    for anio in range(1, anios, 1):
        ganancia = capital * (interes * 0.01)
        capital += ganancia
        print(f"Año {anio}, tu capital total será de: ${round(capital, 2)}")


calcular_inversion(float(input("Capital a invertir: \n")), float(
    input("Porcentaje de interés \n %")), int(input("Tiempo en años: \n")))
