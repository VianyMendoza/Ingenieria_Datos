def verificar_contrasenia(contrasenia_almacenada, contrasenia_acceso):    
    if contrasenia_almacenada != contrasenia_acceso:
        print("Contraseña incorrecta, vuelva a intentarlo.")
        
verificar_contrasenia(input("Define tu contrasenia: \n"), input("Confirma tu contraseña: \n"))