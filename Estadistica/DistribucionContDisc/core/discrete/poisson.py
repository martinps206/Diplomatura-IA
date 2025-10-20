import numpy as np
from scipy.stats import poisson
from core.base_distribution import BaseDistribution

class PoissonDistribution(BaseDistribution):
    def __init__(self, lam: float = None, lmbda: float = None):
        """Constructor que acepta ambos nombres de parámetro: `lam` y `lmbda`.

        Esto mantiene compatibilidad con llamadas existentes en la CLI.
        """
        if lam is None and lmbda is None:
            raise ValueError("PoissonDistribution requires 'lam' or 'lmbda' parameter")
        self.lam = lam if lam is not None else lmbda

    def pmf(self, k):
        return poisson.pmf(k, self.lam)

    def mean(self):
        return self.lam

    def variance(self):
        return self.lam

    def sample(self, n_samples):
        return np.random.poisson(self.lam, n_samples)

    def explain(self):
        return (
            "📘 **Distribución de Poisson**\n"
            "Modela el número de eventos en un intervalo con tasa media λ.\n\n"
            "E[X] = Var(X) = λ\n\n"
            "💡 **Aplicación en IA**: modela conteos discretos, como el número de ocurrencias de palabras en NLP (modelo Bag-of-Words) o la frecuencia de clics en modelos publicitarios."
        )
