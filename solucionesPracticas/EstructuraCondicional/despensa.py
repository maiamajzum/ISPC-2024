#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
#Si el cliente compra desde 12 hasta 24 unidades el costo tiene un descuento del 10%.
#Mas de 24 u el descuento es del 15 %
#Jubilado 10% de descuento extra al total.
#calcular cuanto paga el cliente

precio_unitario = 1000
unidades = int(input("Ingrese la cantidad de leche a comprar en unidades: "))
jubilado = int(input("Si es jubilado presione 1, sino presione 0: "))

costo_total = unidades * precio_unitario

if 12 <= unidades <= 24:
    descuento = 0.1  # 10% de descuento
elif unidades > 24:
    descuento = 0.15  # 15% de descuento
else:
    descuento = 0  # Sin descuento

# Aplica descuento extra para jubilados
if jubilado == 1:
    descuento += 0.1  # 10% de descuento extra

# Calcula el monto total con descuento
monto_total_descuento = costo_total * (1 - descuento)

print(f"Usted debe abonar {monto_total_descuento} Pesos")
