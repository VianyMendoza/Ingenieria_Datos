def contar_letra(frase, letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

"""
%s, %i: Estos son especificadores de formato que se utilizan dentro de la cadena de formato ("La letra '%s' aparece %2i veces en la frase '%s'.") para indicar dónde deben insertarse los valores de las variables letra, contador y frase.
'%s', '%2i': Estos especificadores indican el tipo de datos esperados:
    %s espera una cadena (string).
    %i espera un número entero (integer).
%2i: Este especificador de formato para %i asegura que el número entero (contador en este caso) se formatee con al menos dos caracteres de ancho, lo cual es útil para alinear correctamente la salida cuando se imprimen números.
% (letra, contador, frase): Es una tupla de valores que coinciden con los especificadores de formato en la cadena de formato. Aquí, letra, contador y frase son variables que se pasan como argumentos a la función print() y se insertan en los lugares correspondientes de la cadena de formato.
"""



contar_letra(input("Escribe tu frase: \n"), input("¿Qué letra buscamos? \n"))

"""
OTRA SOLUCION
def contar_letra(frase, letra):
    caracter_lista = []
    frase_limpia = frase.replace(" ", "")
    for i in frase_limpia:
        caracter_lista.append(i)

    indice = 0
    x = 0

    while indice < len(caracter_lista):
        if caracter_lista[indice] == letra:
            x += 1
        else:
            x
        indice += 1
    
    print(f"La letra {letra} se repite {x} en tu frase")

contar_letra(input("Escribe tu frase: \n"), input("¿Qué letra buscamos? \n"))

"""