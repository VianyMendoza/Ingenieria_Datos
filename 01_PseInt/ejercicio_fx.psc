Funcion Saludar(nombre)
	Escribir "Hola ", nombre
Fin Funcion

Función CalcularDoble(num)
	doble<-num*2
	Escribir "El doble es: ", doble
FinFuncion

Función Calculartriple(num)
	triple<-num*3
Escribir "El triple es: ", triple
FinFuncion

Algoritmo ejercicio_funcion
	Escribir "Cuál es tu nombre?"
	Leer nombre_user
	Saludar(nombre_user)
	
	Escribir  "Cuál es el número"
	Leer num_calcular
	CalcularDoble(num_calcular)
	Calculartriple(num_calcular)
FinAlgoritmo
