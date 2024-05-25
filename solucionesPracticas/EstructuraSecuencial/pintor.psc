Algoritmo pintor
	definir long, altura, area, manodeobra Como Entero
	Escribir 'Ingrese la longitud de la pared en metros:'
    Leer long
	Escribir 'Ingrese la altura en metros:'
    Leer altura
	Escribir 'Ingrese el costo de mano de obra por metro cuadrado en pesos:'
    Leer costo
	area <- long * altura
	manodeobra <- costo * area
	Escribir 'Usted debe pintar una pared de ', area, ' metros cuadrados'
    Escribir 'El costo de mano de obra será de ', manodeobra, ' pesos'
FinAlgoritmo
