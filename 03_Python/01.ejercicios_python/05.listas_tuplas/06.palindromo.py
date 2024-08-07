def palindromo(palabra):
    lista_palabra = list(palabra)
    lista_palabra.reverse()
    palabra_inversa = "".join(lista_palabra)

    if palabra_inversa == palabra:
        print(f"La palabra '{palabra}' es palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es palíndromo.")

palindromo(input("Define tu palabra: \n"))