def asignar_grupo (genero, nombre):
    grupo_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    grupo_2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    inicial = nombre[0:1:]

    if genero.upper() =="FEM" and inicial.lower() in grupo_1:
         print("Grupo A")
    elif genero.upper() =="MASC" and inicial.lower() in grupo_2:
         print("Grupo A")
    else:
         print("Grupo B")

asignar_grupo(input("Género del alumno (FEM / MASC):"), input("Nombre del alumno:"))

