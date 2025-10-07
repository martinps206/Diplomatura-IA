import numpy as np
from scipy.stats import norm

def power_z_test(delta, sigma, n, alpha=0.05, two_sided=True):
    se = sigma / np.sqrt(n)
    if two_sided:
        z_alpha = norm.ppf(1 - alpha/2)
        power = norm.cdf((delta / se) - z_alpha) + (1 - norm.cdf((delta / se) + z_alpha))
    else:
        z_alpha = norm.ppf(1 - alpha)
        power = 1 - norm.cdf(z_alpha - (delta / se))
    return power

def required_n_for_power(delta, sigma, power_target=0.8, alpha=0.05, two_sided=True):
    if two_sided:
        z_alpha = norm.ppf(1 - alpha/2)
    else:
        z_alpha = norm.ppf(1 - alpha)
    z_beta = norm.ppf(power_target)
    n = ((z_alpha + z_beta) * sigma / delta)**2
    return int(np.ceil(n))
