def mostrar_menu():
    print("Ingrese el número de la opción deseada")
    print("1. Agregar persona")
    print("2. Modificar persona")
    print("3. Eliminar persona")
    print("4. Mostrar agenda")
    print("5. Salir")

def agregar_persona(agenda):
    persona = {}
    persona['apellido'] = input("Ingrese el apellido: ")
    persona['nombre'] = input("Ingrese el nombre: ")
    persona['dni'] = input("Ingrese el DNI: ")
    persona['email'] = input("Ingrese el email: ")
    persona['telefono'] = input("Ingrese el número de teléfono: ")
    agenda.append(persona)
    print("Persona agregada correctamente.")

def modificar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    for persona in agenda:
        if persona['dni'] == dni:
            print("Persona encontrada:")
            print(persona)
            opcion = input(("¿Qué campo desea modificar? (apellido/nombre/email/telefono): "))
            if opcion in persona:
                nuevo_valor = input(f"Ingrese el nuevo valor para {opcion}: ")
                persona[opcion]=nuevo_valor
                print("Persona modificada correctamente.")
        else:    
            print("Persona no encontrada.")

def eliminar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")
    for persona in agenda:
        if persona['dni'] == dni:
            agenda.remove(persona)
            print("Persona eliminada correctamente.")
            
        else:
            print("Persona no encontrada.")

def mostrar_agenda(agenda):
    print("Agenda")
    for persona in agenda:
        print("DNI:", persona['dni'])
        print("Apellido:", persona['apellido'])
        print("Nombre:", persona['nombre'])
        print("Email:", persona['email'])
        print("Teléfono:", persona['telefono'])


agenda = []
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de opción: ")

    if opcion == '1':
        agregar_persona(agenda)
    elif opcion == '2':
        modificar_persona(agenda)
    elif opcion == '3':
        eliminar_persona(agenda)
    elif opcion == '4':
        mostrar_agenda(agenda)
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")