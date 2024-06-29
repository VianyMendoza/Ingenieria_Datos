def verificar_contrasena (contrasena, conf_contrasena):
    if contrasena == conf_contrasena:
        print("Contraseña exitosa, puede acceder.")
    else:
        print("Su contraseña no coincide, acceso denegado.")
    
verificar_contrasena(input("Contraseña: \n"),input("Confirme su contraseña: \n"))