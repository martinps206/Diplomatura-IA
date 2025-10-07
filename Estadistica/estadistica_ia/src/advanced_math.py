import numpy as np

def pca_svd(X, k=2, center=True):
    X = np.asarray(X, dtype=float)
    if center:
        X = X - X.mean(axis=0)
    n = X.shape[0]
    U, S, VT = np.linalg.svd(X, full_matrices=False)
    components = VT[:k]
    scores = X.dot(components.T)
    explained_var = (S**2)/(n-1)
    explained_ratio = explained_var / explained_var.sum()
    return scores, components, explained_ratio[:k]

def gaussian_kde_manual(x, points, bandwidth):
    x = np.asarray(x)
    points = np.asarray(points)
    n = len(points)
    const = 1.0 / (n * bandwidth * np.sqrt(2*np.pi))
    diffs = (x[:, None] - points[None, :]) / bandwidth
    vals = const * np.exp(-0.5 * diffs**2)
    return vals.sum(axis=1)
