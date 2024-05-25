Algoritmo pintor
    definir ancho, alto, area, manodeobra Como Entero
    Escribir 'Ingrese el ancho de la pared en metros:'
    Leer ancho
    Escribir 'Ingrese el alto en metros:'
    Leer alto
    Escribir 'Ingrese el costo de mano de obra por metro cuadrado en pesos:'
    Leer costo
    area <- ancho * alto
    manodeobra <- costo * area
    Escribir 'Usted debe pintar una pared de ', area, ' metros cuadrados'
    Escribir 'El costo de mano de obra será de ', manodeobra, ' pesos'
FinAlgoritmo
