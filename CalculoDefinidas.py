import sympy as sp

def calcular_integral_definida(funcion, lim_inferior, lim_superior):
    # Definir la variable simbólica
    x = sp.symbols('x')

    # Convertir el símbolo ^ a ** para sympy
    funcion = funcion.replace('^', '**')

    # Convertir la función de entrada en una expresión simbólica
    f = sp.sympify(funcion)

    # Calcular la integral definida
    integral = sp.integrate(f, (x, lim_inferior, lim_superior))

    # Calcular la integral indefinida para mostrar pasos
    integral_indefinida = sp.integrate(f, x)

    # Obtener el resultado de la integral y redondearlo
    resultado = f"Resultado de la integral definida: {integral.evalf():.2f}\n"

    # Mostrar los pasos de la integral indefinida
    pasos = f"Pasos para calcular la integral:\n"
    pasos += f"1. Integral indefinida: ∫{f} dx = {integral_indefinida} + C\n"
    pasos += f"2. Evaluar en los límites:\n"
    pasos += f"   - En el límite superior ({lim_superior}): {integral_indefinida.subs(x, lim_superior).evalf():.2f}\n"
    pasos += f"   - En el límite inferior ({lim_inferior}): {integral_indefinida.subs(x, lim_inferior).evalf():.2f}\n"
    pasos += f"3. Resta: {integral_indefinida.subs(x, lim_superior).evalf():.2f} - {integral_indefinida.subs(x, lim_inferior).evalf():.2f} = {integral.evalf():.2f}"

    return resultado, pasos
