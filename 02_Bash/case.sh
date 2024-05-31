#Condicional case
read -p "Ingresa una opción (a/b/c) " opcion

case $opcion in
    a)
        echo "Elegiste la opción A"
        ;;

    b)
        echo "Elegiste la opción B"
        ;;

    c)  
        echo "Elegiste la opción C"
        ;;

    *)
        echo "Opción no válida"
        ;;
 esac

