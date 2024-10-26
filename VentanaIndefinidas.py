import tkinter as tk
from tkinter import messagebox, scrolledtext
import CalculoIndefinidas  
import GraficarIndefinidad # Importar el archivo CalculoIndefinidas.py

def open_integral_indefinida_window():
    # Crear la ventana para calcular la integral indefinida
    window = tk.Toplevel()
    window.title("Calcular Integral Indefinida")
    window.geometry("400x400")  # Tamaño de la ventana
    window.config(bg="#eceff1")  # Fondo gris claro

    # Título
    title_label = tk.Label(window, text="Calcular Integral Indefinida", font=("Arial", 16, "bold"), bg="#eceff1", fg="#37474f")
    title_label.pack(pady=10)

    # Función a integrar
    label_funcion = tk.Label(window, text="Función:", font=("Arial", 12), bg="#eceff1")
    label_funcion.pack(pady=5)
    entry_funcion = tk.Entry(window, font=("Arial", 12))
    entry_funcion.pack(pady=5)

    # Text Area para mostrar resultados
    resultado_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
    resultado_area.pack(pady=10)

    def calcular_integral(funcion):
        try:
            resultado, pasos = CalculoIndefinidas.calcular_integral_indefinida(funcion)  # Lógica para integral indefinida
            resultado_area.delete(1.0, tk.END)  # Limpiar área de texto
            resultado_area.insert(tk.END, resultado + "\n" + pasos)  # Mostrar resultados
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Frame para los botones
    button_frame = tk.Frame(window, bg="#eceff1")
    button_frame.pack(pady=10)

    # Botón para calcular
    button_calcular = tk.Button(button_frame, text="Calcular", font=("Arial", 12), bg="#42a5f5", fg="white",  
                                 command=lambda: calcular_integral(entry_funcion.get()))
    button_calcular.pack(side=tk.LEFT, padx=5)

    button_graficar = tk.Button(button_frame, text="Graficar", font=("Arial", 12), bg="#66bb6a", fg="white",  
    command=lambda: GraficarIndefinidad.graficar_integral_indefinida(entry_funcion.get()))
    button_graficar.pack(side=tk.LEFT, padx=5)


    # Botón para regresar al menú
    button_regresar = tk.Button(button_frame, text="Regresar al Menú", font=("Arial", 12), bg="#ffa726", fg="white", command=window.destroy)
    button_regresar.pack(side=tk.LEFT, padx=5)

    # Botón para salir
    button_salir = tk.Button(button_frame, text="Salir", font=("Arial", 12), bg="#ef5350", fg="white", command=window.quit)
    button_salir.pack(side=tk.LEFT, padx=5)

    # Asegurarse de que la ventana se mantenga abierta
    window.mainloop()

