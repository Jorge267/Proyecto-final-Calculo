import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, integrate, Function

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Integrales con Gráfica")

# Variables
x = symbols('x')
input_text = tk.StringVar()
pasos = []  # Lista para almacenar los pasos de integración

# Caja de texto para la expresión matemática
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=4, width=50, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

# Función para obtener el input de la caja de texto
def click_button(value):
    current_text = input_text.get()
    input_text.set(current_text + str(value))

# Función para limpiar el input
def clear():
    input_text.set("")
    global pasos
    pasos = []  # Limpiar los pasos

# Función para calcular la integral y graficarla
def calcular_y_graficar():
    global pasos
    pasos = []  # Reiniciar pasos al calcular una nueva integral
    try:
        # Obtener la expresión ingresada por el usuario
        expr_str = input_text.get().strip()
        expr = eval(expr_str)  # Evaluar la expresión con sympy
        
        # Calcular la integral indefinida
        integral_expr = integrate(expr, x)
        
        # Almacenar los pasos
        pasos.append(f"Integral de {expr_str}: {integral_expr}")
        
        # Mostrar el resultado en la caja de texto
        input_text.set(f"Resultado: {integral_expr}")
        
        # Graficar la integral
        graficar_integral(integral_expr, expr_str)

    except Exception as e:
        input_text.set(f"Error: {e}")

# Función para graficar la integral
def graficar_integral(integral_expr, expr_str):
    try:
        # Convertir la expresión simbólica a una función numérica usando lambdify
        integral_func = lambdify(x, integral_expr, modules=['numpy'])
        
        # Definir el rango de valores para graficar
        valores_x = np.linspace(-10, 10, 400)
        valores_y = integral_func(valores_x)
        
        # Crear la gráfica
        plt.plot(valores_x, valores_y, label=f"Integral de {expr_str}")
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.title('Gráfica de la Integral')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        input_text.set(f"Error al graficar: {e}")

# Función para mostrar teoremas de integrales
def mostrar_teoremas():
    teoremas = (
        "Teoremas de Integrales:\n\n"
        "1. Si f es continua en [a, b], entonces f tiene una integral definida en [a, b].\n"
        "2. La integral definida de una suma es la suma de las integrales.\n"
        "3. La integral definida de una constante es la constante multiplicada por la longitud del intervalo.\n"
        "4. El Teorema Fundamental del Cálculo relaciona la derivación con la integración."
    )
    input_text.set(teoremas)

# Función para mostrar los pasos de la integral
def mostrar_pasos():
    if pasos:
        # Mostrar los pasos en la caja de texto
        input_text.set("\n".join(pasos))
    else:
        input_text.set("No se han calculado pasos aún.")

# Botones
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('0', 5, 1),
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3),
    ('sin', 2, 4), ('cos', 3, 4), ('tan', 4, 4), ('exp', 5, 4),
    ('C', 5, 0), ('Calcular y Graficar', 5, 2), ('Teoremas', 5, 3),
    ('Pasos', 6, 2)
]

# Crear botones
for (text, row, col) in buttons:
    if text == 'Calcular y Graficar':
        action = calcular_y_graficar
    elif text == 'Teoremas':
        action = mostrar_teoremas
    elif text == 'Pasos':
        action = mostrar_pasos
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: click_button(x)
    
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=action)
    button.grid(row=row, column=col)

# Iniciar la aplicación
root.mainloop()
