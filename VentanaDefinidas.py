import tkinter as tk
from tkinter import messagebox, scrolledtext
import CalculoDefinidas  # Importar el archivo CalculoDefinidas.py

def open_integral_definida_window():
    # Crear la ventana para calcular la integral definida
    window = tk.Toplevel()
    window.title("Calcular Integral Definida")
    window.geometry("400x400")  # Tamaño de la ventana
    window.config(bg="#eceff1")  # Fondo gris claro

    # Título
    title_label = tk.Label(window, text="Calcular Integral Definida", font=("Arial", 16, "bold"), bg="#eceff1", fg="#37474f")
    title_label.pack(pady=10)

    # Función, límite inferior y límite superior
    label_funcion = tk.Label(window, text="Función:", font=("Arial", 12), bg="#eceff1")
    label_funcion.pack(pady=5)
    entry_funcion = tk.Entry(window, font=("Arial", 12))
    entry_funcion.pack(pady=5)

    label_lim_inf = tk.Label(window, text="Límite Inferior:", font=("Arial", 12), bg="#eceff1")
    label_lim_inf.pack(pady=5)
    entry_lim_inf = tk.Entry(window, font=("Arial", 12))
    entry_lim_inf.pack(pady=5)

    label_lim_sup = tk.Label(window, text="Límite Superior:", font=("Arial", 12), bg="#eceff1")
    label_lim_sup.pack(pady=5)
    entry_lim_sup = tk.Entry(window, font=("Arial", 12))
    entry_lim_sup.pack(pady=5)

    # Botón para calcular
    button_calcular = tk.Button(window, text="Calcular", font=("Arial", 12), bg="#42a5f5", fg="white", command=lambda: calcular_integral(entry_funcion.get(), entry_lim_inf.get(), entry_lim_sup.get()))
    button_calcular.pack(pady=20)

    # Text Area para mostrar resultados
    resultado_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
    resultado_area.pack(pady=10)

    def calcular_integral(funcion, lim_inf, lim_sup):
        try:
            lim_inf = float(lim_inf)
            lim_sup = float(lim_sup)
            resultado, pasos = CalculoDefinidas.calcular_integral_definida(funcion, lim_inf, lim_sup)
            resultado_area.delete(1.0, tk.END)  # Limpiar área de texto
            resultado_area.insert(tk.END, resultado + "\n" + pasos)  # Mostrar resultados
        except Exception as e:
            messagebox.showerror("Error", str(e))

    window.mainloop()
