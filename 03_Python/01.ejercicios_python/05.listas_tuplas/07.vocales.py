def vocales(palabra):
    letras = list(palabra)
    a = letras.count('a')
    e = letras.count('e')
    i = letras.count('i')
    o = letras.count('o')
    u = letras.count('u')

    print(f"Tu frase tiene: \n a: {a} \n e: {e} \n i: {i} \n o: {o} \n u: {u}")

vocales(input("¿Cuál es tu palabra o frase? \n"))