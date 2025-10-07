import numpy as np

def randomized_svd(X, k=5, n_iter=2, random_state=0):
    """
    Randomized SVD (Halko et al.). Devuelve U, S, VT (solo primeros k).
    Parámetros:
      - X: matriz (n x p)
      - k: número de componentes
      - n_iter: power iterations (mejora precisión)
    """
    rng = np.random.RandomState(random_state)
    n, p = X.shape
    Omega = rng.normal(size=(p, k+5))
    Y = X.dot(Omega)
    for _ in range(n_iter):
        Y = X.dot(X.T.dot(Y))
    Q, _ = np.linalg.qr(Y)
    B = Q.T.dot(X)
    Uhat, S, VT = np.linalg.svd(B, full_matrices=False)
    U = Q.dot(Uhat)
    return U[:, :k], S[:k], VT[:k, :]
