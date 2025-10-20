import numpy as np
from scipy.stats import t
from core.base_distribution import BaseDistribution

class StudentTDistribution(BaseDistribution):
    def __init__(self, df: int):
        self.df = df

    def pdf(self, x):
        return t.pdf(x, self.df)

    def mean(self):
        return 0 if self.df > 1 else None

    def variance(self):
        if self.df > 2:
            return self.df / (self.df - 2)
        return float('inf')

    def sample(self, n_samples):
        return np.random.standard_t(self.df, n_samples)

    def explain(self):
        return (
            "📘 **Distribución t de Student**\n"
            "Aparece al estimar la media poblacional con varianza desconocida.\n\n"
            "💡 **Aplicación en IA**: útil en A/B tests o validación de modelos cuando las muestras son pequeñas y la varianza es incierta."
        )
