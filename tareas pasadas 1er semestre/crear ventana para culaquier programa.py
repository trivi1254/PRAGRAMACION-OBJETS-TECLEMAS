import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Dimensiones")  # Título de la ventana

# Establecer las dimensiones de la ventana
ancho = 400  # Ancho de la ventana
alto = 500   # Alto de la ventana

# Calcular la posición para centrar la ventana en la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = (ancho_pantalla - ancho) // 2
pos_y = (alto_pantalla - alto) //  2
# Configurar el tamaño y la posición de la ventana
ventana.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")

# Iniciar el bucle principal de la ventana
ventana.mainloop()
