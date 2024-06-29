def division (dividendo, divisor):
    try:
        resultado = int(dividendo) / int(divisor)
        print(f"El resultado de tu división es: {resultado}")
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        
        division(input("Dividendo: \n"),input("Divisor: \n"))

    except:
        print("Valor no válido, intenta de nuevo")

        division(input("Dividendo: \n"),input("Divisor: \n"))


division(input("Dividendo: \n"),input("Divisor: \n"))