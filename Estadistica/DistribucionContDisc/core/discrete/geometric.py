import numpy as np
from scipy.stats import geom
from core.base_distribution import BaseDistribution

class GeometricDistribution(BaseDistribution):
    def __init__(self, p: float):
        self.p = p

    def pmf(self, k):
        return geom.pmf(k, self.p)

    def mean(self):
        return 1 / self.p

    def variance(self):
        return (1 - self.p) / (self.p ** 2)

    def sample(self, n_samples):
        return np.random.geometric(self.p, n_samples)

    def explain(self):
        return (
            "📘 **Distribución Geométrica**\n"
            "Modela el número de ensayos hasta el primer éxito.\n\n"
            "E[X] = 1/p\nVar(X) = (1−p)/p²\n\n"
            "💡 **Aplicación en IA**: útil para modelar el número de iteraciones hasta que un algoritmo converge o el número de intentos hasta un resultado positivo."
        )
