from abc import ABC, abstractmethod
import numpy as np


class BaseDistribution(ABC):
    """Clase abstracta base para todas las distribuciones.

    Proporciona métodos concretos de compatibilidad usados por la CLI, como
    `expectation()` (alias a `mean()`) y `values()` que generan arrays
    (x, pmf/pdf) para graficar.
    """

    @abstractmethod
    def mean(self):
        pass

    @abstractmethod
    def variance(self):
        pass

    @abstractmethod
    def sample(self, n):
        """Genera n muestras aleatorias."""
        pass

    @abstractmethod
    def explain(self):
        """Explicación detallada con contexto en IA."""
        pass

    # Compatibilidad con la API usada por la CLI
    def expectation(self):
        """Alias amigable para obtener la esperanza (E[X])."""
        return self.mean()

    def values(self, num=200):
        """Devuelve una tupla (x, y) con valores para graficar.

        Para distribuciones discretas (definidas con `pmf`) devuelve un rango
        entero adecuado y la pmf. Para continuas (definidas con `pdf`) devuelve
        un vector x y la pdf evaluada.
        """
        # Distribución discreta
        if hasattr(self, "pmf"):
            # Determinar rango k
            if hasattr(self, "n"):
                x = np.arange(0, int(self.n) + 1)
            elif hasattr(self, "lam"):
                # cubrir suficiente masa alrededor de lambda
                max_k = max(15, int(self.lam + 4 * np.sqrt(max(1.0, self.lam))))
                x = np.arange(0, max_k + 1)
            else:
                # fallback genérico
                x = np.arange(0, 21)

            y = np.array([self.pmf(int(k)) for k in x], dtype=float)
            return x, y

        # Distribución continua
        if hasattr(self, "pdf"):
            if hasattr(self, "mu") and hasattr(self, "sigma"):
                low = self.mu - 4 * self.sigma
                high = self.mu + 4 * self.sigma
            elif hasattr(self, "a") and hasattr(self, "b"):
                low = self.a
                high = self.b
            else:
                # intentar inferir de muestras
                try:
                    s = self.sample(1000)
                    low = np.min(s)
                    high = np.max(s)
                    pad = (high - low) * 0.1
                    low -= pad
                    high += pad
                except Exception:
                    low, high = -10, 10

            x = np.linspace(low, high, num)
            y = np.array([self.pdf(xi) for xi in x], dtype=float)
            return x, y

        # Si no se reconoce la API, intentar usar sample como último recurso
        try:
            s = np.asarray(self.sample(1000))
            # si son enteros, graficar histograma aproximado, sino densidad
            if np.issubdtype(s.dtype, np.integer):
                vals, counts = np.unique(s, return_counts=True)
                probs = counts / counts.sum()
                return vals, probs
            else:
                # densidad empírica
                hist, bins = np.histogram(s, bins=100, density=True)
                x = (bins[:-1] + bins[1:]) / 2
                return x, hist
        except Exception:
            # última opción: vacíos
            return np.array([]), np.array([])
