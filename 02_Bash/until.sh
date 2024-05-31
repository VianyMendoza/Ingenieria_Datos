#Bucle until: Ejecuta una condición hasta que sea verdadera.

contador=1

until [ $contador -ge 5 ]; do
    echo "Contador: $contador"
    contador= $((contador + 1))
done