Funcion CalculadoraDescuento(precio, descuento)
	precio_final <- precio - ((descuento/100) * precio)
	Escribir "El precio final con descuento aplicado es: "
	Escribir "$ " precio_final
FinFuncion

Algoritmo CalculadoraFuncion
	Escribir "Hola, �cu�l es el costo de tu producto?"
	Leer precio
	Escribir  "�Cu�l es el % de descuento?"
	Leer descuento
	CalculadoraDescuento(precio, descuento)
FinAlgoritmo
