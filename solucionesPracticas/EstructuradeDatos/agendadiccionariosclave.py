#Desaroollar un modulo que gestione una agenda teefonica en un diccionario. Mostrar un menu de opciones:
#1 Agregar una persona (apellido, nombre, dni, email y número de teléfono)
#2 Modificar una persona dado su DNI
#3 Eliminar una persona segun su DNI
#4 Mostrar toda la agenda
#5 Salir


agenda = {}

def mostrar_menu():
    print("Ingrese el número de la opción deseada")
    print("1. Agregar persona")
    print("2. Modificar persona")
    print("3. Eliminar persona")
    print("4. Mostrar agenda")
    print("5. Salir")

def agregar_persona():
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    dni = input("Ingrese el DNI: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[dni] = {'apellido': apellido, 'nombre': nombre, 'email': email, 'telefono': telefono}
    print("Persona agregada correctamente.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    if dni in agenda:
        print("Persona encontrada:")
        print(agenda[dni])
        opcion = input("¿Qué campo desea modificar? (apellido/nombre/email/telefono): ")
        if opcion in agenda[dni]:
            nuevo_valor = input(f"Ingrese el nuevo valor para {opcion}: ")
            agenda[dni][opcion] = nuevo_valor
            print("Persona modificada correctamente.")
        else:
            print("Campo no válido.")
    else:
        print("Persona no encontrada.")

def eliminar_persona():
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada correctamente.")
    else:
        print("Persona no encontrada.")

def mostrar_agenda():
    print("Agenda")
    for dni, persona in agenda.items():
        print("DNI:", dni)
        print("Apellido:", persona['apellido'])
        print("Nombre:", persona['nombre'])
        print("Email:", persona['email'])
        print("Teléfono:", persona['telefono'])
        


while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            agregar_persona()
        elif opcion == '2':
            modificar_persona()
        elif opcion == '3':
            eliminar_persona()
        elif opcion == '4':
            mostrar_agenda()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")