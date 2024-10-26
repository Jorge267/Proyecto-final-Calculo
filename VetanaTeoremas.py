import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, integrate, simplify

# Variables globales
x = symbols('x')
pasos = []  # Lista para almacenar los pasos detallados de integración

# Función para abrir la ventana de integral teorema
def open_integral_teorema_window():
    # Crear la ventana para calcular la integral teorema
    window = tk.Toplevel()
    window.title("Calcular Integral teorema")
    window.geometry("600x700")  # Ajustar tamaño según necesidades
    window.config(bg="#eceff1")

    # Título
    title_label = tk.Label(window, text="Calcular Integral teorema", font=("Arial", 16, "bold"), bg="#eceff1", fg="#37474f")
    title_label.pack(pady=10)

    # Función de entrada
    label_funcion = tk.Label(window, text="Función:", font=("Arial", 12), bg="#eceff1")
    label_funcion.pack(pady=5)
    entry_funcion = tk.Entry(window, font=("Arial", 12), width=40)
    entry_funcion.pack(pady=5)

    # Área de texto para mostrar resultados y pasos
    resultado_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15, font=("Arial", 12))
    resultado_area.pack(pady=10)

    # Función para calcular la integral y mostrar los pasos detallados
    def calcular_integral(funcion):
        global pasos
        pasos = []  # Reiniciar pasos para cada cálculo
        try:
            # Interpretar la función introducida por el usuario
            expr = eval(funcion)
            pasos.append(f"Paso 1: Interpretación de la función: f(x) = {expr}")

            # Simplificar la expresión, si es posible
            expr_simplificada = simplify(expr)
            pasos.append(f"Paso 2: Simplificación (si es aplicable): {expr_simplificada}")

            # Calcular la integral
            integral_expr = integrate(expr_simplificada, x)
            pasos.append(f"Paso 3: Cálculo de la integral indefinida: ∫ f(x) dx = {integral_expr}")

            # Simplificar el resultado final de la integral, si aplica
            integral_expr_simplificada = simplify(integral_expr)
            pasos.append(f"Paso 4: Simplificación de la integral resultante: F(x) = {integral_expr_simplificada}")

            # Mostrar resultados y pasos en el área de texto
            resultado_area.delete(1.0, tk.END)
            resultado_area.insert(tk.END, f"Resultado: {integral_expr_simplificada}\n\n" + "\n".join(pasos))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Función para graficar la integral teorema
    def graficar_integral(funcion):
        try:
            expr = eval(funcion)
            integral_expr = integrate(expr, x)
            integral_func = lambdify(x, integral_expr, modules=['numpy'])
            valores_x = np.linspace(-10, 10, 400)
            valores_y = integral_func(valores_x)
            plt.plot(valores_x, valores_y, label=f"Integral de {funcion}")
            plt.xlabel('x')
            plt.ylabel('F(x)')
            plt.title('Gráfica de la Integral teorema')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            messagebox.showerror("Error al graficar", str(e))

    # Botones en el frame
    button_frame = tk.Frame(window, bg="#eceff1")
    button_frame.pack(pady=10)

    # Botón Calcular
    button_calcular = tk.Button(button_frame, text="Calcular", font=("Arial", 12), bg="#42a5f5", fg="white", 
                                 command=lambda: calcular_integral(entry_funcion.get()))
    button_calcular.pack(side=tk.LEFT, padx=5)

    # Botón Graficar
    button_graficar = tk.Button(button_frame, text="Graficar", font=("Arial", 12), bg="#66bb6a", fg="white", 
                                command=lambda: graficar_integral(entry_funcion.get()))
    button_graficar.pack(side=tk.LEFT, padx=5)

    # Botón para regresar
    button_regresar = tk.Button(button_frame, text="Regresar", font=("Arial", 12), bg="#ffa726", fg="white", command=window.destroy)
    button_regresar.pack(side=tk.LEFT, padx=5)

    # Botón para salir
    button_salir = tk.Button(button_frame, text="Salir", font=("Arial", 12), bg="#ef5350", fg="white", command=window.quit)
    button_salir.pack(side=tk.LEFT, padx=5)

    window.mainloop()
