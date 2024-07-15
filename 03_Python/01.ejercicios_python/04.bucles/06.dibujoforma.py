def dibujar (numero:int):
    i = 1
    while i <= numero:
        ast = "*" * i
        print(ast)
        i += 1

    try:    
        ast = int(numero / 2 )
        print("*" * ast)
        print("*" * ast)
        print("*" * ast)

    except TypeError:
        ast = int((numero-1) / 2 )
        print("*" * ast)
        print("*" * ast)
        print("*" * ast)

dibujar(int(input("Cuántas veces necesitas imprimir * en pantalla?\n")))

"""
MÁS SIMPLE: 
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))
"""