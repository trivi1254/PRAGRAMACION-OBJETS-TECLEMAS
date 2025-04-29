import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Funciones para resolver diversos problemas matemáticos

def calcular():
    try:
        # Evaluar la expresión matemática ingresada
        expr = entry.get()
        x = sp.symbols('x')  # Definir 'x' como símbolo
        resultado = sp.sympify(expr)
        label_resultado.config(text=f"Resultado: {resultado}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def resolver_ecuacion():
    try:
        # Resolución de ecuaciones algebraicas
        ecuacion = entry.get()
        x = sp.symbols('x')
        solucion = sp.solve(ecuacion, x)
        label_resultado.config(text=f"Solución: {solucion}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def derivada():
    try:
        # Derivada de la función
        expr = entry.get()
        x = sp.symbols('x')
        derivada = sp.diff(expr, x)
        label_resultado.config(text=f"Derivada: {derivada}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def integral():
    try:
        # Integral indefinida de la función
        expr = entry.get()
        x = sp.symbols('x')
        integral = sp.integrate(expr, x)
        label_resultado.config(text=f"Integral: {integral}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def matriz_determinante():
    try:
        # Cálculo del determinante de una matriz
        entrada_matriz = entry.get().split(";")
        matriz = [list(map(float, fila.split())) for fila in entrada_matriz]
        determinante = sp.Matrix(matriz).det()
        label_resultado.config(text=f"Determinante: {determinante}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def resolver_sistema_ecuaciones():
    try:
        # Resolver un sistema de ecuaciones lineales
        ecuaciones = entry.get().split(";")
        x, y, z = sp.symbols('x y z')
        sistema = [sp.Eq(*map(sp.sympify, eq.split('='))) for eq in ecuaciones]
        solucion = sp.solve(sistema, (x, y, z))
        label_resultado.config(text=f"Solución: {solucion}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def raiz_cuadrada():
    try:
        # Raíz cuadrada
        num = float(entry.get())
        resultado = sp.sqrt(num)
        label_resultado.config(text=f"Raíz cuadrada: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingresa un número válido")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Avanzada con SymPy")
ventana.geometry("600x500")
ventana.config(bg="#f4f4f4")

# Etiqueta de instrucciones
label_instrucciones = tk.Label(ventana, text="Ingresa un problema matemático:", bg="#f4f4f4", font=("Arial", 12))
label_instrucciones.pack(pady=10)

# Caja de entrada
entry = tk.Entry(ventana, width=30, font=("Arial", 14), borderwidth=2, relief="solid")
entry.pack(pady=10)

# Botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", font=("Arial", 14), command=calcular, bg="#4CAF50", fg="white", width=10)
boton_calcular.pack(pady=5)

# Resolución de ecuaciones
boton_ecuacion = tk.Button(ventana, text="Resolver Ecuación", font=("Arial", 14), command=resolver_ecuacion, bg="#FF9800", fg="white", width=15)
boton_ecuacion.pack(pady=5)

# Derivada
boton_derivada = tk.Button(ventana, text="Derivada", font=("Arial", 14), command=derivada, bg="#2196F3", fg="white", width=10)
boton_derivada.pack(pady=5)

# Integral
boton_integral = tk.Button(ventana, text="Integral", font=("Arial", 14), command=integral, bg="#2196F3", fg="white", width=10)
boton_integral.pack(pady=5)

# Matriz
boton_matriz = tk.Button(ventana, text="Determinante Matriz", font=("Arial", 14), command=matriz_determinante, bg="#FF5722", fg="white", width=18)
boton_matriz.pack(pady=5)

# Resolver Sistema de Ecuaciones
boton_sistema = tk.Button(ventana, text="Sistema de Ecuaciones", font=("Arial", 14), command=resolver_sistema_ecuaciones, bg="#9C27B0", fg="white", width=18)
boton_sistema.pack(pady=5)

# Raíz cuadrada
boton_raiz = tk.Button(ventana, text="Raíz cuadrada", font=("Arial", 14), command=raiz_cuadrada, bg="#2196F3", fg="white", width=15)
boton_raiz.pack(pady=5)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="Resultado:", bg="#f4f4f4", font=("Arial", 12))
label_resultado.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()