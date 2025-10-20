"""Módulo para visualizaciones: histogramas y curvas de densidad.

Provee funciones que reciben listas de valores y opcionalmente probabilidades,
devuelven figuras de matplotlib o bytes PNG para servir en una API.
"""
from typing import List, Optional
import io


def plot_histogram(values: List[float], probabilities: Optional[List[float]] = None,
                   bins: int = 10, title: str = "Histograma"):
    """Genera un histograma con curva de densidad sobre los datos.

    Args:
        values: lista de valores numéricos.
        probabilities: ignoradas para la visualización base, pero pueden usarse
            para ponderar el histograma si se desea.
        bins: número de bins del histograma.
        title: título de la figura.

    Returns:
        matplotlib.figure.Figure: figura creada.
    """
    # Import matplotlib/seaborn lazily to avoid loading compiled extensions
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(values, bins=bins, stat="density", kde=True, ax=ax, color="#4c72b0")
    ax.set_title(title)
    ax.set_xlabel("Valor")
    ax.set_ylabel("Densidad")
    plt.tight_layout()
    return fig

def figure_to_png_bytes(fig) -> bytes:
    """Convierte una figura de matplotlib a bytes PNG en memoria.

    El caller es responsable de cerrar la figura si ya no se usa (plt.close).
    """
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    buf.seek(0)
    data = buf.getvalue()
    buf.close()
    # Cerrar la figura de manera segura
    try:
        import matplotlib.pyplot as _plt
        _plt.close(fig)
    except Exception:
        try:
            fig.clf()
        except Exception:
            pass
    return data
