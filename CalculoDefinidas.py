import sympy as sp

def calcular_integral_definida(funcion, lim_inferior, lim_superior):
    x = sp.symbols('x')

    # Convertir el símbolo ^ a ** para sympy
    funcion = funcion.replace('^', '**')

    try:
        f = sp.sympify(funcion)
    except (sp.SympifyError, TypeError):
        return "Error: La función ingresada no es válida.", ""

    try:
        integral = sp.integrate(f, (x, lim_inferior, lim_superior))
        integral_indefinida = sp.integrate(f, x)

        resultado = f"**Resultado de la integral definida:** {integral.evalf():.2f}\n"
        pasos = (
            "---------------------------\n"
            "**Pasos para calcular la integral:**\n"
            "---------------------------\n"
            f"1. **Integral indefinida:**\n"
            f"   ∫{f} dx = {integral_indefinida} + C\n"
            "---------------------------\n"
            "2. **Evaluar en los límites:**\n"
            f"   - En el límite superior ({lim_superior}): {integral_indefinida.subs(x, lim_superior).evalf():.2f}\n"
            f"   - En el límite inferior ({lim_inferior}): {integral_indefinida.subs(x, lim_inferior).evalf():.2f}\n"
            "---------------------------\n"
            "3. **Resta:**\n"
            f"   {integral_indefinida.subs(x, lim_superior).evalf():.2f} - {integral_indefinida.subs(x, lim_inferior).evalf():.2f} = {integral.evalf():.2f}\n"
            "---------------------------\n"
        )
    except Exception as e:
        return f"Error al calcular la integral: {str(e)}", ""

    return resultado, pasos
