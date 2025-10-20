import numpy as np
from scipy.stats import uniform
from core.base_distribution import BaseDistribution

class UniformDistribution(BaseDistribution):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def pdf(self, x):
        return uniform.pdf(x, self.a, self.b - self.a)

    def mean(self):
        return (self.a + self.b) / 2

    def variance(self):
        return ((self.b - self.a) ** 2) / 12

    def sample(self, n_samples):
        return np.random.uniform(self.a, self.b, n_samples)

    def explain(self):
        return (
            "📘 **Distribución Uniforme Continua**\n"
            "Todos los valores en [a,b] son igualmente probables.\n\n"
            "E[X] = (a+b)/2, Var(X) = ((b−a)²)/12\n\n"
            "💡 **Aplicación en IA**: se usa para inicialización aleatoria de pesos en redes neuronales (p.ej. inicialización uniforme de Xavier o He)."
        )
