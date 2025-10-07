import numpy as np

def sample_mean(x):
    return np.mean(x)

def sample_variance(x):
    return np.var(x, ddof=1)

def sample_std(x):
    return np.std(x, ddof=1)

def iqr(x):
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    return q3 - q1

def coeff_variation(x):
    mu = sample_mean(x)
    s = sample_std(x)
    return s / mu
