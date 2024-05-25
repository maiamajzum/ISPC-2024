personas = {}

def mostrar_menu():
    print("MENU")
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
    personas= {'apellido': apellido, 'nombre': nombre,'DNI':dni, 'email': email, 'telefono': telefono}
    print("Persona agregada correctamente.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    if dni in persona:
        print("Persona encontrada:")
        print(persona[dni])
        opcion = input("¿Qué campo desea modificar? (apellido/nombre/email/telefono): ")
        if opcion in persona:
            nuevo_valor = input(f"Ingrese el nuevo valor para {opcion}: ")
            persona[opcion] = nuevo_valor
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
    for dni in persona.items():
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