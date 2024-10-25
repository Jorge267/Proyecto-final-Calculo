import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def graficar_integral_definida(funcion, lim_inferior, lim_superior):
    try:
        # Definir la variable simbólica
        x = sp.symbols('x')

        # Convertir el símbolo ^ a ** para sympy
        funcion = funcion.replace('^', '**')

        # Convertir la función de entrada en una expresión simbólica
        f = sp.sympify(funcion)

        # Convertir límites a flotantes
        lim_inferior = float(lim_inferior)
        lim_superior = float(lim_superior)

        # Crear un rango de valores para x
        x_vals = np.linspace(lim_inferior - 1, lim_superior + 1, 400)

        # Evaluar la función en el rango de x
        y_vals = [float(f.subs(x, val).evalf()) for val in x_vals]

        # Comprobar si hay valores infinitos o NaN
        if np.any(np.isinf(y_vals)) or np.any(np.isnan(y_vals)):
            raise ValueError("La función genera valores no finitos en el rango especificado.")

        # Graficar la función
        plt.figure(figsize=(8, 4))
        plt.plot(x_vals, y_vals, label=f'f(x) = {f}', color='blue')

        # Colorear el área bajo la curva entre los límites
        x_fill = np.linspace(lim_inferior, lim_superior, 400)
        y_fill = [float(f.subs(x, val).evalf()) for val in x_fill]

        # Comprobar si hay valores infinitos o NaN en el área de llenado
        if np.any(np.isinf(y_fill)) or np.any(np.isnan(y_fill)):
            raise ValueError("La función genera valores no finitos en el rango de integración.")

        plt.fill_between(x_fill, y_fill, color='lightblue', alpha=0.5)

        # Configurar la gráfica
        plt.title("Gráfica de la Integral Definida")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.legend()
        plt.grid()

        # Mostrar la gráfica
        plt.show()
    except Exception as e:
        print("Error al graficar:", str(e))
