# core/utils/random_seed.py
import numpy as np
import random

def set_random_seed(seed: int = 42):
    """
    Fija una semilla aleatoria para garantizar reproducibilidad.

    Args:
        seed (int): número de semilla.
    """
    np.random.seed(seed)
    random.seed(seed)
    print(f"🔒 Semilla aleatoria fijada en: {seed}")
