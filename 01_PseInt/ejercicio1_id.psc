Algoritmo ejercicio1_id
	
	Definir num1, num2 Como Real	
	Escribir  "�Cu�l es el primer n�mero a sumar?"
	Leer  num1
	Escribir  "�Cu�l es el segundo n�mero a sumar?"
	Leer  num2
	suma <- num1+num2
	Escribir "El resultado de sumar " num1 " y " num2 " es: " suma
	resta <- num1 - num2
	Escribir "El resultado de restar " num1 " y " num2 " es: " resta
	multiplicacion <- num1 * num2
	Escribir "El resultado de multiplicar " num1 " y " num2 " es: " multiplicacion
	
	Definir long_rect, alt_rect, area_rect Como Real
	Escribir "�Cu�l es la altura de tu rect�ngulo?"
	Leer alt_rect
	Escribir "�Cu�l es la longitug de tu rect�ngulo?"
	Leer long_rect
	area_rect <- alt_rect*long_rect
	Escribir "El �rea de tu rect�ngulo es de " area_rect "m2"
	
	Definir radio_circ, area Como Real
	Escribir "�Cu�l es el radio de tu c�rculo?"
	Leer radio_circ
	area_circ <- (PI) * (radio_circ *radio_circ)
	Escribir "El �rea de tu c�rculo es de " area_circ "m2"
	
	Definir long_triang, alt_triang, area_triang Como Real
	Escribir "�Cu�l es la altura de tu tri�ngulo?"
	Leer alt_triang
	Escribir "�Cu�l es la longitug de tu tri�ngulo?"
	Leer long_triang
	area_triang <- (alt_triang*long_triang)/2
	Escribir "El �rea de tu tri�ngulo es de " area_triang "m2"
	
	Definir a, b, c, resultado_x Como Real
	Escribir "�Cu�l es el valor de a?"
	Leer a
	Escribir "�Cu�l es el valor de a?"
	Leer b
	Escribir "�Cu�l es el valor de a?"
	Leer c
	resultado_x <- raiz((b*b)-4*(a)*(c))
	Escribir "El resultado de la raiz cuadrada para tu ecuaci�n es " resultado_x
		
	Definir sueldo Como Real
	Escribir "�Cu�l es tu sueldo mensual?"
	Leer sueldo
	sueldo_anual <- sueldo*12
	Escribir "Tu sueldo anual como programador es de $" sueldo_anual
	
	Definir grados_celcius, grados_farenheit Como Real
	Escribir  "Cu�l es la temperatura en grados Celsius?"
	Leer grados_celcius
	grados_farenheit <- (1.8*grados_celcius)+32
	Escribir "La temperatura en grados Farenheit es de " grados_farenheit "�"
	
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
























