def enlistar_vector_a():
    a = []
    i = 0   
    while True:
        vector_a = input(f"Ingresa el numero para la posición {i} del vector x (deje vacío para terminar la captura):  ")
        if vector_a == "":
            break
        a.append(float(vector_a))
        i += 1
    return a

def enlistar_vector_b():
    b = []
    i = 0   
    while True:
        vector_b = input(f"Ingresa el numero para la posición {i} del vector y (deje vacío para terminar la captura):   ")
        if vector_b == "":
            break
        b.append(float(vector_b))
        i += 1
    return b

def calcular_vector(a, b):
    x = list((a))
    y = list((b))

    #SOL 1
    productos = [ a * b for a, b in zip(x, y)]

    total = 0
    for i in productos:
        total += i
    print(f"El producto de los vectores {x} y {y}, es: {total}")

    #SOL 2
    product = 0
    for i in range(len(x)):
        product += x[i] * y[i]
    print(f"El producto de los vectores {x} y {y}, es: {product}")   

vector_a = enlistar_vector_a()
vector_b = enlistar_vector_b()
calcular_vector(vector_a, vector_b)