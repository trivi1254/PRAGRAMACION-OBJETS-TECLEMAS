import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import sqlite3

class RentCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("zxRentCar - Registro de Clientes")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Variables de control
        self.dni_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.modelo_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.fecha_nacimiento_var = tk.StringVar()
        self.tiene_tc_var = tk.StringVar(value="No")
        
        self.create_database()
        self.create_widgets()
        self.load_data()
    
    def create_database(self):
        """Crea la base de datos y la tabla si no existen"""
        conn = sqlite3.connect('zxrentcar.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                dni TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                modelo TEXT NOT NULL,
                marca TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL,
                tiene_tc TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar expansión de columnas y filas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="Registro de Clientes", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Campos del formulario
        ttk.Label(main_frame, text="DNI:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.dni_var, width=30).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Nombre:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.nombre_var, width=30).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Modelo:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.modelo_var, width=30).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Marca:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.marca_var, width=30).grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Fecha de Nacimiento:").grid(row=5, column=0, sticky=tk.W, pady=5)
        fecha_frame = ttk.Frame(main_frame)
        fecha_frame.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)
        ttk.Entry(fecha_frame, textvariable=self.fecha_nacimiento_var, width=20).pack(side=tk.LEFT)
        ttk.Button(fecha_frame, text="Seleccionar", command=self.select_date).pack(side=tk.LEFT, padx=(5, 0))
        
        ttk.Label(main_frame, text="¿Tiene tarjeta de crédito?").grid(row=6, column=0, sticky=tk.W, pady=5)
        tc_frame = ttk.Frame(main_frame)
        tc_frame.grid(row=6, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(tc_frame, text="Sí", variable=self.tiene_tc_var, value="Sí").pack(side=tk.LEFT)
        ttk.Radiobutton(tc_frame, text="No", variable=self.tiene_tc_var, value="No").pack(side=tk.LEFT, padx=(10, 0))
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)
        ttk.Button(button_frame, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT)
        
        # Tabla de datos
        ttk.Label(main_frame, text="Clientes Registrados:", font=("Arial", 12, "bold")).grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=(20, 10))
        
        # Crear Treeview (tabla)
        columns = ("dni", "nombre", "modelo", "marca", "fecha_nacimiento", "tiene_tc")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=10)
        
        # Definir encabezados
        self.tree.heading("dni", text="DNI")
        self.tree.heading("nombre", text="Nombres")
        self.tree.heading("modelo", text="Modelo")
        self.tree.heading("marca", text="Marca")
        self.tree.heading("fecha_nacimiento", text="FeNacimiento")
        self.tree.heading("tiene_tc", text="Tiene t/c")
        
        # Definir anchos de columnas
        self.tree.column("dni", width=100)
        self.tree.column("nombre", width=150)
        self.tree.column("modelo", width=100)
        self.tree.column("marca", width=100)
        self.tree.column("fecha_nacimiento", width=120)
        self.tree.column("tiene_tc", width=80)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=9, column=2, sticky=(tk.N, tk.S))
        
        # Configurar expansión para la fila de la tabla
        main_frame.rowconfigure(9, weight=1)
    
    def select_date(self):
        """Abre un diálogo para seleccionar fecha (simulado)"""
        # En una implementación real, aquí se abriría un calendario
        # Por ahora, usamos un valor de ejemplo
        self.fecha_nacimiento_var.set("01/01/2000")
    
    def calcular_edad(self, fecha_nacimiento):
        """Calcula la edad basada en la fecha de nacimiento"""
        try:
            nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
            hoy = date.today()
            edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
            return edad
        except ValueError:
            return 0
    
    def guardar(self):
        """Valida y guarda los datos en la base de datos"""
        # Validar campos obligatorios
        if not all([self.dni_var.get(), self.nombre_var.get(), self.modelo_var.get(), 
                   self.marca_var.get(), self.fecha_nacimiento_var.get()]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Validar edad (mayor de 18 años)
        edad = self.calcular_edad(self.fecha_nacimiento_var.get())
        if edad < 18:
            messagebox.showerror("Error", "El cliente debe ser mayor de 18 años")
            return
        
        # Validar tarjeta de crédito
        if self.tiene_tc_var.get() == "No":
            messagebox.showerror("Error", "El cliente debe tener tarjeta de crédito")
            return
        
        # Guardar en la base de datos
        try:
            conn = sqlite3.connect('zxrentcar.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clientes (dni, nombre, modelo, marca, fecha_nacimiento, tiene_tc)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.dni_var.get(), self.nombre_var.get(), self.modelo_var.get(),
                 self.marca_var.get(), self.fecha_nacimiento_var.get(), self.tiene_tc_var.get()))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Éxito", "Cliente registrado correctamente")
            self.limpiar()
            self.load_data()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El DNI ya existe en la base de datos")
    
    def limpiar(self):
        """Limpia todos los campos excepto la tabla"""
        self.dni_var.set("")
        self.nombre_var.set("")
        self.modelo_var.set("")
        self.marca_var.set("")
        self.fecha_nacimiento_var.set("")
        self.tiene_tc_var.set("No")
    
    def load_data(self):
        """Carga los datos en la tabla"""
        # Limpiar tabla existente
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Cargar datos desde la base de datos
        conn = sqlite3.connect('zxrentcar.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        conn.close()
        
        # Insertar datos en la tabla
        for row in rows:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = RentCarApp(root)
    root.mainloop()