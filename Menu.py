import tkinter as tk
from tkinter import ttk
import VentanaDefinidas
import VentanaIndefinidas  # Importación del módulo
import VetanaTeoremas

# Función para crear la ventana principal
def create_window():
    # Crear ventana principal
    window = tk.Tk()
    window.title("Calculadora de Integrales")
    window.geometry("400x350")  # Tamaño ideal
    window.config(bg="#eceff1")  # Fondo gris claro

    # Estilo
    style = ttk.Style()
    style.theme_use('clam')  # Usar un tema de estilo
    
    # Estilos para cada botón
    style.configure("DefButton.TButton", font=("Arial", 12), padding=10, ba2a5ckground="#4f5", foreground="white")
    style.map("DefButton.TButton", background=[('active', '#1e88e5')], foreground=[('active', 'white')])
    
    style.configure("IndefButton.TButton", font=("Arial", 12), padding=10, background="#66bb6a", foreground="white")
    style.map("IndefButton.TButton", background=[('active', '#43a047')], foreground=[('active', 'white')])
    
    style.configure("TheoremButton.TButton", font=("Arial", 12), padding=10, background="#ffa726", foreground="white")
    style.map("TheoremButton.TButton", background=[('active', '#fb8c00')], foreground=[('active', 'white')])
    
    style.configure("ExitButton.TButton", font=("Arial", 12), padding=10, background="#ef5350", foreground="white")
    style.map("ExitButton.TButton", background=[('active', '#e53935')], foreground=[('active', 'white')])

    # Título en la ventana
    title_label = ttk.Label(window, text="Calculadora de Integrales", font=("Arial", 16, "bold"), background="#eceff1", foreground="#37474f")
    title_label.pack(pady=20)
    
    # Crear los botones con colores personalizados
    button1 = ttk.Button(window, text="Calcular Integral Definida", style="DefButton.TButton", command=VentanaDefinidas.open_integral_definida_window)
    button1.pack(pady=10)
    
    button2 = ttk.Button(window, text="Calcular Integral Indefinida", style="IndefButton.TButton", command=VentanaIndefinidas.open_integral_indefinida_window)
    button2.pack(pady=10)
    
    button3 = ttk.Button(window, text="Teorema de Integrales", style="TheoremButton.TButton", command=VetanaTeoremas.open_integral_teorema_window)
    button3.pack(pady=10)
    
    button4 = ttk.Button(window, text="Salir", style="ExitButton.TButton", command=window.quit)
    button4.pack(pady=10)

    # Ejecutar la ventana
    window.mainloop()

# Llamar a la función para crear la ventana
create_window()
