def asignar_grupo (genero, nombre):
    inicial = nombre[0:1:]

    if genero.upper() =="FEM" and inicial.lower() <'m':
         print("Grupo A")
    elif genero.upper() =="MASC" and inicial.lower() >'n':
         print("Grupo A")
    else:
         print("Grupo B")

asignar_grupo(input("Género del alumno (FEM / MASC):"), input("Nombre del alumno:"))