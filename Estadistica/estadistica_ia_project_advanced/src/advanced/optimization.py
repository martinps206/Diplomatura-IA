import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def newton_logistic(X, y, max_iter=20, tol=1e-6):
    n, p = X.shape
    beta = np.zeros(p)
    for it in range(max_iter):
        p_pred = sigmoid(X.dot(beta))
        W = p_pred * (1 - p_pred)
        grad = X.T.dot(y - p_pred)
        XWX = (X * W[:, None]).T.dot(X)
        try:
            delta = np.linalg.solve(XWX, grad)
        except np.linalg.LinAlgError:
            delta = np.linalg.lstsq(XWX, grad, rcond=None)[0]
        beta_new = beta + delta
        if np.linalg.norm(beta_new - beta) < tol:
            beta = beta_new
            break
        beta = beta_new
    return beta
