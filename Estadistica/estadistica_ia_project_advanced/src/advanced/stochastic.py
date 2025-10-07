import numpy as np

def brownian_motion(T=1.0, n=1000, seed=0):
    rng = np.random.RandomState(seed)
    dt = T / n
    increments = rng.normal(loc=0.0, scale=np.sqrt(dt), size=n)
    path = np.concatenate([[0.0], np.cumsum(increments)])
    return path, increments

def ornstein_uhlenbeck(theta=1.0, mu=0.0, sigma=0.3, T=1.0, n=1000, seed=0):
    rng = np.random.RandomState(seed)
    dt = T / n
    x = np.zeros(n+1)
    for i in range(n):
        x[i+1] = x[i] + theta*(mu - x[i])*dt + sigma*np.sqrt(dt)*rng.normal()
    return x
