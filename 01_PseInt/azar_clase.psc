Algoritmo azar_clase
	Definir num_intento, num_azar Como Entero
	num_random <- azar (100)
	intentos <- 10
	
	Escribir "Adivina el n�mero entre 0 y 100:"
	Escribir "Te quedan " intentos " intentos"	
	Leer num_intento
	
	Mientras intentos > 1 y num_random <> num_intento Hacer
		Si num_random > num_intento Entonces
			Escribir "El n�mero es muy bajo"
			intentos <- intentos - 1
			Escribir "Te quedan " intentos " intentos"	
			Escribir "Adivina el n�mero entre 0 y 100:"
			Leer num_intento
		SiNo
			Si num_random < num_intento Entonces
				Escribir "El n�mero es muy alto"
				intentos <- intentos - 1
				Escribir "Te quedan " intentos " intentos"	
				Escribir "Adivina el n�mero entre 0 y 100:"
				Leer num_intento
			SiNo 
				Escribir "Ganaste"
			Fin Si
		Fin Si
	Fin Mientras
	
	Si num_random = num_intento Entonces
		Escribir "Ganaste"
	SiNo
		Escribir "Perdiste, el n�mero era " num_random
	Fin Si
		
FinAlgoritmo
