Algoritmo ejercicio1
	Escribir "Digita el primer n�mero"
	Leer num1
	Escribir "Digita el segundo n�mero"
	Leer num2
	sumar<- num1+num2
	Escribir "El resultado de sumar "+n1+" + "+n2+"es igual a:" 
	Escribir sumar
	
	Definir radio, diametro, volumen Como Real
	Escribir "�Cu�l es el diametro de tu esfera?"
	Leer diametro
	radio <- diametro/2
	volumen_calc <- 	((4* (radio*radio*radio))*3.14)/3
	Escribir "El volumen de tu esfera es de:" volumen_calc "m3"
	
	Definir numero_repeticiones Como Entero
	Escribir "�Cu�l es tu nombre?"
	Leer nombre_usuario
	Escribir "�Cu�ntas veces lo escribo?"
	Leer numero_repeticiones
	Mientras i < numero_repeticiones Hacer
		Escribir nombre_usuario
		i=i+1
	Fin Mientras
	
	
	Escribir "�Cu�l es el n�mero a evaluar?"
	Leer numero_usuario
	numero_revisado <- numero_usuario/2
	Si	numero_revisado Es entero Entonces
		Escribir "Este n�mero es par"
	SiNo 
		Escribir"Es impar"
	FinSi
	
	Definir numero_factorial Como Entero
	Escribir "�Cu�l es el n�mero a factorizar?"
	Leer numero_factorial
	Mientras i>=1 Hacer
		suma_final <- (numero_factorial*i)+(numero_factorial*i)
	FinMientras
	i=numero_factorial-1
	
	
	
FinAlgoritmo
