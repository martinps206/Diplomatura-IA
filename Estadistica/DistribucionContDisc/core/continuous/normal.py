import numpy as np
from scipy.stats import norm
from core.base_distribution import BaseDistribution

class NormalDistribution(BaseDistribution):
    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        return norm.pdf(x, self.mu, self.sigma)

    def mean(self):
        return self.mu

    def variance(self):
        return self.sigma ** 2

    def sample(self, n_samples):
        return np.random.normal(self.mu, self.sigma, n_samples)

    def explain(self):
        return (
            "📘 **Distribución Normal (Gaussiana)**\n"
            "La clásica 'curva de campana'.\n\n"
            "E[X]=μ, Var(X)=σ²\n"
            "Teorema Central del Límite: la media de muchas variables aleatorias tiende a ser normal.\n\n"
            "💡 **Aplicación en IA**: modela ruido gaussiano en regresión, errores de predicción, y distribuciones latentes en modelos como autoencoders variacionales."
        )
