#Funcion de alcance local, no puede ser llamada fuera de su alcance
#definir función
saludar() {
    local mensaje= "Hola mundo!"
    echo $mensaje #Funciona
}
#Llamar a la función 

saludar
echo $mensaje #No imprime nada

