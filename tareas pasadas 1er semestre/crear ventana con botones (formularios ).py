import tkinter as tk
from tkinter import messagebox


# Función para guardar los datos
def guardar_datos():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()

    # Aquí puedes agregar el código para guardar los datos en un archivo o base de datos
    print(f"Nombre: {nombre}, Correo: {correo}, Teléfono: {telefono}")

    # Mostrar un mensaje de confirmación
    messagebox.showinfo("Registro", "Los datos han sido guardados exitosamente.")

    # Limpiar campos después de guardar
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")

# Crear etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Correo:").grid(row=1, column=0, padx=10, pady=10)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, padx=10, pady=10)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1, padx=10, pady=10)

# Botón para guardar los datos
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.grid(row=3, columnspan=2, pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()