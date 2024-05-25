#pedir al usuario ingresar 10 nombres no repetidos, guardarlos en una lista y mostrarlos

nombres= []
for n in range (10):
    nombre= str(input("Ingrese un mombre: "))
    if nombre in nombres:
         print ("El nombre ya se encuentra en la lista, intente con otro")
    else:
         nombres.append(nombre)
print("Los nombres ingresados son: ")
for nombre in nombres:
     print(nombre)

#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

del nombres [2]
del nombres [-1]
nombres.sort()
print("La lista con los datos eliminados es: ")
for nombre in nombres:
     print(nombre)