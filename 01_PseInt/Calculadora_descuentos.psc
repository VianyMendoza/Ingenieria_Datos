Algoritmo descuentos
	Definir precio, porcentaje_descuento, porcentaje_decimal, descuento, precio_final Como Real
	Escribir "Hola, �cu�l es el costo de tu producto?"
	Leer precio
	Escribir  "�Cu�l es el % de descuento?"
	Leer porcentaje_descuento
	
	porcentaje_decimal <- porcentaje_descuento/100
	descuento <- precio * porcentaje_decimal
	precio_final <- precio - descuento
	
	Escribir "El precio final con descuento aplicado es: "
	Escribir "$ " precio_final
FinAlgoritmo
