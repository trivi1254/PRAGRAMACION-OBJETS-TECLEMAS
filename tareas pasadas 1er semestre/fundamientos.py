import tkinter as tk
from tkinter import messagebox
import re  # Importar el módulo para validación de correo


def calcular_propina():
    try:
        nombre = entry_nombre.get().strip()
        apellido = entry_apellido.get().strip()
        cedula = entry_cedula.get().strip()
        correo = entry_correo.get().strip()

        # Validar que los campos de texto no estén vacíos
        if not nombre or not apellido or not cedula or not correo:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Validar formato de correo electrónico
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "Ingrese un correo electrónico válido.")
            return

        # Validar que los campos de monto y propina no estén vacíos
        if not entry_monto.get().strip() or not entry_propina.get().strip():
            messagebox.showerror("Error", "Debe ingresar un monto y una propina.")
            return

        monto = round(float(entry_monto.get().strip()), 2)
        propina = round(float(entry_propina.get().strip()), 2)

        # Aplicar el 15% de incremento al subtotal
        subtotal_incrementado = round(monto * 1.15, 2)  # Aumenta el 15%
        total = round(subtotal_incrementado + propina, 2)

        # Mostrar los resultados
        label_resultado.config(text=f"Nombre: {nombre} {apellido}\n\n"
                                    f"Cédula: {cedula}\n\n"
                                    f"Correo: {correo}\n\n"
                                    f"Subtotal (+15%): ${subtotal_incrementado:.2f}\n\n"
                                    f"Propina: ${propina:.2f}\n\n"
                                    f"Total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos en los campos de monto y propina.")


# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Propinas")
root.geometry("400x650")  # Ventana más espaciosa

# Campos de nombre, apellido y cédula
tk.Label(root, text="Nombre:", font=("Arial", 12)).pack(pady=5)
entry_nombre = tk.Entry(root, font=("Arial", 12))
entry_nombre.pack(pady=5)

tk.Label(root, text="Apellido:", font=("Arial", 12)).pack(pady=5)
entry_apellido = tk.Entry(root, font=("Arial", 12))
entry_apellido.pack(pady=5)

tk.Label(root, text="Correo electrónico:", font=("Arial", 12)).pack(pady=5)
entry_correo = tk.Entry(root, font=("Arial", 12))
entry_correo.pack(pady=5)

tk.Label(root, text="Número de Cédula o RUC:", font=("Arial", 12)).pack(pady=5)
entry_cedula = tk.Entry(root, font=("Arial", 12))
entry_cedula.pack(pady=5)

# Campo para ingresar monto
tk.Label(root, text="Total de la cuenta:", font=("Arial", 12)).pack(pady=5)
entry_monto = tk.Entry(root, font=("Arial", 12))
entry_monto.pack(pady=5)

# Campo para propina
tk.Label(root, text="Propina a agregar:", font=("Arial", 12)).pack(pady=5)
entry_propina = tk.Entry(root, font=("Arial", 12))
entry_propina.pack(pady=5)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", font=("Arial", 12), command=calcular_propina)
btn_calcular.pack(pady=10)

# Label para mostrar los resultados
label_resultado = tk.Label(root, text="", font=("Arial", 12), justify="left")
label_resultado.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()