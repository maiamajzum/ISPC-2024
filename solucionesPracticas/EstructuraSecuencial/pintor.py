#Un pintor de casas debe hacer un presupuesto para un cliente. 
#Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar.
#El cliente necesita saber el costo de la mano de obra para pintar una pared rectangular.
#El pintor cobra un monto fijo por metro cuadrado.
#Se requiere conocer el costo de mano de obra.

ancho = int (input ('Ingrese el ancho de la pared en metros: '))
alto = int (input ('Ingrese el alto en metros: '))
costo =  int (input ('Ingrese el costo de mano de obra por metro cuadrado en pesos: '))

area = ancho*alto
manodeobra= costo*area
print('Usted debe pintar una pared de ',area, ' metros cuadrados')
print('El costo de mano de obra sera de ',manodeobra, 'pesos')