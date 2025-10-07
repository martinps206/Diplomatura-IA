import numpy as np
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap

def swiss_roll_embeddings(n_samples=800, random_state=0):
    X, t = make_swiss_roll(n_samples, noise=0.05, random_state=random_state)
    pca = PCA(n_components=2).fit_transform(X)
    iso = Isomap(n_neighbors=12, n_components=2).fit_transform(X)
    return pca, iso, t
