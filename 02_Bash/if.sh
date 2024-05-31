 #Condicionales if
 read -p "Ingresa un numero " numero2
 
 if [ $numero2 -gt 10 ]; then
    echo "El numero es mayor a 10"
elif [ $numero2 -eq 10 ]; then
    echo "El numero es igual a 10"
else
    echo El numero es menor a 10
fi
