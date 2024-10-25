import tkinter as tk
from tkinter import messagebox, scrolledtext
import CalculoDefinidas  # Importar el archivo CalculoDefinidas.py
import GraficarDefinida  # Importar el archivo GraficarDefinida.py

def open_integral_indefinida_window():

    window = tk.Toplevel()
    window.title("Calcular Integral Definida")
    window.geometry("400x500")  # Tamaño de la ventana aumentado
    window.config(bg="#eceff1")  # Fondo gris claro



    

    window.mainloop()