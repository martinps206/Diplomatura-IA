from src.data_loader import generate_large_synthetic
from src.visuals import plot_series, plot_hist, plot_scatter
from src.advanced.spectral_analysis import compute_fft, welch_psd
from src.advanced.bootstrap import bootstrap_ci
from src.advanced.bayesian_mh import mh_normal_mean
from src.advanced.stochastic import brownian_motion, ornstein_uhlenbeck
from src.advanced.manifold import swiss_roll_embeddings
from src.advanced.optimization import newton_logistic
from src.advanced.pca_compare import compare_pca
from src.advanced.hypothesis_power import power_z_test
import os, numpy as np, pandas as pd

def run_demo():
    # Generar datos
    df = generate_large_synthetic(n=20000)
    df.to_csv('data/synthetic_advanced.csv', index=False)

    # Spectral (ejemplo para base_demand)
    series = df['base_demand'].values[:12000]
    freqs, psd = compute_fft(series)
    plot_series(freqs, psd, 'FFT PSD (base_demand)', xlabel='freq', ylabel='psd', filename='fft_psd.png')

    # Bootstrap
    price_per_item = (df['price'] / df['quantity']).values
    lower, upper, boots = bootstrap_ci(price_per_item[:8000], np.median, n_boot=500)
    print('Bootstrap median CI:', lower, upper)

    # MCMC (MH) - pequeño subset
    sample = price_per_item[:600]
    samples_mu = mh_normal_mean(sample, prior_mu=0.0, prior_sigma=100.0, sigma=np.std(sample), n_samples=1200, burn=300)

    # Stochastic
    bm_path, _ = brownian_motion(T=1.0, n=1200)
    plot_series(range(len(bm_path)), bm_path, 'Brownian motion', filename='brownian.png')

    # Manifold
    pca_emb, iso_emb, t = swiss_roll_embeddings(n_samples=800)
    plot_scatter(pca_emb[:,0], pca_emb[:,1], 'Swiss PCA', filename='swiss_pca.png')
    plot_scatter(iso_emb[:,0], iso_emb[:,1], 'Swiss Isomap', filename='swiss_iso.png')

    # Optimization demo
    rng = np.random.RandomState(0)
    X = rng.normal(size=(400,3))
    X = np.hstack([np.ones((X.shape[0],1)), X])
    true_beta = np.array([0.1, 0.8, -0.6, 0.4])
    logits = X.dot(true_beta)
    y = (1/(1+np.exp(-logits)) > rng.rand(X.shape[0])).astype(int)
    beta_hat = newton_logistic(X, y)
    print('Estimated beta:', beta_hat)

if __name__ == '__main__':
    run_demo()
