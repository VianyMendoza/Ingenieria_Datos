Algoritmo promedio_alumno
	Definir cantidad_notas Como Entero
	Definir acumulado_notas Como Real
	Definir promedio Como Real
		Escribir ("¿Cuántas notas ingresarás?")
		Leer cantidad_notas
		acumulado_notas<-0
		Para i<-1 Hasta cantidad_notas Hacer
			Escribir "Notas ",i," obtenida por el alumno:"
			Leer nta
			acumulado_notas<-acumulado_notas+nta
			
		FinPara
		
		promedio<-acumulado_notas/cantidad_notas
		
		Escribir "El promedio es: ",promedio
	
FinAlgoritmo
