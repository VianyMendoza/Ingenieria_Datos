Algoritmo aleatorio_alg

	Definir num_secreto, num_intento Como Entero
	num_secreto <- Aleatorio(1,5)
	i<-1
	Escribir "Adivina el n�mero, intento " i " de 10"
	Leer num_intento
	i=i+1
	Si num_intento <> num_secreto Entonces
		Repetir
			Escribir "Fallaste, int�ntalo de nuevo. Intento " i " de 10"
			Leer num_intento
			Si num_intento <> num_secreto Entonces
				Escribir "Fallaste, int�ntalo de nuevo. Intento " i " de 10"
				Leer num_intento	
			SiNo
				Escribir "Felicidades!! Adivinaste el n�mero"
			Fin Si
			i=i+1
		Hasta Que i=10
		
	SiNo
		Escribir "Felicidades!! Adivinaste el n�mero"
	Fin Si
	
	
	
FinAlgoritmo
