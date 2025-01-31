import tkinter as tk
from tkinter import messagebox
import json

class Contacto:
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono  = telefono
        self.email = email
        self.direccion  = direccion

class GestorContactos:
    def __init__(self, archivo="contactos.json"):
        self.contactos = []
        self.archivo = archivo  # Asignamos el valor a self.archivo
        self.cargar_contactos()  # Carga los contactos desde el archivo

    def cargar_contactos(self):
        """Carga los contactos desde un archivo JSON"""
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
                self.contactos = [Contacto(**c) for c in datos]  # Convierte el diccionario a objetos Contacto
        except FileNotFoundError:
            # Si el archivo no existe, se empieza con una lista vacía
            self.contactos = []

    def guardar_contactos(self):
        """Guarda la lista de contactos en un archivo JSON"""
        with open(self.archivo, "w") as file:
            # Guarda los contactos como una lista de diccionarios
            json.dump([contacto.__dict__ for contacto in self.contactos], file, indent=4)

    def agregar_contacto(self, nombre, telefono, email, direccion):
        """Agrega un nuevo contacto"""
        contacto = Contacto(nombre, telefono, email, direccion)
        self.contactos.append(contacto)
        self.guardar_contactos()  # Guarda los cambios en el archivo

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por nombre"""
        encontrado = False
        for i in range(len(self.contactos)):
            if self.contactos[i].nombre == nombre:
                self.contactos.pop(i)
                encontrado = True
                break
        if encontrado:
            self.guardar_contactos()  # Guarda los cambios en el archivo después de eliminar
        return encontrado

    def editar_contacto(self, nombre, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion):
        """Edita un contacto existente"""
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                contacto.direccion = nueva_direccion
                self.guardar_contactos()  # Guarda los cambios después de editar
                return True
        return False

    def mostrar_contactos(self):
        """Muestra todos los contactos"""
        return self.contactos



class InterfazGrafica:
    def __init__(self, root):
        self.gestor = GestorContactos()
        self.root = root
        self.root.title("Gestor de Contactos")

        # Etiquetas y campos de entrada para agregar contactos
        self.nombre_label = tk.Label(root, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.telefono_label = tk.Label(root, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = tk.Entry(root)
        self.telefono_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.direccion_label = tk.Label(root, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = tk.Entry(root)
        self.direccion_entry.pack()

        # Botón para agregar contacto
        self.agregar_btn = tk.Button(root, text="Agregar contacto", command=self.agregar_contacto)
        self.agregar_btn.pack()

        # Listbox para mostrar los contactos
        self.contactos_listbox = tk.Listbox(root, height=10, width=50)
        self.contactos_listbox.pack()
        self.contactos_listbox.bind('<ButtonRelease-1>', self.contacto_seleccionado)

        # Etiqueta para mostrar el mensaje si no hay contactos
        self.mensaje_no_contactos = tk.Label(root, text="No hay contactos", fg="red")
        self.mensaje_no_contactos.pack()

        # Mostrar contactos al iniciar
        self.mostrar_contactos()

    def agregar_contacto(self):
        nombre = self.nombre_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        direccion = self.direccion_entry.get()

        if not nombre or not telefono or not email or not direccion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        self.gestor.agregar_contacto(nombre, telefono, email, direccion)
        messagebox.showinfo("Éxito", f"Contacto {nombre} agregado correctamente.")

        # Limpiar campos después de agregar
        self.nombre_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

        # Actualizar la vista de contactos
        self.mostrar_contactos()

    def eliminar_contacto(self, nombre, ventana_detalles=None):
        if self.gestor.eliminar_contacto(nombre):
            messagebox.showinfo("Éxito", f"Contacto {nombre} eliminado correctamente.")
            if ventana_detalles:
                ventana_detalles.destroy()  # Cierra la ventana de detalles si está abierta
        else:
            messagebox.showerror("Error", f"El contacto '{nombre}' no existe.")

        # Actualizar la vista de contactos
        self.mostrar_contactos()

    def editar_contacto(self, contacto, ventana_detalles):
        ventana_editar = tk.Toplevel(self.root)
        ventana_editar.title(f"Editar {contacto.nombre}")

        # Crear campos de entrada con los valores actuales del contacto
        nuevo_nombre_label = tk.Label(ventana_editar, text="Nuevo Nombre:")
        nuevo_nombre_label.pack()
        nuevo_nombre_entry = tk.Entry(ventana_editar)
        nuevo_nombre_entry.insert(0, contacto.nombre)
        nuevo_nombre_entry.pack()

        nuevo_telefono_label = tk.Label(ventana_editar, text="Nuevo Teléfono:")
        nuevo_telefono_label.pack()
        nuevo_telefono_entry = tk.Entry(ventana_editar)
        nuevo_telefono_entry.insert(0, contacto.telefono)
        nuevo_telefono_entry.pack()

        nuevo_email_label = tk.Label(ventana_editar, text="Nuevo Email:")
        nuevo_email_label.pack()
        nuevo_email_entry = tk.Entry(ventana_editar)
        nuevo_email_entry.insert(0, contacto.email)
        nuevo_email_entry.pack()

        nueva_direccion_label = tk.Label(ventana_editar, text="Nueva Dirección:")
        nueva_direccion_label.pack()
        nueva_direccion_entry = tk.Entry(ventana_editar)
        nueva_direccion_entry.insert(0, contacto.direccion)
        nueva_direccion_entry.pack()

        # Botón para guardar los cambios de edición
        guardar_btn = tk.Button(ventana_editar, text="Guardar cambios", command=lambda: self.guardar_editar(contacto, nuevo_nombre_entry.get(), nuevo_telefono_entry.get(), nuevo_email_entry.get(), nueva_direccion_entry.get(), ventana_editar, ventana_detalles))
        guardar_btn.pack()

    def guardar_editar(self, contacto, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion, ventana_editar, ventana_detalles):
        if self.gestor.editar_contacto(contacto.nombre, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion):
            messagebox.showinfo("Éxito", f"Contacto {nuevo_nombre} editado correctamente.")
            ventana_editar.destroy()  # Cierra la ventana de edición
            ventana_detalles.destroy()  # Cierra la ventana de detalles
            self.mostrar_contactos()
        else:
            messagebox.showerror("Error", "Error al editar el contacto.")

    def mostrar_contactos(self):
        self.contactos_listbox.delete(0, tk.END)
        contactos = self.gestor.mostrar_contactos()
        
        if len(contactos) == 0:
            self.mensaje_no_contactos.pack()  # Muestra el mensaje si no hay contactos
        else:
            self.mensaje_no_contactos.pack_forget()  # Oculta el mensaje si hay contactos
            for contacto in contactos:
                self.contactos_listbox.insert(tk.END, contacto.nombre)

    def contacto_seleccionado(self, event):
        selected_index = self.contactos_listbox.curselection()
        if selected_index:
            contacto = self.gestor.mostrar_contactos()[selected_index[0]]
            self.abrir_ventana_detalles(contacto)

    def abrir_ventana_detalles(self, contacto):
        ventana_detalles = tk.Toplevel(self.root)
        ventana_detalles.title(f"Detalles de {contacto.nombre}")

        # Mostrar detalles del contacto
        nombre_label = tk.Label(ventana_detalles, text=f"Nombre: {contacto.nombre}")
        nombre_label.pack()
        telefono_label = tk.Label(ventana_detalles, text=f"Teléfono: {contacto.telefono}")
        telefono_label.pack()
        email_label = tk.Label(ventana_detalles, text=f"Email: {contacto.email}")
        email_label.pack()
        direccion_label = tk.Label(ventana_detalles, text=f"Dirección: {contacto.direccion}")
        direccion_label.pack()

        # Botones para eliminar y editar contacto
        eliminar_btn = tk.Button(ventana_detalles, text="Eliminar contacto", command=lambda: self.eliminar_contacto(contacto.nombre, ventana_detalles))
        eliminar_btn.pack()

        editar_btn = tk.Button(ventana_detalles, text="Editar contacto", command=lambda: self.editar_contacto(contacto, ventana_detalles))
        editar_btn.pack()

def main():
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()
