Algoritmo a�oBisiesto
	Definir  a�o Como Entero
	Escribir "�Cu�l es el a�o?"
	Leer a�o
	
	Si a�o MOD 4 = 0 Y a�o MOD 100 <> 0  Entonces
			Escribir "Este a�o es bisiesto"
	SiNo
		Si a�o MOD 100 = 0 Y a�o MOD 400 = 0 Entonces
			Escribir "Este a�o es bisiesto"
		SiNo
			Escribir "Este a�o no es bisiesto"
		Fin Si
	Fin Si
	
FinAlgoritmo
