import numpy as np
from scipy import stats

def safe_log1p(x):
    return np.log1p(x)

def box_cox_transform(x):
    y, _ = stats.boxcox(x + 1e-8)
    return y

def z_score(x):
    return (x - np.mean(x)) / (np.std(x, ddof=1))
