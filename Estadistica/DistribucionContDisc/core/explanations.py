# core/explanations.py
def general_intro():
    return (
        "📚 **Introducción a las Distribuciones de Probabilidad**\n\n"
        "Una distribución de probabilidad describe cómo se comporta una variable aleatoria.\n"
        "Las *discretas* modelan conteos o sucesos separados (p.ej., éxitos, clicks, eventos),\n"
        "mientras que las *continuas* modelan magnitudes que pueden tomar infinitos valores (p.ej., tiempo, temperatura, error).\n\n"
        "Las distribuciones son el núcleo de la estadística y la inferencia en IA, ya que permiten:\n"
        "- Modelar incertidumbre y ruido.\n"
        "- Definir funciones de pérdida derivadas de la verosimilitud.\n"
        "- Formular modelos bayesianos.\n"
        "- Evaluar el rendimiento de modelos bajo incertidumbre.\n"
    )


def inference_intro():
    return (
        "🎯 **Introducción a la Inferencia Estadística**\n\n"
        "La inferencia busca deducir propiedades de una población a partir de una muestra.\n"
        "Se basa en estimar parámetros, probar hipótesis y cuantificar el error.\n\n"
        "📊 Conceptos clave:\n"
        "- Error tipo I (α): rechazar una hipótesis verdadera.\n"
        "- Error tipo II (β): no rechazar una hipótesis falsa.\n"
        "- Potencia: 1−β (capacidad de detectar diferencias reales).\n"
        "- p-valor: evidencia contra la hipótesis nula.\n"
        "- Intervalos de confianza: rango probable para el parámetro real.\n\n"
        "💡 En IA, la inferencia se usa en validación de modelos, selección de características,\n"
        "detección de sesgos, y análisis de significancia de resultados experimentales."
    )


def ai_applications_summary():
    return (
        "🤖 **Aplicaciones Directas en Inteligencia Artificial**\n\n"
        "1️⃣ **Regresión lineal:** Asume ruido gaussiano en la variable dependiente.\n"
        "2️⃣ **Clasificación binaria:** Modela la variable objetivo como Bernoulli/Binomial.\n"
        "3️⃣ **Conteos:** Usa modelos Poisson o binomial negativa.\n"
        "4️⃣ **Bayesianismo:** Emplea priors conjugados (ej. Beta-Binomial) para actualizar creencias.\n\n"
        "Ejemplo: con prior Beta(α,β) y k éxitos en n ensayos, la posterior es Beta(α+k, β+n−k).\n"
        "Esto se aplica en IA para modelar tasas de conversión, fiabilidad de clasificadores o ajuste dinámico de hiperparámetros."
    )


def explain_expectation(value):
    """Genera una explicación amigable de la esperanza (valor esperado).

    Args:
        value (float): Valor de la esperanza (E[X]).

    Returns:
        str: Texto explicativo breve (también imprime en consola para uso CLI).
    """
    text = (
        f"🔎 Esperanza (E[X]): {value:.4f}\n"
        "La esperanza representa el valor promedio que tomaría la variable aleatoria\n"
        "si repitiéramos el experimento un gran número de veces. No siempre es un valor\n"
        "posible de observar en una muestra puntual, pero sí el centro de la distribución.\n"
    )
    print(text)
    return text


def explain_variance(value):
    """Genera una explicación amigable de la varianza.

    Args:
        value (float): Valor de la varianza (Var[X]).

    Returns:
        str: Texto explicativo breve (también imprime en consola para uso CLI).
    """
    text = (
        f"📐 Varianza (Var[X]): {value:.4f}\n"
        "La varianza mide la dispersión alrededor de la esperanza.\n"
        "Una varianza pequeña indica que los valores tienden a agruparse cerca de la media,\n"
        "mientras que una varianza grande indica mayor dispersión.\n"
    )
    print(text)
    return text


__all__ = [
    "general_intro",
    "inference_intro",
    "ai_applications_summary",
    "explain_expectation",
    "explain_variance",
]
