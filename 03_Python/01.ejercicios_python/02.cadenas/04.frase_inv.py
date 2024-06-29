def invertir_frase (frase):
    print(frase[::-1])   
    print(frase[0:len(frase):2])
    print(frase * 2)
    

print(invertir_frase(input("Introduce una frase: ")))
