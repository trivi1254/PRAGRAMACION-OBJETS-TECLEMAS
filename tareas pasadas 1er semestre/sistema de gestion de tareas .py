import tkinter as tk
from tkinter import messagebox
import json
import os

# Constantes para mensajes de error
ERROR_ENTRADA_VACIA = "Por favor, ingrese una descripción de la tarea."
ERROR_SELECCION_TAREA = "Por favor, seleccione una tarea."
ERROR_ID_INVALIDO = "ID de tarea inválido."
ERROR_TAREA_NO_ENCONTRADA = "Tarea no encontrada."

class TareaNoEncontradaError(Exception):
    pass

class Tarea:
    """Representa una tarea individual."""

    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class GestorTareas:
    """Gestiona la lógica de las tareas y la persistencia de datos."""

    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        """Carga las tareas desde el archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    data = json.load(file)
                    self.tareas = [Tarea(t["descripcion"], t["completada"]) for t in data]
            except json.JSONDecodeError:
                print("Error al leer el archivo de tareas. Creando un nuevo archivo.")

    def guardar_tareas(self):
        """Guarda las tareas en el archivo JSON."""
        with open(self.archivo, "w") as file:
            json.dump([t.__dict__ for t in self.tareas], file, indent=4)

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()

    def completar_tarea(self, id_tarea):
        """Marca una tarea como completada."""
        if not isinstance(id_tarea, int) or id_tarea <= 0:
            raise ValueError(ERROR_ID_INVALIDO)
        try:
            self.tareas[id_tarea - 1].completada = True
            self.guardar_tareas()
        except IndexError:
            raise TareaNoEncontradaError(ERROR_TAREA_NO_ENCONTRADA)

    def eliminar_tarea(self, id_tarea):
        """Elimina una tarea de la lista."""
        if not isinstance(id_tarea, int) or id_tarea <= 0:
            raise ValueError(ERROR_ID_INVALIDO)
        try:
            self.tareas.pop(id_tarea - 1)
            self.guardar_tareas()
        except IndexError:
            raise TareaNoEncontradaError(ERROR_TAREA_NO_ENCONTRADA)

class Aplicacion:
    """Interfaz gráfica para el gestor de tareas."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        self.gestor = GestorTareas()

        self.lista_tareas = tk.Listbox(self.root, width=50, height=10)
        self.lista_tareas.pack(pady=20)

        self.entry_tarea = tk.Entry(self.root, width=40)
        self.entry_tarea.pack(pady=10)

        self.boton_agregar = tk.Button(self.root, text="Agregar tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(self.root, text="Completar tarea", command=self.completar_tarea)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(self.root, text="Eliminar tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        self.actualizar_lista()

    def actualizar_lista(self):
        """Actualiza la lista de tareas en la interfaz."""
        self.lista_tareas.delete(0, tk.END)
        for i, tarea in enumerate(self.gestor.tareas, 1):
            self.lista_tareas.insert(tk.END, f"{i}. {tarea}")

    def agregar_tarea(self):
        """Controlador para agregar una tarea."""
        descripcion = self.entry_tarea.get()
        if not descripcion:
            messagebox.showwarning("Entrada vacía", ERROR_ENTRADA_VACIA)
            return
        self.gestor.agregar_tarea(descripcion)
        self.entry_tarea.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        """Controlador para completar una tarea."""
        try:
            tarea_id = self._obtener_id_tarea_seleccionada()
            self.gestor.completar_tarea(tarea_id)
            self.actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", ERROR_SELECCION_TAREA)
        except TareaNoEncontradaError:
            messagebox.showerror("Error", ERROR_TAREA_NO_ENCONTRADA)

    def eliminar_tarea(self):
        """Controlador para eliminar una tarea."""
        try:
            tarea_id = self._obtener_id_tarea_seleccionada()
            self.gestor.eliminar_tarea(tarea_id)
            self.actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", ERROR_SELECCION_TAREA)
        except TareaNoEncontradaError:
            messagebox.showerror("Error", ERROR_TAREA_NO_ENCONTRADA)

    def _obtener_id_tarea_seleccionada(self):
        """Obtiene el ID de la tarea seleccionada en la lista."""
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            raise ValueError
        return int(self.lista_tareas.get(seleccion[0]).split(".")[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()