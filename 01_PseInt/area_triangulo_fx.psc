Funcion CalculoTriangulo(base, altura)
	area<- (base*altura)/2
	Escribir "El área de tu triángulo es de " area "m2"
Fin Funcion

Algoritmo AreaTriangulo
	Escribir "¿Cuál es la altura de tu triángulo?"
	Leer altura
	Escribir "¿Cuál es la longitug de tu triángulo?"
	Leer base
	CalculoTriangulo(base, altura)
FinAlgoritmo
