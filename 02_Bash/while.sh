#Bucle while: Ejecuta un conjunto de comandos mientras la condición sea verdadera.
contador=1

while [ $contador -le 5 ]; do
    echo "Contador: $contador"
    contador= $((contador + 1))
done