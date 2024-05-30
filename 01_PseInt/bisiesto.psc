Algoritmo añoBisiesto
	Definir  año Como Entero
	Escribir "¿Cuál es el año?"
	Leer año
	
	Si año MOD 4 = 0 Y año MOD 100 <> 0  Entonces
			Escribir "Este año es bisiesto"
	SiNo
		Si año MOD 100 = 0 Y año MOD 400 = 0 Entonces
			Escribir "Este año es bisiesto"
		SiNo
			Escribir "Este año no es bisiesto"
		Fin Si
	Fin Si
	
FinAlgoritmo
