def enlistar_asignaturas():
    """
    Esta función genera la lista de materias
    """

    lista_asign = []
       
    while True:
        materia = input("Ingresa el nombre de la asgnatura (deje vacío para terminar): ")
        if materia == "":
            break
        lista_asign.append(materia)

    return lista_asign

def calificar(lista_asignaturas): 
    """
    Esta función registra las calificaciones
    """
    
    calificacion = []
    
    for materia in lista_asignaturas:
        nota = input(f"Qué nota obtuviste en {materia}? \n")
        calificacion.append(float(nota))
        
    print("Estas son tus calificaciones: ")
    for materia, nota in zip(lista_asignaturas, calificacion):
        print(f"    *En {materia} obtuviste: {nota}.")

    promedio = sum(calificacion) / len(calificacion)
    print(f"Tu promedio es  de {promedio}")
    
    return calificacion

def reprobadas(lista_asignaturas, lista_calificaciones):
    """
    Esta función muestra las materias a recursar
    """
    dict_evaluacion = dict(zip(lista_asignaturas, lista_calificaciones))
    print(dict_evaluacion)

    aprobadas = {y: x for y, x in dict_evaluacion.items() if x >= 6}
    reprobadas = {y: x for y, x in dict_evaluacion.items() if x <= 6}

    print(f"Materias aprobadas:")
    for aprobada in aprobadas:
        print(f"   *{aprobada}")
    print("------------------------------")
    print(f"Materias reaprobadas:")
    for reprobada in reprobadas:
        print(f"   *{reprobada}")

mis_asignaturas = enlistar_asignaturas()
mis_calificaciones = calificar(mis_asignaturas)
reprobadas(mis_asignaturas, mis_calificaciones)