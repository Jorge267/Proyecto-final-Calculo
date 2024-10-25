import sympy as sp

def calcular_integral_indefinida(funcion):
    x = sp.symbols('x')

    # Convertir el símbolo ^ a ** para sympy
    funcion = funcion.replace('^', '**')

    try:
        f = sp.sympify(funcion)
    except (sp.SympifyError, TypeError):
        return "Error: La función ingresada no es válida.", ""

    try:
        integral_indefinida = sp.integrate(f, x)

        resultado = f"**Resultado de la integral indefinida:** ∫{f} dx = {integral_indefinida} + C"
        pasos = (
            "---------------------------\n"
            "**Pasos para calcular la integral:**\n"
            "---------------------------\n"
            f"1. **Integral indefinida:**\n"
            f"   ∫{f} dx = {integral_indefinida} + C\n"
            "---------------------------\n"
        )
    except Exception as e:
        return f"Error al calcular la integral: {str(e)}", ""

    return resultado, pasos
