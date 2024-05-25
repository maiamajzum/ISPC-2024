Algoritmo despensa
	
    Definir precio_unitario, unidades, jubilado, costo_total, descuento, monto_total_descuento Como Real
	
    precio_unitario <- 1000
    Escribir "Ingrese la cantidad de leche a comprar en unidades: "
    Leer unidades
    Escribir "Si es jubilado presione 1, sino presione 0: "
    Leer jubilado
	
    costo_total <- unidades * precio_unitario
	
    Si unidades>12 y unidades < 24 Entonces
        descuento <- 0.1  // 10% de descuento
    Sino
        Si unidades > 24 Entonces
            descuento <- 0.15  // 15% de descuento
        Sino
            descuento <- 0  // Sin descuento
        FinSi
    FinSi
	
    // Aplica descuento extra para jubilados
    Si jubilado = 1 Entonces
        descuento <- descuento + 0.1  // 10% de descuento extra
    FinSi
	
    // Calcula el monto total con descuento
    monto_total_descuento <- costo_total * (1 - descuento)
	
    Escribir "Usted debe abonar ", monto_total_descuento, " Pesos"
	
FinAlgoritmo