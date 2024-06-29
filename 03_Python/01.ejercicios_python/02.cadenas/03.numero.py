#tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
#print('El número de teléfono es ', tel[4:-3])

def numero_completo (numero):
    print(f"El número de teléfono es: \n {numero[4:-3]}")
    
print(numero_completo(input("Introduce el número telefónico con el formato +xx-xxxxxxxxx-xx: \n")))
