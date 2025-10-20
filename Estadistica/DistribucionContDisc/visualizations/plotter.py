# visualizations/plotter.py
import matplotlib.pyplot as plt
import numpy as np

class DistributionPlotter:
    """Clase encargada de graficar distribuciones discretas y continuas."""

    @staticmethod
    def plot_distribution(distribution, x_range, kind="auto", samples=None):
        """
        Grafica la distribución (PMF o PDF) y, opcionalmente, muestras simuladas.

        Args:
            distribution: instancia de BaseDistribution (con métodos pmf/pdf).
            x_range: rango de valores a evaluar (lista o np.array).
            kind: "pmf", "pdf" o "auto".
            samples: muestras simuladas opcionales.
        """
        plt.figure(figsize=(8, 4))
        title = distribution.__class__.__name__

        # Determinar tipo de gráfico
        if kind == "auto":
            kind = "pdf" if hasattr(distribution, "pdf") else "pmf"

        if kind == "pmf":
            y = [distribution.pmf(x) for x in x_range]
            plt.stem(x_range, y, use_line_collection=True)
            plt.ylabel("P(X=k)")
        else:
            y = [distribution.pdf(x) for x in x_range]
            plt.plot(x_range, y, lw=2)
            plt.ylabel("f(x)")

        plt.title(f"{title} ({kind.upper()})")
        plt.xlabel("x")

        # Mostrar muestras si existen
        if samples is not None:
            plt.hist(samples, bins=20, density=True, alpha=0.4, label="Muestras simuladas")
            plt.legend()

        plt.grid(alpha=0.3)
        plt.show()


def plot_distribution(x, y, continuous=False, title=None):
    """Función de compatibilidad utilizada por la CLI.

    Permite pasar arrays `x` e `y` ya calculados (pmf/pdf) y parámetros simples
    que usa `main.py` (continuous, title).
    """
    plt.figure(figsize=(8, 4))
    if continuous:
        plt.plot(x, y, lw=2)
        plt.ylabel("f(x)")
    else:
        # gráfico discreto
        plt.stem(x, y, use_line_collection=True)
        plt.ylabel("P(X=k)")

    if title is None:
        title = "Distribución"

    plt.title(title)
    plt.xlabel("x")
    plt.grid(alpha=0.3)
    plt.show()
