Funcion Saludar(nombre)
	Escribir "Hola ", nombre
Fin Funcion

Funci�n CalcularDoble(num)
	doble<-num*2
	Escribir "El doble es: ", doble
FinFuncion

Funci�n Calculartriple(num)
	triple<-num*3
Escribir "El triple es: ", triple
FinFuncion

Algoritmo ejercicio_funcion
	Escribir "Cu�l es tu nombre?"
	Leer nombre_user
	Saludar(nombre_user)
	
	Escribir  "Cu�l es el n�mero"
	Leer num_calcular
	CalcularDoble(num_calcular)
	Calculartriple(num_calcular)
FinAlgoritmo
