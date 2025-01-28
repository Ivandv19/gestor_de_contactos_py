class Contacto:

    def __init__(self, nombre, Teléfono, email, dirección):
        self.nombre = nombre
        self.Teléfono = Teléfono
        self.email = email
        self.dirección = dirección

class GestorContactos:

    def __init__(self):
        self.contactos = []
        
    def agregar_contacto(self, nombre, Teléfono, email, dirección):
        contacto = Contacto(nombre, Teléfono, email, dirección)
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        encontrado = False  # Variable para verificar si se encuentra el contacto
        for i in range(len(self.contactos)):
            if self.contactos[i].nombre == nombre:  # Comparamos el nombre del contacto
                print(f"Contacto '{nombre}' eliminado correctamente.")
                self.contactos.remove(self.contactos[i])  # Eliminamos el contacto
                encontrado = True
                break  # Salimos del bucle una vez eliminado
        
        if not encontrado:
            print(f"El contacto '{nombre}' no existe.")  # Si no se encuentra el contacto, mostramos el mensaje

    def mostrar_contactos(self):
    # Mostrar solo el número de contactos
        print(f"\nNúmero de contactos: {len(self.contactos)}")
    
    # Si hay contactos, mostramos sus detalles
        if self.contactos:
            contactos_info = []
            for contacto in self.contactos:
                contactos_info.append(f"Nombre: {contacto.nombre}, Teléfono: {contacto.Teléfono}, Email: {contacto.email}, Dirección: {contacto.dirección}")
            return "\n".join(contactos_info)
        return ""  # Si no hay contactos, no se muestra nada más

def mostrar_menu():
    print("\n--- Menú de Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    return input("Elige una opción: ")

def main():
    gestor = GestorContactos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingresa el nombre del contacto: ")
            telefono = input("Ingresa el teléfono del contacto: ")
            email = input("Ingresa el email del contacto: ")
            direccion = input("Ingresa la dirección del contacto: ")
            gestor.agregar_contacto(nombre, telefono, email, direccion)
            print(f"Contacto {nombre} agregado correctamente.")
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            gestor.eliminar_contacto(nombre)
        
        elif opcion == "3":
            print("\nLista de contactos:")
            print(gestor.mostrar_contactos())
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción válida.")

if __name__ == "__main__":
    main()
