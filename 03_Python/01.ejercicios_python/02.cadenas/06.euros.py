def precio (total_euros):
    euros = total_euros[:total_euros.find('.'):]
    centavos = total_euros[total_euros.find('.')+1::]
    print(f"El total es de {euros} euros")
    print(f"Con {centavos} centavos")

print(precio(input("Costo total: ")))
    