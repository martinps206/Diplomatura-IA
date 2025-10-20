import numpy as np
from scipy.stats import binom
from core.base_distribution import BaseDistribution

class BinomialDistribution(BaseDistribution):
    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p

    def pmf(self, k):
        return binom.pmf(k, self.n, self.p)

    def mean(self):
        return self.n * self.p

    def variance(self):
        return self.n * self.p * (1 - self.p)

    def sample(self, n_samples):
        return np.random.binomial(self.n, self.p, n_samples)

    def explain(self):
        return (
            "📘 **Distribución Binomial**\n"
            "Modela el número de éxitos en *n* ensayos independientes con probabilidad *p* de éxito.\n\n"
            "E[X] = n·p\nVar(X) = n·p·(1−p)\n\n"
            "💡 **Aplicación en IA**: se usa para modelar tareas binarias (acierto/error), por ejemplo en clasificación supervisada binaria o en la métrica de precisión sobre varios ensayos."
        )
