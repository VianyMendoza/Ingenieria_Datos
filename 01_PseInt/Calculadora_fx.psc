Funcion CalculadoraDescuento(precio, descuento)
	precio_final <- precio - ((descuento/100) * precio)
	Escribir "El precio final con descuento aplicado es: "
	Escribir "$ " precio_final
FinFuncion

Algoritmo CalculadoraFuncion
	Escribir "Hola, ¿cuál es el costo de tu producto?"
	Leer precio
	Escribir  "¿Cuál es el % de descuento?"
	Leer descuento
	CalculadoraDescuento(precio, descuento)
FinAlgoritmo
