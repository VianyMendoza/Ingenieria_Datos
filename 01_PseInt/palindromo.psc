Algoritmo palindromo
	Definir palabra, inversa Como Cadena
	Definir i, long Como Entero
	
	Escribir "Ingrese una palabra"
	Leer palabra
	
	long <- Longitud (palabra)
	
	Para i<-long hasta 1 Hacer
		inversa<-Concatenar(inversa, Subcadena(palabra, i, i))
	FinPara
	
	Si palabra=inversa Entonces
		Escribir  "La palabra es palindromo"
	SiNo
		Escribir  "La palabra no es palindromo"
	FinSi
	
FinAlgoritmo
