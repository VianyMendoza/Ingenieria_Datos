def asignaturas():
    lista_asign = []
    calificacion = []

    while True:
        materia = input("Ingresa el nombre de la asgnatura (deje vacío para terminar): ")
        if materia == "":
            break
        lista_asign.append(materia)
    
    
    for materia in lista_asign:
        nota = input(f"Qué nota sacaste en {materia}? \n")
        calificacion.append(int(nota))
    promedio = sum(calificacion) / len(calificacion)

    print("Estas son tus calificaciones: ")
    for materia in lista_asign:
        print(f"    *En {materia} sacaste {nota}.")

    print(f"Tu promedio es {promedio}")

asignaturas()
