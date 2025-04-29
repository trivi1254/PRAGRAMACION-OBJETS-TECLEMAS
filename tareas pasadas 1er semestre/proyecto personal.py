import tkinter as tk
import random
import string
from tkinter import messagebox # Importa el módulo para mostrar mensajes emergentes
import os
#cree la ventana principal
ventana = tk.Tk()
ventana.title("generador de contraseñas")
ventana.configure(bg="sky blue")#establece el color de fondo de la ventana
#establezca las dimensiones de la ventana\
ancho = 500
alto = 600
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = (ancho_pantalla - ancho) // 4
pos_y = (alto_pantalla - alto) // 4
ventana.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
#crea los widgets de la interfaz
label_instruccion = tk.Label(ventana,text="Generador de contraseñas",fg="red",font=("Arial black",17),bg="sky blue",borderwidth=5,relief=tk.GROOVE)#crea una etiqueta o titulo
label_instruccion.pack()
label_instruccion = tk.Label(ventana, text="Ingrese el numnero de digitos :",font=("Arial black",12),bg="sky blue",pady=13)#crea una etiqueta o titulo
label_instruccion.pack()
entry_digitos = tk.Entry(ventana)#crea un cuadro de texto para escribir
entry_digitos.pack(pady=10)
label_instruccion = tk.Label(ventana, text="",font=("Arial black",12),bg="sky blue",pady=13)#crea una etiqueta o titulo
label_instruccion.pack()
contraseñas_generadas = []  # Lista para almacenar contraseñas generadas

#funcion para generar contraseñas
def generar_contrasena():
    digitos = int(entry_digitos.get())
    contrasena = ""
    for i in range(digitos):
        contrasena += random.choice(string.ascii_letters + string.digits + string.punctuation)
    label_contrasena = tk.Label(ventana,text=f"Contraseña generada: {contrasena}",font=("Arial black",12),bg="sky blue",pady=10)
    label_contrasena.pack()
    contraseñas_generadas.append(contrasena)#agrega la contraseña generada a la lista de contraseñas
#crea un boton para generar contraseñas
boton_generar = tk.Button(ventana,text="Generar contraseña",font=("Arial black",12),bg="pink",fg="white",command=generar_contrasena)
boton_generar.pack(pady=10)
ventana_contraseñas = None  # Variable para almacenar la ventana secundaria
#guardar contraseñas en un archivo de texto
def guardar_contraseñas():
    if contraseñas_generadas:
        ruta_guardado = os.path.join(os.path.expanduser("~"), "Documents", "contraseñas.txt") # otra forma de crear rutas.

        try:
            with open(ruta_guardado, "w") as archivo:
                for contrasena in contraseñas_generadas:
                    archivo.write(contrasena + "\n")
            messagebox.showinfo("Información", f"Contraseñas guardadas en {ruta_guardado}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el directorio {os.path.dirname(ruta_guardado)}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el archivo: {e}")
    else:
        messagebox.showinfo("Información", "No hay contraseñas para guardar.")

boton_guardar = tk.Button(ventana, text="Guardar contraseñas", font=("Arial black", 12), bg="orange", fg="black", command=guardar_contraseñas)
boton_guardar.pack(pady=10)

ventana.mainloop()
