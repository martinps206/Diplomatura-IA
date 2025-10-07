import numpy as np

def bootstrap_ci(data, stat_func, n_boot=2000, alpha=0.05, random_state=0):
    rng = np.random.RandomState(random_state)
    n = len(data)
    boots = np.empty(n_boot)
    for i in range(n_boot):
        sample = rng.choice(data, size=n, replace=True)
        boots[i] = stat_func(sample)
    lower = np.percentile(boots, 100*(alpha/2))
    upper = np.percentile(boots, 100*(1-alpha/2))
    return lower, upper, boots
