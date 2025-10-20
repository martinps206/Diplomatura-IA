import numpy as np
from scipy.stats import chi2
from core.base_distribution import BaseDistribution

class ChiSquareDistribution(BaseDistribution):
    def __init__(self, k: int):
        self.k = k

    def pdf(self, x):
        return chi2.pdf(x, self.k)

    def mean(self):
        return self.k

    def variance(self):
        return 2 * self.k

    def sample(self, n_samples):
        return np.random.chisquare(self.k, n_samples)

    def explain(self):
        return (
            "📘 **Distribución Chi-cuadrado (χ²)**\n"
            "Suma de los cuadrados de k variables normales estándar.\n\n"
            "E[X]=k, Var(X)=2k\n\n"
            "💡 **Aplicación en IA**: usada en selección de características (test χ²) para evaluar independencia entre variables categóricas y la variable objetivo."
        )
