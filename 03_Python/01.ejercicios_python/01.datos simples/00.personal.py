
def saludar(nombre, apellido):
    saludo = f"¡Hola, {nombre} {apellido}!" 
    return saludo


def fecha_nacimiento (dia, mes, año):
    edad = 2024 - int(año)
    resultado = f"Tu edad es de {edad} años"
    
    suma_numerologia = dia + mes + año
    numerologia = f"Tu número es {suma_numerologia}"
    
    return resultado
    return numerologia
    
    
print("Escribe tu nombre, seguido de tu apellido")
print(saludar(input(), input()))

print("¿Cuál es tu fecha de nacimiento?")
print(fecha_nacimiento(input(), input(), input()))

