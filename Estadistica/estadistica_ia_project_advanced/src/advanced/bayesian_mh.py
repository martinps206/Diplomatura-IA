import numpy as np

def mh_normal_mean(data, prior_mu=0.0, prior_sigma=10.0, sigma=1.0,
                   n_samples=5000, burn=1000, prop_scale=0.5, random_state=0):
    rng = np.random.RandomState(random_state)
    def log_post(mu):
        return -0.5*((mu - prior_mu)**2)/(prior_sigma**2) - 0.5*np.sum((data - mu)**2)/(sigma**2)
    samples = []
    mu_curr = np.mean(data)
    ll_curr = log_post(mu_curr)
    for i in range(n_samples + burn):
        mu_prop = mu_curr + rng.normal(scale=prop_scale)
        ll_prop = log_post(mu_prop)
        if np.log(rng.rand()) < (ll_prop - ll_curr):
            mu_curr, ll_curr = mu_prop, ll_prop
        if i >= burn:
            samples.append(mu_curr)
    return np.array(samples)
