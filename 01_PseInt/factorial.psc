Algoritmo factorial
	Definir numFact Como Entero
	Escribir "�Cu�l es el n�mero a factorizar?"
	Leer numFact
	i <- numFact
	Escribir i
	
	Mientras i>1 Hacer
		i <- i-1
		numFact <- numFact * i
	Fin Mientras
	
	Escribir "El resultado es " numFact
	
FinAlgoritmo