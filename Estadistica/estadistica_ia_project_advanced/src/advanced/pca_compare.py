import numpy as np
from sklearn.decomposition import PCA
from .randomized_svd import randomized_svd

def compare_pca(X, k=5):
    """
    Compara PCA (sklearn) con una implementación de SVD aleatorizada.
    Parámetros:
      - X: matriz de datos (n x p)
      - k: número de componentes
    Retorna:
      - scores_sklearn: proyecciones (n x k) con PCA de sklearn
      - scores_rand: proyecciones (n x k) usando randomized_svd
      - explained_ratio: array con las varianzas explicadas por sklearn
    Notas:
      - Se centra X antes de aplicar PCA.
      - randomized_svd devuelve U, S, VT aproximados; usamos VT para proyectar.
    """
    X = np.asarray(X, dtype=float)
    # centrar columnas
    Xc = X - X.mean(axis=0)

    # PCA exacta via sklearn (SVD completa)
    pca = PCA(n_components=k, svd_solver='full', random_state=0)
    scores_sklearn = pca.fit_transform(Xc)
    explained_ratio = pca.explained_variance_ratio_

    # Randomized SVD (aproximada)
    U, S, VT = randomized_svd(Xc, k=k)
    # VT tiene forma (k, p) -> las filas son los componentes principales aproximados
    # proyección = Xc @ VT.T (n x k)
    scores_rand = Xc.dot(VT.T)

    return scores_sklearn, scores_rand, explained_ratio
