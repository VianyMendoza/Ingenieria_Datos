def lista():
    lista_num = []
    for n in range(1,11):
        lista_num.append(n)
    print(lista_num)
    return lista_num

def ordenar_lista(lista_valores):
    lista_valores.sort(reverse=True)
    print(lista_valores)

def ordenar_lista2(lista_valores):
    lista_valores.sort(reverse=True)
    for n in lista_valores:
        print(n, end=",")

mi_lista = lista()
ordenar_lista(mi_lista)
ordenar_lista2(mi_lista)
