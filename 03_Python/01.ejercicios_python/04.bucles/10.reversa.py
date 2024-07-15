def voltar_palabra(palabra):
    reversa = palabra[len(palabra)::-1]
    for i in reversa:
        print(i)

voltar_palabra(input("¿Cuál es tu nombre?\n"))

"""
OTRA SOLUCION:
    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i])
"""