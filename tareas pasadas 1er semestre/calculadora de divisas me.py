import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Divisas")

# Establecer dimensiones de la ventana
ancho = 400
alto = 500
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = (ancho_pantalla - ancho) // 4
pos_y = (alto_pantalla - alto) // 4
ventana.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")

# Crear los widgets de la interfaz
label_instruccion = tk.Label(ventana, text="Ingresa la cantidad:")
label_instruccion.pack()

entry_dolares = tk.Entry(ventana)
entry_dolares.pack(pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=20)

# Función de conversión de dólares a euros
def convertir_dolares_a_euros():
    try:
        dolares = float(entry_dolares.get())  # Obtener el valor ingresado
        tasa_cambio = 0.85  # Ejemplo de tasa de cambio
        euros = dolares * tasa_cambio
        label_resultado.config(text=f"{dolares} dólares son {euros:.2f} euros.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido.")

# Función de conversión de euros a dólares
def convertir_euros_a_dolares():
    try:
        euros = float(entry_dolares.get())  # Obtener el valor ingresado
        tasa_cambio = 1.18  # Ejemplo de tasa de cambio (1 euro = 1.18 dólares)
        dolares = euros * tasa_cambio
        label_resultado.config(text=f"{euros} euros son {dolares:.2f} dólares.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido.")

# Crear botones para las conversiones
opcion1 = tk.Button(ventana, text="1. Dólares a Euros", command=convertir_dolares_a_euros)
opcion1.pack(pady=10)

opcion2 = tk.Button(ventana, text="2. Euros a Dólares", command=convertir_euros_a_dolares)
opcion2.pack(pady=10)

# Iniciar la ventana principal
ventana.mainloop()
